#!/usr/bin/env python3
"""Critic Mode round log and score graph.

  python3 critic_graph.py add <round.json> [--dir .beast/critic] [--max-rounds N]
  python3 critic_graph.py render [--dir .beast/critic]

`add` validates one round of critic scores, appends it to rounds.jsonl, rebuilds
graph.html and scoreboard.md, and prints a status line:

  PASS         every aspect is at or above the bar
  CONTINUE     below the bar, still improving
  STALLED      the lowest score has not improved for two rounds
  ROUND_LIMIT  the round cap was reached
  REPORT_ONLY  level C (critique only)

Exit code: 0 for PASS and REPORT_ONLY, 2 for CONTINUE, 3 for STALLED or ROUND_LIMIT, 1 for bad input.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

LEVELS = {"A": {"bar": 9, "max_rounds": 6}, "B": {"bar": 7, "max_rounds": 4}, "C": {"bar": None, "max_rounds": 1}}
COLORS = ["#2563eb", "#dc2626", "#059669", "#d97706", "#7c3aed", "#0891b2", "#be185d", "#4d7c0f", "#9a3412", "#475569"]


def load_rounds(folder: Path) -> list[dict]:
    log = folder / "rounds.jsonl"
    if not log.exists():
        return []
    return [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate(round_data: dict) -> list[str]:
    problems: list[str] = []
    level = round_data.get("level")
    if level not in LEVELS:
        problems.append("level must be A, B, or C")
    scores = round_data.get("scores")
    if not isinstance(scores, list) or not scores:
        return problems + ["scores must be a non-empty list"]
    if len(scores) > 10:
        problems.append("at most 10 critics per round")
    seen: set[str] = set()
    for i, s in enumerate(scores, start=1):
        aspect = str(s.get("aspect", "")).strip()
        if not aspect:
            problems.append(f"score {i}: missing aspect")
        elif aspect in seen:
            problems.append(f"score {i}: aspect '{aspect}' appears twice")
        seen.add(aspect)
        score = s.get("score")
        if not isinstance(score, (int, float)) or isinstance(score, bool) or not 1 <= score <= 10:
            problems.append(f"score {i} ({aspect}): score must be a number from 1 to 10")
            continue
        if not str(s.get("benchmark", "")).strip():
            problems.append(f"score {i} ({aspect}): missing benchmark")
        if score < 10 and not str(s.get("why_not_10", "")).strip():
            problems.append(f"score {i} ({aspect}): a score under 10 needs why_not_10")
        if score < 10 and not s.get("suggestions"):
            problems.append(f"score {i} ({aspect}): a score under 10 needs at least one suggestion")
    return problems


def status_for(rounds: list[dict], max_rounds: int | None) -> str:
    latest = rounds[-1]
    level = latest["level"]
    bar = LEVELS[level]["bar"]
    if bar is None:
        return "REPORT_ONLY"
    lows = [min(s["score"] for s in r["scores"]) for r in rounds]
    if lows[-1] >= bar:
        return "PASS"
    if len(rounds) >= (max_rounds or LEVELS[level]["max_rounds"]):
        return "ROUND_LIMIT"
    if len(lows) >= 3:
        means = [sum(s["score"] for s in r["scores"]) / len(r["scores"]) for r in rounds]
        if lows[-1] <= lows[-3] and means[-1] <= means[-3]:
            return "STALLED"
    return "CONTINUE"


def render(folder: Path, rounds: list[dict], status: str) -> None:
    latest = rounds[-1]
    bar = LEVELS[latest["level"]]["bar"]
    aspects: list[str] = []
    for r in rounds:
        for s in r["scores"]:
            if s["aspect"] not in aspects:
                aspects.append(s["aspect"])

    width, height, left, top, bottom = 760, 320, 40, 16, 34
    plot_w, plot_h = width - left - 16, height - top - bottom
    n = len(rounds)

    def x(i: int) -> float:
        return left + (plot_w / 2 if n == 1 else plot_w * i / (n - 1))

    def y(v: float) -> float:
        return top + plot_h * (10 - v) / 9

    svg = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="Critic scores by round">']
    for v in range(1, 11):
        svg.append(f'<line x1="{left}" x2="{width - 16}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="grid"/>')
        svg.append(f'<text x="{left - 8}" y="{y(v) + 4:.1f}" class="tick" text-anchor="end">{v}</text>')
    for i, r in enumerate(rounds):
        svg.append(f'<text x="{x(i):.1f}" y="{height - 10}" class="tick" text-anchor="middle">Round {r["round"]}</text>')
    if bar is not None:
        svg.append(f'<line x1="{left}" x2="{width - 16}" y1="{y(bar):.1f}" y2="{y(bar):.1f}" class="bar"/>')
        svg.append(f'<text x="{width - 20}" y="{y(bar) - 6:.1f}" class="barlabel" text-anchor="end">pass bar {bar}</text>')
    for k, aspect in enumerate(aspects):
        color = COLORS[k % len(COLORS)]
        pts = [(x(i), y(s["score"])) for i, r in enumerate(rounds) for s in r["scores"] if s["aspect"] == aspect]
        if len(pts) > 1:
            path = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            svg.append(f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="2"/>')
        for px, py in pts:
            svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{color}"/>')
    svg.append("</svg>")

    rows, md_rows = [], []
    first = {s["aspect"]: s["score"] for s in rounds[0]["scores"]}
    for k, s in enumerate(sorted(latest["scores"], key=lambda item: item["score"])):
        color = COLORS[aspects.index(s["aspect"]) % len(COLORS)]
        ok = bar is None or s["score"] >= bar
        tips = "".join(f"<li>{html.escape(str(t))}</li>" for t in s.get("suggestions", []))
        rows.append(
            f'<tr><td><span class="dot" style="background:{color}"></span>{html.escape(s["aspect"])}</td>'
            f'<td>{html.escape(str(s.get("benchmark", "")))}</td>'
            f'<td class="num">{first.get(s["aspect"], "-")}</td>'
            f'<td class="num {"ok" if ok else "low"}">{s["score"]}</td>'
            f'<td>{html.escape(str(s.get("why_not_10", "")))}<ul>{tips}</ul></td></tr>'
        )
        md_rows.append(
            f'| {s["aspect"]} | {s.get("benchmark", "")} | {first.get(s["aspect"], "-")} | {s["score"]} | {s.get("why_not_10", "")} |'
        )

    low = min(s["score"] for s in latest["scores"])
    refresh = "" if status in {"PASS", "REPORT_ONLY"} else '<meta http-equiv="refresh" content="10">'
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{refresh}
<title>Critic scores</title>
<style>
:root{{--bg:#fafaf9;--ink:#1c1917;--muted:#57534e;--line:#e7e5e4;--card:#fff}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0c0a09;--ink:#f5f5f4;--muted:#a8a29e;--line:#292524;--card:#1c1917}}}}
body{{margin:0;padding:24px 16px;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,sans-serif}}
main{{max-width:860px;margin:0 auto}}h1{{font-size:22px;margin:0 0 4px}}p.sub{{color:var(--muted);margin:0 0 16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px;margin-bottom:16px;overflow-x:auto}}
svg{{width:100%;height:auto;min-width:520px}}.grid{{stroke:var(--line)}}.tick{{fill:var(--muted);font-size:11px}}
.bar{{stroke:#16a34a;stroke-dasharray:6 4;stroke-width:1.5}}.barlabel{{fill:#16a34a;font-size:11px}}
table{{border-collapse:collapse;width:100%;min-width:560px}}th,td{{text-align:left;padding:8px;border-top:1px solid var(--line);vertical-align:top}}
th{{color:var(--muted);font-weight:600;border-top:0}}.num{{font-variant-numeric:tabular-nums;font-weight:600}}
.ok{{color:#16a34a}}.low{{color:#dc2626}}.dot{{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:8px}}
ul{{margin:4px 0 0;padding-left:18px;color:var(--muted)}}
</style></head><body><main>
<h1>Critic scores: {html.escape(status)}</h1>
<p class="sub">Level {latest["level"]}{f", pass bar {bar}" if bar else ", critique only"}. Round {latest["round"]}. Lowest score {low}. Updated {html.escape(latest["logged_at"])}.</p>
<div class="card">{"".join(svg)}</div>
<div class="card"><table><thead><tr><th>Aspect</th><th>Benchmark</th><th>First</th><th>Now</th><th>Why not 10, and next fixes</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
</main></body></html>
"""
    (folder / "graph.html").write_text(page, encoding="utf-8")
    board = [
        f"# Critic scoreboard: {status}",
        "",
        f"Level {latest['level']}, round {latest['round']}, lowest score {low}" + (f", pass bar {bar}." if bar else ", critique only."),
        "",
        "| Aspect | Benchmark | First | Now | Why not 10 |",
        "| :--- | :--- | ---: | ---: | :--- |",
        *md_rows,
        "",
    ]
    (folder / "scoreboard.md").write_text("\n".join(board), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Log critic rounds and draw the score graph.")
    ap.add_argument("command", choices=["add", "render"])
    ap.add_argument("round_file", nargs="?")
    ap.add_argument("--dir", default=".beast/critic")
    ap.add_argument("--max-rounds", type=int, default=None)
    args = ap.parse_args()

    folder = Path(args.dir)
    rounds = load_rounds(folder)

    if args.command == "add":
        if not args.round_file:
            print("[ERROR] add needs a round JSON file", file=sys.stderr)
            return 1
        try:
            data = json.loads(Path(args.round_file).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"[ERROR] cannot read round file: {exc}", file=sys.stderr)
            return 1
        problems = validate(data)
        if rounds and data.get("level") != rounds[0]["level"]:
            problems.append(f"level changed from {rounds[0]['level']}; start a new folder to change level")
        if problems:
            print("[ERROR] round rejected:")
            for p in problems:
                print(f"  - {p}")
            return 1
        data["round"] = len(rounds) + 1
        data["logged_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / "rounds.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(data) + "\n")
        rounds.append(data)
    elif not rounds:
        print(f"[ERROR] no rounds logged in {folder}", file=sys.stderr)
        return 1

    status = status_for(rounds, args.max_rounds)
    render(folder, rounds, status)
    latest = rounds[-1]
    low = min(latest["scores"], key=lambda s: s["score"])
    print(f"STATUS: {status} | round {latest['round']} | lowest {low['score']} ({low['aspect']}) | graph: {folder / 'graph.html'}")
    return {"PASS": 0, "REPORT_ONLY": 0, "CONTINUE": 2}.get(status, 3)


if __name__ == "__main__":
    raise SystemExit(main())
