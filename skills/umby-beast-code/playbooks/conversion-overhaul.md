# Playbook: Conversion Overhaul (Landing Page, Pricing, or Storefront PDP)

Use when optimizing signup velocity, demo bookings, or e-commerce add-to-cart / checkout conversion without resorting to sleazy dark patterns.

## Mandatory Checklist

1. **Friction & Information-Scent Audit (`../../umby-archetypes/SKILL.md`):** Evaluate the current (or planned) surface against the 5-Second Test: Can a skeptical buyer immediately tell *what this is*, *who it is for*, *concrete mechanism/price certainty*, and *the single next action*?
2. **Above-the-Fold Restructuring:** Eliminate competing navbar CTAs, vague taglines, and decorative hero banners that push proof or the buy-box below `800px` on desktop or `650px` on mobile.
3. **Interactive Proof Over Claims:** Replace static boastful claims with verifiable evidence: an interactive product sandbox, real before/after latency or cost math, transparent variant/shipping/return certainty (for commerce), or concrete customer architecture examples.
4. **Objection-Killing Copy Pass (`../../sick-social/SKILL.md`):** Rewrite headlines, pricing tier differentials, FAQ/risk-reversal microcopy, and form labels using `sick-social/references/web-conversion-copy.md`. Verify zero AI tells via `sick_social_lint.py`.
5. **Form & Checkout Ergonomics (`../../umby-craft/SKILL.md`):** Minimize input fields, set proper `autocomplete`, `inputMode`, and `type` attributes for mobile keyboards, validate inline on blur (not on first keystroke), and preserve form state across errors.
6. **Mobile Thumb-Zone & Speed Verification (`../../umby-verify/SKILL.md`):** Verify `>=44x44px` tap targets, sticky mobile buy/action ergonomics where appropriate, `CLS < 0.05`, and crisp rendering on `375x812` and `1440x900`.
