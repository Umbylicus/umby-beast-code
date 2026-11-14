# Universal Capability & Model-Tier Routing Matrix

`beast-code` is runtime-neutral. Never hardcode vendor-specific model IDs that break on other hosts, and never simulate subagents when running in a single-thread environment.

## 1. Detect Host Capabilities First

At session start, note which of these capabilities exist in your current environment:
- **Delegation / Subagents:** Native subagent or swarm spawning (`invoke_subagent`, `Task`, Claude subagents, Cursor agents, Grok subagents).
- **Browser / Visual Capture:** Built-in browser agent, Playwright MCP, or local CLI (`npx playwright`, headless Chrome).
- **Shell Execution:** Ability to run `python3` static verifiers, `npm`/`pnpm`/`bun` dev servers, typecheckers, and test suites.
- **Interactive Question Tool:** Structured multiple-choice UI tool vs. plain-text conversational questions.

## 2. Role-to-Strength Routing (When Multi-Model Selection Exists)

If your host lets you pick models for delegated tasks, match the cognitive demand of the role rather than using one setting blindly:

| Role | Cognitive Demand | Recommended Tier | Fallback Rule |
| :--- | :--- | :--- | :--- |
| **Coordinator / Architect / Discovery** | Deep product synthesis, aesthetic taste, architectural tradeoffs | Parent chat's primary frontier model (e.g., Gemini 4 Carbon, Claude Opus 5.5, Fable 5.2 at high effort) | Always runs in the initiating top-level conversation. |
| **Scoped Slice Builder (`builder`)** | Accurate, fast TypeScript/JSX/CSS implementation from a locked spec | Inherit parent frontier model, or host's high-speed frontier coding tier when building disjoint slices in parallel | Omit explicit `model` parameter if host model slugs are unknown so it inherits cleanly. |
| **Visual & UX Critic (`design-critic`)** | Multimodal spatial reasoning over rendered mobile/desktop screenshots | Strongest multimodal frontier model available (ideally a *different* family from the builder when cross-model pools exist) | Inherit parent model in a **fresh subagent context** so it has zero builder bias. |
| **Clarity Auditor (`comment-slicer`)** | Skeptical code reading, hunting narration comments, suppressions & alibis | Fast, high-precision reasoning tier in a **read-only** fresh subagent | Run `slicer_scan.py` + explicit read-only self-audit pass if subagents are unavailable. |
| **Human Copywriter (`sick-social`)** | Voice nuance, burstiness control, idiomatic sharpness | Strongest prose/judgment frontier model + mandatory `sick_social_lint.py` pass | Any frontier model paired with strict `sick_social_lint.py` enforcement. |

## 3. Subagent Hygiene Rules

1. **Single Coordinator:** Only the top-level chat owns the user brief, playbook checklist, git integration, and final verification. Child builders and critics do not recursively spawn grandchildren unless explicitly running `arena`.
2. **Disjoint Write Ownership:** Never assign two parallel builders to edit the same file, global CSS token sheet, or shared router config simultaneously. Lock shared primitives (`tokens.css`, core UI primitives, types) in a sequential Phase A before fanning out route/section builders in Phase B.
3. **Fresh Context for Review:** Never ask a builder subagent to grade its own UI or code clarity. Spawn a fresh read-only critic and pass only: (a) user intent & brief, (b) target files/URLs/screenshots, and (c) the critic role prompt.
4. **Honest Single-Agent Fallback:** If no subagent tool exists, run the deterministic scripts (`preflight_recon.py`, `audit_ui_slop.py`, `slicer_scan.py`, `sick_social_lint.py`, `verify_surface_readiness.py`) and perform a dedicated critique pass after rendering. Label the review `local self-audit + static scripts` rather than claiming independent multi-agent sign-off.
