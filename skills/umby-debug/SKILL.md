---
name: umby-debug
description: Finds and fixes the real cause of a bug instead of patching the symptom. Reproduces the failure on the surface the user touched, narrows the cause by halving the search space with runtime evidence, puts a failing check in place before the fix, and proves the fix on the same surface. Use for any reported defect, crash, wrong output, flaky behavior, or "it broke after the last change", and whenever two fixes in a row have failed.
license: MIT
metadata:
  version: "1.0.0"
  tree: "umby-beast-code"
---

# Umby Debug

A fix is a claim about a cause. Without a reproduction you cannot test the claim, so reproduction comes first.

## Steps

1. **Reproduce it yourself, where the user saw it.** Browser bug: in a browser. Command-line bug: in a terminal. Game bug: in the running game. Write down the exact steps and what you saw. If it will not reproduce, tighten the conditions, add logging, or build the trigger by hand before doing anything else. Ask the user only after you have tried, and say exactly what you could not reach.
2. **State what should happen** in one sentence. That is the check the fix has to pass.
3. **Halve the search space.** List where the fault could be. Pick the test that rules out the most. Run it and read real values: logs, breakpoints, network payloads, stored data. Repeat. Do not reason from the code alone when you can look.
   - If it worked before, find the change that broke it (`git bisect` or a manual halving of recent commits).
4. **Name the cause** as one sentence about a wrong decision in the code or data: "the cart total is computed before the discount is loaded". If the sentence describes a symptom ("the total is sometimes wrong"), keep going.
5. **Write the failing check first.** A test, script, or scripted browser run that fails now for the reason you named. Commit it before the fix when the project uses git. If a real test would cost far more than the bug is worth, use the closest thing you can run and say so in the report.
6. **Fix the cause, at the cause.** Change the place where the wrong decision is made. Then look for the same mistake elsewhere and fix those too.
7. **Prove it on the original surface.** Repeat the steps from step 1. The failing check passes. The surrounding tests still pass. A unit test going green is not proof the user's bug is gone.

## Rules

- **Two failed fixes means stop fixing.** Write down the assumption both fixes shared, find an observation that would be different if it were false, and make that observation.
- **No guard without a reason.** Add a null check or a retry only for a situation that is meant to occur. Anywhere else it hides the bug.
- **Nothing ships on a hunch.** Every changed line traces to something you observed. Extra "just in case" changes come out.
- **A timing trick is not a fix.** No sleeps, no delayed callbacks, no silenced warnings over a cause you have not found.
- **Bugs that only appear after a restart or over time** point at saved state: caches, storage, the database, leftover files.
- **An inconclusive result is not a pass.** Say it was inconclusive.

## Report

What was broken, in the user's terms. The cause, in one sentence. The fix and where. The failing-then-passing output, pasted. Anything related you found and did not fix.

## Definition of done

The original steps no longer produce the bug. A check exists that fails without the fix and passes with it. Existing tests pass. The report labels each claim as measured, inferred, or a guess.
