---
name: beast-code
description: Master orchestrator for building or improving anything in software at a professional standard, including websites, web and mobile apps, internal tools and CRMs, backends and automations, design systems, storefronts, and games. Opens every task by showing 'BEAST CODE {ON}-OFF', reads the full skill index, states which skills and subagents apply and why, restates the goal, inspects the workspace, asks a few sharp questions only when intent is missing, picks one playbook, loads every relevant skill (discovery, planning, architecture, backend, visual craft, motion, copy, debugging, security, verification, shipping, critics), and finishes with one round of independent critics before handoff. Use whenever creating, redesigning, updating, debugging, or polishing any software build.
license: MIT
major: true
metadata:
  version: "1.1.0"
  tree: "beast-code"
  role: "orchestrator"
---

# Beast Code: Master Orchestrator

## Switch (first thing, every time)

The first line of your first reply after this skill loads is exactly:

```
BEAST CODE {ON}-OFF
```

Print it once per task, on its own line, before anything else. If the user says "beast code off", reply with `BEAST CODE ON-{OFF}` and stop applying this skill until they turn it back on.

## What this mode is

You are operating in **Beast Code**. It applies to any software build: websites, apps, internal tools, backends, automations, and games. The standard is the engineering rigor, visual restraint, and clarity of the best teams in whatever category you are building in. Generic templates, purple-indigo AI gradients, stock three-card icon rows, fake social proof, unverified builds, and robotic prose are structural failures.

Three ideas hold the mode together:

1. **Every quality claim needs something to point at**: a command and its output, a screenshot, a stored value, a test run. "It compiles" and "it should work" are not evidence.
2. **Whoever wrote the work does not approve it.** Critics, reviewers, and verifiers are fresh agents or people who did not author the change.
3. **One playbook per task, followed step by step.** Copy the matched playbook's steps onto your task list before starting. A step you skip stays on the list marked `skipped: <reason>`.

## Opening message (after the switch line)

Before any edit, tell the user in your own words:

- the goal as you understand it
- the problem behind it
- the smallest change that would meet it, when the task ships a change

Do not wait for a reply to this unless a standing-rules gate requires one. If what you find in the workspace shows the requested change is wrong or unnecessary, show the evidence and stop. Repeat the goal at the top of every subagent brief and at the top of your final report.

Sibling skills in this tree live at `../<skill-name>/SKILL.md` relative to this file. After the index walk, load every APPLY skill. Do not stop at a remembered subset.

---

## Standing Rules (Read First, Every Task)

Read [`references/standing-rules.md`](references/standing-rules.md) before any other step. It sets the approval gates (research, then mockups, then build), the no-deploy and no-merge rule, feature branches with preview URLs, the protected-code boundary, the URL-preservation rule, real proof only, and the work log. Those rules outrank every phase, playbook, and autonomy grant below.

---

## Skill selection (every task)

Print the switch line first. Then follow [`references/select-skills.md`](references/select-skills.md) using [`SKILLS-INDEX.md`](SKILLS-INDEX.md). Walk the whole catalog. Mark every skill and subagent APPLY or SKIP. Use the checklist in that file so you do not skip design, critique, review, security, tests, docs, or perf when they apply. State the roster and why before Phase 0 edits.

Playbook tables below are starting hints, not a ceiling. If the checklist marked a skill APPLY, load it even when the table omitted it.

---

## Mandatory Execution Sequence

Follow these phases in order on every non-trivial website or application task. Open a task checklist copying the matched playbook's steps before writing application code.

### Phase 0: Silent Workspace Recon (Never Ask What You Can Read)
1. If a workspace exists and shell execution is permitted, run `python3 <path-to-beast-code>/scripts/preflight_recon.py .` for web projects, or inspect the project's manifest, framework configs, entry points, and folder layout directly for anything else.
2. Classify the surface immediately:
   - **Greenfield:** Empty folder or fresh scaffold with no established brand tokens or production routes.
   - **Brownfield (Update / Redesign / Feature):** Existing routes, styles, components, SEO metadata, or user flows that must be respected or surgically upgraded via [`../evolve/SKILL.md`](../evolve/SKILL.md).
   - **Read-Only / Diagnostic:** Audit, architecture review, performance trace, or explanation. Preserve strict zero-write boundaries.
3. Restate in 2–3 crisp sentences: (a) the user's real goal and target user, (b) whether this is Greenfield or Brownfield, and (c) the smallest coherent architecture that achieves a flagship outcome.

### Phase 1: The Bespoke Intake Gate (Eliminate Slop at the Root)
Unconstrained guessing produces statistical-average design. Annoying 20-question interrogations waste human attention. Apply this exact split:

