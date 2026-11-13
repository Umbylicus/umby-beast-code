# Master Research Report: Building Billion-Dollar Websites with Frontier Agents

## 1. Why Unconstrained Frontier Models Produce "AI Slop"

Frontier models like Gemini 4 Carbon, Claude Opus 5.5, Fable 5.2, and Grok have extraordinary coding and reasoning capacity, yet a raw prompt like *"Build a modern landing page for my AI analytics startup"* reliably produces recognizable "AI slop." That failure comes from four statistical mechanics in how language models sample tokens:

1. **Mode Collapse to the Training Mean.** Most public HTML/Tailwind repositories on GitHub are tutorials, hackathon prototypes, and unmodified shadcn/Bootstrap templates. Without explicit structural constraints, next-token prediction converges on `bg-slate-950`, `from-indigo-500 via-purple-500 to-pink-500`, `Inter` at uniform weights, centered hero blocks with glowing radial blobs, and three identical rounded-xl feature cards with Lucide icons in tinted squares.
2. **Code Before Intent or Data Shape.** Unconstrained agents start emitting JSX within 200 tokens. Because they have not locked a brand tension, an information hierarchy, a user task, or a domain state model, every component invents its own spacing (`p-5` here, `px-[22px]` there), colors, and boolean flags (`isOpen`, `isAnimating`, `hasError`).
3. **Blindness to Rendered Pixels.** Reading JSX does not reveal line-wrap orphans, broken contrast on translucent surfaces, mobile horizontal scrollbars, hydration flashes, or sluggish `ease-in` transitions. Agents declare victory because `npm run build` exited `0`, without ever opening a real viewport across breakpoints.
4. **Statistical Prose Flattening.** In both UI copy and blog/social writing, models optimize for universally safe phrasing. That produces low sentence-length variance (monotonous 14-to-18-word sentences), hollow contrast formulas (*"It's not just X, it's Y"*), em-dash chains, abstract buzzwords (*seamless, elevate, landscape, delve, supercharge*), and generic CTAs (*"Get Started"* repeated four times).

Eliminating AI slop permanently requires replacing "prompt and pray" with an **enforced procedural architecture**: upfront intent extraction, mathematical design tokens, domain state modeling, scoped implementation, deterministic static scanners, adversarial cross-review, and real-browser pixel verification.

---

## 2. How Multi-Billion-Dollar Web Teams Actually Engineer Quality

Studying the frontend systems of **Apple, Stripe, Linear, Shopify, and Amazon** reveals five distinct pillars that separate flagship websites from templates. Our `umby-beast-code` skill tree encodes all five directly into agent procedures.

### Apple: Narrative Pacing, Optical Physics, and Restraint
* **Contrast Oscillation:** Apple product pages never stack five dark sections of equal height. They alternate deep cinema stages (`#000000` / `#0a0a0c` for hardware/media drama) with high-key editorial breathers (`#f5f5f7` with `#1d1d1f` ink) to reset visual fatigue.
* **Concentric Geometry:** Nested containers never share the same border radius. Inner radius equals outer radius minus padding ($R_{\text{inner}} = \max(0, R_{\text{outer}} - P)$), keeping curvature optically parallel.
* **Scroll-Linked Physics Over Decorative Bounces:** Elements do not randomly float or bounce on scroll. Scroll progress drives meaningful physical state changes (hardware rotation, exploded layer reveals, optical zoom into a specific detail) at 60/120fps using GPU-composited `transform` and `opacity` or canvas frame sequences.
* **Headline Compression:** Tight display tracking (`-0.025em` to `-0.04em` above `40px`), generous body leading (`1.47` to `1.6`), `text-wrap: balance` on headlines, and zero exclamation marks.

### Stripe: Precision Surfaces, Live Product Sandboxes, and Perceptual Color
* **Interactive Proof Over Screenshots:** Instead of pasting static PNG screenshots of dashboards, Stripe builds lightweight, interactive, deterministic DOM miniatures of its actual product (live API request switchers, animated payment forms, interactive billing sliders) directly inside marketing sections.
* **Hairline Lighting Architecture:** Depth comes from `1px` borders with low-alpha contrast (`rgba(15, 23, 42, 0.08)` in light mode; `rgba(255, 255, 255, 0.08)` in dark mode) paired with a `1px` top inner specular highlight (`inset 0 1px 0 rgba(255, 255, 255, 0.12)`), rather than heavy, muddy drop shadows.
* **Perceptual Color Scales (OKLCH):** Neutral grays are tinted subtly (`0.008` to `0.018` chroma in OKLCH) toward the brand hue so surfaces feel cohesive rather than sterile.

