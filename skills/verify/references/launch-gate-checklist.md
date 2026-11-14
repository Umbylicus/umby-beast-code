# Production Web Launch Gate Checklist

## 1. Visual & Layout Integrity
- [ ] Zero horizontal scrollbar (`document.documentElement.scrollWidth <= window.innerWidth`) at `375px`, `430px`, `768px`, `1440px`, and `1920px`.
- [ ] Concentric border radii and consistent 4pt/8pt token spacing across all sections.
- [ ] Body measure constrained to `<=72ch`; headings use `text-wrap: balance`; dynamic figures use `tabular-nums`.
- [ ] Both Light and Dark themes (if supported) meet WCAG AA contrast (`>=4.5:1` prose, `>=3:1` large display & UI controls).

## 2. Interaction, States & Accessibility
- [ ] Every interactive element uses semantic `<button>`, `<a href>`, or `<input>` (or full ARIA role + keyboard handlers) with visible `:focus-visible` styling.
- [ ] Touch targets measure `>=44x44px` on mobile viewports.
- [ ] Empty, loading, validation-error, and network-failure states are implemented with specific human recovery microcopy.
- [ ] `prefers-reduced-motion: reduce` disables spatial motion/scroll-jacking while keeping all content accessible.

## 3. Performance & Core Web Vitals Hygiene
- [ ] Production build (`next build` / `astro build` / `vite build`) completes with zero TypeScript or bundler errors.
- [ ] Above-the-fold LCP image preloads (`fetchpriority="high"`, eager loading) with explicit `width`/`height` or `aspect-ratio` (`CLS < 0.05`).
- [ ] Below-the-fold heavy media, modals, and 3D scenes lazy-load cleanly.
- [ ] Zero `console.error`, uncaught promise rejections, or hydration mismatches.

## 4. Technical SEO & Metadata (Public Pages)
- [ ] Unique, specific `<title>` (`25–60` chars) and `<meta name="description">` (`110–160` chars, zero AI clichés) per route.
- [ ] Exactly one `<h1>` per route with logical `<h2>` -> `<h3>` hierarchy.
- [ ] Canonical URL, OpenGraph (`og:title`, `og:description`, `og:image`), Twitter card meta, favicon, and valid `robots.txt` / `sitemap.xml` where applicable.
- [ ] Every page with JSON-LD passes Google's Rich Results Test with zero errors, and the structured data matches visible page content (no review or rating markup without real on-page reviews).

## 5. Numbers Gate (see `SKILL.md` Step 5)
- [ ] Lighthouse mobile scores `>=95` for Performance, Accessibility, Best Practices, and SEO on every key page template, measured on the production build or preview URL.
- [ ] Zero broken internal or external links; on a rebuild, every old URL returns `200` or a `301` to its mapped replacement.
- [ ] Existing tests, typecheck, and production build all pass.
- [ ] Zero lorem ipsum, placeholder copy, or invented proof in rendered pages.
