# Playbook: Existing Website Upgrade (Brownfield Evolution)

Use when modernizing, restyling, de-slopping, refactoring, or expanding a live or existing website codebase.

## Mandatory Checklist

1. **Recon & Route/SEO Inventory (`../../evolve/SKILL.md`):** Run `preflight_recon.py`. Inventory all live routes, `<title>`/meta/canonical tags, JSON-LD schemas, analytics events, environment requirements, and critical conversion forms/checkouts. Nothing in this inventory may regress silently.
2. **Before-State Visual Baseline:** Boot the existing site locally and capture baseline screenshots at `375px` and `1440px` before changing styles. Note exact layout, contrast, typography, and copy failures.
3. **Alignment Check (`../../discover/SKILL.md`):** Confirm with the user (in <=4 focused questions if unstated) what brand equity must stay (logo, primary hex, domain copy facts) versus what should be replaced wholesale.
4. **Subtract Dead Weight First:** Remove conflicting CSS overrides, unused template blocks, stock purple-blue AI gradients, and duplicate component variants before layering new styles.
5. **Global Token Lift (`../../craft/SKILL.md`):** Upgrade the root CSS variable / Tailwind token layer first so typography scale, neutral surfaces, hairline borders, and focus rings elevate site-wide without breaking component APIs.
6. **Surgical Section & Copy Migration (`../../archetypes/SKILL.md` + `../../sick-social/SKILL.md`):** Upgrade high-impact views in ordered verifiable units (Navigation -> Hero -> Primary Proof/Product Flow -> Pricing/PDP -> Footer). Migrate callers and delete superseded components in the same unit. Rewrite generic copy via `sick-social` while preserving 100% of verified product facts.
7. **Clarity & Slop Audit (`../../comment-slicer/SKILL.md`):** Run `slicer_scan.py` and `audit_ui_slop.py` on the branch diff.
8. **Before/After Parity & Regression Gate (`../../verify/SKILL.md`):** Compare new `375px`/`768px`/`1440px`/`1920px` renders against baseline, verify every inventoried route returns `200`, confirm zero broken links or lost SEO metadata via `verify_surface_readiness.py`, and run existing test suites.
