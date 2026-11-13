---
name: umby-help
description: Navigates the Umby Beast Code skill tree, sharpens rough user prompts into concrete multi-billion-dollar engineering and design briefs without executing prematurely, and guides multi-model setup across Claude, Gemini, Fable/Codex, Grok, and Cursor. Use when unsure which skill fits or when asked to '/umby-help' or 'sharpen my prompt'.
license: MIT
metadata:
  version: "1.0.0"
  tree: "umby-beast-code"
---

# Umby Help: Skill Tree Navigator & Prompt Sharpener

## Mode 1: Skill Tree Router (When the User Asks Which Skill Fits)

Identify the user's goal in one sentence and hand them the exact command:
- **Build or upgrade anything end to end (website, app, tool, backend, game):** Use **`umby-beast-code`** (orchestrates the entire tree automatically).
- **Write human-sounding social posts (X, LinkedIn, HN, Threads), blog posts, or landing copy:** Use **`sick-social`**.
- **Purge narration comments, dead code, workarounds, and `@ts-ignore` slop from code:** Use **`comment-slicer`**.
- **Run a 2–3 candidate parallel design bakeoff or adversarial break-test:** Use **`umby-arena`**.
- **Run a 4-viewport visual critique, accessibility, and SEO launch check:** Use **`umby-verify`**.
- **Make or improve a game:** Use **`umby-game-mode`** (folder scaffold, asset tracking, ten-critic loop).
- **Score a build against the best in its category and loop until it clears a bar:** Use **`umby-critic-mode`** (it asks for a quality level and how many critics).
- **Fix a bug at its cause:** Use **`umby-debug`**.
- **Plan long or multi-session work in files:** Use **`umby-plan`**.
- **Build a database, API, webhook, job, or integration:** Use **`umby-backend`**.
- **Check security and privacy before launch:** Use **`umby-secure`**.
- **Commit, open a pull request, or answer review comments:** Use **`umby-ship`**.
- **Surgical direct access:** `umby-discover` (intake brief), `umby-architect` (domain types & stack), `umby-craft` (OKLCH tokens & UI physics), `umby-motion` (springs & scrollytelling), `umby-archetypes` (Apple/Shopify/Stripe/Linear page blueprints), `umby-evolve` (brownfield upgrades).

---

## Mode 2: Prompt Sharpener (When Asked to *"Sharpen"* a Prompt Before Building)

Do **not** execute the build yet. Rewrite the user's rough prompt so it includes what a Staff Design Engineer at Apple, Stripe, or Linear would specify upfront—while keeping genuine product choices open as bracketed slots:

1. **Audience, Skepticism & Primary Viewport Action**
2. **Aesthetic Archetype & 3 Real Craft Benchmarks** (from `../umby-discover/references/aesthetic-archetypes.md`)
3. **Domain State & Interactive Proof Mechanic** (live sandbox, URL-backed filters, optimistic cart—replacing static filler)
4. **Explicit Anti-Slop Constraints** (OKLCH tokens, concentric radii, `sick-social` copy lint, `comment-slicer` clarity pass)
5. **Definition of Verified Done** (`375px`/`768px`/`1440px`/`1920px` real-browser inspection + zero console/hydration errors)

Return **only** the sharpened prompt inside a copyable block plus 2–3 open choices for the user to fill in or approve.
