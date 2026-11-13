# Playbook: Visual Polish & De-Slop Pass

Use when an application or page already works functionally, but looks generic, inconsistent, cluttered, or recognizably AI-generated.

## Mandatory Checklist

1. **Render & Diagnose First (`../../umby-verify/SKILL.md`):** Capture current screenshots across `375px` and `1440px` (light & dark) and run `audit_ui_slop.py`. List the top ranked visual failures using the Squint, Grayscale, and Anti-Slop tests before touching CSS.
2. **Subtraction Pass (`../../umby-craft/SKILL.md`):** Strip nested card-in-card borders, competing drop shadows, decorative glowing blobs, emoji icons, redundant section dividers, and unnecessary badge colors.
3. **Token Normalization:** Snap every stray spacing value to the 4/8pt scale, collapse font sizes to a strict 5–6 step hierarchy with clear `>=1.25x` contrast on headings, enforce concentric border radii, and unify neutrals onto a hue-tinted OKLCH ramp.
4. **Optical & Micro-Interaction Refinement (`../../umby-motion/SKILL.md`):** Apply `text-wrap: balance` to headings, `tabular-nums` to figures, optical alignment to icon-text pairs, `1px` alpha hairlines, and crisp `120–180ms` hover/press/focus states.
5. **Copy Tightening (`../../sick-social/SKILL.md`):** Replace generic labels (*"Learn More"*, *"Submit"*, *"Seamless Integration"*) with specific verbs and concrete outcomes; run `sick_social_lint.py`.
6. **Before/After Pixel Proof (`../../umby-verify/SKILL.md`):** Re-capture identical viewports, inspect side by side against the Step 1 baseline, and confirm zero regressions in contrast, overflow, or keyboard focus.
