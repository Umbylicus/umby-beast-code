# Precision Easing Curves & Spring Physics Reference

## 1. Custom `cubic-bezier()` Palette (Ban Default `ease` and `linear` for UI)

```css
:root {
  /* Crisp Expo Out — Primary choice for UI entrances, cards, dialogs */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);

  /* Quart Out — Micro-interactions, button hovers, subtle reveals */
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);

  /* iOS / Vaul Sheet Curve — Drawers, bottom sheets, slide-over bags */
  --ease-sheet: cubic-bezier(0.32, 0.72, 0, 1);

  /* Crisp Exit — Dismissing toasts or closing overlays (120ms-150ms) */
  --ease-in-exit: cubic-bezier(0.32, 0, 0.67, 0);

  /* Symmetric Morph — Shared-element state switches on screen */
  --ease-in-out-quint: cubic-bezier(0.83, 0, 0.17, 1);
}
```

*(Exception: use `linear` strictly for continuous infinite marquees, progress spinners, or scrub-linked 0-to-1 scroll progress timelines.)*

## 2. Spring Configurations (`motion/react` / Physics Engines)

Avoid rubbery, high-bounce toy springs (`bounce > 0.3`) on professional interfaces:

| Interaction Surface | Stiffness | Damping | Mass | Feel |
| :--- | :--- | :--- | :--- | :--- |
| **Snappy Toggle / Pill Tab Indicator (`layoutId`)** | `480` | `36` | `0.8` | Instant, zero overshoot, razor-sharp |
| **Button Tactile Press (`whileTap={{ scale: 0.98 }}`)** | `600` | `35` | `0.6` | Physical mechanical switch |
| **Modal / Command Palette Arrival** | `380` | `32` | `0.9` | Confident settle, zero wobble |
| **Draggable Drawer / Sheet (`vaul` style)** | `320` | `34` | `1.0` | Natural momentum with clean stop |
| **Playful Consumer Card Toss (Archetype 10 only)** | `340` | `24` | `1.0` | Slight 4% organic settle |

## 3. Micro-Interaction Recipes That Signal Craft

- **Button Press:** `active:scale-[0.985]` over `100ms` so clicks feel tactile on both mouse and touch.
- **Copy-to-Clipboard Confirmation:** Morph copy icon -> checkmark (`scale(0.6) + blur(2px) -> scale(1) + blur(0)` over `160ms` `--ease-out-expo`), hold `1400ms`, morph cleanly back; keep button width locked so siblings never shift.
- **Number Transitions:** Animate financial/metric changes over `250ms` with `tabular-nums` so digits roll cleanly without horizontal layout wobble.
