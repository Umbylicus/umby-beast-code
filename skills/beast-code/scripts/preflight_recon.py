#!/usr/bin/env python3
"""
Beast Code Preflight Workspace Recon
Zero-dependency repository inspector for greenfield vs. brownfield classification.
Usage: python3 preflight_recon.py [target_dir] [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "node_modules",
    ".next",
    ".nuxt",
    ".svelte-kit",
    ".astro",
    "dist",
    "build",
    "out",
    "coverage",
    ".turbo",
    ".vercel",
    "__pycache__",
    ".venv",
    "venv",
}


def read_json_safe(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def detect_package_manager(root: Path) -> str:
    if (root / "bun.lock").exists() or (root / "bun.lockb").exists():
        return "bun"
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "package-lock.json").exists():
        return "npm"
    return "none-detected"


def scan_workspace(root: Path) -> dict:
    if not root.exists():
        return {"error": f"Path does not exist: {root}"}

    top_entries = [p.name for p in root.iterdir() if not p.name.startswith(".DS_Store")]
    pkg_path = root / "package.json"
    pkg = read_json_safe(pkg_path) if pkg_path.exists() else {}
    deps = {
        **pkg.get("dependencies", {}),
        **pkg.get("devDependencies", {}),
    }

    frameworks = []
    for key, label in [
        ("next", "Next.js"),
        ("astro", "Astro"),
        ("react", "React"),
        ("vue", "Vue"),
        ("nuxt", "Nuxt"),
        ("svelte", "Svelte"),
        ("@remix-run/react", "Remix"),
        ("react-router", "React Router"),
        ("@shopify/hydrogen", "Shopify Hydrogen"),
        ("vite", "Vite"),
    ]:
        if key in deps:
            frameworks.append(f"{label} ({deps[key]})")

    styling = []
    for key, label in [
        ("tailwindcss", "Tailwind CSS"),
        ("@tailwindcss/postcss", "Tailwind v4 PostCSS"),
        ("@tailwindcss/vite", "Tailwind v4 Vite"),
        ("sass", "Sass/SCSS"),
        ("styled-components", "styled-components"),
    ]:
        if key in deps:
            styling.append(f"{label} ({deps[key]})")

    motion_3d = []
    for key, label in [
        ("motion", "Motion"),
        ("framer-motion", "Framer Motion"),
        ("gsap", "GSAP"),
        ("lenis", "Lenis"),
        ("@studio-freight/lenis", "Lenis (legacy)"),
        ("three", "Three.js"),
        ("@react-three/fiber", "React Three Fiber"),
        ("@react-three/drei", "Drei"),
    ]:
        if key in deps:
            motion_3d.append(label)

    ui_primitives = []
    for key, label in [
        ("@base-ui-components/react", "Base UI"),
        ("react-aria-components", "React Aria"),
        ("vaul", "Vaul"),
        ("sonner", "Sonner"),
        ("cmdk", "cmdk"),
        ("lucide-react", "Lucide Icons"),
        ("@phosphor-icons/react", "Phosphor Icons"),
    ]:
        if key in deps:
            ui_primitives.append(label)
    if any(k.startswith("@radix-ui/") for k in deps):
        ui_primitives.append("Radix UI")
    if (root / "components.json").exists():
        ui_primitives.append("shadcn/ui config")

    testing = []
    for key, label in [
        ("@playwright/test", "Playwright"),
        ("playwright", "Playwright"),
        ("vitest", "Vitest"),
        ("jest", "Jest"),
        ("@axe-core/playwright", "axe-core Playwright"),
    ]:
        if key in deps:
            testing.append(label)

    route_files: list[str] = []
    style_files: list[str] = []
    token_signals: list[str] = []
    source_count = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        rel_dir = Path(dirpath).relative_to(root)
        for fname in filenames:
            rel_file = str(rel_dir / fname) if str(rel_dir) != "." else fname
            ext = Path(fname).suffix.lower()
            if ext in {".ts", ".tsx", ".js", ".jsx", ".astro", ".vue", ".svelte", ".mdx"}:
                source_count += 1
                if re.search(r"(^|/)(page|route|layout)\.(tsx|ts|jsx|js|astro|svelte)$", rel_file) or rel_file.startswith(("pages/", "src/pages/", "app/", "src/app/")):
                    if len(route_files) < 40:
                        route_files.append(rel_file)
            if ext in {".css", ".scss"}:
                style_files.append(rel_file)
                try:
                    css_text = (Path(dirpath) / fname).read_text(encoding="utf-8", errors="ignore")
                    if "--" in css_text and (":root" in css_text or "@theme" in css_text):
                        token_signals.append(rel_file)
                except Exception:
                    pass
            if fname == "index.html" and len(route_files) < 40:
                route_files.append(rel_file)

    mode = "greenfield"
    if source_count > 3 or len(style_files) > 1 or len(route_files) > 1:
        mode = "brownfield"
    elif len(top_entries) == 0:
        mode = "empty-directory"

    agent_files = [
        f
        for f in ["AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules"]
        if (root / f).exists()
    ]

    return {
        "workspace": str(root.resolve()),
        "classification": mode,
        "package_manager": detect_package_manager(root),
        "scripts": list(pkg.get("scripts", {}).keys()),
        "frameworks": frameworks,
        "styling": styling,
        "ui_primitives": ui_primitives,
        "motion_and_3d": motion_3d,
        "testing": testing,
        "typescript": (root / "tsconfig.json").exists(),
        "source_file_count": source_count,
        "style_files": style_files[:15],
        "token_files_detected": token_signals[:10],
        "sample_routes": route_files[:25],
        "agent_instruction_files": agent_files,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect workspace before web build/upgrade.")
    parser.add_argument("path", nargs="?", default=".", help="Workspace directory path")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    report = scan_workspace(Path(args.path))
    if args.json:
        print(json.dumps(report, indent=2))
        return 0 if "error" not in report else 1

    if "error" in report:
        print(f"[ERROR] {report['error']}", file=sys.stderr)
        return 1

    print(f"=== PREFLIGHT RECON: {report['workspace']} ===")
    print(f"Mode Classification : {report['classification'].upper()}")
    print(f"Package Manager     : {report['package_manager']}")
    print(f"Frameworks          : {', '.join(report['frameworks']) or 'None detected'}")
    print(f"Styling             : {', '.join(report['styling']) or 'None detected'}")
    print(f"UI Primitives       : {', '.join(report['ui_primitives']) or 'None detected'}")
    print(f"Motion / 3D         : {', '.join(report['motion_and_3d']) or 'None detected'}")
    print(f"Testing             : {', '.join(report['testing']) or 'None detected'}")
    print(f"TypeScript          : {'Yes' if report['typescript'] else 'No'}")
    print(f"NPM Scripts         : {', '.join(report['scripts']) or 'None'}")
    print(f"Source Files        : {report['source_file_count']}")
    print(f"Token CSS Files     : {', '.join(report['token_files_detected']) or 'None detected'}")
    print(f"Sample Routes       : {', '.join(report['sample_routes'][:10]) or 'None detected'}")
    print(f"Agent Rules Present : {', '.join(report['agent_instruction_files']) or 'None'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
