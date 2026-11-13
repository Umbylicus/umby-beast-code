# End-to-End Operating Manual: How to Use the `umby-beast-code` Skill Tree

## The Core Mental Model

You only need to remember **three primary entry commands** in day-to-day work:

1. **`umby-beast-code`** (`/umby-beast-code`, `$umby-beast-code`, or *"Use umby-beast-code to..."*) — Your master entry point for **building any new website/app** OR **updating, restyling, debugging, and scaling any existing website/app**. It inspects the project, asks 4–5 high-leverage questions when intent is missing, picks the exact execution playbook, and pulls in every other skill automatically.
2. **`sick-social`** (`/sick-social`, `$sick-social`, or *"Use sick-social to..."*) — Your direct entry point whenever you want **human-sounding social media posts, X threads, LinkedIn essays, launch posts, changelogs, or full blog posts** with zero AI tells, verified by a deterministic burstiness and lexicon linter. (`umby-beast-code` also calls `sick-social` automatically whenever writing website copy!)
3. **`comment-slicer`** (`/comment-slicer`, `$comment-slicer`, or *"Run comment-slicer on this diff"*) — Your ruthless clarity and anti-slop code auditor. Hunts AI narration comments, dead JSX corpses, `@ts-ignore` / `eslint-disable` / `!important` cowards, and workaround alibis, demanding clean structural fixes. (`umby-beast-code` also runs `comment-slicer` automatically after every code batch!)

All other skills in the tree (`umby-discover`, `umby-architect`, `umby-craft`, `umby-motion`, `umby-archetypes`, `umby-evolve`, `umby-arena`, `umby-verify`, `umby-help`) can be invoked directly whenever you want surgical control, or left to `umby-beast-code` to orchestrate automatically.

---

## Workflow 1: Building a Brand-New Flagship Website (Greenfield)

### Example Prompt
```text
/umby-beast-code Build a flagship marketing website and interactive pricing calculator for [Brand Name], a B2B treasury platform for hardware startups.
```

### What Happens Step by Step
1. **Preflight Recon (`preflight_recon.py`):** Sees an empty or fresh repo. Never wastes questions on observable file facts.
2. **Surgical Discovery (`umby-discover`):** Asks 4–5 sharp questions (or states explicit defaults if you added *"run autonomously"*):
   * Primary conversion action (e.g., book a live demo vs. self-serve sandbox signup)?
   * Aesthetic direction & tension (e.g., *Precision Dark Monolith* like Linear/Raycast vs. *Swiss Editorial Light* like Stripe Press/Mercury)?
   * Proof assets available now (real metrics/logos/product flows vs. honest interactive product simulation)?
   * Preferred stack (e.g., Next.js App Router + Tailwind v4 vs. Astro 5 + React Islands)?
3. **Architecture & Token Lock (`umby-architect` + `umby-craft`):**
   * Writes CSS custom properties in OKLCH (`starter-tokens.css` adapted to your brand hue), fluid `clamp()` typography, concentric border radii, and layout rhythm **before** building page sections.
   * Models interactive state (e.g., the pricing calculator inputs, currency toggles, URL query sync) as clean typed structures.
4. **Category Blueprint & Human Copy (`umby-archetypes` + `sick-social`):**
   * Structures non-repetitive section rhythm (Hero with live interactive treasury sandbox -> Contrast proof strip -> Asymmetric bento workflow -> Spec-table security breakdown -> Transparent calculator -> Direct CTA).
   * Runs every headline, subhead, and microcopy string through `sick-social` + `sick_social_lint.py` so zero *"Unlock the future of seamless finance"* slop survives.
5. **Motion & Interaction Polish (`umby-motion`):**
   * Applies `120–200ms` snappy `cubic-bezier(0.16, 1, 0.3, 1)` transitions, `tabular-nums` on animated numbers, and `prefers-reduced-motion` fallbacks.
6. **Slicer Clarity Sweep (`comment-slicer`):**
   * Runs `slicer_scan.py` + `audit_ui_slop.py` + fresh review pass to strip narration comments, arbitrary hex leaks, fake social proof, and weak types.
7. **Real-Pixel Verification (`umby-verify`):**
   * Boots the dev server, captures `375px`, `768px`, `1440px`, and `1920px` viewports in light/dark modes, runs the 5-Lens Visual Critique, fixes the top layout/contrast issues, verifies zero console/hydration errors, and checks SEO metadata.

---

## Workflow 2: Updating or De-Slopping an Existing Website (Brownfield)

