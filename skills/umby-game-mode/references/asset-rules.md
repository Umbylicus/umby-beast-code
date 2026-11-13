# Asset rules

## Names

- Lowercase letters, digits, underscores, and hyphens. No spaces. Web servers treat `Player.png` and `player.png` as different files.
- Pattern: `<category>_<name>_<variant>_<frame>.<ext>`, for example `enemy_slime_idle_01.png`, `sfx_jump_small_01.ogg`, `ui_button_hover.png`.
- Pad frame numbers: `_01`, `_02`.
- Code refers to the manifest `id`, never the path, so files can move without code changes.

## Source and exported files

- Layered and project files (`.aseprite`, `.psd`, `.kra`, `.blend`, `.fbx`) live in `assets/src-art/`. They are not served and need no manifest entry.
- Runtime files are exported from them by a script in `scripts/`, so an export can be repeated.
- Only runtime files are bundled.

## Formats

- **2D images:** PNG or WebP. Pack sprites that load together into one atlas.
- **3D:** `.glb`, with mesh and texture compression when the files are large. Validate models before shipping.
- **Sound effects:** short, loaded and decoded during the loading screen.
- **Music:** a compressed looping format. No single audio format plays in every browser, so test on the browsers you target and ship a second format if one fails.
- **Fonts:** `woff2` on the web.

## The manifest

`assets/manifest.json` is a list. One entry per runtime asset:

```json
{
  "id": "enemy_slime_idle",
  "file": "assets/sprites/enemy/enemy_slime_idle_01.png",
  "type": "sprite",
  "license": "CC0-1.0",
  "source": "https://example.com/pack",
  "author": "Pack Author",
  "generated": false,
  "notes": ""
}
```

- `license` is required. Use `original` for work made in this project, an SPDX id for anything else, or `generated` with the tool named in `notes`.
- Add the entry when the file is added, not at the end.
- `CREDITS.md` lists every entry whose license asks for credit, and thanks the rest.

## Licensing

- Prefer public-domain (CC0) packs. Attribution licenses are fine when `CREDITS.md` carries the credit. Share-alike and non-commercial licenses need the user's OK first.
- Check the license of the exact file. Repackaged bundles sometimes carry a different license from the original.
- Save the license text in `LICENSES/` for every third-party pack and font.
- For generated assets, record the tool and date, and only claim what that tool's terms allow.
- Never ship an asset with no known license, and never one that depicts or imitates another game's characters, logos, or art.
