---
name: archetypes
description: Category-specific UX, layout, conversion, and architectural blueprints modeled on multi-billion-dollar leaders across five major web surfaces (Apple-tier flagship product storytelling, Shopify/Amazon e-commerce conversion, Stripe/Linear SaaS marketing with live interactive sandboxes, dense pro-tool web applications, and Fumadocs/Stripe-grade documentation and editorial blogs). Use when structuring pages, user flows, and section rhythm for a specific website category.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Archetypes: Category-Leader Website Blueprints

A luxury skincare storefront, a B2B developer API platform, and a dense financial web app require fundamentally different information architecture and pacing. Never apply a SaaS landing page structure to an e-commerce store or a marketing hero to an authenticated dashboard.

Load **only** the reference blueprint matching your current target surface:

1. **Flagship Product, Hardware & Narrative Launch Sites (Apple / Daylight / Teenage Engineering caliber):**
   Read [`references/flagship-scrollytelling.md`](references/flagship-scrollytelling.md)
2. **High-Conversion E-Commerce, DTC Storefronts & Catalogs (Shopify / Amazon / Aesop caliber):**
   Read [`references/ecommerce-conversion.md`](references/ecommerce-conversion.md)
3. **B2B SaaS, AI Infrastructure & Product-Led Marketing (Stripe / Linear / Dub / Raycast caliber):**
   Read [`references/saas-and-product-led.md`](references/saas-and-product-led.md)
4. **Authenticated Web Apps, Dashboards & Pro Workbenches (Linear App / Midday / Figma caliber):**
   Read [`references/dense-webapp-workbench.md`](references/dense-webapp-workbench.md)
5. **Developer Docs, Knowledge Hubs, Editorial Blogs & Changelogs (Stripe Docs / Fumadocs / Press caliber):**
   Read [`references/editorial-and-docs.md`](references/editorial-and-docs.md)

---

## Universal Cross-Category Rules

- **Rhythm Alternation:** Map out every section's geometry before coding. Never place two identical 3-column grids back to back.
- **Above-the-Fold Discipline:** Within `900px` desktop height (`750px` mobile), the visitor must grasp: (1) concrete product category & mechanism, (2) visual/interactive proof of craft, and (3) one unmistakable next step.
- **Navigation Restraint:** Top navigation holds at most **4–5 top-level destinations** plus **1 primary action** (and subtle `Sign in` / `Bag (2)` utility). Everything secondary belongs in clean categorized menus or the footer.
