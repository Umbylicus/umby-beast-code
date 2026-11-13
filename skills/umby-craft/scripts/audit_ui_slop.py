#!/usr/bin/env python3
"""
Umby Craft — Deterministic UI Slop & Anti-Pattern Scanner
Scans JSX/TSX/Astro/Vue/Svelte/HTML/CSS files for visual AI tells, fake social proof,
inaccessible fake buttons, layout-thrashing transitions, and arbitrary pixel soup.

Usage: python3 audit_ui_slop.py [path ...] [--strict] [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

UI_EXTENSIONS = {".tsx", ".jsx", ".astro", ".vue", ".svelte", ".html", ".css", ".scss"}
IGNORE_DIRS = {
    ".git",
    "node_modules",
    ".next",
    ".astro",
    ".nuxt",
    "dist",
    "build",
    "out",
    "coverage",
    "__pycache__",
}

RULES: list[tuple[str, str, re.Pattern[str], str]] = [
    (
        "ERROR",
        "AI_GRADIENT_CLICHE",
        re.compile(
            r"(from-(?:indigo|purple|violet|fuchsia)-[456]00[^\"'\n]{0,60}(?:via|to)-(?:purple|pink|fuchsia|indigo)-[456]00|"
            r"linear-gradient\([^)]*#(?:6366f1|8b5cf6|a855f7)[^)]*#(?:ec4899|d946ef|8b5cf6))",
            re.IGNORECASE,
        ),
        "Stock indigo/purple/pink AI gradient detected. Replace with solid brand accent or subtle OKLCH surface lighting.",
    ),
    (
        "ERROR",
        "FAKE_SOCIAL_PROOF",
        re.compile(
            r"\b(10,000\+\s*(?:happy\s+)?(?:users|teams|customers|developers)|"
            r"trusted\s+by\s+\d{1,3},000\+|lorem\s+ipsum|acme\s+corp|john\s+doe|jane\s+doe)\b",
            re.IGNORECASE,
        ),
        "Placeholder or fabricated social proof detected. Use verified metrics or an honest interactive product artifact.",
    ),
    (
        "ERROR",
        "FAKE_DIV_BUTTON",
        re.compile(r"<(div|span)\b[^>]*\bonClick\s*=", re.IGNORECASE),
        "Interactive <div>/<span> with onClick detected. Use semantic <button type=\"button\"> or <a> for keyboard & screen-reader support.",
    ),
    (
        "ERROR",
        "DEAD_HASH_LINK",
        re.compile(r"<a\b[^>]*\bhref\s*=\s*[\"']#[\"']", re.IGNORECASE),
        "Dead href=\"#\" placeholder link detected. Wire to a real route/section ID or use a <button>.",
    ),
    (
        "WARN",
        "EMOJI_UI_CHROME",
        re.compile(r"[\U0001F680\u2728\U0001F525\U0001F4A1\u26A1\U0001F389\U0001F31F]"),
        "Decorative emoji (🚀/✨/🔥/💡/⚡) found in UI source. Use a uniform stroke SVG icon set instead of emojis.",
    ),
    (
        "WARN",
        "TRANSITION_ALL_THRASH",
        re.compile(r"\btransition-all\b|transition\s*:\s*all\b"),
        "transition-all animates layout properties and causes jank. Transition explicit properties (transform, opacity, colors).",
    ),
    (
        "WARN",
        "BLUR_BLOB_THEATER",
        re.compile(r"\bblur-3xl\b[^\n\"']*\b(?:bg-(?:purple|indigo|pink|violet|blue)-|opacity-[234]0)"),
        "Glowing blur-3xl background blob detected. Verify it is intentional lighting, not decorative AI hero filler.",
    ),
    (
        "WARN",
        "IMPORTANT_OVERRIDE",
        re.compile(r"(?<!0\.01ms\s)!important\b"),
        "CSS !important override detected (excluding reduced-motion reset). Fix cascade specificity or token layer instead.",
    ),
    (
        "WARN",
        "ARBITRARY_PIXEL_SPRAWL",
        re.compile(r"\b(?:p|px|py|pt|pb|pl|pr|m|mx|my|mt|mb|gap)-\[(?:11|13|15|17|19|21|22|23|25|26|27|29|31|33|35)px\]"),
        "Off-grid arbitrary Tailwind pixel spacing detected. Snap to the 4pt/8pt token scale.",
    ),
    (
        "WARN",
        "IMG_MISSING_ALT",
        re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>", re.IGNORECASE),
        "<img> element without an alt attribute. Provide descriptive alt text or alt=\"\" if purely decorative.",
    ),
]


def iter_files(targets: list[str]) -> list[Path]:
    collected: list[Path] = []
    for raw in targets:
        p = Path(raw)
        if p.is_file() and p.suffix.lower() in UI_EXTENSIONS:
            collected.append(p)
        elif p.is_dir():
            for dirpath, dirnames, filenames in os.walk(p):
                dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
                for fn in filenames:
                    fp = Path(dirpath) / fn
                    if fp.suffix.lower() in UI_EXTENSIONS:
                        collected.append(fp)
    return sorted(set(collected))


def scan_file(path: Path) -> list[dict]:
    findings: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception:
        return findings

    for idx, line in enumerate(lines, start=1):
        for severity, code, pattern, message in RULES:
            if code == "FAKE_DIV_BUTTON" and ("role=" in line and "tabIndex" in line):
                continue
            match = pattern.search(line)
            if match:
                findings.append(
                    {
                        "severity": severity,
                        "code": code,
                        "file": str(path),
                        "line": idx,
                        "snippet": line.strip()[:120],
                        "message": message,
                    }
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan UI source files for AI-slop patterns.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to scan")
    parser.add_argument("--strict", action="store_true", help="Fail on WARN as well as ERROR")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    files = iter_files(args.paths)
    all_findings: list[dict] = []
    for f in files:
        all_findings.extend(scan_file(f))

    errors = [x for x in all_findings if x["severity"] == "ERROR"]
    warns = [x for x in all_findings if x["severity"] == "WARN"]
    failed = bool(errors) or (args.strict and bool(warns))

    if args.json:
        print(
            json.dumps(
                {
                    "verdict": "FAIL" if failed else "PASS",
                    "files_scanned": len(files),
                    "error_count": len(errors),
                    "warn_count": len(warns),
                    "findings": all_findings,
                },
                indent=2,
            )
        )
        return 1 if failed else 0

    print(f"=== UMBY UI SLOP AUDIT ({len(files)} UI files scanned) ===")
    if not all_findings:
        print("VERDICT: PASS — Zero UI slop patterns detected.")
        return 0

    for item in all_findings:
        print(f"[{item['severity']}] {item['code']} @ {item['file']}:{item['line']}")
        print(f"  Snippet : {item['snippet']}")
        print(f"  Fix     : {item['message']}")

    print(f"\nSummary: {len(errors)} ERROR(s), {len(warns)} WARN(s) -> VERDICT: {'FAIL' if failed else 'PASS (with warnings)'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
