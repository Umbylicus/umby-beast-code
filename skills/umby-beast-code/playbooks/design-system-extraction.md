# Playbook: Design System Extraction & Token Unification

Use when turning a scattered multi-page codebase into a clean, single-source-of-truth design system, or establishing a shared `ui` package in a monorepo.

## Mandatory Checklist

1. **Audit Existing Values (`../../umby-evolve/SKILL.md`):** Run `preflight_recon.py` and `audit_ui_slop.py` across the repo to catalog all hardcoded colors, font sizes, border radii, shadows, and duplicate button/input/modal implementations.
2. **Authoritative Semantic Token Layer (`../../umby-craft/SKILL.md`):** Consolidate primitives into a two-tier CSS custom property architecture:
   - **Scale Primitives:** OKLCH neutral & brand steps, fluid `clamp()` type steps, 4/8pt spacing scale, easing curves.
   - **Semantic Tokens:** `--bg-canvas`, `--bg-surface`, `--bg-elevated`, `--ink-primary`, `--ink-secondary`, `--ink-muted`, `--border-hairline`, `--accent-primary`, `--status-danger`, etc., switching cleanly between light and dark schemes.
3. **Core Primitive Contracts (`../../umby-architect/SKILL.md`):** Build composable, accessible primitives (`Button`, `Input`, `Select`, `Dialog`/`Drawer`, `Card`, `Badge`, `Tabs`, `Tooltip`) with strict variant unions (`cva` or typed CSS modules) rather than open-ended boolean prop soup.
4. **Migrate & Delete Legacy (`../../umby-evolve/SKILL.md`):** Migrate routes component-by-component, deleting superseded one-off components and hardcoded hex values in the same verified pass.
5. **System Showcase & Visual Gate (`../../umby-verify/SKILL.md`):** Render all primitive states (light/dark, hover/focus/disabled/error) and verify migrated production routes across `375px` and `1440px`.
