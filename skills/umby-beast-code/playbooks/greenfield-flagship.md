# Playbook: Greenfield Flagship Build

Use when building a brand-new website, storefront, launch page, or web application from scratch.

## Mandatory Checklist

1. **Preflight & Scope Lock:** Run `preflight_recon.py` on target directory. State user goal, target audience, and deliverable boundaries.
2. **Bespoke Intake (`../../umby-discover/SKILL.md`):** Ask at most 4–5 high-contrast product & creative direction questions (or record autonomous defaults in `.umby/decisions.tsv` if explicitly granted). Lock the **Creative & Functional Contract**: one primary viewport action, chosen aesthetic archetype, 3 craft-caliber references, typography pair, OKLCH hue anchor, and section rhythm sequence.
3. **Architecture & Stack Selection (`../../umby-architect/SKILL.md`):** Choose the leanest stack matching the surface (e.g., Astro for content/marketing-first, Next.js App Router for interactive SaaS/headless commerce). Define domain types, URL-backed state, and server/client boundaries before creating components.
4. **Token & Primitive Foundation (`../../umby-craft/SKILL.md`):** Write root CSS custom properties (`tokens.css` / `@theme`) with fluid `clamp()` typography, 4/8pt spacing scale, hue-tinted OKLCH neutrals, single high-conviction accent, concentric radii, and hairline borders. Build core Button, Surface, Input, and Typography primitives with all interactive states (`hover`, `active`, `focus-visible`, `disabled`, `loading`).
5. **Category Blueprint & Copy Origination (`../../umby-archetypes/SKILL.md` + `../../sick-social/SKILL.md`):** Structure sections using the matched category blueprint (zero repeated 3-card icon rows). Draft all headlines, subheads, proof blocks, and microcopy via `sick-social` and verify with `sick_social_lint.py`.
6. **Vertical-Slice Implementation & Motion (`../../umby-motion/SKILL.md`):** Build the full user journey in verifiable slices (parallelizing disjoint sections via `agents/umby-builder.md` only after Step 4 tokens/primitives are locked). Add purposeful `120–220ms` ease-out/spring transitions and `prefers-reduced-motion` support.
7. **Clarity & Anti-Slop Sweep (`../../comment-slicer/SKILL.md`):** Run `slicer_scan.py` and `audit_ui_slop.py` across all authored files. Fix every `RESHAPE_REQUIRED` workaround, arbitrary hex leak, fake metric, or narration comment.
8. **Real-Browser 4-Viewport Gate (`../../umby-verify/SKILL.md`):** Render live in browser across `375px`, `768px`, `1440px`, and `1920px` (light & dark if supported). Run the 5-Lens Visual Critique, fix the top 3–5 visual/UX defects, verify zero console/hydration errors, and run `verify_surface_readiness.py` for SEO/landmarks.