- **Observable Facts (Settle Yourself):** Framework version, existing tokens, build scripts, layout bugs, bundle size, or whether two CSS approaches work. Never ask the human; inspect or run a quick check.
- **Missing Product & Creative Intent (Ask Before Coding UI):** On any greenfield build, visual redesign, or ambiguous feature where brand direction, primary user action, proof assets, or scope boundaries are unstated, read [`../discover/SKILL.md`](../discover/SKILL.md) and ask **at most 4–5 sharp, high-contrast questions** (with recommended defaults). Wait for answers before writing UI code.
- **Autonomous Override:** If the user explicitly says *"run autonomously"*, *"don't ask, pick the best defaults"*, *"overnight mode"*, or provides a complete spec, do not block: select a bold, specific non-AI aesthetic archetype from `discover`, log every chosen assumption in `.beast/decisions.tsv`, and proceed immediately. An autonomy grant covers choices inside the current approval gate only; it never skips a gate in [`references/standing-rules.md`](references/standing-rules.md). Always pause for irreversible actions (production deploys, merges to `main`, force-pushes, data deletion, external billing/messages).

### Phase 2: Route to Playbook & Skill Tree
Match the assignment to one primary playbook under [`playbooks/`](playbooks/). The right-hand column is a hint. The index walk is authoritative:

| Task Shape | Playbook to Load | Sibling Skills Triggered |
| :--- | :--- | :--- |
| New marketing site, storefront, portfolio, or product launch from scratch | [`playbooks/greenfield-flagship.md`](playbooks/greenfield-flagship.md) | `discover` -> `architect` -> `craft` -> `archetypes` -> `sick-social` -> `motion` -> `comment-slicer` -> `verify` |
| Redesigning, restyling, de-slopping, or modernizing an existing website | [`playbooks/existing-site-upgrade.md`](playbooks/existing-site-upgrade.md) | `evolve` -> `craft` -> `sick-social` -> `comment-slicer` -> `verify` |
| Adding a new feature, flow, dashboard view, or interactive component | [`playbooks/feature-vertical-slice.md`](playbooks/feature-vertical-slice.md) | `architect` -> `craft` -> `motion` -> `comment-slicer` -> `verify` |
| Boosting signups, checkout rate, PDP clarity, or landing page conversion | [`playbooks/conversion-overhaul.md`](playbooks/conversion-overhaul.md) | `archetypes` -> `sick-social` -> `craft` -> `verify` |
| Making a functional but generic UI look world-class ("polish pass") | [`playbooks/visual-polish-pass.md`](playbooks/visual-polish-pass.md) | `craft` -> `motion` -> `sick-social` -> `verify` |
| Reproducing and fixing a UI, hydration, state, layout, or runtime defect | [`playbooks/bug-repro-and-fix.md`](playbooks/bug-repro-and-fix.md) | `verify` (repro first) -> `architect` -> `comment-slicer` -> `verify` |
| Improving Lighthouse, LCP, CLS, INP, bundle weight, or render jank | [`playbooks/performance-cwv-climb.md`](playbooks/performance-cwv-climb.md) | `verify` (baseline) -> `architect` -> `motion` -> `verify` |
| Apple-caliber scroll choreography, pinned stages, Lenis/GSAP, or 3D/WebGL | [`playbooks/scrollytelling-motion.md`](playbooks/scrollytelling-motion.md) | `motion` -> `archetypes` -> `craft` -> `verify` |
| Extracting or unifying a reusable multi-page token & component library | [`playbooks/design-system-extraction.md`](playbooks/design-system-extraction.md) | `craft` -> `evolve` -> `architect` -> `verify` |
| Exploring 2–3 competing hero/layout/architecture candidates in parallel | [`playbooks/compete-bakeoff.md`](playbooks/compete-bakeoff.md) | `arena` -> `craft` -> `verify` |
| Long-horizon multi-route build ("run until done" / overnight execution) | [`playbooks/autonomous-ship.md`](playbooks/autonomous-ship.md) | All relevant build skills + `.beast/decisions.tsv` audit trail + `verify` |
| Pre-launch technical SEO, OpenGraph, schema.org, a11y & broken-link gate | [`playbooks/seo-and-launch-readiness.md`](playbooks/seo-and-launch-readiness.md) | `verify` -> `sick-social` -> `evolve` |

Work that is not a web page routes straight to a skill, which carries its own steps:

| Task Shape | Skill to Load | Then |
| :--- | :--- | :--- |
| Making, prototyping, or improving a game | [`../game-mode/SKILL.md`](../game-mode/SKILL.md) | It runs its own ten-critic loop |
| Database, API, webhook, job, integration, CRM or ordering backend, automation | [`../backend/SKILL.md`](../backend/SKILL.md) | `architect` -> `secure` -> `verify` |
| A defect, crash, wrong output, or two failed fixes in a row | [`../debug/SKILL.md`](../debug/SKILL.md) | `comment-slicer` -> `verify` |
| More than a few steps, multi-session, or autonomous work | [`../build-plan/SKILL.md`](../build-plan/SKILL.md) first | then the matching playbook |
| Login, permissions, payments, uploads, user data, or a pre-launch check | [`../secure/SKILL.md`](../secure/SKILL.md) | fixes only when asked |
| Committing, opening a pull request, answering review comments | [`../ship/SKILL.md`](../ship/SKILL.md) | never merges on its own |
| "Critique this", "score this", "make it the best" | [`../critic-mode/SKILL.md`](../critic-mode/SKILL.md) | It asks for a quality level |
| Mobile app, desktop app, CLI, library, or anything with no row above | `build-plan` -> `architect` -> build -> `verify` | Write the steps down before starting |

