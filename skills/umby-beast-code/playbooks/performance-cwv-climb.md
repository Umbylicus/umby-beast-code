# Playbook: Performance & Core Web Vitals Climb

Use when optimizing LCP, CLS, INP, bundle size, server TTFB, scroll framerate, or Lighthouse scores.

## Mandatory Checklist

1. **Measure Baseline First:** Build in production mode (`next build` / `astro build` / `vite build`), not dev mode, and capture concrete baseline numbers: JS bundle kB per route, LCP ms, CLS score, INP/TBT ms, or frame drop profile. Never optimize blind.
2. **Explain the Bottleneck:** Identify the true limiter before editing: render-blocking fonts/CSS, unoptimized hero media without `fetchpriority="high"`, massive client `"use client"` trees pulling heavy libraries, main-thread hydration waterfalls, or non-composited CSS animations (`top`/`height`/`box-shadow` on scroll).
3. **One Hypothesis Per Measured Iteration:**
   - Move static trees to Server Components or Astro islands.
   - Preload primary `.woff2` subset with `font-display: swap` or metric-matched fallback; set explicit `width`/`height` or `aspect-ratio` on every image/video/skeleton (`CLS = 0.00`).
   - Lazy-load below-the-fold modals, charts, and 3D canvases (`dynamic()` / IntersectionObserver).
   - Convert layout-thrashing animations to GPU-composited `transform` and `opacity`.
4. **Re-Measure & Vet the Number:** Re-run the exact production benchmark. Keep only changes that measurably improve the target metric without degrading visual craft or accessibility.
5. **Visual Parity Check (`../../umby-verify/SKILL.md`):** Confirm zero missing fonts, broken images, or hydration mismatches across `375px` and `1440px`.
