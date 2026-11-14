# Scrollytelling, Smooth Scroll & 3D/WebGL Performance Laws

## 1. Scroll-Linked Storytelling (Apple / Darkroom Pattern)

1. **Never Block Reading:** Standard prose, feature explanations, pricing, and footers must be readable immediately without waiting for `IntersectionObserver` delays. Reserve scroll-driven choreography for **1 or 2 dedicated hero/product stages**.
2. **Native First, GSAP When Pinning:**
   - For simple scroll progress bars or parallax depth (`<=24px` subtle offset), prefer native CSS Scroll-Driven Animations (`animation-timeline: view()`) where supported with clean static fallback.
   - For multi-beat pinned product stages, use `GSAP` + `ScrollTrigger` wrapped inside `@gsap/react`'s `useGSAP(() => { ... }, { scope: containerRef })` so pins, spacers, and matchMedia listeners clean up 100% on client route navigation.
3. **Lenis Smooth Scroll Guardrails:**
   - If enabling `lenis`, sync it to GSAP's ticker (`gsap.ticker.lagSmoothing(0)`), add `data-lenis-prevent` on every scrollable modal, drawer, code block, and select dropdown, and disable `lenis` automatically when `prefers-reduced-motion: reduce` matches.

## 2. React Three Fiber / Three.js / Canvas Frame Sequences

1. **Zero-Blank-Canvas Rule:** Always render an instant server-rendered HTML/AVIF poster silhouette in the exact stage geometry while Three.js / GLTF assets stream, then crossfade cleanly over `300ms` once the first WebGL frame compiles shaders.
2. **Battery & Frame Budget Protection:**
   - Set `<Canvas dpr={[1, 1.5]} frameloop="demand">` whenever the scene only updates on scroll, pointer move, or camera orbit—never burn 120fps GPU cycles when the viewport is idle or scrolled off-screen!
   - Compress `.glb` geometry with Meshopt/Draco and textures to `.ktx2` / `.webp` (`<=2MB` total initial 3D payload).
3. **Mobile Breakpoint Strategy:** On `<768px` viewports, simplify shader complexity, disable pointer-hover raycasting, and verify vertical touch scrolling passes unimpeded over the `<Canvas>` (`touch-action: pan-y`).
