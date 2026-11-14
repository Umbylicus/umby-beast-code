---
name: critic-mode
description: Runs a panel of independent critics over anything being built (website, app, game, tool, document) and loops fix-then-recritique until every aspect clears the chosen bar. Each critic owns one aspect and scores the build against the best-known product for that aspect in the same category, says why it is not a 10, and gives the next writer specific fixes. Asks the user for a quality level (best in class, great, or critique only) and how many critics to run, logs every round, and keeps a live score graph anyone can open. Use via '/critic-mode', when asked to critique, score, rank, or "make this the best", or when another skill needs a quality loop.
license: MIT
major: true
metadata:
  version: "1.1.0"
  tree: "beast-code"
  role: orchestrator
---

# Critic Mode

One lead (you) runs the loop. Critics judge. Writers fix. Nobody grades their own work.

## Skill selection (every task)

Follow the shared procedure in [`../beast-code/references/select-skills.md`](../beast-code/references/select-skills.md) using [`../beast-code/SKILLS-INDEX.md`](../beast-code/SKILLS-INDEX.md). Do this after the two quality questions, before round 1. State which skills and subagents you chose and why. Load `verify` for evidence, `comment-slicer` after writer batches, `secure` if the thing handles accounts or payments, `game-mode`'s ten aspects when the subject is a game, and `design-critic` for UI screenshots.

This mode raises quality by measurement. It cannot promise a result: a loop can stall, and the stop rules below exist so it stalls in front of the user instead of burning tokens in the dark.

Files it keeps in the project:

```
.beast/critic/
  plan.md          level, bar, critics, aspects, benchmarks
  evidence/        screenshots, test output, recordings for each round
  rounds.jsonl     one line per round (written by the script)
  graph.html       live score graph (open in any browser)
  scoreboard.md    latest scores and reasons as text
```

## Step 1: Ask two questions

Use the host's multiple-choice tool if it has one. Otherwise ask as a numbered list. Skip a question the user already answered.

**Question 1. How good does this need to be?**

- **A. Best in class.** Loop until every aspect scores 9 or higher. *Warn the user in the option text: this is token-heavy, often many rounds with a full panel each round.*
- **B. Great.** Loop until every aspect scores 7 or higher. Medium token use.
- **C. Critique only.** One round. Critics score and suggest. Nothing is changed.

**Question 2. How many critics?** Offer 3, 5, or 10, and accept any number from 1 to 10. Default to 10 for level A, 5 for B, 3 for C. One critic per aspect.

Write the answers to `.beast/critic/plan.md`.

## Step 2: Pick the aspects and a benchmark for each

1. State in one sentence what is being built and its category (for example "online ordering app for a restaurant", "top-down roguelike", "B2B invoicing dashboard").
2. Choose one aspect per critic from [`references/aspect-library.md`](references/aspect-library.md). Take the aspects that matter most for this category first. For a game, use the ten in `../game-mode/references/ten-aspects.md`.
3. For each aspect, name the benchmark: the highest-ranked product of this kind **for that one aspect**. Different aspects usually have different benchmarks. With web access, find it from current rankings, review aggregates, and awards for that specific craft, and note the source. Measure against the best even when the build is small; the score shows the distance. Without web access, use your best-known leader and label it `opinion`. If no clear leader exists, name two strong examples.
4. A benchmark is a quality bar. Critics compare how well the job is done. Nothing is copied from it: no names, art, text, layouts, levels, or code.
5. Add the aspect and benchmark table to `plan.md` and show it to the user before round 1.

## Step 3: Build the evidence pack

Critics judge the real thing, not a description of it. Before each round, put fresh evidence in `.beast/critic/evidence/round-N/`:

- the build, typecheck, and test output
- the running product: screenshots at phone and desktop sizes, or a recording or frame captures for a game
- console and error logs from a real run
- measured numbers where the aspect needs them (load time, frame time, Lighthouse)
- the paths of the source files in scope