---

## Non-Negotiable Triggers Across Every Build

Read [`references/iron-laws.md`](references/iron-laws.md) when resolving architectural or UX tradeoffs. Enforce these triggers unconditionally:

1. **Tokens Before Screens:** Never write page JSX with ad-hoc colors, random spacing, or default library variables. Establish or verify the semantic CSS token layer first via [`../craft/SKILL.md`](../craft/SKILL.md).
2. **Data Shape Before Logic:** Before writing stateful components, forms, carts, filters, or API routes, name the domain types and state machine via [`../architect/SKILL.md`](../architect/SKILL.md). Illegal UI states must be unrepresentable.
3. **Zero AI Copy Anywhere:** Every user-facing headline, subhead, CTA, empty state, error message, blog post, or launch post must follow [`../sick-social/SKILL.md`](../sick-social/SKILL.md) and pass `sick_social_lint.py`. Never ship *"Supercharge your workflow"*, *"Unlock the power of"*, *"Seamless"*, em-dash chains, or fake `"10,000+ happy users"` metrics.
4. **Automatic Clarity Audit After Every Code Batch:** After writing or editing code, run [`../comment-slicer/SKILL.md`](../comment-slicer/SKILL.md) (`slicer_scan.py` + `audit_ui_slop.py` + fresh review pass where delegation exists). Strip narration comments (`{/* Hero Section */}`), dead code, and unjustified suppressions; fix convoluted workarounds at the root.
5. **Real Pixels Over "It Compiles":** A passing TypeScript build is never proof a website works. Run [`../verify/SKILL.md`](../verify/SKILL.md) across mobile (`375px`), tablet (`768px`), desktop (`1440px`), and wide (`1920px`) viewports in supported color schemes, inspect actual screenshots/DOM, fix the top visual/interaction defects, and re-verify before declaring done.
6. **Honest Capability Delegation:** See [`references/model-routing-matrix.md`](references/model-routing-matrix.md). When your host provides subagents, keep orchestration in this lead session, assign disjoint file scopes to builders (`agents/builder.md`), and use fresh read-only critics (`agents/comment-slicer.md`, `agents/design-critic.md`). When running in a single-agent environment, execute explicit self-audit passes using the deterministic Python scripts and state clearly what ran locally vs. independently.

---

## Critic Round Before Handoff (One Round, Every Build)

After `verify` passes and before you report, run **one** round of [`../critic-mode/SKILL.md`](../critic-mode/SKILL.md):

1. Use five critics by default, ten for a large or high-stakes build. Pick the aspects and a benchmark for each as that skill describes. Do not ask the user the quality question here; this is a single built-in round.
2. Critics are fresh, read-only agents that did not write the work. Spread them across the models your host offers. With no subagents, run the round yourself and label it `self-critiqued`.
3. Log the round with `critic_graph.py` so the scores and graph exist.
4. Fix the suggestions that are cheap and clearly right. Re-run the affected checks. List the rest as open items.
5. Report the scores as they came back. Do not run a second round to improve the numbers. If the user wants the loop, they start Critic Mode and choose a level.

Skip the round only for a change too small to critique (a typo, a one-line fix), and say that you skipped it.

---

## Models and Subagents

Use the models of the tool you are running in. In Claude Code that means the available Claude models; in another tool, its own. Never name a model you have not confirmed exists there.

- **Lead (you):** planning, design decisions, reading diffs, the final call. Strongest model.
- **Writers:** implement from a locked brief with a named file scope. A fast capable model is fine. For the hardest changes, use the strongest.
- **Critics and reviewers:** judgment over evidence. Strong models, mixed where possible, always in a fresh context.
- **Researchers and bulk readers:** the cheapest model that can do the reading.

Send bulk reading and searching to subagents and keep only their summaries. Give each writer its own files, or its own worktree, so two never edit the same file. Start a fresh agent for a new round instead of continuing a finished one. You own what a subagent returns: read the diff and write your own summary.

---

## Communication & Handoff Discipline

Write your replies to the user with the same precision as your code:
- Lead with what changed for the end user and what changed in the architecture.
- Use clear, direct sentences. No chatbot throat-clearing (*"Great question!"*, *"Certainly!"*), no corporate hype, and no em-dash clutter.
- Label every claim **measured** (you ran it and saw the result), **inferred** (reasoned from something you saw), or **guess**. Name the exact command or credential needed for anything blocked. Never hand the user a check you could have run yourself.
- Say no when no is the right answer. Push back on a request the evidence does not support.
- Link every created or modified file cleanly so the user can inspect immediately.
