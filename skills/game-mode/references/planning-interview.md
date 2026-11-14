# Game planning interview (grill)

There is no `grill-me` skill in this tree. Run this interview yourself. If the host has a `/grill-me` command or a multiple-choice question tool, use it as the UI — the required fields and push-back rules below still apply.

Do not scaffold, write game code, or pick skills until `docs/game-plan.md` is **AGREED**.

## How to grill

- **One cluster at a time.** Ask 3–4 questions per turn, each with 3–4 concrete options and your recommended option first. Do not dump a 20-question form.
- **Skip what the folder already answers.** Read the workspace first.
- **Push on mush.** Vague answers (`fun`, `cool`, `a bit like everything`, `whatever engine is best`, `maybe multiplayer later`) are not answers. Name the problem in one sentence, offer a sharp contrast, and ask again.
- **Name conflicts.** If two answers cannot both be true (Unity + "it has to open from a tweeted link this afternoon"; online multiplayer + "one evening prototype"; photoreal assets + "code-only art"), stop and make the user pick.
- **Recommend for the best possible game they can actually finish.** Challenge an engine or platform that fights the scope. A 2D browser loop should not start in Unity. A native 3D sim should not start on a raw `<canvas>` unless they have a reason.
- **Keep going.** This is back-and-forth, not one round. Continue until every required field is specific enough that a builder would not have to guess.
- **Then write the plan and wait.** Show `docs/game-plan.md`. Status stays `DRAFT` until the user agrees (or they already granted autonomy for this gate). Only then set Status to `AGREED`.

Autonomy covers choices inside this gate; it does not skip writing the plan file.

## Required fields

Every field below must have a real value in the plan. Invent nothing the user did not pick or grant.

1. **Working title and pitch.** One paragraph: the player's main verb, what makes a run interesting, what makes this game its own. Original work only. Comparables are quality bars, never something to copy.
2. **Genre and core loop.** Name the genre. Describe one loop: verb → challenge → fail/succeed → retry or reward. Name 2–3 comparable games as bars, not as templates.
3. **Target platform.** Web, desktop, mobile, or console. Primary device and orientation if mobile.
4. **Engine / framework.** Phaser, PixiJS, Three.js, Babylon, Godot, Unity, plain canvas, React Native, or another named tool. Write *why this one* for this platform and scope.
5. **Scope of the first shippable.** One polished loop, a short full game, or a prototype that tests one idea. What is explicitly out.
6. **Art style.** Palettes, shapes, camera (2D / 2.5D / 3D). Not "nice" or "modern".
7. **Art and audio source.** Code-generated, CC0 packs, user-supplied, or generated assets (with license tracking). This changes the manifest.
8. **Controls.** Keyboard, mouse, touch, gamepad, or combinations. What the player actually presses for the main verb.
9. **Multiplayer.** None, local, or online. If online: authoritative server or not, and whether v1 can ship without it. Default to none unless they have a reason.
10. **Win, lose, progression.** How a run ends. What carries over. What "best possible" means for v1 content (how many levels, enemies, weapons, or equivalent).
11. **Quality level.** Same as Critic Mode: A (all ten aspects ≥ 9), B (all ten ≥ 7), C (one round, no fix loop). Warn that A is token-heavy.
12. **Non-goals.** At least three things this build will not do.

## Suggested clusters (adapt, do not skip fields)

**Cluster 1 — What the game is**
Genre, core verb, comparable bars, what would make a first session feel fair.

**Cluster 2 — Where it runs and what it is built in**
Platform, engine/framework, why that pairing, what you refuse to use.

Push examples:
- "Browser, one-file share" vs "installable desktop" vs "phone in portrait".
- Phaser / PixiJS / plain canvas for 2D web; Three.js / Babylon for 3D web; Godot for 2D/3D with an editor; Unity for native/console; React Native only if the game is a mobile app first.

**Cluster 3 — Feel**
Art style, camera, art/audio source, controls, juice you can afford at this scope.

**Cluster 4 — Shape of v1**
Scope, win/lose, content budget, multiplayer, non-goals, quality level.

## Conflicts to call out

| They said | Also said | Force a pick |
| :--- | :--- | :--- |
| Unity / Unreal | Must run in a link tonight | Web engine, or drop the link constraint |
| Online multiplayer | One-loop prototype this session | Ship single-player; log multiplayer as a later unit |
| Photoreal / big licensed soundtrack | Code-generated placeholders | Style down, or they supply assets now |
| "Like game X" as the product | Original-work rule | Same genre and verb, different world, names, and look |

## Plan file

Write [`../references/game-plan-template.md`](game-plan-template.md) to `docs/game-plan.md`. Fill every heading. The rest of Game Mode reads that file and does not contradict it.
