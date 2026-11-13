---
name: comment-slicer
description: Cuts comments that cost the reader more than they give, and does it without ever changing what the code does. Sorts every comment into cut, move-into-code, or stay using a three-question test, treats check silencers like '@ts-ignore' and 'eslint-disable' as a separate audit, and never touches comments that tools depend on (build directives, pragmas, license headers). Comment-only edits are applied; anything that would change code is proposed and applied one at a time behind a green build. Use after a batch of code is written, before a commit or review, or directly via '/comment-slicer'.
license: MIT
metadata:
  version: "2.0.0"
  tree: "umby-beast-code"
---

# Comment Slicer

A comment is a second copy of the truth that nothing checks. Each one either saves the next reader a mistake or teaches them something false after the code moves on. The slicer keeps the first kind and cuts the rest.

It has one safety promise: **slicing never changes behavior.** Read "Build safety" before the first edit.

## Build safety (read first)

1. **Record a baseline.** Before touching anything, run the project's build, typecheck, and tests, and note the result. If the baseline is already red, say so and slice comments only.
2. **Two kinds of edit, two rules.**
   - *Comment-only edits* (deleting or rewording a comment) are applied directly.
   - *Code edits* (a rename, a new type, removing a silencer) are listed as proposals first. Apply them one at a time, re-run the baseline checks after each, and revert any that turns a check red.
3. **Never touch a machine-read comment.** Some comments are instructions to a tool. Removing one can break the build or change output. Leave all of these exactly as they are:
   - shebang lines, encoding lines, and license or SPDX headers
   - compiler and build directives (`//go:build`, `// +build`, `#pragma`, `/// <reference ...>`, `// @ts-check`, `/** @jsx ... */`)
   - bundler hints (`/* webpackChunkName: ... */`, `/* @vite-ignore */`, `/*#__PURE__*/`)
   - formatter and coverage markers (`prettier-ignore`, `istanbul ignore`, `c8 ignore`, `fmt: off`)
   - source map lines, template conditionals, and doc comments a generator turns into published API docs
   - any comment a script in the repo greps for (check `package.json` scripts and CI config before cutting a marker you do not recognize)
4. **Stay in scope.** Slice only the files named, or the current diff. Skip vendored code, generated files, lockfiles, and anything the standing rules list as protected.
5. **When unsure whether a tool reads it, it stays** and goes in the report as a question.

## The three-question test

Ask these of every human-read comment, in order. Stop at the first one that decides it.

1. **Is it true right now?** Check it against the code beside it. A comment that is wrong, stale, or about code that no longer exists is **cut**.
2. **Could the code say this itself?** If a better name, a small extracted function, a type, or a test assertion would carry the same information, the verdict is **move**: the knowledge goes into the code and the comment goes away. Comments that only restate the next line, label a section, or narrate steps need no move. They are simply **cut**.
3. **Does the knowledge come from outside this codebase?** A fact the code cannot hold stays: a rule from a contract or regulation, the behavior of someone else's system, a measured number and where it came from, a link to the decision record. That comment **stays**, shortened to the fact and its source.

A comment that passes none of the three is cut.

Some cases the test settles quickly:

| Comment | Verdict | Reason |
| :--- | :--- | :--- |
| `// loop over users` | cut | restates the line |
| `{/* Pricing section */}` | cut | the component name says it |
| commented-out code | cut | version control keeps history |
| `// TODO fix later` with no ticket | cut, or attach a ticket | a note nobody owns |
| `// HACK: called twice, so we skip the first` | move | fix the double call, then the note is unneeded |
| `// don't touch this` | move | encode the reason as a test or a type |
| `// Stripe retries webhooks for 3 days, so this must be idempotent` | stay | outside fact that explains a design choice |
| `// 250ms: longest p95 seen in load test, see docs/perf.md` | stay | a number with its source |

## Silencer audit

A silencer turns off a check: `@ts-ignore`, `@ts-expect-error`, `eslint-disable`, `biome-ignore`, `# type: ignore`, `# noqa`, a cast through `any` or `unknown`, `!important`, `suppressHydrationWarning`. Handle these separately from prose comments, because removing one is a code edit.

For each silencer:

1. Find out what the silenced check is protecting.
2. If the check is right and the code is wrong, propose the real fix. The silencer goes when the fix lands green.
3. If the check is wrong for this line (a known false positive, generated code, a third-party type gap), the silencer stays and gets a one-line reason naming the tool rule.
4. Never delete a silencer without the fix. That turns a hidden problem into a broken build.

## Workflow

1. **Baseline.** Run build, typecheck, and tests. Note the result.
2. **Scan.** Run the bundled scanner over the scope:
   ```bash
   python3 <path-to-comment-slicer>/scripts/slicer_scan.py <files-or-dirs>
   ```
   It lists candidates by kind and marks machine-read comments as `PROTECTED`. It finds candidates. It does not decide.
3. **Judge.** Apply the three-question test and the silencer audit to each candidate. Where the host has subagents, hand the judging to the read-only reviewer in [`../../agents/comment-slicer.md`](../../agents/comment-slicer.md) so the code's author is not the one grading it. With no subagents, do the pass yourself and label the report `author-sliced`.
4. **Apply comment-only edits.**
5. **Propose code edits** as a list. Apply them one at a time behind the baseline checks, or leave them for the operator if the task did not ask for code changes.
6. **Re-check.** Run the baseline checks and the scanner again. The result must be no worse than the baseline.

## Report

- Scope sliced, and the baseline result before and after.
- Counts: cut, moved, stayed, protected.
- Each move and silencer fix: `file:line`, what changed, and the check that stayed green.
- Open proposals not applied, and any comment left as a question.

## Definition of done

Build, typecheck, and tests match or beat the baseline. No machine-read comment was changed. Every remaining comment states an outside fact or a reason the code cannot hold. Every remaining silencer has a named reason.
