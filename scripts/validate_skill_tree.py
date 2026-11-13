#!/usr/bin/env python3
"""
Umby Beast Code skill tree validator.
Checks:
  1. Every skill has valid SKILL.md frontmatter (name matches folder, description present and <=1024 chars).
  2. Every relative markdown link in skills/, agents/, adapters/, and docs/ resolves.
  3. No machine-specific paths are committed.
  4. Each bundled Python tool passes a positive and a negative test.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_SKILLS = {
    "umby-beast-code",
    "umby-discover",
    "umby-plan",
    "umby-architect",
    "umby-backend",
    "umby-craft",
    "umby-motion",
    "umby-archetypes",
    "umby-evolve",
    "umby-arena",
    "umby-debug",
    "umby-secure",
    "umby-verify",
    "umby-ship",
    "umby-critic-mode",
    "umby-game-mode",
    "comment-slicer",
    "sick-social",
    "umby-help",
}

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#\s]+)(?:#[^)]*)?\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm_raw = text[4:end]
    result: dict[str, str] = {}
    for line in fm_raw.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


def run_cmd(cmd: list[str], stdin_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        input=stdin_text,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    failures: list[str] = []

    # 1. Check skills inventory & frontmatter
    skills_dir = ROOT / "skills"
    found_skills = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    missing = EXPECTED_SKILLS - found_skills
    if missing:
        failures.append(f"Missing expected skills: {sorted(missing)}")

    for skill_name in sorted(found_skills):
        skill_md = skills_dir / skill_name / "SKILL.md"
        if not skill_md.exists():
            failures.append(f"{skill_name}: missing SKILL.md")
            continue
        content = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if name != skill_name:
            failures.append(f"{skill_name}: frontmatter name '{name}' != folder '{skill_name}'")
        if not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", name) or len(name) > 64:
            failures.append(f"{skill_name}: invalid universal skill name '{name}'")
        if not desc or len(desc) > 1024:
            failures.append(f"{skill_name}: missing or >1024 char description ({len(desc)} chars)")

    # 2. Check markdown relative links across skills/, agents/, adapters/, docs/
    for folder in ["skills", "agents", "adapters", "docs"]:
        base = ROOT / folder
        if not base.exists():
            continue
        for md_file in base.rglob("*.md"):
            txt = md_file.read_text(encoding="utf-8")
            txt_no_code = re.sub(r"```.*?```", "", txt, flags=re.DOTALL)
            txt_no_code = re.sub(r"`[^`\n]+`", "", txt_no_code)
            for m in MD_LINK_RE.finditer(txt_no_code):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:", "file://", "conversation://")):
                    continue
                resolved = (md_file.parent / target).resolve()
                if not resolved.exists():
                    failures.append(f"Broken relative link in {md_file.relative_to(ROOT)} -> {target}")

    # 3. No private paths or local-only files referenced as required reading
    for scan_root in [ROOT / "skills", ROOT / "agents", ROOT / "adapters", ROOT / "docs"]:
        for f in scan_root.rglob("*"):
            if f.is_file() and f.suffix in {".md", ".py", ".css", ".sh"} and not f.name.endswith(".local.md"):
                if "/Users/" in f.read_text(encoding="utf-8", errors="ignore"):
                    failures.append(f"Machine-specific path found in {f.relative_to(ROOT)}")

    # 4. Behavioral tests on all 5 Python tools
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # 4a. preflight_recon.py
        recon = run_cmd([sys.executable, str(ROOT / "skills/umby-beast-code/scripts/preflight_recon.py"), str(tmp_path), "--json"])
        if recon.returncode != 0 or '"empty-directory"' not in recon.stdout:
            failures.append(f"preflight_recon.py failed empty dir test: {recon.stderr or recon.stdout}")

        # 4b. audit_ui_slop.py (slop must FAIL, clean must PASS)
        sloppy_tsx = tmp_path / "SloppyHero.tsx"
        sloppy_tsx.write_text(
            'export function Hero() { return <div onClick={() => {}} className="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">Trusted by 10,000+ happy users <a href="#">Start</a></div>; }\n',
            encoding="utf-8",
        )
        ui_fail = run_cmd([sys.executable, str(ROOT / "skills/umby-craft/scripts/audit_ui_slop.py"), str(sloppy_tsx)])
        if ui_fail.returncode == 0:
            failures.append("audit_ui_slop.py unexpectedly PASSED a sloppy TSX fixture")

        clean_tsx = tmp_path / "CleanHero.tsx"
        clean_tsx.write_text(
            'export function Hero() { return <section className="bg-[var(--bg-canvas)]"><button type="button">Open live sandbox</button></section>; }\n',
            encoding="utf-8",
        )
        ui_pass = run_cmd([sys.executable, str(ROOT / "skills/umby-craft/scripts/audit_ui_slop.py"), str(clean_tsx), "--strict"])
        if ui_pass.returncode != 0:
            failures.append(f"audit_ui_slop.py failed clean TSX fixture: {ui_pass.stdout}")

        # 4c. slicer_scan.py (narration + @ts-ignore must FAIL, clean must PASS)
        dirty_code = tmp_path / "dirty.tsx"
        dirty_code.write_text(
            "// @ts-ignore\nexport function Card() {\n  return <div>{/* Hero Section */}<span>Ok</span></div>;\n}\n",
            encoding="utf-8",
        )
        slicer_fail = run_cmd([sys.executable, str(ROOT / "skills/comment-slicer/scripts/slicer_scan.py"), str(dirty_code)])
        if slicer_fail.returncode == 0:
            failures.append("slicer_scan.py unexpectedly PASSED dirty code fixture")

        clean_code = tmp_path / "clean.ts"
        clean_code.write_text(
            "// SPDX-License-Identifier: MIT\nexport function centsToDisplay(cents: number): string {\n  return `$${(cents / 100).toFixed(2)}`;\n}\n",
            encoding="utf-8",
        )
        slicer_pass = run_cmd([sys.executable, str(ROOT / "skills/comment-slicer/scripts/slicer_scan.py"), str(clean_code), "--strict"])
        if slicer_pass.returncode != 0:
            failures.append(f"slicer_scan.py failed clean code fixture: {slicer_pass.stdout}")

        # 4d. sick_social_lint.py (AI slop must FAIL, bursty human prose must PASS)
        ai_slop_post = (
            "Let's dive in! In today's fast-paced digital landscape, AI is not just a tool, it's a game-changer — "
            "delving into seamless workflows and unlocking the power of innovation. Let that sink in.\n"
        )
        lint_fail = run_cmd([sys.executable, str(ROOT / "skills/sick-social/scripts/sick_social_lint.py"), "--stdin"], stdin_text=ai_slop_post)
        if lint_fail.returncode == 0:
            failures.append("sick_social_lint.py unexpectedly PASSED an AI-slop post")

        human_post = (
            "We deleted our entire Redis caching tier on Tuesday afternoon.\n\n"
            "Everyone on the call expected p99 checkout latency to spike past 600ms once raw traffic hit Postgres directly, "
            "because that old cache had been sitting in front of the orders table since 2022. Latency dropped from 410ms to 28ms instead. "
            "Why? Three missing composite indexes were hiding behind stale cache serialization overhead that burned 300ms on every miss.\n\n"
            "Measure the query plan first. Caches hide sins until traffic doubles.\n"
        )
        lint_pass = run_cmd([sys.executable, str(ROOT / "skills/sick-social/scripts/sick_social_lint.py"), "--stdin"], stdin_text=human_post)
        if lint_pass.returncode != 0:
            failures.append(f"sick_social_lint.py failed clean human post:\n{lint_pass.stdout}")

        # 4e. verify_surface_readiness.py (bad HTML must FAIL, valid HTML must PASS)
        bad_html = tmp_path / "bad.html"
        bad_html.write_text("<html><head><title>React App</title></head><body><img src='a.png'><a href='#'>x</a></body></html>", encoding="utf-8")
        surf_fail = run_cmd([sys.executable, str(ROOT / "skills/umby-verify/scripts/verify_surface_readiness.py"), str(bad_html)])
        if surf_fail.returncode == 0:
            failures.append("verify_surface_readiness.py unexpectedly PASSED bad HTML")

        good_html = tmp_path / "good.html"
        good_html.write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Vektor — Real-Time Treasury Ledger</title>'
            '<meta name="description" content="Reconcile Stripe, Ramp, and NetSuite payouts every night with deterministic audit trails.">'
            '<meta property="og:title" content="Vektor"><meta property="og:image" content="https://example.com/og.png">'
            '<link rel="canonical" href="https://example.com/"></head>'
            '<body><main><h1>Close your books every night.</h1><img src="/ledger.avif" alt="Automated ledger reconciliation view">'
            '<a href="/sandbox">Open live sandbox</a></main></body></html>',
            encoding="utf-8",
        )
        surf_pass = run_cmd([sys.executable, str(ROOT / "skills/umby-verify/scripts/verify_surface_readiness.py"), str(good_html)])
        if surf_pass.returncode != 0:
            failures.append(f"verify_surface_readiness.py failed good HTML:\n{surf_pass.stdout}")


        # 4f. critic_graph.py (bad round rejected, low round CONTINUE, passing round PASS, graph written)
        cg = str(ROOT / "skills/umby-critic-mode/scripts/critic_graph.py")
        cdir = tmp_path / "critic"
        bad_round = tmp_path / "bad_round.json"
        bad_round.write_text(json.dumps({"level": "A", "scores": [{"aspect": "Speed", "benchmark": "X", "score": 11}]}), encoding="utf-8")
        if run_cmd([sys.executable, cg, "add", str(bad_round), "--dir", str(cdir)]).returncode != 1:
            failures.append("critic_graph.py accepted an out-of-range score")

        def critic_round(score: int) -> Path:
            p = tmp_path / f"round_{score}.json"
            p.write_text(json.dumps({"level": "A", "scores": [
                {"aspect": "Speed", "benchmark": "X", "score": score, "why_not_10": "slow start", "suggestions": ["preload"]},
                {"aspect": "Clarity", "benchmark": "Y", "score": 9, "why_not_10": "one vague label", "suggestions": ["rename"]},
            ]}), encoding="utf-8")
            return p

        low = run_cmd([sys.executable, cg, "add", str(critic_round(6)), "--dir", str(cdir)])
        if low.returncode != 2 or "CONTINUE" not in low.stdout:
            failures.append(f"critic_graph.py did not report CONTINUE on a low round: {low.stdout}")
        high = run_cmd([sys.executable, cg, "add", str(critic_round(9)), "--dir", str(cdir)])
        if high.returncode != 0 or "PASS" not in high.stdout:
            failures.append(f"critic_graph.py did not report PASS on a passing round: {high.stdout}")
        if not (cdir / "graph.html").exists() or not (cdir / "scoreboard.md").exists():
            failures.append("critic_graph.py did not write graph.html and scoreboard.md")

        # 4g. game_scaffold.py (fresh scaffold passes check, unlisted asset fails it)
        gs = str(ROOT / "skills/umby-game-mode/scripts/game_scaffold.py")
        game = tmp_path / "game"
        if run_cmd([sys.executable, gs, "init", str(game), "--engine", "phaser"]).returncode != 0:
            failures.append("game_scaffold.py init failed")
        if run_cmd([sys.executable, gs, "check", str(game)]).returncode != 0:
            failures.append("game_scaffold.py check failed on a fresh scaffold")
        (game / "assets/sprites/Hero Idle.png").write_bytes(b"x")
        if run_cmd([sys.executable, gs, "check", str(game)]).returncode == 0:
            failures.append("game_scaffold.py check passed with an unlisted, badly named asset")

    print("=== UMBY BEAST CODE SKILL TREE VALIDATION ===")
    print(f"Skills Validated : {len(found_skills)} / {len(EXPECTED_SKILLS)} ({', '.join(sorted(found_skills))})")
    if failures:
        print(f"VERDICT: FAIL ({len(failures)} issue(s))")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("VERDICT: PASS — all skills, relative links, and 7 bundled tools passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
