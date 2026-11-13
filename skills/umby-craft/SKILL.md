---
name: umby-craft
description: Enforces multi-billion-dollar visual design engineering, perceptual OKLCH color systems, fluid typography, concentric border geometry, optical alignment, full interactive state matrices, and strict elimination of the 30 visual AI-slop patterns. Includes a starter CSS token system and an automated UI slop scanner script. Use whenever creating, styling, restyling, or reviewing any web page, component library, storefront, or application interface.
license: MIT
metadata:
  version: "1.0.0"
  tree: "umby-beast-code"
---

# Umby Craft: Visual Systems, Optical Physics & Zero-Slop UI

> **Standing rules apply.** Before changing anything, read [`../umby-beast-code/references/standing-rules.md`](../umby-beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

Taste is not magic; taste is **systematic restraint plus optical precision**. Unconstrained agents scatter colors, invent random spacing, center everything, slap glowing purple gradients behind generic headlines, and ship only the happy-path screenshot. Follow this exact sequence to produce Apple-, Stripe-, Linear-, and Aesop-caliber interfaces every time.

Read on demand:
- [`references/token-physics.md`](references/token-physics.md): Exact numeric rules for OKLCH color, fluid type, spacing, concentric radii, and optical alignment.
- [`references/starter-tokens.css`](references/starter-tokens.css): Production CSS custom property & Tailwind v4 `@theme` baseline.
- [`references/anti-slop-banlist.md`](references/anti-slop-banlist.md): The 30 visual tells of AI-generated UI and their exact fixes.

---

## Step 1: Establish or Adopt the Token System First

1. Inspect the codebase before writing styles. If semantic tokens already exist, **use them exclusively** and improve them at `:root` rather than introducing stray hex values.
2. On greenfield projects (or brownfield token lifts), create your root token sheet from [`references/starter-tokens.css`](references/starter-tokens.css) tuned to the project's chosen archetype from `umby-discover`.
3. **Zero Stray Values:** Every surface, text tone, border, radius, shadow, and spacing step in component code must resolve to a system token or scale step.

---

## Step 2: Build Grayscale Hierarchy Before Color

Lay out every view so its hierarchy passes the **Squint Test** in pure grayscale:
- **One Focal Anchor Per Viewport:** Step down clearly from primary headline to supporting body (`>=1.5x` size contrast on marketing heroes; `>=1.25x` in dense app views). Never pair `15px` and `16px` expecting hierarchy.
- **Proximity Before Boxes:** Group related elements with tight internal spacing (`4px–12px`) and separate distinct sections with generous spatial breath (`64px–128px` on marketing; `24px–32px` in apps) **before** reaching for card borders. Never put cards inside cards inside cards.
- **Disciplined Alignment:** Left-align multi-line prose and data. Center only short symmetric hero lockups or compact empty states, and never exceed `65–72ch` line measure on body copy (`45–55ch` on subtitles).

---

## Step 3: Apply Perceptual Color & Surface Architecture

1. **Hue-Tinted OKLCH Neutrals:** Pure `#000000` dark modes halate on OLED screens, and pure `#808080` grays look dead. Tint your neutral ramp subtly (`0.005–0.015` OKLCH chroma) toward your brand hue.
2. **The 90 / 8 / 2 Budget:** 90% neutral canvas and ink, 8% quiet structural steps (`1px` alpha hairlines, subtle raised fills), and 2% high-conviction accent reserved strictly for the primary CTA and active selection.
3. **Hairlines & Specular Edges Over Muddy Shadows:** Separate surfaces via `2–4%` lightness shifts or `1px` low-alpha borders (`rgba(15,23,42,0.08)` light / `rgba(255,255,255,0.08)` dark). On dark raised surfaces, add a `1px` top inner highlight (`inset 0 1px 0 rgba(255,255,255,0.09)`) instead of heavy outer drop shadows.

---

## Step 4: Enforce Optical Precision Details

- **Concentric Nested Radii:** Whenever an inner element sits inside a rounded container with padding $P$, set $R_{\text{inner}} = \max(0, R_{\text{outer}} - P)$ (e.g., `20px` outer card with `8px` padding -> `12px` inner image/button radius).
- **Typography Mechanics:**
  - Maximum **2 font families** (1 display + 1 body, or 1 super-family + 1 monospace for code/metrics).
  - Apply `text-wrap: balance` to headings and short callouts; `text-wrap: pretty` to body paragraphs.
  - Apply `font-variant-numeric: tabular-nums` to all prices, counters, tables, timers, and axis labels so digits never jitter.
  - Compress display tracking (`-0.025em` to `-0.04em` above `36px`); open uppercase micro-label tracking (`+0.06em` to `+0.08em` at `11px–12px`).
- **Icons:** One consistent icon set (`Lucide`, `Phosphor`, or custom `1.5px` stroke SVGs) optically sized to adjacent text (`16px`–`18px` beside `14px`–`16px` text). **Never use emojis as UI icons or feature bullets.**

---

## Step 5: Implement the Complete State & Accessibility Matrix

Every interactive surface must intentionally handle all 9 states:
1. `default`
2. `hover` (subtle brightness/surface shift; gated behind `@media (hover: hover)`)
3. `active` / pressed (`transform: scale(0.985)` or `translateY(1px)` tactile feedback)
4. `focus-visible` (`2px` high-contrast offset ring—never `outline: none` without replacement)
5. `disabled` (`opacity: 0.45`, `cursor: not-allowed`, non-interactive)
6. `loading` (exact-geometry skeleton or inline spinner preserving button width so layout never shifts)
7. `empty` (clear explanation + one direct creation/reset action)
8. `error` (specific cause + human recovery step, paired with `aria-invalid` / `aria-describedby`)
9. `overflow` (long German words, 3-line titles, `0` items vs. `10,000` items, narrow `375px` mobile width)

Hit targets must be `>=44x44px` on touch viewports (`>=32px` dense desktop controls) with WCAG AA minimum contrast (`>=4.5:1` normal text, `>=3:1` large text and active UI boundaries).

---

## Step 6: Run the Deterministic UI Slop Scanner

Before handing off or moving to browser verification, run:
```bash
python3 <path-to-umby-craft>/scripts/audit_ui_slop.py <target-src-dir>
```
Resolve every `ERROR` and review every `WARN` against [`references/anti-slop-banlist.md`](references/anti-slop-banlist.md).