### Example Prompt
```text
/umby-beast-code Upgrade our current website in this repo. Keep all existing URLs, blog slugs, and Stripe checkout working, but make the design and copy look like a $5B category leader instead of a generic template.
```

### What Happens Step by Step
1. **Baseline & Blast-Radius Audit (`umby-evolve` + `preflight_recon.py`):**
   * Maps every existing route, `<title>`/canonical/JSON-LD tag, analytics hook, and checkout form contract so zero revenue or SEO equity breaks.
   * Screenshots the current live/local site across viewports to establish a before-state baseline.
2. **Subtract Before Adding:**
   * Identifies conflicting CSS files, stock purple-blue gradients, inconsistent spacing values, and redundant wrapper components.
3. **Global Token Lift First (`umby-craft`):**
   * Upgrades root typography, OKLCH color ramps, border hairlines, and button/input primitives globally so the entire site improves in coherence immediately.
4. **Section-by-Section Surgical Upgrade:**
   * Rebuilds high-impact surfaces (Navbar, Hero, Product Showcase, Pricing/PDP Buy Box, Footer) in verifiable increments, deleting legacy dead components in the same commit wave.
5. **Copy De-Slopping (`sick-social`) & Clarity Gate (`comment-slicer` + `umby-verify`):**
   * Rewrites generic copy while preserving real product facts, then proves route parity, mobile responsiveness, and Lighthouse/CWV health.

---

## Workflow 3: High-Stakes Design Bakeoff ("Compete Mode")

When you want the absolute best hero section, landing page direction, or tricky UI interaction and have subagent/worktree support:

```text
/umby-arena Run a 3-way bakeoff for our homepage hero and interactive product showcase: Candidate A (Editorial High-Key Light), Candidate B (Precision Dark Hardware Stage), Candidate C (Split Interactive Sandbox). Judge against conversion clarity and craft, then graft the best details into the winner.
```

---

## Workflow 4: Writing Viral-Caliber Human Posts & Blogs with `sick-social`

### Example Prompts
```text
/sick-social Write an X thread + a LinkedIn founder post announcing that we cut our API p99 latency from 410ms to 28ms by deleting our caching layer and fixing 3 Postgres indexes. Raw notes: [paste rough notes]
```

```text
/sick-social Write a 1,400-word engineering & product blog post on why most AI analytics dashboards fail CFOs. Ask me 3 quick questions first to get our real customer stories.
```

### Why It Never Sounds Like AI
* Starts mid-friction (`in media res`), never with *"In today's fast-paced world..."*
* Mixes 3-word blunt sentences with 24-word specific explanations (enforced mathematically by `sick_social_lint.py` checking sentence-length standard deviation).
* Zero em-dashes (`—`), zero *"Not X, it's Y"*, zero forced rules of three, zero emoji bullet spam, zero LinkedIn broetry, and zero fake-profound closing summaries.

---

## Workflow 5: Autonomous / Overnight Execution

When stepping away for hours on a multi-page build or full-site migration:

```text
/umby-beast-code Run autonomously until complete. Build all 6 routes in docs/spec.md, run comment-slicer and umby-verify on every route, keep a decision log in .umby/decisions.tsv, and do not stop until every check passes locally. Do not push or deploy.
```

Under an explicit autonomous grant:
* Observable questions are settled by running code or prototypes, never pausing.
* Genuine product calls not covered by your spec take the most conservative reversible option and log the rationale + how to reverse it in `.umby/decisions.tsv`.
* Irreversible boundaries (production deploy, force-push, deleting user data, paid API spend, external emails) **still pause unconditionally**.

---

## Workflow 6: Critic Mode (score it, fix it, score it again)

```text
/umby-critic-mode Critique the checkout flow in this repo.
```

It asks two questions: how good it needs to be (A best in class at 9/10, B great at 7/10, C critique only) and how many critics to run. Each critic owns one aspect, compares it with the best product in the category for that aspect, explains why it is not a 10, and lists fixes for the next writer. Fresh writers apply the fixes, fresh critics score again, and the loop stops on a pass, a stall, or the round cap. Open `.umby/critic/graph.html` at any time to watch the scores.

## Workflow 7: Game Mode

```text
/umby-game-mode Make a small top-down roguelike that runs in the browser.
```

It asks about genre, engine, scope, art source, and quality level, scaffolds an organized project with an asset manifest, builds a playable core loop first, then runs ten critics, one per aspect of game quality. Games are original work: comparable games set the bar and nothing is copied from them.

