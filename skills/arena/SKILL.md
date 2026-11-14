---
name: arena
description: Orchestrates parallel multi-agent design bakeoffs, disjoint slice swarms, and adversarial cross-model stress testing. Spawns competing architectural or UI candidates in isolated worktrees/directories, scores them with a fresh critic, grafts the strongest micro-details into the winning base, or tries to break a candidate with run-proven findings. Includes clean sequential fallback for single-agent environments.
license: MIT
major: true
metadata:
  version: "1.1.0"
  tree: "beast-code"
  role: orchestrator
---

# Arena: Parallel Bakeoffs, Grafting & Adversarial Stress-Testing

> **Standing rules apply.** Before changing anything, read [`../beast-code/references/standing-rules.md`](../beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

## Skill selection (every task)

Follow the shared procedure in [`../beast-code/references/select-skills.md`](../beast-code/references/select-skills.md) using [`../beast-code/SKILLS-INDEX.md`](../beast-code/SKILLS-INDEX.md). State the roster before spawning candidates. Typical APPLY set: `discover` for the brief, `architect` / `craft` for each candidate, `builder` writers, `design-critic` + `comment-slicer` to judge, `verify` on the winner, `sick-social` if copy is in play.

Single-shot generation locks you into the first plausible layout or architecture the model samples. Use `arena` in two high-leverage modes:
- **Mode A — Design / Architecture Bakeoff ("Compete & Graft"):** Build 2–3 genuinely distinct candidates in parallel, judge rendered pixels/code against an explicit rubric, pick the strongest backbone, and graft the best 1–2 ideas from the runners-up.
- **Mode B — Adversarial Stress-Test ("Break It With Proof"):** Unleash fresh read-only critics (across diverse model families when available) to try to break a diff, UI flow, or architecture; keep **only** defects proven by a failing run, DOM check, or screenshot.

Read [`references/critic-and-judge-prompts.md`](references/critic-and-judge-prompts.md) for ready-to-dispatch subagent prompts.

---

## Mode A: Design & Architecture Bakeoff (6 Phases)

1. **Frame Contract & Rubric:**
   - Name the exact artifact (e.g., Homepage Hero + Interactive Product Stage) and 5 concrete grading criteria (5-second clarity, anti-slop visual craft, typographic hierarchy, interaction responsiveness, code cleanliness).
   - Assign each candidate (`Candidate 1`, `Candidate 2`, optionally `Candidate 3`) a **distinct structural archetype** from `../discover/references/aesthetic-archetypes.md`—never trivial color swaps.
2. **Isolate Output Scopes:**
   - Give every candidate a strictly isolated git worktree (`git worktree add`), branch, or route namespace (`/arena/a`, `/arena/b`, `/arena/c`) so writers never collide on shared files.
3. **Fan Out:**
   - *With subagents:* Launch all candidates concurrently in background using `agents/builder.md` role rules.
   - *Without subagents:* Build each candidate cleanly in its isolated route/directory without cross-pollination.
4. **Render & Cross-Judge:**
   - Capture `375px` and `1440px` screenshots of every candidate.
   - Spawn a fresh read-only judge (`agents/design-critic.md`—ideally on a different model family than the builders) with only the user brief, rubric, code paths, and screenshots.
5. **Pick Base & Graft Cleanly:**
   - Pick the single candidate whose spatial hierarchy and domain model are cleanest to maintain.
   - Inspect losing candidates once for superior micro-details (e.g., a sharper interactive toggle, better mobile nav collapse, stronger headline hook) and **re-implement those grafts natively** inside the winning token system—never copy-paste mismatched styles.
6. **Verify & Clean Up:**
   - Run `../verify/SKILL.md` and `../comment-slicer/SKILL.md` on the unified winner, then remove temporary arena routes/worktrees.

---

## Mode B: Adversarial Stress-Test (4 Phases)

1. **Scope & Intent:** State the exact branch diff / target routes and user intent in 3 sentences.
2. **Dispatch Breakers:** Spawn 1–3 fresh read-only critics (diverse models if supported) with the Adversarial Breaker prompt in [`references/critic-and-judge-prompts.md`](references/critic-and-judge-prompts.md).
3. **Keep Only Run-Proven Defects:** Re-run or visually confirm every claimed defect. Discard hypothetical nitpicks, aesthetic bike-shedding, or unverified guesses. Deduplicate shared root causes.
4. **Report Ranked Findings:** Present confirmed defects with exact file/line, reproduction command or viewport screenshot, user impact, and minimal root-cause fix.
