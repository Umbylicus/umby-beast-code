---
name: game-mode
description: Builds original video games end to end with an organized project folder, a tracked asset pipeline, and a ten-critic quality loop. Starts with a back-and-forth planning interview (engine/framework, platform, genre and core loop, art style, scope, controls, multiplayer, quality bar) that pushes on vague answers until an agreed plan is written to docs/game-plan.md. Only then does it read the skill index, pull in every relevant sibling skill, scaffold, build the playable core loop, and run ten critics. Use via '/game-mode' or whenever asked to make, prototype, or improve a game.
license: MIT
major: true
metadata:
  version: "1.1.0"
  tree: "beast-code"
  role: orchestrator
---

# Game Mode

You are the orchestrator. You grill until the plan is real, keep the folder clean, read every diff, and run the critic loop. Writers build. Critics judge.

Three rules sit above everything else:

1. **Original games only.** Comparable games set a quality bar for one aspect at a time. Never reproduce a specific game: no copied names, characters, art, music, levels, story, or overall look. If the request is to remake an existing game, say you can build an original game in that genre with similar mechanics, and continue on that basis.
2. **The standing rules apply**: read `../beast-code/references/standing-rules.md` (approval gates, no publishing without a go, logging).
3. **No code before an agreed plan.** Run the planning interview. Write `docs/game-plan.md`. Wait until Status is `AGREED`. Then read the skill index and build from that file.

There is no `grill-me` skill in this tree. The interview lives in [`references/planning-interview.md`](references/planning-interview.md). If the host has `/grill-me` or a question tool, use it as the UI for that interview.

---

## Step 1: Planning interview (do not build yet)

Follow [`references/planning-interview.md`](references/planning-interview.md) in full.

Ask about, at least: framework/engine (Phaser, PixiJS, Three.js, Babylon, Godot, Unity, plain canvas, React Native, or another named tool), target platform, genre and core loop, art style, scope, controls, multiplayer, win/lose, content budget, art/audio source, and quality level.

Go back and forth. Push on weak or vague answers. Do not accept "fun", "whatever is best", or "maybe multiplayer later" as a decision. Recommend the pairing of platform and engine that can actually produce the best game they can finish.

Write the filled template from [`references/game-plan-template.md`](references/game-plan-template.md) to `docs/game-plan.md` with Status `DRAFT`. Show it. Stop until the user agrees or has granted autonomy for this gate. Then set Status to `AGREED`.

The rest of this skill, including scaffold and critics, follows `docs/game-plan.md`. If a later choice disagrees with the file, update the file and say so.

---

## Step 2: Skill selection from the index

The plan is the job. Follow [`../beast-code/references/select-skills.md`](../beast-code/references/select-skills.md) using [`../beast-code/SKILLS-INDEX.md`](../beast-code/SKILLS-INDEX.md).

Load every APPLY skill. Typical APPLY set for a game (confirm against the index, do not assume this is complete):

- `build-plan` when the plan is more than a few steps
- `architect` for game state, entities, and configs
- `backend` and `secure` when multiplayer, accounts, or persistence leave the device
- `craft` and `motion` when there is a web or app UI shell, HUD, or juice
- `sick-social` for any player-facing words (menu, tutorial, store copy)
- `comment-slicer` after every code batch
- `debug` if a defect shows up
- `verify` before critics
- `critic-mode` for the ten-aspect loop (its critic-round rules, not a second quality interview — the plan already set A/B/C)
- `builder` / `design-critic` subagents when the host has them

State the roster and why, and write it into the "Skills chosen for this build" table in `docs/game-plan.md`. Then continue.

---

## Step 3: Lock the benchmarks

Open [`references/ten-aspects.md`](references/ten-aspects.md) and [`references/genre-benchmarks.md`](references/genre-benchmarks.md). For each of the ten aspects, the benchmark is **the highest-ranked game of this style for that one aspect**. Pick it like this:

1. **Define the style.** Use the genre and the agreed comparables in `docs/game-plan.md`. They tell you the style. They are not automatically the benchmarks.
2. **Find the top-ranked game per aspect.** With web access, look up who is ranked best in that style for each aspect: review-aggregate scores, year-end and all-time lists, and awards given for that specific craft (art direction, audio, game design, narrative, technical achievement). Take the one at the top.
3. **Use the best, whatever its budget.** A small game is still scored against the top of its style. The score shows the distance. The quality level in the plan decides how much of that distance has to be closed.
4. **Record the source.** Put the ranking or award next to each pick. With no web access, fall back to the starter table, mark the pick `opinion`, and tell the user the benchmarks were not checked against current rankings.
5. **Keep it current.** Rankings change as new games ship. Prefer a recent source over the starter table.

Write the table into `docs/game-plan.md` (and a short copy in `docs/design.md` if that file exists). Show it. They can swap any pick.

This is the research gate. Wait for a go unless the user granted autonomy.

---

## Step 4: Scaffold the folder

