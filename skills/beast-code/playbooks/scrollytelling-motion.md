# Playbook: Scrollytelling, Choreography & Interactive 3D/WebGL

Use when building Apple-caliber scroll-linked storytelling, studio portfolios, hardware showcases, GSAP/Lenis stages, or React Three Fiber scenes.

## Mandatory Checklist

1. **Narrative Storyboard First (`../../archetypes/SKILL.md`):** Map the scroll arc in 4–6 distinct beats (Opening Hook -> Physical/Interactive Reveal -> Precision Detail Zoom -> Spec Proof -> Direct Action). Every pinned stage must communicate a concrete product truth—never hijack scroll for empty spectacle.
2. **Physics & Cleanup Architecture (`../../motion/SKILL.md`):**
   - Animate strictly `transform` (`translate3d`, `scale`, `rotate`), `opacity`, and `clip-path` (or scrubbed `<canvas>` / WebGL uniforms).
   - Scope all GSAP ScrollTriggers inside `useGSAP()` (or framework equivalent) so route transitions dispose pins cleanly without ghost spacers.
   - Never hijack native scroll velocity inside nested modals, code blocks, or data tables.
3. **Progressive Enhancement & Fallback:**
   - Render a high-craft static poster/layout immediately before WebGL/heavy assets finish streaming so LCP stays fast.
   - Cap DPR to `[1, 1.5]` or adapt dynamically on mobile/battery-constrained devices.
   - Provide a complete, dignified `prefers-reduced-motion: reduce` layout where content reads cleanly with instant crossfades instead of scrubbed camera flights.
4. **Typography & Contrast Over Media (`../../craft/SKILL.md`):** Guarantee `>=4.5:1` text legibility across every frame of a moving background using controlled scrims or dedicated high-contrast stage zones.
5. **60fps & Mobile Touch Verification (`../../verify/SKILL.md`):** Test full scroll top-to-bottom and rapid reverse-scroll on both `1440px` desktop and `375px` mobile touch emulation; verify zero stuck pins, horizontal overflow, or WebGL context loss errors.
