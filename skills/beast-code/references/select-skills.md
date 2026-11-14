# Select skills from the index (shared)

Every **major** skill follows this procedure before writing application code or copy. Do not duplicate this logic in the skill body; read this file.

`game-mode` is the exception to "first thing": it runs its planning interview and writes `docs/game-plan.md` first, then runs this procedure with that plan as the job. Other majors run this immediately after their switch/banner line (if any) and standing rules.

This works in every supported CLI. After install, skills are siblings in the host skill directory (`~/.claude/skills`, `~/.cursor/skills`, `~/.codex/skills`, `~/.gemini/config/skills`, `~/.grok/skills`, `~/.agents/skills`, or `<project>/.agents/skills`). Read them as `../<name>/SKILL.md` relative to the skill that loaded this file. The catalog that is installed with this tree is [`../SKILLS-INDEX.md`](../SKILLS-INDEX.md) (from `beast-code/`) or [`SKILLS-INDEX.md`](../SKILLS-INDEX.md) beside this folder.

Subagents (`builder`, `design-critic`, `comment-slicer`) install into `~/.claude/agents` and `~/.cursor/agents`. If the host has no subagent directory, run those briefs yourself and label the pass `self-<role>`.

## Procedure

1. **Read the whole catalog.** Open `SKILLS-INDEX.md` for this tree (installed copy: `beast-code/SKILLS-INDEX.md`). Walk every skill and every subagent. Do not stop at a remembered shortlist or at the playbook's hint column.
2. **Name the job.** One sentence: what is being built or changed, for whom, and on what surface (greenfield site, brownfield upgrade, game, copy-only, backend, bug, critique, …).
3. **Mark every row APPLY or SKIP.** For each entry in the index, decide now. SKIP needs a one-line reason. APPLY means you will load that `SKILL.md` or agent brief and follow it, not merely mention the name.
4. **Run the checklist** so a relevant skill is not skipped:

   - [ ] **Intake / brief** (`discover`) — brand, audience, primary action, or scope is missing
   - [ ] **Plan** (`build-plan`) — more than a few steps, multi-session, or autonomous
   - [ ] **Architecture** (`architect`) — state, data shape, stack, or URL contracts
   - [ ] **Backend** (`backend`) — database, API, webhook, job, integration
   - [ ] **Visual craft** (`craft`) — UI, tokens, layout, states
   - [ ] **Motion** (`motion`) — interaction timing, scroll, animation
   - [ ] **Category blueprint** (`archetypes`) — a known site/app category
   - [ ] **Brownfield** (`evolve`) — existing URLs, SEO, checkout, or styles to keep
   - [ ] **Bakeoff / adversarial** (`arena`) — competing candidates or break-it review
   - [ ] **Copy** (`sick-social`) — any user-facing words
   - [ ] **Comments** (`comment-slicer`) — after code is written
   - [ ] **Debug** (`debug`) — a defect, crash, or two failed fixes
   - [ ] **Security** (`secure`) — auth, payments, uploads, user data, webhooks
   - [ ] **Verify / tests** (`verify`) — anything a person can see or touch
   - [ ] **Perf** (`verify` + `architect`) — CWV, jank, bundle, render
   - [ ] **Docs** — README, changelog, or editorial the user asked for (use `sick-social` for prose)
   - [ ] **Ship** (`ship`) — committing or opening a pull request
   - [ ] **Critics** (`critic-mode`) — a build is being judged or finished
   - [ ] **Game** (`game-mode`) — the thing is a game
   - [ ] **Design critic** (subagent `design-critic`) — rendered UI to inspect
   - [ ] **Builder** (subagent `builder`) — scoped implementation with a locked brief
5. **Load every APPLY item.** Read `../<name>/SKILL.md` (or the matching agent file). Invoke it at the phase it belongs to. A playbook table is a hint, not a ceiling: if the checklist marked a skill APPLY, load it even when the playbook row omitted it.
6. **Say the roster before building.** Tell the user which skills and subagents you chose and why, and which you skipped. Do this in the first working message after any mode switch line.
7. **Do not recurse majors.** You are already the lead major skill. Do not restart another major skill's full intake unless the user actually asked for that mode.
   - `game-mode` — load it only when the deliverable is a game (it owns intake and the ten-critic loop).
   - `critic-mode` — when you need a scoring loop, load its critic-round rules; skip its quality-level interview unless the user started critic-mode or asked how good it must be.
   - `arena` — load it when the job is a bakeoff or adversarial pass, not as a nested second orchestrator.
   - `sick-social` — load its laws and linter whenever copy is written; skip its "ask for raw material" pause when the parent skill already has the facts.
   - `beast-code` — if another major is already lead, do not print a second `BEAST CODE {ON}-OFF` or restart its playbook picker; use its standing rules, iron laws, and verify/critic finish when they apply.

## Definition of done for this step

The index was read in this task. Every APPLY skill will be loaded. The user-visible roster names the chosen skills and the reason for each.
