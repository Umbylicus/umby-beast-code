---
name: build-plan
description: Writes a build plan and a decision log to files so long or multi-step work survives context resets, handoffs, and overnight runs. Splits work into small pieces, each one finished by a pass-or-fail check, orders them by risk and dependency, marks what can run in parallel, and records every assumption with how to reverse it. Use before any build with more than a few steps, for autonomous or multi-session work, when asked for a plan, or when picking up work someone else started.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Plan

A plan in chat disappears when the context does. Put it in the project.

```
.beast/
  plan.md          the units of work and their checks
  decisions.tsv    one row per choice made without asking
  work-log.md      what was finished and when
```

## Write the plan

1. **Goal.** Three lines at the top of `plan.md`: what the user wants, the problem behind it, and how anyone can tell it is done. "Done" must be something that can pass or fail.
2. **Unknowns first.** List what you do not know. Anything you could find out by running something, find out now with a throwaway test instead of asking. Leave only real preference or product choices for the user.
3. **Units.** Break the work into units small enough to finish and check in one sitting. Each unit has:
   - what changes, and in which files
   - the check that proves it (a command, a test, a screen to look at) and what a pass looks like
   - what it depends on
4. **Order.** Riskiest unknown first. Shared foundations (types, tokens, schema, project setup) before anything built on them. Removal of dead code before new code.
5. **Parallel or not.** Units that touch different files and share no state can run side by side. Units that write the same file or the same data run one after another. Say which is which.
6. **Stops.** Mark every point that needs the user: approval gates, anything irreversible, anything that costs money or reaches other people.

Plan format:

```markdown
# Plan: <goal in a few words>
Goal: ...
Problem: ...
Done when: ...

## Units
- [ ] 1. <what> | files: ... | check: `<command>` passes | depends on: none
- [ ] 2. <what> | files: ... | check: ... | depends on: 1
- [ ] STOP: operator approves mockups

## Open questions for the operator
```

## Work the plan

- Do one unit, run its check, tick the box only when the check passed, then start the next. Never start a unit on top of a failing one.
- If a unit turns out wrong, change the plan in the file and say why. Do not quietly do something else.
- Log each choice made without asking in `decisions.tsv` with tab-separated columns: `time`, `unit`, `decision`, `why`, `how to reverse`, `evidence path`. Add rows. Never edit or delete an old row. If one was wrong, add a new row that replaces it.
- When a unit lands, add a line to `work-log.md`: what, when, who asked.

## Picking up existing work

Read `plan.md`, `decisions.tsv`, and the recent git history before touching anything. Trust the trail for what was done, and do not redo it. Do not trust it for whether it works: run the checks of the finished units once. Then continue from the first unticked unit.

## Definition of done

`plan.md` exists with a pass-or-fail goal. Every ticked unit has a check that was actually run. Every unasked choice has a row in `decisions.tsv`. The stops are marked.
