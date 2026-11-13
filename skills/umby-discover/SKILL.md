---
name: umby-discover
description: Conducts surgical, high-leverage creative and product discovery before building or redesigning a website or web app. Eliminates generic AI slop by resolving missing brand direction, buyer skepticism, conversion priority, aesthetic tension, and real proof assets in 4-5 sharp questions, then locking a concrete Creative and Functional Contract. Use at the start of any greenfield website/app build, rebrand, or underspecified UI request.
license: MIT
metadata:
  version: "1.0.0"
  tree: "umby-beast-code"
---

# Umby Discover: Surgical Brief & Creative Direction

> **Standing rules apply.** Before changing anything, read [`../umby-beast-code/references/standing-rules.md`](../umby-beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

Generic prompts force agents to guess, and an LLM's guess is the statistical average of the internet. Your job here is to lock a **specific, opinionated, category-leading product and visual identity** before writing a line of component code—without subjecting the user to a tedious 20-question survey.

---

## Step 1: Separate Observable Facts from Missing Intent

1. Check workspace files first (`package.json`, existing CSS tokens, brand assets, `README.md`, existing routes). **Never ask a question the repository already answers.**
2. Audit the user's request against the **Five Pillars of a Non-Slop Brief**:
   - **Pillar 1 — Job & Primary Action:** Who lands here, what skepticism do they carry, and what is the *single* action we want them to complete?
   - **Pillar 2 — Aesthetic Archetype & Tension:** Where does this sit visually? (Read [`references/aesthetic-archetypes.md`](references/aesthetic-archetypes.md) for the 12 non-AI archetypes.)
   - **Pillar 3 — Proof & Content Reality:** Do we have real product data, metrics, photography, or live interactive mechanics—or should we build an honest interactive simulation instead of fake `"10,000+ customers"` filler?
   - **Pillar 4 — Surface Scope & Stack:** Which pages/flows belong in Pass 1, and what stack constraints apply (Astro static speed vs. Next.js interactive app vs. Shopify headless)?
   - **Pillar 5 — Brownfield Constraints (Updates Only):** Which URLs, logos, brand hexes, or checkout/auth contracts are sacred?

---

## Step 2: Run the 4–5 Question Intake Gate

If 2 or more pillars above are genuinely missing (and the user did not request immediate autonomous execution), pause before writing UI code and ask **3 to 5 surgical questions** selected from [`references/question-bank.md`](references/question-bank.md).

### Rules for Asking Great Discovery Questions
- **Use Host Question UI When Available:** If your environment provides a structured multiple-choice question tool (e.g., `ask_question`), use it with 3–4 concrete, contrasting options per question and put your recommended choice first prefixed with `(Recommended)`. Otherwise, present a clean, numbered plain-text list.
- **Offer Concrete Contrasts, Not Open-Ended Homework:** Never ask *"What colors and fonts do you like?"* Instead offer sharp directional pairings: e.g., *"(Recommended) Precision Dark Monolith (Linear / Raycast caliber: obsidian `#0b0c0e`, crisp hairline borders, single electric accent, interactive product stage)"* vs. *"Editorial High-Key Light (Stripe Press / Mercury caliber: warm alabaster `#faf9f6`, editorial serif display + clean grotesk body, generous daylight spacing)"*.
- **Cap at 5 Questions Maximum:** One round of sharp questions is invigorating; three rounds of nitpicking feels broken.

---

## Step 3: Lock the Creative & Functional Contract

Once the user answers (or immediately using your best archetype match if running under an explicit autonomous grant), write down the compact **Design & Product Contract** (either inline in 12–15 lines or saved to `.umby/DESIGN_BRIEF.md` on multi-route projects):

1. **Audience & Skepticism:** One sentence naming who visits and the exact doubt the page must overcome in 5 seconds.
2. **Primary Viewport Action:** Exactly one primary CTA verb phrase (e.g., `"Start interactive sandbox"`, `"Add 250g bag · $24"`).
3. **Chosen Archetype & 3 Craft Benchmarks:** Named archetype from [`references/aesthetic-archetypes.md`](references/aesthetic-archetypes.md) + 3 real-world products whose *quality bar* (never copied IP/assets) anchors the build.
4. **Typography Pair & Scale:** Display family + Body family + Mono family, with explicit weights and tracking rules.
5. **OKLCH Palette Anchor:** Base surface lightness/hue tint, primary ink, hairline alpha, and the single high-conviction accent color.
6. **Section Rhythm Sequence:** Ordered list of 5–8 page beats where **no two adjacent sections share the same grid geometry**.
7. **Anti-Goals (Explicit Exclusions):** 3 specific clichés banned for this project (e.g., *"No purple-blue SaaS glow, no 3-column Lucide icon feature row, no unverified customer headshots"*).

Hand this locked contract directly to [`../umby-architect/SKILL.md`](../umby-architect/SKILL.md) and [`../umby-craft/SKILL.md`](../umby-craft/SKILL.md).