### Linear & Raycast: Pro-Tool Density, Speed as UX, and Monochrome Discipline
* **92% Neutral, 8% Accent:** Chrome recedes completely. One sharp accent marks the primary action or active selection; semantic colors (amber, emerald, crimson) appear strictly for real system state.
* **Frequency-Bound Motion:** Actions executed dozens of times per day (command palettes, row selection, tab switching, filter toggles) complete in `80ms–140ms` with snappy `cubic-bezier(0.16, 1, 0.3, 1)` ease-out curves or high-stiffness springs—never sluggish `350ms` transitions that delay input.
* **Keyboard-First & Optimistic:** Every stateful mutation updates local UI state immediately with clean rollback on failure, paired with visible `focus-visible` rings and `Cmd+K` navigation.

### Shopify & Amazon: Conversion Velocity, Information Scent, and Zero Friction
* **Sub-Second First Input & LCP:** Amazon's classic latency research and Shopify's storefront telemetry both demonstrate that every `100ms` of interaction or load delay measurably erodes checkout completion. Above-the-fold hero images preload with explicit `width`/`height` (`CLS = 0.00`), while below-the-fold heavy media lazy-loads cleanly.
* **Above-the-Fold Buy Box Clarity:** On commerce PDPs, price, variant availability, shipping/return certainty, real review distribution, and the primary `Add to bag` trigger sit immediately accessible without scrolling past brand poetry.
* **URL-Backed State:** Selected size, color, sort order, active filter facets, and pagination live in URL search parameters so every view is shareable, reload-safe, and back-button predictable.

---

## 3. Lessons from Hackathon Winners, Design-Engineering Competitions & Elite Agent Workflows

Analyzing multi-time winners of Anthropic Claude Code Hackathons, Cursor/Vercel build competitions, Awwwards Site of the Month engineering breakdowns, and top production agent harnesses surfaces seven repeatable patterns:

1. **Work Backward from the 60-Second Walkthrough.** Winners never build database tables in isolation for four hours and bolt UI on at the end. They define the exact user journey first, build a runnable vertical slice with real interactive states in the first pass, and deepen data/integrations behind clean boundaries.
2. **Inspect First, Then Grill on Missing Intent.** Elite workflows separate *observable repository facts* (which the agent must read from `package.json`, `tsconfig.json`, and CSS files itself) from *human product intent* (brand positioning, target buyer, risk appetite, visual tension). Asking 4–5 sharp, high-contrast questions upfront prevents 95% of mid-build rewrites.
3. **Context Window Isolation via Scoped Subagents.** Dumping 40 file reads, build logs, and Playwright traces into a single conversation degrades model attention ("context rot"). Top builders keep one **Lead Coordinator** owning the spec and acceptance contract, while delegating disjoint write slices, static audits, and fresh-eye visual reviews to isolated subagents.
4. **Design It Twice (Parallel Bakeoffs + Grafting).** On high-leverage surfaces—particularly hero sections, navigation architecture, or complex state models—spawning two or three parallel candidates with distinct structural directions, judging them against an explicit rubric, picking the cleanest base, and grafting the best micro-details from the runners-up consistently beats any single-shot generation.
5. **Encode Rules in Scripts, Not Longer Prompts.** When an agent repeatedly makes a mistake (leaving narration comments, using em-dashes, introducing arbitrary hex values, forgetting mobile viewports), adding paragraph #47 to a prompt yields diminishing returns. Writing a 100-line deterministic check script that fails the step forces 100% compliance.
6. **Fresh-Context Adversarial Critique.** An agent reviewing code or screenshots it generated two turns ago suffers from confirmation bias. Passing raw diffs and rendered viewport screenshots to a *fresh* read-only critic (ideally on a different model family when available) uncovers layout collisions, fake states, and logic bugs immediately.
7. **Brownfield Respect ("Clear the Ground First").** When upgrading an existing production website, amateur agents pile new Tailwind classes, wrapper `<div>`s, and duplicate components on top of old ones. Senior workflows map existing routes and SEO metadata first, extract or upgrade the root token layer, delete dead legacy callers in the same wave, and verify visual parity or intentional improvement per route.

