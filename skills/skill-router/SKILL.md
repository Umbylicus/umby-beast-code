---
name: skill-router
description: Navigates the Beast Code skill tree, sharpens rough user prompts into concrete multi-billion-dollar engineering and design briefs without executing prematurely, and guides multi-model setup across Claude, Gemini, Fable/Codex, Grok, and Cursor. Use when unsure which skill fits or when asked to '/skill-router' or 'sharpen my prompt'.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Skill Router: Skill Tree Navigator & Prompt Sharpener

## Mode 1: Skill Tree Router (When the User Asks Which Skill Fits)

Identify the user's goal in one sentence and hand them the exact command:
- **Build or upgrade anything end to end (website, app, tool, backend, game):** Use **`beast-code`** (orchestrates the entire tree automatically).
- **Write human-sounding social posts (X, LinkedIn, HN, Threads), blog posts, or landing copy:** Use **`sick-social`**.
- **Purge narration comments, dead code, workarounds, and `@ts-ignore` slop from code:** Use **`comment-slicer`**.
- **Run a 2–3 candidate parallel design bakeoff or adversarial break-test:** Use **`arena`**.
- **Run a 4-viewport visual critique, accessibility, and SEO launch check:** Use **`verify`**.
- **Make or improve a game:** Use **`game-mode`** (planning interview until an agreed `docs/game-plan.md`, then scaffold, build, ten-critic loop).
- **Score a build against the best in its category and loop until it clears a bar:** Use **`critic-mode`** (it asks for a quality level and how many critics).
- **Fix a bug at its cause:** Use **`debug`**.
- **Plan long or multi-session work in files:** Use **`build-plan`**.
- **Build a database, API, webhook, job, or integration:** Use **`backend`**.
- **Check security and privacy before launch:** Use **`secure`**.
- **Commit, open a pull request, or answer review comments:** Use **`ship`**.
- **Surgical direct access:** `discover` (intake brief), `architect` (domain types & stack), `craft` (OKLCH tokens & UI physics), `motion` (springs & scrollytelling), `archetypes` (Apple/Shopify/Stripe/Linear page blueprints), `evolve` (brownfield upgrades).

---

## Mode 2: Prompt Sharpener (When Asked to *"Sharpen"* a Prompt Before Building)

Do **not** execute the build yet. Rewrite the user's rough prompt so it includes what a Staff Design Engineer at Apple, Stripe, or Linear would specify upfront—while keeping genuine product choices open as bracketed slots:

1. **Audience, Skepticism & Primary Viewport Action**
2. **Aesthetic Archetype & 3 Real Craft Benchmarks** (from `../discover/references/aesthetic-archetypes.md`)
3. **Domain State & Interactive Proof Mechanic** (live sandbox, URL-backed filters, optimistic cart—replacing static filler)
4. **Explicit Anti-Slop Constraints** (OKLCH tokens, concentric radii, `sick-social` copy lint, `comment-slicer` clarity pass)
5. **Definition of Verified Done** (`375px`/`768px`/`1440px`/`1920px` real-browser inspection + zero console/hydration errors)

Return **only** the sharpened prompt inside a copyable block plus 2–3 open choices for the user to fill in or approve.
