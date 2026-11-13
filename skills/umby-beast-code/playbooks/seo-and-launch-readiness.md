# Playbook: Technical SEO, Accessibility & Launch Readiness Gate

Use before launching any public website, storefront, blog, or marketing property to production.

## Mandatory Checklist

1. **Metadata & Social Card Completeness (`../../umby-verify/SKILL.md`):** Run `verify_surface_readiness.py` against the built site or live local URL. Ensure every indexable route has a unique, non-generic `<title>` (`<=60` chars), specific `<meta name="description">` (`120–160` chars written via `sick-social`), canonical URL, and high-contrast `1200x630` OpenGraph / Twitter image card.
2. **Crawlability & Structured Data:** Verify `robots.txt`, `sitemap.xml`, clean semantic heading hierarchy (exactly one `<h1>` per page, no skipped heading levels), and valid JSON-LD (`Organization`, `Product`, `Article`, `FAQPage`, or `SoftwareApplication` matching actual visible content).
3. **Accessibility & Keyboard Walk:** Verify semantic landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`), skip-to-content link, `>=4.5:1` body contrast, visible `:focus-visible` outlines across every interactive control, descriptive `alt` text on informative images (`alt=""` on decorative elements), and accessible form error associations (`aria-describedby` / `aria-invalid`).
4. **Resilience & Edge Pages:** Confirm custom, on-brand `404` and `500`/error boundary pages with clear navigation home, favicon/manifest icons in light & dark browser tabs, and legal/privacy links where required.
5. **Production Build & Link Integrity:** Run a clean production build, crawl all internal `<a href>` targets to guarantee zero broken links, and verify mobile + desktop renders.
