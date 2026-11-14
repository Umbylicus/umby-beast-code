#!/usr/bin/env python3
"""
Verify — HTML Landmark, A11y & Technical SEO Readiness Verifier
Audits either a live HTTP(S) URL (e.g. http://localhost:3000) or built .html files in a directory.

Usage:
  python3 verify_surface_readiness.py http://localhost:3000 [--json]
  python3 verify_surface_readiness.py ./dist [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


class SurfaceHTMLInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title_parts: list[str] = []
        self.has_lang = False
        self.has_viewport = False
        self.meta_description = ""
        self.has_og_title = False
        self.has_og_image = False
        self.has_canonical = False
        self.h1_count = 0
        self.heading_levels: list[int] = []
        self.has_main = False
        self.imgs_missing_alt = 0
        self.empty_links = 0
        self.buttons_missing_type = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {k.lower(): (v or "") for k, v in attrs}
        t = tag.lower()

        if t == "html" and attr_map.get("lang", "").strip():
            self.has_lang = True
        elif t == "title":
            self.in_title = True
        elif t == "meta":
            name = attr_map.get("name", "").lower()
            prop = attr_map.get("property", "").lower()
            content = attr_map.get("content", "").strip()
            if name == "viewport" and content:
                self.has_viewport = True
            elif name == "description" and content:
                self.meta_description = content
            elif prop == "og:title" and content:
                self.has_og_title = True
            elif prop == "og:image" and content:
                self.has_og_image = True
        elif t == "link":
            rel = attr_map.get("rel", "").lower()
            if "canonical" in rel and attr_map.get("href", "").strip():
                self.has_canonical = True
        elif t in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            lvl = int(t[1])
            self.heading_levels.append(lvl)
            if lvl == 1:
                self.h1_count += 1
        elif t == "main" or attr_map.get("role", "").lower() == "main":
            self.has_main = True
        elif t == "img":
            if "alt" not in attr_map:
                self.imgs_missing_alt += 1
        elif t == "a":
            href = attr_map.get("href", "").strip()
            if href in {"", "#", "javascript:void(0)"}:
                self.empty_links += 1
        elif t == "button":
            if "type" not in attr_map:
                self.buttons_missing_type += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def evaluate_html(label: str, html_text: str) -> dict:
    inspector = SurfaceHTMLInspector()
    inspector.feed(html_text)
    title = "".join(inspector.title_parts).strip()

    errors: list[str] = []
    warnings: list[str] = []

    if not inspector.has_lang:
        errors.append("Missing `lang` attribute on <html>.")
    if not inspector.has_viewport:
        errors.append("Missing `<meta name=\"viewport\">` tag.")
    if not title:
        errors.append("Missing or empty `<title>`.")
    elif title.lower() in {"react app", "vite app", "create next app", "document", "home"}:
        errors.append(f"Generic default `<title>` detected: '{title}'.")
    if not inspector.has_main:
        errors.append("Missing semantic `<main>` landmark.")
    if inspector.h1_count == 0:
        errors.append("Zero `<h1>` elements found on page.")
    elif inspector.h1_count > 1:
        warnings.append(f"Multiple `<h1>` elements found ({inspector.h1_count}); prefer a single primary `<h1>`.")
    if inspector.imgs_missing_alt > 0:
        errors.append(f"{inspector.imgs_missing_alt} `<img>` tag(s) missing `alt` attribute.")
    if inspector.empty_links > 0:
        errors.append(f"{inspector.empty_links} `<a>` link(s) use empty or placeholder `href=\"#\"`.")

    if not inspector.meta_description:
        warnings.append("Missing `<meta name=\"description\">` for search previews.")
    elif len(inspector.meta_description) < 50 or len(inspector.meta_description) > 175:
        warnings.append(f"Meta description length ({len(inspector.meta_description)} chars) outside optimal 70-165 range.")
    if not inspector.has_og_title:
        warnings.append("Missing `og:title` social card tag.")
    if not inspector.has_og_image:
        warnings.append("Missing `og:image` social preview image tag.")
    if not inspector.has_canonical:
        warnings.append("Missing `<link rel=\"canonical\">` tag.")

    for prev, curr in zip(inspector.heading_levels, inspector.heading_levels[1:]):
        if curr > prev + 1:
            warnings.append(f"Skipped heading hierarchy level: `<h{prev}>` jumped directly to `<h{curr}>`.")
            break

    return {
        "target": label,
        "title": title,
        "errors": errors,
        "warnings": warnings,
        "status": "FAIL" if errors else "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify HTML landmarks, a11y basics, and SEO readiness.")
    parser.add_argument("target", help="HTTP(S) URL or path to HTML file / build directory")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    results: list[dict] = []
    target = args.target

    if target.startswith(("http://", "https://")):
        try:
            req = urllib.request.Request(target, headers={"User-Agent": "BeastVerify/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                body = resp.read().decode("utf-8", errors="ignore")
            results.append(evaluate_html(target, body))
        except Exception as exc:
            print(f"[ERROR] Failed to fetch {target}: {exc}", file=sys.stderr)
            return 1
    else:
        p = Path(target)
        if p.is_file():
            results.append(evaluate_html(str(p), p.read_text(encoding="utf-8", errors="ignore")))
        elif p.is_dir():
            html_files = []
            for dirpath, dirnames, filenames in os.walk(p):
                dirnames[:] = [d for d in dirnames if d not in {"node_modules", ".git"}]
                for fn in filenames:
                    if fn.endswith(".html") and not fn.startswith("404"):
                        html_files.append(Path(dirpath) / fn)
            if not html_files:
                print(f"[ERROR] No .html files found inside {p}", file=sys.stderr)
                return 1
            for hf in sorted(html_files)[:30]:
                results.append(evaluate_html(str(hf), hf.read_text(encoding="utf-8", errors="ignore")))
        else:
            print(f"[ERROR] Target not found: {target}", file=sys.stderr)
            return 1

    any_fail = any(r["status"] == "FAIL" for r in results)
    if args.json:
        print(json.dumps({"verdict": "FAIL" if any_fail else "PASS", "results": results}, indent=2))
        return 1 if any_fail else 0

    print(f"=== SURFACE READINESS REPORT ({len(results)} surface(s)) ===")
    for r in results:
        print(f"\n[{r['status']}] {r['target']} (title: {r['title']!r})")
        for e in r["errors"]:
            print(f"  ERROR : {e}")
        for w in r["warnings"]:
            print(f"  WARN  : {w}")
        if not r["errors"] and not r["warnings"]:
            print("  Clean : All HTML landmark, image alt, link, and SEO checks passed.")

    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
