# The 20 Iron Laws of Zero-Slop Web & Software Engineering

Cite the specific law that governed any non-obvious architectural or design tradeoff in your handoff.

## I. Product & Visual Craft Laws

1. **One Primary Action Per Viewport.** Every screen and section has one unmistakable job. If two CTAs compete at equal visual weight, demote one to quiet secondary chrome or cut it.
2. **Clear the Ground First.** Premium feel comes from removing competing borders, extra card wrappers, redundant badges, and decorative noise before introducing anything new.
3. **Grayscale Hierarchy First.** Size, weight, alignment, and spatial grouping must establish clear reading order with zero color applied. Color reinforces hierarchy; it never rescues a flat layout.
4. **90 / 8 / 2 Color Budget.** Roughly 90% hue-tinted neutrals (surfaces + ink), 8% subtle structural tones (borders + muted fills), and 2% high-conviction accent reserved for primary actions and active state.
5. **Optical Over Mathematical.** Align icons to cap-height/x-height optically, calculate nested border radii concentrically ($R_{\text{inner}} = \max(0, R_{\text{outer}} - \text{padding})$), use `tabular-nums` on dynamic metrics, and constrain body measure to `45–72ch`.
6. **Rhythm Oscillation.** Never stack three consecutive sections with identical layout geometry, height, or card count. Alternate dense proof, expansive visual stage, asymmetric split, and focused conversion moments.
7. **Every State Is Designed.** Happy-path mockups are 20% of UI engineering. Default, hover, active press, keyboard `focus-visible`, loading, empty, error with recovery path, partial data, and long-text overflow must all look intentional.
8. **Physics-Driven, Frequency-Bound Motion.** High-frequency product controls respond in `80–150ms` (or `0ms`); expressive marketing transitions use snappy `cubic-bezier(0.16, 1, 0.3, 1)` ease-out or damped springs on `transform` and `opacity` only, with complete `prefers-reduced-motion` parity.
9. **Mechanism Over Adjective in Copy.** Never claim a product is *"blazingly fast, seamless, and revolutionary."* State the concrete mechanism or verified number (*"Syncs 50,000 rows in 38ms over IndexedDB"*). Never fabricate metrics, logos, or testimonials.

## II. Architecture & Code Clarity Laws

10. **Shape the Data Before the Screen.** Encode state as discriminated unions, explicit state machines, or declarative registries—never scattered boolean flags (`isLoading && !isError && isReady`) that permit impossible UI states.
11. **Guards at Boundaries, Purity Inside.** Parse and validate external inputs (URL params, form payloads, API responses, env vars, CMS fields) once at the boundary with strict schemas; keep internal components and domain functions pure and trusted.
12. **URL Is the First State Manager.** Search queries, active tabs, filter facets, sort order, pagination, and shareable modal/variant states belong in URL search params so reload, deep-linking, and browser Back work natively.
13. **First-Principles Integration.** When adding a new requirement to an existing site, integrate it as if it belonged to the foundational token and component architecture from day one—never bolt on inline style overrides or `!important` patches.
14. **Finish Every Migration.** During brownfield upgrades, do not leave `ButtonNew`, `ButtonV2`, and `OldHeroBackup` rotting side by side. Migrate in-scope callers and delete dead code in the same verified unit.
15. **Make It Quick to Read.** Collapse single-caller wrapper components, eliminate prop-drilling tunnels where composition works, keep mutable state in the narrowest possible leaf, and make names honest enough that narration comments are unnecessary.
16. **Automate What Must Stay True.** Whenever an invariant matters (token compliance, zero dead links, copy burstiness, comment hygiene, responsive overflow), enforce it via a repeatable script, type constraint, or lint check rather than hoping future prompts remember.

## III. Verification & Execution Laws

17. **Build in Checked Slices.** Break large builds into vertical slices that each compile, render, and pass behavioral checks end-to-end before starting the next slice.
18. **Falsify Before Patching Twice.** If two fix attempts sharing an assumption fail the same check, stop patching. Write down the assumption, instrument the exact runtime/DOM state to falsify it, and fix the root cause.
19. **Test User-Observable Behavior, Not Internals.** Assert what a user or caller sees and does (accessible roles, rendered text, URL changes, network payloads, keyboard flows), never private hook state or brittle CSS class strings.
20. **Real Surface Proof Only.** Never claim visual polish without inspecting rendered viewports; never claim performance wins without baseline vs. after measurements; never claim live integration verification when only mocked contracts ran.
