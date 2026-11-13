# Token Physics: Exact Numbers for Billion-Dollar Web Interfaces

## 1. Fluid Typography Scale (`clamp()`)

Use 5 to 6 distinct type steps total. Timid `1px–2px` differences look accidental:

| Token | Role | Fluid Size (`375px` -> `1440px`) | Line Height | Letter Spacing | Weight |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `--text-hero` | Marketing Hero Display | `clamp(2.5rem, 1.6rem + 3.8vw, 4.75rem)` | `1.04` | `-0.035em` | `600` (or `400` Editorial Serif) |
| `--text-h1` | Page / Section H1 | `clamp(1.875rem, 1.4rem + 2vw, 3rem)` | `1.12` | `-0.028em` | `600` |
| `--text-h2` | Subsection H2 | `clamp(1.375rem, 1.15rem + 0.9vw, 1.875rem)` | `1.22` | `-0.02em` | `600` |
| `--text-h3` | Card / Module Title | `1.125rem` (`18px`) | `1.35` | `-0.012em` | `500`–`600` |
| `--text-body-lg` | Lead Subtitle / Intro | `clamp(1.0625rem, 1rem + 0.25vw, 1.25rem)` | `1.55` | `-0.005em` | `400` |
| `--text-body` | Standard Web Prose | `1rem` (`16px`) marketing / `0.875rem` (`14px`) dense app | `1.6` / `1.45` | `0em` | `400` |
| `--text-caption` | Metadata / Helper | `0.8125rem` (`13px`) | `1.4` | `+0.005em` | `400`–`500` |
| `--text-eyebrow` | Sparse Category Tag | `0.75rem` (`12px`) uppercase | `1.2` | `+0.07em` | `600` |

## 2. Spatial Rhythm Scale (4pt / 8pt Grid)

Permitted spacing tokens only: `2px` (optical nudge), `4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`, `96px`, `128px`.
- **Internal vs. External Law:** Padding inside a container (`16px–24px`) must always be smaller than the gap separating major section groups (`64px–128px`), and gap between icon + label (`8px`) must be smaller than gap between adjacent buttons (`12px`).
- **Container Max-Widths:**
  - Long-form reading / blog post: `680px` (`~65ch`)
  - Focused SaaS / editorial layout: `1120px`–`1200px`
  - Storefront / multi-column app grid: `1280px`–`1440px` with `clamp(16px, 4vw, 48px)` horizontal gutter.

## 3. Perceptual OKLCH Surface & Ink Architecture

Why OKLCH beats HSL/RGB: changing hue in HSL swings perceived brightness wildly (yellow looks blinding, blue looks muddy at `"50%"` lightness). In OKLCH (`oklch(Lightness Chroma Hue)`), equal `L` means equal human-perceived lightness.

### Light Mode Ratios (Example Hue `255` Cool Slate / Adapt `H` to Brand)
- `--bg-canvas`: `oklch(0.99 0.003 255)` (crisp daylight, subtle warmth/coolness)
- `--bg-subtle`: `oklch(0.968 0.005 255)` (secondary band or recessed well)
- `--bg-surface`: `oklch(1.00 0 0)` (elevated card over subtle canvas)
- `--ink-primary`: `oklch(0.17 0.012 255)` (rich charcoal, never harsh `#000` on pure white)
- `--ink-secondary`: `oklch(0.42 0.014 255)` (`>=7:1` AAA contrast)
- `--ink-muted`: `oklch(0.55 0.012 255)` (`>=4.6:1` AA contrast; never lighter for readable text!)
- `--border-hairline`: `oklch(0.17 0.012 255 / 0.09)`

### Dark Mode Ratios (Elevation = Lighter Surface, Never Inverted Shadows)
- `--bg-canvas`: `oklch(0.14 0.008 260)` (deep obsidian, not `#000000` unless hardware OLED stage)
- `--bg-surface`: `oklch(0.18 0.010 260)` (level 1 card)
- `--bg-elevated`: `oklch(0.22 0.012 260)` (popover / modal / command menu)
- `--ink-primary`: `oklch(0.96 0.005 260)`
- `--ink-secondary`: `oklch(0.72 0.010 260)`
- `--ink-muted`: `oklch(0.58 0.010 260)` (`>=4.5:1` over `--bg-canvas`)
- `--border-hairline`: `oklch(0.98 0.005 260 / 0.085)`
- `--highlight-top`: `inset 0 1px 0 oklch(1 0 0 / 0.08)`

## 4. Concentric Border Radius & Optical Nudges

- Pick **one** personality radius family per brand:
  - *Architectural / Luxury:* `0px`–`4px`
  - *Precision Pro-Tool / SaaS:* `6px` buttons/inputs, `10px–12px` cards, `16px` modals
  - *Hardware / Tactile Consumer:* `10px–9999px` buttons, `20px–28px` stage containers
- **Concentric Formula:** `innerRadius = Math.max(0, outerRadius - containerPadding)`.
- **Play Triangle / Asymmetric Icon Nudge:** Triangles and chevrons inside circular buttons have visual mass shifted toward the flat edge; nudge `1px–1.5px` toward the pointed tip for optical centering.
