#!/usr/bin/env python3
"""
Sick Social — Deterministic Human-Voice, Burstiness & Anti-AI-Slop Linter
Audits social media posts, blog articles, and website copy for:
  1. Banned AI lexicon ("delve", "tapestry", "landscape", "seamless", "leverage", etc.)
  2. Hollow contrast formulas ("not just X, it's Y", "isn't about X, it's about Y")
  3. Em-dash / double-hyphen overuse
  4. Staged throat-clearing openers & mic-drop closers ("Let's dive in", "Let that sink in")
  5. Bold-colon bullet soup ("- **Speed:** Speed is...") & decorative emoji bullets
  6. LinkedIn "broetry" (excessive single-sentence double-spaced lines)
  7. Low sentence-length burstiness (monotonous robotic pacing on multi-sentence prose)

Usage:
  python3 sick_social_lint.py draft.md [--allow-emdash] [--json]
  python3 sick_social_lint.py --stdin < draft.txt
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

BANNED_WORDS = [
    r"\bdelve(?:s|d|ing)?\b",
    r"\btapestr(?:y|ies)\b",
    r"\btestament\b",
    r"\bunderscore(?:s|d|ing)?\b",
    r"\bpivotal\b",
    r"\bcrucial\b",
    r"\bintricate\b",
    r"\binterplay\b",
    r"\bfoster(?:s|ed|ing)?\b",
    r"\bseamless(?:ly)?\b",
    r"\bsupercharg(?:e|es|ed|ing)\b",
    r"\bunleash(?:es|ed|ing)?\b",
    r"\bunlock(?:s|ed|ing)?\s+the\s+(?:power|potential|future)\b",
    r"\bgame-?changer\b",
    r"\brevolutioniz(?:e|es|ed|ing)\b",
    r"\bleverag(?:e|es|ed|ing)\b",
    r"\butiliz(?:e|es|ed|ing)\b",
    r"\belevat(?:e|es|ed|ing)\b",
    r"\bsynerg(?:y|ies)\b",
    r"\bholistic\b",
    r"\bbeacon\b",
    r"\brealm\b",
    r"\bvibrant\b",
    r"\bembark(?:s|ed|ing)?\b",
    r"\bnavigat(?:e|ing)\s+the\s+[a-z\s]*landscape\b",
    r"\bdigital\s+landscape\b",
    r"\bevolving\s+landscape\b",
    r"\bfurthermore\b",
    r"\bmoreover\b",
]

CONTRAST_FORMULAS = [
    (
        "NOT_X_BUT_Y",
        re.compile(
            r"\b(?:it['’]?s\s+not\s+(?:just|merely|only|about)\b[^.!?\n]{2,80}\b(?:it['’]?s|but)\b|"
            r"not\s+(?:just|merely|only)\s+[^.!?\n]{2,60},?\s+but\s+(?:also\s+|rather\s+)?|"
            r"this\s+isn['’]?t\s+(?:just\s+)?about\s+[^.!?\n]{2,60}[.;—-]\s*it['’]?s\s+about)",
            re.IGNORECASE,
        ),
        "Hollow 'Not X, but Y' contrast tell. State what the thing actually does directly.",
    ),
    (
        "STAGED_OPENER_OR_CLOSER",
        re.compile(
            r"(\blet['’]?s\s+(?:dive\s+in|explore|unpack|break\s+this\s+down)\b|"
            r"\bin\s+today['’]?s\s+(?:fast-paced|ever-changing|modern|digital)\b|"
            r"\bhere['’]?s\s+the\s+(?:thing|truth| kicker|reality)\s*:|"
            r"\blet\s+that\s+sink\s+in\b|"
            r"\bread\s+that\s+again\b|"
            r"\band\s+that['’]?s\s+the\s+(?:real\s+win|whole\s+game|secret)\b|"
            r"\bthe\s+future\s+(?:looks\s+bright|is\s+already\s+here)\b|"
            r"\bexciting\s+times\s+(?:ahead|lie\s+ahead)\b|"
            r"\bi\s+hope\s+this\s+helps\b|"
            r"^#{1,3}\s+(?:conclusion|final\s+thoughts|wrapping\s+up)\s*$)",
            re.IGNORECASE | re.MULTILINE,
        ),
        "Staged AI opener, mic-drop closer, or 'Conclusion' filler heading detected -> Cut completely.",
    ),
    (
        "THREADBOI_CLICHE",
        re.compile(r"(🧵|\b1/\d+\b|99%\s+of\s+people\s+get)", re.IGNORECASE),
        "Formulaic X thread cliché ('🧵', '1/N', '99% of people get') -> Open with a real fact or observation.",
    ),
    (
        "BOLD_COLON_LIST_SOUP",
        re.compile(r"^\s*[-*]\s+\*\*[^*\n]{2,40}:\*\*"),
        "Bold-label-and-colon bullet item ('- **Label:** ...') -> Write natural prose or plain unbolded items.",
    ),
    (
        "EMOJI_BULLET_SPAM",
        re.compile(r"^\s*[\U0001F680\u2728\U0001F525\U0001F4A1\u2705\u26A1\U0001F449]"),
        "Emoji used as a line/bullet opener -> Remove decorative emoji bullets.",
    ),
]

BANNED_WORD_RE = re.compile("|".join(BANNED_WORDS), re.IGNORECASE)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def strip_code_and_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5 :]
    text = CODE_FENCE_RE.sub("", text)
    text = re.sub(r"`[^`\n]+`", "CODE_TOKEN", text)
    return text


def split_sentences(prose: str) -> list[str]:
    cleaned_lines = []
    for line in prose.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|") or s.startswith(">"):
            continue
        cleaned_lines.append(s)
    joined = " ".join(cleaned_lines)
    raw = re.split(r"(?<=[.!?])\s+", joined)
    return [seg.strip() for seg in raw if len(seg.split()) >= 2]


def analyze_text(raw_text: str, allow_emdash: bool = False) -> dict:
    prose = strip_code_and_frontmatter(raw_text)
    lines = raw_text.splitlines()
    errors: list[dict] = []
    warnings: list[dict] = []

    in_fence = False
    for idx, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        line_no_inline_code = re.sub(r"`[^`]+`", "", line)

        for m in BANNED_WORD_RE.finditer(line_no_inline_code):
            errors.append(
                {
                    "line": idx,
                    "code": "BANNED_AI_WORD",
                    "match": m.group(0),
                    "message": f"Banned AI vocabulary '{m.group(0)}'. Replace with a plain concrete word.",
                }
            )

        if not allow_emdash and ("—" in line_no_inline_code or " -- " in line_no_inline_code):
            errors.append(
                {
                    "line": idx,
                    "code": "EM_DASH_TELL",
                    "match": "—" if "—" in line_no_inline_code else " -- ",
                    "message": "Em-dash connector detected. Use a period, comma, parentheses, or explicit conjunction.",
                }
            )

        for code, pattern, msg in CONTRAST_FORMULAS:
            m = pattern.search(line_no_inline_code)
            if m:
                errors.append(
                    {
                        "line": idx,
                        "code": code,
                        "match": m.group(0)[:60],
                        "message": msg,
                    }
                )

    # Check LinkedIn "broetry" (many consecutive single-sentence paragraphs separated by blank lines)
    paragraphs = [
        p.strip()
        for p in re.split(r"\n\s*\n", prose)
        if p.strip() and not p.strip().startswith(("#", "-", "*", "|", "1."))
    ]
    if len(paragraphs) >= 6:
        one_liner_count = sum(1 for p in paragraphs if len(re.split(r"[.!?]+", p.strip(".!?"))) == 1 and len(p.split()) <= 16)
        ratio = one_liner_count / len(paragraphs)
        if ratio >= 0.70:
            errors.append(
                {
                    "line": 1,
                    "code": "LINKEDIN_BROETRY_CADENCE",
                    "match": f"{one_liner_count}/{len(paragraphs)} single-line paragraphs",
                    "message": "Over 70% of paragraphs are isolated one-liners ('broetry'). Group related thoughts into real 2-4 sentence paragraphs.",
                }
            )

    # Compute Burstiness (standard deviation of sentence word counts)
    sentences = split_sentences(prose)
    word_counts = [len(s.split()) for s in sentences]
    burstiness_sd = 0.0
    mean_words = 0.0
    if len(word_counts) >= 2:
        mean_words = sum(word_counts) / len(word_counts)
        variance = sum((w - mean_words) ** 2 for w in word_counts) / len(word_counts)
        burstiness_sd = round(math.sqrt(variance), 2)

    if len(word_counts) >= 6 and burstiness_sd < 4.2:
        errors.append(
            {
                "line": 1,
                "code": "LOW_BURSTINESS_MONOTONE",
                "match": f"SD={burstiness_sd} words across {len(word_counts)} sentences",
                "message": "Robotic uniform sentence lengths detected (SD < 4.2). Mix short 3-6 word punches with longer 18-28 word specific clauses.",
            }
        )
    elif len(word_counts) >= 6 and burstiness_sd < 5.5:
        warnings.append(
            {
                "line": 1,
                "code": "MODERATE_BURSTINESS",
                "match": f"SD={burstiness_sd} words",
                "message": "Sentence variance is borderline (aim for SD >= 5.5 on long-form essays).",
            }
        )

    return {
        "verdict": "FAIL" if errors else "PASS",
        "sentence_count": len(word_counts),
        "mean_sentence_words": round(mean_words, 1),
        "burstiness_sd": burstiness_sd,
        "error_count": len(errors),
        "warn_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint social, blog, and web copy for human cadence and zero AI tells.")
    parser.add_argument("file", nargs="?", help="Markdown or text file to lint")
    parser.add_argument("--stdin", action="store_true", help="Read draft text from stdin")
    parser.add_argument("--allow-emdash", action="store_true", help="Permit em-dashes when matching an author's sample voice")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if args.stdin:
        raw = sys.stdin.read()
    elif args.file:
        p = Path(args.file)
        if not p.exists():
            print(f"[ERROR] File not found: {p}", file=sys.stderr)
            return 1
        raw = p.read_text(encoding="utf-8", errors="ignore")
    else:
        parser.print_help()
        return 1

    report = analyze_text(raw, allow_emdash=args.allow_emdash)
    if args.json:
        print(json.dumps(report, indent=2))
        return 1 if report["verdict"] == "FAIL" else 0

    print("=== SICK SOCIAL VOICE & ANTI-SLOP LINT ===")
    print(
        f"Sentences: {report['sentence_count']} | Avg length: {report['mean_sentence_words']}w | "
        f"Burstiness SD: {report['burstiness_sd']}w | Verdict: {report['verdict']}"
    )
    for err in report["errors"]:
        print(f"  [ERROR] Line {err['line']} ({err['code']}): {err['match']!r} -> {err['message']}")
    for warn in report["warnings"]:
        print(f"  [WARN]  Line {warn['line']} ({warn['code']}): {warn['match']!r} -> {warn['message']}")
    if not report["errors"] and not report["warnings"]:
        print("  CLEAN: Passes human burstiness, structure, and zero-AI-tell lexicon checks.")
    return 1 if report["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