If the product cannot be run here, say so in `plan.md`. Critics then cap any aspect that depends on running it at 6.

## Step 4: Run the critics

Spawn every critic in one message so they run in parallel. Each one gets the brief in [`references/critic-brief.md`](references/critic-brief.md) with its aspect, its benchmark, and the evidence paths filled in.

Rules that keep the scores honest:

- **Fresh context.** A critic has no chat history and never sees another critic's output or any earlier score.
- **Read-only.** Critics do not edit anything.
- **Never the author.** An agent that wrote or fixed the work does not critique it.
- **Reasons before the number.** The brief makes each critic list evidence and gaps first, then score.
- **Mixed models.** Use whatever models your host offers and spread critics across them (in Claude Code, mix the available Claude models; in other tools, mix theirs). Put the strongest model on the aspects that need judgment. A model tends to be easy on work that looks like its own.
- **Hard caps.** A failing build, failing tests, or missing evidence caps the affected aspects at 6, whatever else looks good.

With no subagent tool, run the critics one after another yourself, re-reading the brief each time, and label the round `self-critiqued`. Say plainly in the report that this is weaker than independent critics.

## Step 5: Log the round and update the graph

Collect the critic outputs into one JSON file and hand it to the script:

```bash
python3 <path-to-critic-mode>/scripts/critic_graph.py add .beast/critic/round-N.json
```

The round file looks like this:

```json
{"level": "A", "scores": [
  {"aspect": "Checkout flow", "benchmark": "Example Shop", "score": 7,
   "why_not_10": "Card errors clear the form.",
   "suggestions": ["Keep field values after a declined card."]}
]}
```

The script validates it, appends it to `rounds.jsonl`, rebuilds `graph.html` and `scoreboard.md`, and prints one status:

| Status | Meaning | What you do |
| :--- | :--- | :--- |
| `PASS` | every aspect is at or above the bar | go to Step 7 |
| `CONTINUE` | below the bar and still improving | go to Step 6 |
| `STALLED` | two rounds with no gain in the lowest score | stop and ask the user |
| `ROUND_LIMIT` | hit the round cap (6 for A, 4 for B) | stop and ask the user |
| `REPORT_ONLY` | level C | go to Step 7 |

Tell the user where `graph.html` is after round 1. It refreshes itself, so they can leave it open.

On `STALLED` or `ROUND_LIMIT`, show the scoreboard and offer: keep going for N more rounds, accept the current build, lower the bar, or change approach on the stuck aspect. Never lower the bar yourself.

## Step 6: Fix, then go again

1. Gather every critic's `why_not_10` and `suggestions`. Drop duplicates. Order by lowest score first.
2. Where two suggestions conflict, you decide, and you write the decision in `plan.md`.
3. Split the fixes into scopes that do not share files. Spawn a **fresh writer** per scope. Each writer gets the goal, its file scope, the exact suggestions it owns, and the checks it must keep green. Writers never see the scores, only the fixes.
4. When the writers return, read the diffs yourself. Run build, typecheck, and tests. Revert any change that breaks a check or lowers an aspect that was already passing.
5. Rebuild the evidence pack and return to Step 4 with **new** critics. Give each new critic the previous round's suggestions for its aspect, marked as "claimed fixed", so it checks them. Do not give it the previous score.

The standing rules in `../beast-code/references/standing-rules.md` still apply to writers: no deploys, no merges, no protected code.

## Step 7: Report

- The level, the bar, and how many rounds ran.
- A table: aspect, benchmark, first score, final score.
- For each aspect still under 10: the critic's reason.
- What changed between the first and last round.
- For level C: the ranked suggestion list, with nothing applied.
- The path to `graph.html`.
- Whether critics were independent or `self-critiqued`.

## Definition of done

Levels A and B: the script printed `PASS`, or the user chose to stop after a `STALLED` or `ROUND_LIMIT` pause. Level C: one round logged and the suggestions delivered. In every case the graph and scoreboard exist and the report states the real final scores.
