#!/usr/bin/env python3
"""Comment Slicer scanner.

Lists comment candidates in source files so a reviewer can judge them. It never edits files.

Kinds reported:
  PROTECTED  a comment a tool reads. Never change it. (info only)
  SILENCER   a check is switched off here. Needs a fix or a named reason. (error)
  NARRATION  a label or step note that restates the code. (error)
  DEAD_CODE  commented-out code. (error)
  LOOSE_TODO a TODO/FIXME/HACK with no ticket or link. (warning)

Usage:
  python3 slicer_scan.py <file-or-dir> [more ...] [--strict] [--json]

Exit code 1 when any error is found (or any warning with --strict), else 0.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SOURCE_SUFFIXES = {
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro",
    ".css", ".scss", ".html", ".py", ".go", ".rs", ".gd", ".cs", ".swift", ".kt", ".java",
}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", "out", ".next", ".godot", "vendor", "__pycache__", ".venv"}

# Text of a comment, wherever it sits on the line.
COMMENT_BODY = re.compile(
    r"\{/\*(?P<jsx>.*?)\*/\}"
    r"|/\*(?P<block>.*?)\*/"
    r"|<!--(?P<html>.*?)-->"
    r"|(?<![:\"'\w])//(?P<slash>.*)$"
    r"|(?:^|\s)#(?P<hash>(?![0-9a-fA-F]{3,8}\b).*)$"
)

PROTECTED = re.compile(
    r"^\s*(?:"
    r"!|-\*-\s*coding|(?:vim?:|coding[:=])|SPDX-License-Identifier|copyright\b|\(c\)|license\b"
    r"|go:\w+|\+build\b|pragma\b|/\s*<reference\b|@ts-check\b|@ts-nocheck\b|@jsx\w*\b|@flow\b"
    r"|webpack\w+\s*:|@vite-ignore\b|#__PURE__|@__PURE__"
    r"|prettier-ignore|istanbul ignore|c8 ignore|v8 ignore|fmt:\s*(?:off|on|skip)|rustfmt::skip"
    r"|[#@]\s*sourceMappingURL|region\b|endregion\b|\[if\s|<!\[endif\]"
    r")",
    re.IGNORECASE,
)

SILENCER = re.compile(
    r"@ts-ignore|@ts-expect-error|eslint-disable|biome-ignore|type:\s*ignore|\bnoqa\b|pylint:\s*disable|nolint\b",
    re.IGNORECASE,
)
CODE_SILENCER = re.compile(r":\s*any\b|\bas\s+any\b|as\s+unknown\s+as\b|!important|suppressHydrationWarning")

SECTION_WORDS = (
    r"hero|header|footer|nav(?:bar|igation)?|sidebar|main|content|features?|pricing|testimonials?|faq|cta|"
    r"card|modal|button|form|icons?|stats|imports?|state|hooks?|handlers?|helpers?|utils?|types?|styles?|"
    r"render|return|constants?|setup|cleanup|section|container|wrapper|"
    r"phase\s*\d+|step\s*\d+|part\s*\d+"
)
NARRATION = re.compile(
    rf"^\s*(?:[-=*#~]{{3,}}.*|(?:the\s+)?(?:{SECTION_WORDS})(?:\s+(?:section|area|block|part|component|logic|code|here))?\s*[:.]?"
    r"|(?:handle|handles|set|sets|get|gets|loop|loops|iterate|check|checks|return|returns|render|renders|"
    r"create|creates|define|defines|initialize|initializes|increment|import|call|calls|update|updates)\b.{0,40})\s*$",
    re.IGNORECASE,
)
DEAD_CODE = re.compile(
    r"^\s*(?:import\s.+from\s|(?:const|let|var|function|class|def|return|if|for|while)\b.*[({=:;]|"
    r"</?[A-Za-z][\w.]*[^>]*>|[\w.]+\(.*\)\s*;?\s*$|[\w.]+\s*=\s*.+;\s*$)"
)
TODO = re.compile(r"\b(?:TODO|FIXME|HACK|XXX)\b", re.IGNORECASE)
HAS_REF = re.compile(r"https?://|#\d+|\b[A-Z]{2,}-\d+\b")


def comment_text(line: str, suffix: str) -> str | None:
    m = COMMENT_BODY.search(line)
    if not m:
        return None
    if m.group("hash") is not None and suffix not in {".py", ".gd"}:
        return None
    if m.group("slash") is not None and suffix in {".py", ".gd", ".css", ".html"}:
        return None
    return next(g for g in m.groups() if g is not None).strip()


def scan_file(path: Path) -> list[dict]:
    found: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return found

    def add(n: int, kind: str, level: str, text: str) -> None:
        found.append({"file": str(path), "line": n, "kind": kind, "level": level, "text": text.strip()[:90]})

    for n, line in enumerate(lines, start=1):
        text = comment_text(line, path.suffix)
        if n == 1 and line.startswith("#!"):
            add(n, "PROTECTED", "info", line)
            continue
        if text is None:
            if CODE_SILENCER.search(line):
                add(n, "SILENCER", "error", line)
            continue
        if PROTECTED.search(text):
            add(n, "PROTECTED", "info", text)
        elif SILENCER.search(text):
            add(n, "SILENCER", "error", text)
        elif TODO.search(text):
            if not HAS_REF.search(text):
                add(n, "LOOSE_TODO", "warn", text)
        elif DEAD_CODE.search(text):
            add(n, "DEAD_CODE", "error", text)
        elif NARRATION.match(text):
            add(n, "NARRATION", "error", text)
        if CODE_SILENCER.search(line.split("//")[0]):
            add(n, "SILENCER", "error", line)
    return found


def gather(targets: list[str]) -> list[Path]:
    files: list[Path] = []
    for t in targets:
        p = Path(t)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file() and f.suffix in SOURCE_SUFFIXES and not (set(f.parts) & SKIP_DIRS):
                    files.append(f)
        else:
            print(f"[ERROR] Not found: {t}", file=sys.stderr)
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description="List comment candidates for Comment Slicer. Read-only.")
    ap.add_argument("targets", nargs="+")
    ap.add_argument("--strict", action="store_true", help="Warnings also fail the scan")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    files = gather(args.targets)
    findings = [f for path in files for f in scan_file(path)]
    errors = [f for f in findings if f["level"] == "error"]
    warns = [f for f in findings if f["level"] == "warn"]
    protected = [f for f in findings if f["kind"] == "PROTECTED"]
    failed = bool(errors) or (args.strict and bool(warns))

    if args.json:
        print(json.dumps({"files": len(files), "verdict": "FAIL" if failed else "PASS", "findings": findings}, indent=2))
        return 1 if failed else 0

    print(f"=== COMMENT SLICER SCAN ({len(files)} file(s)) ===")
    for f in findings:
        tag = {"error": "CANDIDATE", "warn": "WARN", "info": "LEAVE"}[f["level"]]
        print(f"  [{tag}] {f['file']}:{f['line']} {f['kind']}: {f['text']}")
    print(
        f"Summary: {len(errors)} candidate(s), {len(warns)} warning(s), {len(protected)} protected -> "
        f"VERDICT: {'FAIL' if failed else 'PASS'}"
    )
    if protected:
        print("Protected comments are read by tools. Do not change them.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
