---
name: verify
description: Proves websites and web applications actually work and look world-class before delivery. Executes real-browser rendering across 4 mandatory viewports (375px, 768px, 1440px, 1920px) in light and dark modes, runs the 5-Lens Visual Critique loop with mandatory defect repair, verifies zero console/hydration errors, checks keyboard accessibility, Core Web Vitals, and audits technical SEO/HTML landmarks via a bundled script. Use before declaring any web build, redesign, UI feature, or bug fix complete.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Verify: Real-Browser Pixel Proof, A11y & Launch Gate

> **Standing rules apply.** Before changing anything, read [`../beast-code/references/standing-rules.md`](../beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

`npm run build` exiting `0` proves only that syntax parsed. Never declare a user-facing website or web app complete from reading JSX alone.

Read [`references/launch-gate-checklist.md`](references/launch-gate-checklist.md) for full pre-release audit criteria.

---

## Step 1: Boot & Render Across 4 Real Viewports

Start the local dev or production server and inspect the live rendered DOM using whichever browser tool your host provides (native `browser` subagent, Playwright MCP, `npx playwright screenshot`, or headless Chrome CLI):

| Viewport | Dimensions | Primary Defect Class Caught |
| :--- | :--- | :--- |
| **Mobile Portrait** | `375 x 812` | Horizontal overflow (`scrollWidth > innerWidth`), crushed navbars, tiny `<44px` tap targets, giant unscaled headings |
| **Tablet / Split** | `768 x 1024` | Awkward 2-vs-3 column grid orphans, broken sidebar collapse transitions |
| **Standard Desktop** | `1440 x 900` | Primary above-the-fold composition, line-length measure, sticky buy-box / TOC alignment |
| **Wide Monitor** | `1920 x 1080` | Unconstrained full-bleed stretching, 140-character unreadable lines, broken background edges |

Capture **both Light and Dark schemes** whenever theme switching is supported.

*Honest Capability Rule:* If your runtime strictly forbids opening a browser or running a local server (e.g., restricted cloud sandbox or pure chat window), state `BROWSER_UNVERIFIED` explicitly and provide the exact Playwright/local check command for the user—never fabricate visual confirmation.

---

## Step 2: Run the 5-Lens Visual Critique (Fix Top Issues Before Handoff)

Actually open and look at the captured PNGs (ideally delegating critique to a fresh `agents/design-critic.md` subagent that did not author the CSS):

1. **The 5-Second Clarity Lens:** Within 5 seconds on `1440px` and `375px`, is the product's mechanism and single primary action unmistakable?
2. **The Squint & Grayscale Lens:** Blur your eyes or view desaturated—is there one dominant focal anchor with clear step-downs, or is everything shouting at equal weight?
3. **The Alignment & Geometry Lens:** Do left edges align along clean vertical rails? Are nested border radii concentric? Is spacing visibly tighter *inside* groups than *between* groups?
4. **The Stress & State Lens:** Test hover, active press, keyboard `Tab` focus rings (`:focus-visible`), mobile menu drawer open/close, empty/error form submission, and long text wrapping.
5. **The Zero-Slop Scan:** Verify zero items from `../craft/references/anti-slop-banlist.md` remain.

**Mandatory Repair Loop:** Rank the top 3–5 visual or interaction defects uncovered, fix them in code, and **re-capture the affected viewports** to confirm the fix worked without introducing new regressions.

---

## Step 3: Runtime Console, Hydration & Accessibility Check

- Verify **zero** uncaught `console.error`s, failed network `404` assets, or React/SSR hydration mismatch warnings during page load and primary interaction.
- Press `Tab` sequentially from the top of the document: focus must move in logical visual order, never get trapped outside modals, never disappear (`outline: none`), and trigger buttons on `Enter`/`Space` and overlays closed on `Escape`.

---

## Step 4: Run the Automated HTML, Landmark & SEO Readiness Script

Run the bundled verifier against either built `.html` output (`out/`, `dist/`, `.next/server/app/`) or a live local URL (`http://localhost:3000`):

```bash
python3 <path-to-verify>/scripts/verify_surface_readiness.py http://localhost:3000
# or against static/built HTML files:
python3 <path-to-verify>/scripts/verify_surface_readiness.py ./dist
```

Resolve all reported `ERROR`s (`missing <main>`, `multiple or zero <h1>`, `missing <title>` / meta description, `dead href="#"`, `unlabeled inputs/images`) before final handoff.

---

## Step 5: Numbers Gate (Definition of Done)

Work is not done until every line below is checked and reported with its actual result. If a check cannot be run here, mark it `UNVERIFIED`, say why, and give the owner the exact command or link. Never report a number you did not measure.

1. **Lighthouse 95+:** Run Lighthouse in mobile mode against the production build or preview URL (not the dev server). Performance, Accessibility, Best Practices, and SEO must each score `95` or higher on every key page template. Report the four scores per page.
2. **Mobile at 430px and 375px:** Besides the Step 1 viewports, capture `430 x 932` (large phones) and `375 x 812`. Zero horizontal overflow, no clipped text, tap targets `>=44px` at both widths.
3. **Rich Results Test:** For every page that ships JSON-LD, run Google's Rich Results Test (`https://search.google.com/test/rich-results`) on the preview URL or the pasted page code. Zero errors, and the structured data must match what is visibly on the page.
4. **Broken links:** Crawl every internal link and check every external link on the changed pages. Zero `404`s, zero dead `#` links. On a rebuild, also request every URL from the old site and confirm each returns `200` or a `301` to its mapped replacement.
5. **Accessibility AA:** Lighthouse accessibility is only a floor. Also confirm the Step 3 keyboard walk, WCAG AA contrast (`>=4.5:1` text, `>=3:1` large text and UI), labeled form fields, and `alt` text.
6. **Tests passing:** Run the project's existing test suite, typecheck, and production build. All pass. New behavior has a behavioral test where the project has a test setup.
7. **Real copy only:** No lorem ipsum, placeholder text, sample names, or invented proof anywhere in the rendered pages. `audit_ui_slop.py` and `sick_social_lint.py` pass on the touched files.
