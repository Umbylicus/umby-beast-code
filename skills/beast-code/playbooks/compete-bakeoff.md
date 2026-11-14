# Playbook: Compete Bakeoff (Parallel Design & Architecture Arena)

Use when one design or architectural guess could lock in a mediocre shape, and you want 2–3 distinct candidates compared side by side with the strongest elements grafted into the winner.

## Mandatory Checklist

1. **Frame the Contract & Rubric (`../../arena/SKILL.md`):** Define the exact surface being built (e.g., Homepage Hero + Interactive Demo) and a 5-criterion grading rubric (1. 5-second clarity & conversion pull, 2. Visual restraint & zero AI-look tropes, 3. Typography & spatial rhythm, 4. Interaction physics & responsiveness, 5. Code maintainability).
2. **Assign Divergent Aesthetic/Structural Directions:** Give each candidate an isolated output path/worktree and a genuinely distinct structural thesis from `../../discover/references/aesthetic-archetypes.md` (never three minor color tweaks of the same layout).
3. **Parallel Generation:** Spawn isolated `builder` subagents (or execute clean sequential branches if single-agent) to build runnable, real-DOM candidates.
4. **Render & Cross-Judge (`../../verify/SKILL.md`):** Screenshot every candidate at `375px` and `1440px`. Score each candidate criterion-by-criterion via a fresh `design-critic` (using a cross-family model when available).
5. **Select Base & Graft First-Principles Improvements:** Pick the candidate with the strongest spatial backbone and cleanest architecture. Hand-port only the 1–2 superior micro-details (e.g., an interactive toggle or copy hook) from runners-up so the final artifact stays 100% coherent under one token system.
6. **Final Slicer & Pixel Gate (`../../comment-slicer/SKILL.md` + `../../verify/SKILL.md`):** Clean up losing worktrees/temp directories and run the full quality gate on the unified winner.