Read the engine from `docs/game-plan.md`. Map it to a `game_scaffold.py` id:

| Plan says | `--engine` |
| :--- | :--- |
| Phaser | `phaser` |
| PixiJS | `pixi` |
| Plain canvas | `canvas` |
| Three.js | `three` |
| Babylon | `babylon` |
| Godot | `godot` |
| Unity | `unity` |
| React Native | `react-native` |
| Anything else named | closest row, or `canvas` for 2D web and `three` for 3D web, and note the mapping in the plan |

```bash
python3 <path-to-game-mode>/scripts/game_scaffold.py init <project-dir> --engine <id>
```

This creates the layout in [`references/folder-layouts.md`](references/folder-layouts.md), an empty `assets/manifest.json`, `CREDITS.md`, `LICENSES/`, `docs/`, and `tests/`. It will not overwrite an already-agreed `docs/game-plan.md`. Never dump files in the project root. Every file goes in the folder the layout names for it.

---

## Step 5: Assets with a paper trail

Follow [`references/asset-rules.md`](references/asset-rules.md). In short:

- Every asset gets a manifest entry (id, file, type, license, source, author, generated or not) the moment it is added.
- Source files (layered art, project files) stay in the source-art folder. Only exported, optimized files ship.
- Third-party assets need a license that allows the use, with the license text saved in `LICENSES/`.
- Generated assets record the tool and the date. Do not claim a license the tool's terms do not give.
- No asset may depict or imitate another game's characters, logos, or art.

Check the folder at any time:

```bash
python3 <path-to-game-mode>/scripts/game_scaffold.py check <project-dir>
```

It fails on files missing from the manifest, manifest entries with no file or no license, bad file names, and stray files in the root.

---

## Step 6: Build the core loop first

Follow `docs/game-plan.md`. Do not add systems the plan listed as non-goals.

1. **Playable slice.** Before any content, build the smallest thing that is the game: the main verb, one challenge, a fail state, and a restart, using the agreed controls. Placeholder shapes are fine. This is the mockup gate: show it and wait for a go.
2. **Shape before code.** Name the game state as explicit states (boot, menu, playing, paused, game over), entities as one module each, and tuning values in one config file. Use a fixed timestep for simulation and a seeded random generator so runs can be replayed.
3. **Feel pass.** Tune movement and input before adding content: response time, acceleration, forgiveness windows, camera. Then feedback: hit reactions, particles, short screen shake, sound on every key action. Base timing effects on elapsed time, not frame counts.
4. **Content.** Levels, enemies, items, or cards up to the v1 budget in the plan. Each new piece introduces one idea. Write the difficulty curve in `docs/balance.md`.
5. **Shell.** Menu, pause, settings with volume that persists, onboarding taught through play, game over and retry. Player-facing words go through `sick-social` if that skill was APPLY.

Delegate code to writers with disjoint file scopes once the state shape and config exist. Read every diff yourself. After each batch, run `comment-slicer`.

---

## Step 7: Verify it runs

Before any critic sees it, run `verify` if it was APPLY, and:

- Build and typecheck pass. Logic tests pass.
- A smoke test that matches the platform: headless browser for web (load, ready flag, start a run with the agreed controls, 30 seconds, fail state, retry, zero console errors); editor/play-mode or device smoke for Godot, Unity, or React Native.
- Capture frame times during that run: average FPS, worst 1%, longest frame.
- Screenshots at start, mid-run, and game over, at the plan's target sizes.
- `game_scaffold.py check` passes.

Put the output in `.beast/critic/evidence/round-N/`. If the game cannot be run here, say so. Critics then cap play-dependent aspects at 6.

---

## Step 8: The ten-critic loop

Run `../critic-mode/SKILL.md` from its Step 3, with these settings already decided in the plan:

- **Critics:** ten, one per aspect in `references/ten-aspects.md`.
- **Benchmarks:** the table in `docs/game-plan.md`.
- **Level and bar:** the plan's quality level (A is 9, B is 7, C is one round).
- **Brief:** Critic Mode's brief, with the aspect's checks and its 5, 7, and 9 descriptions pasted in.

Each round the critics say why the aspect is not a 10 and what the next writer should change. You merge those into fix scopes, spawn fresh writers, re-verify with Step 7, and run ten new critics. The score graph at `.beast/critic/graph.html` shows every round. The loop stops on pass, on a stall, or at the round cap, and on the last two it stops to ask the user.

---

## Step 9: Handoff

- How to run it, and the controls, matching `docs/game-plan.md`.
- The final score table with benchmarks, first and last scores, and each remaining reason.
- The graph path, rounds run, and whether critics were independent.
- Asset and license summary from the manifest.
- What was cut, and what the next round would improve.

## Definition of done

`docs/game-plan.md` is AGREED and the build matches it. The game runs from a clean checkout with one command. The smoke test passes with no console errors. `game_scaffold.py check` passes. Every asset is in the manifest with a license. The critic loop ended in `PASS`, or the user chose to stop, and the report shows the real scores.
