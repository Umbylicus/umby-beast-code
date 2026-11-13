# Playbook: Bug Reproduction & Root-Cause Fix

Use when fixing broken layouts, hydration mismatches, race conditions, stale state, broken responsive views, or failing interactions.

## Mandatory Checklist

1. **Reproduce on the Real Surface First:** Reproduce the exact symptom in a live browser, Playwright script, or failing behavioral test before changing application code. If reproduction requires missing credentials/data, report the exact blocker rather than guessing.
2. **Trace Input-to-Output & Falsify:** Trace the smallest path from trigger (DOM event, URL change, network response, CSS cascade) to the broken output. If two hypotheses compete, instrument and falsify before editing. Never slap a `setTimeout`, `suppressHydrationWarning`, `overflow: hidden` band-aid, or `@ts-ignore` over an unexamined root cause.
3. **Structural Root-Cause Fix (`../../umby-architect/SKILL.md`):** Fix the defect at the first place the invariant broke (e.g., modeling async race cancellation via `AbortController` or state machine rather than adding a boolean guard). Check sibling callers for the same bug class.
4. **Regression Test:** Add a behavioral test (Playwright or component/unit test asserting user-observable output) that fails without the fix and passes with it.
5. **Clarity & Surface Verification (`../../comment-slicer/SKILL.md` + `../../umby-verify/SKILL.md`):** Run `slicer_scan.py` to ensure no apology comments or debug leftovers remain, then verify the live fix across desktop and mobile viewports.
