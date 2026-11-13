---
name: umby-game-mode
description: Builds original video games end to end with an organized project folder, a tracked asset pipeline, and a ten-critic quality loop. Starts with a short multiple-choice intake (genre and comparable games, platform and engine, scope, art source, quality level), scaffolds a clean folder layout with an asset manifest and credits file, builds a playable core loop first, then runs ten critics who each score one aspect against the best-regarded game in the genre for that aspect, and keeps fixing and re-scoring until the chosen bar is met. Use via '/umby-game-mode' or whenever asked to make, prototype, or improve a game.
license: MIT
metadata:
  version: "1.0.0"
  tree: "umby-beast-code"
---

# Umby Game Mode

You are the orchestrator. You plan, keep the folder clean, read every diff, and run the critic loop. Writers build. Critics judge.

Two rules sit above everything else:

1. **Original games only.** Comparable games set a quality bar for one aspect at a time. Never reproduce a specific game: no copied names, characters, art, music, levels, story, or overall look. If the request is to remake an existing game, say you can build an original game in that genre with similar mechanics, and continue on that basis.
2. **The standing rules apply**: read `../umby-beast-code/references/standing-rules.md` (approval gates, no publishing without a go, logging).

## Step 1: Intake (one round of multiple choice)

Read the folder first and skip anything it already answers. Use the host's question tool if it has one. Ask at most five, each with three or four options and your recommended option first.

1. **Genre and comparables.** "Which is closest?" Offer genres that fit the request, and ask which existing games it should feel like. Their answer picks the benchmark set.
2. **Platform and engine.** Browser 2D (Phaser or PixiJS), browser 3D (Three.js or Babylon), or Godot. Recommend browser 2D unless the idea needs 3D or native export.
3. **Scope of the first build.** One polished level or loop (recommended), a short full game, or a prototype to test one idea.
4. **Art and audio source.** Generated in code (shapes, shaders, synthesized sound), free licensed packs (CC0 first), assets the user supplies, or AI-generated assets. Each choice changes the license tracking.
5. **Quality level.** The same three as Critic Mode:
   - **A. Best in class.** Loop until all ten aspects score 9 or higher. *Warn: token-heavy, expect many rounds of ten critics plus writers.*
   - **B. Great.** Loop until all ten score 7 or higher. Medium token use.
   - **C. Critique only.** Build, then one round of scores and suggestions with no fix loop.

Write the answers and a one-paragraph design pitch to `docs/design.md`. The pitch names the player's main verb, what makes a run interesting, and what makes this game its own.

## Step 2: Lock the benchmarks

Open [`references/ten-aspects.md`](references/ten-aspects.md) and [`references/genre-benchmarks.md`](references/genre-benchmarks.md). For each of the ten aspects, name the game regarded as best in this genre **for that aspect**. Use the user's comparables where they fit. With web access, check each pick against a real source. Mark unsourced picks as opinion. Put the table in `docs/design.md` and show it to the user.

This is the research gate. Wait for a go unless the user granted autonomy.

## Step 3: Scaffold the folder

```bash
python3 <path-to-umby-game-mode>/scripts/game_scaffold.py init <project-dir> --engine phaser|three|godot
```

This creates the layout in [`references/folder-layouts.md`](references/folder-layouts.md), an empty `assets/manifest.json`, `CREDITS.md`, `LICENSES/`, `docs/`, and `tests/`. Never dump files in the project root. Every file goes in the folder the layout names for it.

## Step 4: Assets with a paper trail

Follow [`references/asset-rules.md`](references/asset-rules.md). In short:

- Every asset gets a manifest entry (id, file, type, license, source, author, generated or not) the moment it is added.
- Source files (layered art, project files) stay in the source-art folder. Only exported, optimized files ship.
- Third-party assets need a license that allows the use, with the license text saved in `LICENSES/`.
- Generated assets record the tool and the date. Do not claim a license the tool's terms do not give.
- No asset may depict or imitate another game's characters, logos, or art.

Check the folder at any time:

```bash
python3 <path-to-umby-game-mode>/scripts/game_scaffold.py check <project-dir>
```

It fails on files missing from the manifest, manifest entries with no file or no license, bad file names, and stray files in the root.

## Step 5: Build the core loop first

1. **Playable slice.** Before any content, build the smallest thing that is the game: the main verb, one challenge, a fail state, and a restart. Placeholder shapes are fine. This is the mockup gate: show it and wait for a go.
2. **Shape before code.** Name the game state as explicit states (boot, menu, playing, paused, game over), entities as one module each, and tuning values in one config file. Use a fixed timestep for simulation and a seeded random generator so runs can be replayed.
3. **Feel pass.** Tune movement and input before adding content: response time, acceleration, forgiveness windows, camera. Then feedback: hit reactions, particles, short screen shake, sound on every key action. Base timing effects on elapsed time, not frame counts.
4. **Content.** Levels, enemies, items, or cards. Each new piece introduces one idea. Write the difficulty curve in `docs/balance.md`.
5. **Shell.** Menu, pause, settings with volume that persists, onboarding taught through play, game over and retry.

Delegate code to writers with disjoint file scopes once the state shape and config exist. Read every diff yourself.

## Step 6: Verify it runs

Before any critic sees it:

- Build and typecheck pass. Logic tests pass.
- A headless browser smoke test loads the game, waits for a ready flag the game sets, starts a run by keyboard, plays scripted input for 30 seconds, reaches a fail state, and retries. Zero console errors.
- Capture frame times during that run: average FPS, worst 1%, longest frame.
- Save canvas screenshots at start, mid-run, and game over, at desktop and phone sizes.
- `game_scaffold.py check` passes.

Put the output in `.umby/critic/evidence/round-N/`. If the game cannot be run here, say so. Critics then cap play-dependent aspects at 6.

## Step 7: The ten-critic loop

Run `../umby-critic-mode/SKILL.md` from its Step 3, with these settings already decided:

- **Critics:** ten, one per aspect in `references/ten-aspects.md`.
- **Benchmarks:** the table from Step 2.
- **Level and bar:** the user's answer from intake (A is 9, B is 7, C is one round).
- **Brief:** Critic Mode's brief, with the aspect's checks and its 5, 7, and 9 descriptions pasted in.

Each round the critics say why the aspect is not a 10 and what the next writer should change. You merge those into fix scopes, spawn fresh writers, re-verify with Step 6, and run ten new critics. The score graph at `.umby/critic/graph.html` shows every round. The loop stops on pass, on a stall, or at the round cap, and on the last two it stops to ask the user.

## Step 8: Handoff

- How to run it, and the controls.
- The final score table with benchmarks, first and last scores, and each remaining reason.
- The graph path, rounds run, and whether critics were independent.
- Asset and license summary from the manifest.
- What was cut, and what the next round would improve.

## Definition of done

The game runs from a clean checkout with one command. The smoke test passes with no console errors. `game_scaffold.py check` passes. Every asset is in the manifest with a license. The critic loop ended in `PASS`, or the user chose to stop, and the report shows the real scores.
