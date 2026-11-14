# Gemini / Antigravity Workspace Rules — Umby Beast Code Standard

For all website, storefront, design system, web application, and content tasks, follow the **`beast-code`** skill tree (`~/.gemini/config/skills/` or `.agents/skills/`):

- Read `beast-code/SKILL.md` to route tasks across `discover`, `architect`, `craft`, `motion`, `archetypes`, `evolve`, `arena`, `comment-slicer`, `sick-social`, and `verify`.
- Enforce OKLCH semantic tokens, concentric border radii, fluid `clamp()` typography, `tabular-nums`, and zero visual AI-slop tropes (`audit_ui_slop.py`).
- Enforce human burstiness and zero AI tells across all UI copy, blogs, and social posts via `sick-social` (`sick_social_lint.py`).
- After code batches, run `comment-slicer` (`slicer_scan.py`). Before completion, verify live rendered viewports (`375px`, `768px`, `1440px`, `1920px`) using the browser subagent or Playwright and confirm zero console/hydration errors (`verify`).
