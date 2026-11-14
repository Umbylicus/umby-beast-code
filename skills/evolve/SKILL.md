---
name: evolve
description: Audits, refactors, restyles, and upgrades existing brownfield websites and web apps without breaking production URLs, SEO equity, analytics hooks, checkout flows, or user state. Executes baseline visual capture, dead-code subtraction, global token lifts, and one-wave component migrations. Use whenever updating, redesigning, modernizing, or adding to an existing website codebase.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Evolve: Brownfield Website Audit & Surgical Upgrade Engine

> **Standing rules apply.** Before changing anything, read [`../beast-code/references/standing-rules.md`](../beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

Most agent failures on existing websites happen because the agent either **timidly patches inline Tailwind classes onto broken HTML** (creating Frankenstein CSS) or **recklessly nukes routes, SEO slugs, form handlers, and analytics hooks** while chasing a fresh look.

Read [`references/migration-and-seo-safety.md`](references/migration-and-seo-safety.md) before modifying routes, URLs, or shared layouts.

---

## The 6-Step Brownfield Upgrade Protocol

### 1. Inventory Sacred Contracts Before Editing
Run `preflight_recon.py` and build a compact **Protected Surface List**:
- Every existing route path and dynamic slug (`/pricing`, `/blog/[slug]`, `/products/[handle]`, `/api/*`).
- SEO equity: `<title>` keywords, canonical tags, `sitemap.xml`, `robots.txt`, `301` redirects, and JSON-LD structured data.
- Revenue & integration wires: Stripe/Shopify checkout actions, auth callbacks, CRM/webhook form field `name` attributes, and analytics event IDs.

### 2. Capture the Visual & Technical Baseline
Before editing styles or markup:
- Boot the app locally and screenshot key routes at `375px` and `1440px`.
- Run `audit_ui_slop.py` and `slicer_scan.py` to quantify existing hex sprawl, contrast bugs, dead components, and suppressions.

### 3. Subtract Dead Weight Before Adding New Layers
- Delete commented-out sections, unused CSS rules, orphaned duplicate components (`HeroOld.tsx`), and conflicting utility overrides first. Building on a clean floor prevents specificity wars.

### 4. Execute a Root Token Lift First
Before rewriting individual sections, upgrade the global CSS custom properties / Tailwind theme (`--bg-*`, `--ink-*`, `--border-*`, `--font-*`, `--radius-*` per [`../craft/SKILL.md`](../craft/SKILL.md)):
- A clean root token upgrade elevates 80% of an existing site's typography, spacing, and surface polish in one atomic, reversible commit.

### 5. Finish Every Migration
When replacing a shared primitive or redesigning page sections:
- Do not introduce `ButtonV2` alongside `Button` and leave half the site half-migrated unless the user explicitly requested a single-page scope.
- Migrate all in-scope callers to the upgraded component, verify compilation and rendering, and delete the legacy file in the same step.

### 6. Prove Upgrade Quality & Zero Regression
- Compare before vs. after screenshots side by side across `375px` and `1440px`.
- Verify every route in Step 1's Protected Surface List renders `200 OK` with intact form/checkout payloads and upgraded metadata via [`../verify/SKILL.md`](../verify/SKILL.md).
