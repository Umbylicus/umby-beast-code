#!/usr/bin/env python3
"""Umby Game Mode folder scaffold and checker.

  python3 game_scaffold.py init  <project-dir> --engine phaser|three|godot
  python3 game_scaffold.py check <project-dir>

`init` creates the folder layout, an empty asset manifest, CREDITS.md, and starter docs.
It never overwrites an existing file.

`check` fails (exit 1) when:
  - a runtime asset file has no manifest entry
  - a manifest entry points at a missing file, has no license, or repeats an id
  - an asset file name breaks the naming rule
  - an unexpected file sits in the project root
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SHARED = ["assets/src-art", "LICENSES", "docs", "tests", "scripts", ".umby/critic/evidence"]
LAYOUTS = {
    "phaser": [
        "src/config", "src/scenes", "src/entities", "src/systems", "src/ui", "src/level", "src/utils", "src/types",
        "assets/sprites", "assets/atlases", "assets/tilesets", "assets/audio/sfx", "assets/audio/music",
        "assets/fonts", "assets/shaders", "assets/data",
    ],
    "three": [
        "src/core", "src/scenes", "src/entities", "src/systems", "src/render", "src/loaders", "src/ui", "src/data",
        "public/models", "public/textures", "public/audio/sfx", "public/audio/music",
    ],
    "godot": [
        "addons", "scenes/main", "scenes/player", "scenes/enemies", "scenes/levels", "scenes/ui",
        "scripts", "systems", "resources",
        "assets/sprites", "assets/tilesets", "assets/fonts", "assets/shaders",
        "assets/audio/sfx", "assets/audio/music", "assets/models",
    ],
}
ASSET_ROOTS = ["assets", "public"]
ASSET_SUFFIXES = {
    ".png", ".webp", ".jpg", ".jpeg", ".svg", ".gif", ".avif",
    ".ogg", ".mp3", ".wav", ".opus", ".m4a",
    ".woff", ".woff2", ".ttf", ".otf",
    ".glb", ".gltf", ".ktx2", ".basis", ".obj",
    ".glsl", ".wgsl", ".gdshader", ".tmj", ".tsx", ".tres",
}
NOT_ASSETS = {"src-art", "data", "atlases"}
NAME_RULE = re.compile(r"^[a-z0-9][a-z0-9_\-]*(\.[a-z0-9]+)+$")
ROOT_FILES_OK = re.compile(
    r"^(index\.html|package(-lock)?\.json|pnpm-lock\.yaml|yarn\.lock|bun\.lockb?|tsconfig.*\.json|vite\.config\.\w+|"
    r"project\.godot|export_presets\.cfg|icon\.svg(\.import)?|README\.md|CREDITS\.md|LICENSE(\.md|\.txt)?|"
    r"\.gitignore|\.gitattributes|\.editorconfig|\.prettierrc.*|eslint\.config\.\w+|\.eslintrc.*|\.nvmrc|\.env\.example)$"
)

DESIGN_MD = """# Design

## Pitch
One paragraph: the player's main verb, what makes a run interesting, what makes this game its own.

## Intake answers
- Genre and comparables:
- Platform and engine: {engine}
- Scope of first build:
- Art and audio source:
- Quality level (A, B, or C):

## Benchmarks (quality bars only, nothing is copied)
| Aspect | Benchmark game | Source or "opinion" |
| :--- | :--- | :--- |
"""
BALANCE_MD = "# Balance\n\nDifficulty curve, tuning values, and what each change was meant to do.\n"
CREDITS_MD = "# Credits\n\nGenerated from `assets/manifest.json`. List every asset whose license asks for credit.\n"
GITIGNORE = "node_modules/\ndist/\nbuild/\n.godot/\n.DS_Store\n"


def write_new(path: Path, text: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"  created {path}")


def init(root: Path, engine: str) -> int:
    for rel in SHARED + LAYOUTS[engine]:
        (root / rel).mkdir(parents=True, exist_ok=True)
    write_new(root / "assets/manifest.json", "[]\n")
    write_new(root / "CREDITS.md", CREDITS_MD)
    write_new(root / "docs/design.md", DESIGN_MD.format(engine=engine))
    write_new(root / "docs/balance.md", BALANCE_MD)
    write_new(root / ".gitignore", GITIGNORE)
    if engine == "godot":
        write_new(root / "assets/src-art/.gdignore", "")
        write_new(root / "docs/.gdignore", "")
    for d in sorted(p for p in root.rglob("*") if p.is_dir() and ".git" not in p.parts and not any(p.iterdir())):
        write_new(d / ".gitkeep", "")
    print(f"Scaffolded a {engine} game layout in {root}")
    return 0


def asset_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for base in ASSET_ROOTS:
        folder = root / base
        if not folder.is_dir():
            continue
        for f in folder.rglob("*"):
            rel = f.relative_to(root)
            if f.is_file() and f.suffix.lower() in ASSET_SUFFIXES and not (set(rel.parts) & NOT_ASSETS):
                files.append(rel)
    return sorted(files)


def check(root: Path) -> int:
    problems: list[str] = []
    manifest_path = root / "assets/manifest.json"
    entries: list[dict] = []
    if not manifest_path.exists():
        problems.append("assets/manifest.json is missing (run init)")
    else:
        try:
            entries = json.loads(manifest_path.read_text(encoding="utf-8"))
            if not isinstance(entries, list):
                raise ValueError("manifest must be a list")
        except (json.JSONDecodeError, ValueError) as exc:
            problems.append(f"assets/manifest.json is not valid: {exc}")
            entries = []

    listed: set[str] = set()
    ids: set[str] = set()
    for i, e in enumerate(entries, start=1):
        eid, file = str(e.get("id", "")).strip(), str(e.get("file", "")).strip()
        label = eid or f"entry {i}"
        if not eid:
            problems.append(f"manifest entry {i}: missing id")
        elif eid in ids:
            problems.append(f"manifest: id '{eid}' is used twice")
        ids.add(eid)
        if not file:
            problems.append(f"manifest {label}: missing file")
        elif not (root / file).is_file():
            problems.append(f"manifest {label}: file not found: {file}")
        listed.add(file)
        if not str(e.get("license", "")).strip():
            problems.append(f"manifest {label}: missing license")
        if e.get("license") not in {"original", "generated"} and not str(e.get("source", "")).strip():
            problems.append(f"manifest {label}: third-party asset needs a source")

    for rel in asset_files(root):
        if rel.as_posix() not in listed:
            problems.append(f"asset not in manifest: {rel.as_posix()}")
        if not NAME_RULE.match(rel.name):
            problems.append(f"bad asset name (use lowercase, digits, _ and -): {rel.as_posix()}")

    if root.is_dir():
        for f in sorted(root.iterdir()):
            if f.is_file() and not ROOT_FILES_OK.match(f.name):
                problems.append(f"stray file in project root: {f.name}")
    else:
        problems.append(f"project folder not found: {root}")

    print(f"=== GAME FOLDER CHECK: {root} ===")
    print(f"Manifest entries: {len(entries)} | asset files: {len(asset_files(root))}")
    for p in problems:
        print(f"  PROBLEM: {p}")
    print(f"VERDICT: {'FAIL' if problems else 'PASS'}")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold or check an Umby Game Mode project folder.")
    ap.add_argument("command", choices=["init", "check"])
    ap.add_argument("project")
    ap.add_argument("--engine", choices=sorted(LAYOUTS), default="phaser")
    args = ap.parse_args()
    root = Path(args.project)
    return init(root, args.engine) if args.command == "init" else check(root)


if __name__ == "__main__":
    raise SystemExit(main())
