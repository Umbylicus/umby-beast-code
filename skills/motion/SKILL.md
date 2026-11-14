---
name: motion
description: Choreographs 60/120fps web interaction physics, spring dynamics, custom cubic-bezier curves, View Transitions, Apple-caliber scroll-linked stages, and WebGL/React-Three-Fiber progressive fallbacks with zero layout jank. Use whenever adding micro-interactions, menus, sheets, page transitions, scroll reveals, GSAP/Lenis timelines, or interactive 3D scenes.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Motion: Interaction Physics & Scroll Choreography

> **Standing rules apply.** Before changing anything, read [`../beast-code/references/standing-rules.md`](../beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

Great motion feels inevitable and physical; bad motion feels slow, bouncy, and decorative. Most AI-generated motion fails because it uses sluggish `ease-in-out` defaults, animates layout-thrashing properties (`height`, `top`), or slaps delayed scroll fade-ins onto every paragraph.

Read on demand:
- [`references/curves-and-springs.md`](references/curves-and-springs.md): Exact `cubic-bezier` coordinates, `motion/react` spring configs, and duration budgets.
- [`references/scrollytelling-and-3d.md`](references/scrollytelling-and-3d.md): GSAP ScrollTrigger, Lenis, View Transitions, and React Three Fiber performance laws.

---

## The 6 Laws of Billion-Dollar Web Motion

1. **Frequency Dictates Duration:**
   - **High-frequency controls** (>10x/session: command palette, tabs, row selection, dropdown menus, hover states): `80ms–140ms` or instant `0ms`. Never make a power user wait on a `350ms` menu reveal.
   - **Medium-frequency spatial transitions** (drawers, modals, accordions, cart sheets, toast arrivals): `180ms–260ms` snappy ease-out or critically damped spring.
   - **Rare hero / stage choreography** (initial product stage entrance, scrubbed hardware explode): `400ms–700ms` or directly tied 1:1 to user scroll position.
2. **Never Enter on `ease-in`:** Elements entering the screen or responding to a tap must start at peak velocity and decelerate smoothly (`cubic-bezier(0.16, 1, 0.3, 1)` or `cubic-bezier(0.32, 0.72, 0, 1)`). Use `ease-in` (`cubic-bezier(0.32, 0, 0.67, 0)`) only for exits that leave permanently.
3. **GPU-Composited Properties Only:** Animate strictly `transform` (`translate3d`, `scale`, `rotate`), `opacity`, `clip-path`, and `filter` (sparingly). Never animate `width`, `height`, `padding`, `margin`, `top`, or `left` on 60fps paths (use CSS Grid `grid-template-rows: 0fr -> 1fr` or FLIP `layout` transforms when height must morph).
4. **Origin-Aware Scaling:** Popovers, dropdowns, and tooltips must scale from `0.95 -> 1.0` (`never 0 -> 1`, which looks cartoonish) anchored at their trigger's `transform-origin` (`var(--radix-popover-content-transform-origin)`), paired with `opacity: 0 -> 1`.
5. **Interruptibility:** User input always wins. Prefer CSS transitions or physics springs (`motion/react`) over rigid keyframe animations on interactive controls so reversing mid-hover or mid-drag never snaps abruptly.
6. **Mandatory `prefers-reduced-motion` Parity:** When the user enables Reduce Motion, replace spatial travel (`translate`, camera pans, parallax) with clean `120ms` opacity crossfades or instant state updates—never hide content behind an un-triggered scroll observer.
