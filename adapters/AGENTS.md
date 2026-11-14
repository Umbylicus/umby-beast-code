# Project Engineering & Design Standard (Umby Beast Code)

Whenever building, updating, restyling, debugging, or writing copy for any website or web application in this workspace, activate the **`beast-code`** skill tree:

1. **Orchestrate via `beast-code`:** Inspect existing repository tokens, routes, and scripts first (`preflight_recon.py`). Never ask observable repo questions; ask at most 4–5 sharp creative/product direction questions (`discover`) when brand tension, audience, or primary viewport action is unstated.
2. **Architecture & Tokens First:** Model stateful UI with discriminated unions and URL search params (`architect`) and establish perceptual OKLCH semantic tokens, fluid `clamp()` typography, concentric border radii, and `1px` alpha hairlines (`craft`) before building screens.
3. **Zero AI Slop (Visual or Written):**
   - Ban indigo-purple gradients, glowing hero blobs, emoji UI icons, repeated 3-card icon rows, nested card bloat, and fake social proof (`audit_ui_slop.py`).
   - Draft all headlines, microcopy, blog posts, and social announcements using `sick-social` and verify with `sick_social_lint.py` (high sentence burstiness, concrete mechanisms, zero em-dash chains, zero *"Not X, it's Y"* formulas, zero AI buzzwords).
4. **Clarity & Real-Pixel Proof:** Run `comment-slicer` (`slicer_scan.py`) after every code batch to strip narration comments, dead code, and `@ts-ignore`/`any` suppressions. Before declaring any UI work done, render and critique real viewports (`375px`, `768px`, `1440px`, `1920px`) via `verify` and confirm zero console/hydration errors.