---

## 4. Optimal Multi-Model Routing Strategy (Gemini 4 Carbon, Claude Opus 5.5, Fable 5.2, Grok)

Every frontier model family exhibits distinct strengths. Our skill tree is **100% model-agnostic**—it runs end-to-end on a single model when needed, and unlocks cross-family leverage when multiple models are available:

| Cognitive Role | Primary Strength Needed | Optimal Model Tier / Examples | How the Skill Tree Uses It |
| :--- | :--- | :--- | :--- |
| **Lead Architect & Creative Director** | Long-horizon coherence, subtle aesthetic judgment, nuanced product interviewing, multi-file synthesis | **Claude Opus 5.5** / **Gemini 4 Carbon** / **Fable 5.2** (High reasoning effort) | Runs `umby-beast-code`, `umby-discover`, `umby-architect`, and owns final integration. |
| **Multimodal Visual & Layout Critic** | Spatial reasoning over rendered screenshots, detecting optical misalignment, contrast & overflow bugs | **Gemini 4 Carbon** / **Claude Opus 5.5** / **Fable 5.2** | Runs `umby-verify` screenshot critique (`agents/umby-design-critic.md`) across 4 viewports in light & dark mode. |
| **High-Velocity Scoped Builder** | Fast, surgical TypeScript/React/CSS execution against a locked data shape and token spec | **Grok** (high-speed code tier) / **Claude Opus 5.5** / **Gemini 4 Carbon** / **Fable 5.2** | Executes scoped vertical slices via `agents/umby-builder.md` with disjoint file ownership. |
| **Human-Voice Copywriter & Editor** | Nuanced cadence, subtext, wit, idiomatic rhythm, strict adherence to negative linguistic constraints | **Claude Opus 5.5** / **Fable 5.2** / **Gemini 4 Carbon** + `sick_social_lint.py` | Runs `sick-social` for X/LinkedIn posts, essays, blogs, headlines, and UI microcopy. |
| **Adversarial Breaker & Clarity Slicer** | Zero-sycophancy skepticism, hunting edge cases, race conditions, dead comments, and type suppressions | **Cross-Family Model** (e.g., if Lead is Claude, use Gemini or Grok; if Lead is Gemini, use Claude or Fable) | Runs `comment-slicer` (`agents/comment-slicer.md`) and `umby-arena` adversarial interrogation. |

---

## 5. Architecture of the `umby-beast-code` Universal Skill Tree

Rather than stuffing 15,000 words into a single monolithic prompt that starves context, the skill tree uses **Progressive Disclosure** (`SKILL.md` frontmatter discovery + on-demand leaf skills + `references/` manuals + `scripts/` deterministic verifiers):

```text
                         ┌──────────────────────┐
                         │       umby-beast-code       │  ◄── Invoke this ONE skill for any
                         │ (Master Orchestrator)│      website or web app build/update
                         └──────────┬───────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│ umby-discover │           │ umby-evolve   │           │   umby-help   │
│ (Brief & Dir.)│           │ (Update Sites)│           │(Sharpen/Setup)│
└───────┬───────┘           └───────┬───────┘           └───────────────┘
        │                           │
        ▼                           ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│umby-architect │──────────►│  umby-craft   │──────────►│  umby-motion  │
│(Domain & Stack│           │(OKLCH/Type/UI)│           │(Springs/Scroll│
└───────┬───────┘           └───────┬───────┘           └───────┬───────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   umby-archetypes    │
                         │(Apple/Shopify/Linear)│
                         └──────────┬───────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│  umby-arena   │           │  sick-social  │           │ comment-slicer │
│(Bakeoff/Critic│           │(Human Writing)│           │(Clarity/Slop) │
└───────┬───────┘           └───────┬───────┘           └───────┬───────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │     umby-verify      │
                         │(4-Viewport/CWV/SEO)  │
                         └──────────────────────┘
```

Every leaf skill works both **automatically** when `umby-beast-code` routes to it AND **standalone** when you invoke it directly (for example, calling `/sick-social` to draft a launch blog post or X thread, or calling `/comment-slicer` to purge slop from a pull request).
