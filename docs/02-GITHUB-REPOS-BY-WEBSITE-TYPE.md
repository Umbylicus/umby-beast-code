# Curated GitHub Repositories & Reference Architectures by Website Type

## Crucial Warning Before Cloning Any UI Library

Using a popular component library out of the box with default colors, default `0.5rem` radii, and stock layout blocks is the #1 cause of "AI template fatigue." Libraries like **Aceternity UI** or **Magic UI** contain flashy effects (meteors, glowing borders,aurora beams) that instantly scream "2024 AI wrapper" when overused.

**The Billion-Dollar Rule for Open-Source Repos:**
1. **Unstyled Accessible Primitives (`Radix`, `Base UI`, `React Aria`)** are mandatory for complex interactive widgets (dialogs, comboboxes, popovers, menus, drawers) so keyboard navigation, focus trapping, and ARIA states never break.
2. **Design Tokens (`starter-tokens.css` in `umby-craft`)** must override every stock color, font, radius, and border before a single screen renders.
3. **Effect Primitives** are seasoning: at most **one** signature visual mechanic per page (such as an interactive product stage or subtle scroll-linked hardware reveal), never five competing particle effects.

---

## 1. Unstyled Primitives, Token Foundations & Micro-Interaction Kits

Use these as the structural skeleton across almost any React / Next.js / Astro application:

| Repository | Category | Why Top Teams Use It | Anti-Slop Usage Rule |
| :--- | :--- | :--- | :--- |
| **`shadcn-ui/ui`** | Owned Component Primitives | Copies source directly into your repo on top of Radix/Base UI + Tailwind so you own every pixel. | **Never** ship stock `zinc`/`slate` defaults untouched. Immediately replace root CSS variables with custom OKLCH tokens, custom typography, and bespoke button/card variants. |
| **`mui/base-ui`** | Headless UI Primitives | Built by creators of Radix & Floating UI; rock-solid unstyled accessible components for modern React. | Ideal foundation when building a proprietary company design system from scratch without third-party style baggage. |
| **`adobe/react-spectrum`** (`react-aria`) | Accessibility & Press Physics | Industry-gold `usePress`, date pickers, combo boxes, and internationalization across touch, mouse, and screen readers. | Use `react-aria-components` whenever building complex date range pickers, financial tables, or accessible drag-and-drop. |
| **`emilkowalski/vaul`** | Mobile-Native Drawers | Physics-driven drawer/sheet component with iOS-grade velocity, snap points, and background scaling. | Replace clunky mobile modals with `vaul` bottom sheets on `<768px` viewports. |
| **`emilkowalski/sonner`** | Toast Choreography | Stacked, interruptible, gesture-dismissible toast notifications with clean spring transitions. | Restyle surface border and typography to match your token system; keep toast copy factual and concise. |
| **`pacocoursey/cmdk`** | Command Menu (`Cmd+K`) | Fast, composable command palette used by Linear, Vercel, and Raycast web surfaces. | Mandatory for dense SaaS apps and documentation hubs. Pair with instant keyboard shortcuts. |
| **`ibelick/motion-primitives`** | Restrained Motion Building Blocks | Clean, composable `motion/react` primitives (morphing dialogs, animated tabs, progressive blur, text transitions). | Much cleaner and more restrained than flashy "AI beam" kits. Customize spring stiffness (`300–450`) and damping (`28–36`). |

---

## 2. Flagship Marketing, Scrollytelling & 3D / WebGL (Apple / Luxury / Studio Caliber)

When building launch pages, hardware showcases, luxury brand flagships, or interactive storytelling sites:

| Repository | Stack | Best For | Key Engineering Takeaway |
| :--- | :--- | :--- | :--- |
| **`darkroomengineering/lenis`** | Vanilla TS / React | Buttery smooth scroll normalization synced cleanly with `requestAnimationFrame` and native scrollbars. | Built by Darkroom Engineering (Awwwards-winning studio). Respect `prefers-reduced-motion` and disable smooth hijacking inside nested scrollable modals/tables. |
| **`greensock/GSAP`** (`ScrollTrigger`) | JS / React (`@gsap/react`) | Pinning stages, scrubbed timelines, split-line text reveals, and hardware-style scroll choreography. | Always wrap inside `useGSAP()` for automatic cleanup on route unmount; animate only `x`, `y`, `scale`, `rotation`, `opacity`, and `clipPath`. |
| **`pmndrs/react-three-fiber`** + **`pmndrs/drei`** | Three.js + React | Interactive 3D product configurators, studio lighting environments, glass/metal shaders, and camera rigs. | Pair with `<PerformanceMonitor>` from `drei` to dynamically step down DPR (`[1, 1.5]`) on low-power laptops/phones and render a crisp static WebP/AVIF fallback while Canvas hydrates. |
| **`darkroomengineering/satus`** | Next.js + Lenis + WebGL + Tailwind | Studio-grade creative website starter architecture by Darkroom Engineering. | Study its orchestrator pattern for syncing DOM typography layout with WebGL viewport coordinates and clean asset preloading. |
| **`theatre-js/theatre`** | JS / R3F / DOM | Visual motion-design timeline editor for choreographing complex camera paths and keyframe curves in browser. | Lets you fine-tune exact easing curves visually and export deterministic JSON state for production builds. |

---

## 3. High-Conversion E-Commerce & Headless Storefronts (Shopify / Amazon Caliber)

When building direct-to-consumer (DTC) flagship stores, multi-vendor marketplaces, or high-SKU catalogs:

| Repository | Stack | Best For | Key Engineering Takeaway |
| :--- | :--- | :--- | :--- |
| **`vercel/commerce`** | Next.js App Router + Shopify Storefront GraphQL + Tailwind | Ultra-fast headless Shopify storefronts using Server Actions, optimistic cart drawers, and edge caching. | Best starting skeleton for Shopify headless builds. Upgrade its minimal wireframe aesthetic using `umby-craft` + `umby-archetypes/references/ecommerce-conversion.md`. |
| **`Shopify/hydrogen`** | Remix / React Router + Oxygen + Storefront API | Official Shopify headless stack with built-in `<Image>`, `<Money>`, `<CartForm>`, optimistic cart hooks, and sub-request caching. | Choose Hydrogen when deploying directly to Shopify Oxygen or requiring deep B2B catalog, multipass, and localized market routing. |
| **`medusajs/nextjs-starter-medusa`** + **`medusajs/medusa`** | Next.js + Medusa v2 (Node/TS/Postgres) | Self-hosted, fully customizable commerce engine (custom checkout flows, subscriptions, multi-region warehouses, marketplaces). | Best open-source alternative when Shopify's checkout extensibility or fee model is too restrictive. |
| **`blazity/enterprise-commerce`** | Next.js + Algolia/Meilisearch + Tailwind + Shopify | Large-SKU Amazon-style catalogs needing sub-50ms faceted filtering, instant search autocomplete, and high Lighthouse scores. | Study how URL search params, facet counts, and server-rendered category grids stay fast under thousands of SKUs. |
| **`payloadcms/payload`** (`templates/ecommerce`) | Next.js App Router + Payload 3.0 + Stripe | Editorial brand commerce where rich storytelling lookbooks, custom CMS blocks, and product checkout live in one codebase. | Eliminates syncing two separate CMS and commerce webhooks for content-heavy luxury or lifestyle brands. |

---

## 4. Production SaaS Applications & Dense Product Workbenches (Linear / Stripe / Vercel Caliber)

Study or fork these real production codebases (not toy boilerplates) to see how multi-tenant SaaS apps structure auth, billing, tables, and clean UI:

| Repository | Stack | Best For | Key Engineering Takeaway |
| :--- | :--- | :--- | :--- |
| **`midday-ai/midday`** | Next.js + Turborepo + Supabase + Drizzle + Tailwind + shadcn | Financial SaaS, dense data tables, AI assistant drawers, invoice builders, and monochrome precision UI. | One of the cleanest open-source examples of **Linear/Raycast-tier visual restraint** applied to a complex data-heavy web app. |
| **`dubinc/dub`** | Next.js App Router + Prisma + Tinybird + Stripe + Upstash + Tailwind | High-throughput SaaS dashboards, analytics charts, workspace switchers, API key management, and polished marketing/docs integration. | Gold-standard monorepo (`packages/ui`) showing custom modal systems, clean empty states, domain verification flows, and fast filter bars. |
| **`calcom/cal.com`** | Next.js + tRPC + Prisma + Turborepo + Tailwind | Complex scheduling, multi-step booking state machines, timezone math, webhook integrations, and embeddable widgets. | Study its booking flow for low-friction, high-conversion stateful form UX and availability edge cases. |
| **`twentyhq/twenty`** | React + TypeScript + GraphQL + Recoil/Jotai + NestJS | Notion/Linear-grade interactive data grids, inline cell editing, custom keyboard navigation, and kanban boards. | Best open-source reference when building a spreadsheet-like or CRM-grade interactive client workspace. |
| **`nextjs/saas-starter`** | Next.js + Drizzle + Postgres + Stripe + Auth | Clean, minimal SaaS skeleton without bloated 40-package boilerplate debt. | Ideal clean-slate foundation when starting a greenfield B2B SaaS app from scratch before applying `umby-craft` tokens. |

---

## 5. Documentation, Editorial Blogs, Changelogs & Content Sites (Stripe Docs / Press Caliber)

When building developer docs, content engines, SEO hubs, or technical blogs:

| Repository | Stack | Best For | Key Engineering Takeaway |
| :--- | :--- | :--- | :--- |
| **`fuma-nama/fumadocs`** | Next.js App Router (or TanStack Start / Astro) + MDX + Shiki | Stripe/Vercel-caliber documentation, interactive OpenAPI playgrounds, instant search, and zero-bloat RSC rendering. | Cleanest open-source docs architecture today. Customize its CSS variables so your docs match your main marketing site seamlessly. |
| **`withastro/astro`** + **`withastro/starlight`** | Astro + Islands Architecture + Tailwind | Marketing sites, long-form blogs, editorial magazines, and ultra-fast content hubs shipping **0 KB of client JS** by default. | Choose Astro over Next.js whenever the site is 80%+ marketing, editorial, portfolio, or SEO content with isolated interactive islands. |
| **`shuding/nextra`** | Next.js + MDX | Lightweight developer blogs, RFC hubs, and product documentation. | Simple file-system MDX routing built by Vercel design engineering talent. |
| **`timlrx/tailwind-nextjs-starter-blog`** | Next.js + Contentlayer/Velite + MDX | Technical blogs with citations, math/KaTeX, code syntax highlighting, tag archives, and RSS/sitemap out of the box. | Strip its default pink accent and apply `umby-craft` editorial serif/sans pairing + `sick-social` blog structure. |

---

## 6. Automated Verification, Accessibility & Performance Tooling

| Repository / Tool | Role in the `umby-verify` Gate |
| :--- | :--- |
| **`microsoft/playwright`** + **`@axe-core/playwright`** | Multi-viewport screenshot capture (`375px`, `768px`, `1440px`, `1920px`), real keyboard navigation tests, and automated WCAG AA/AAA contrast & ARIA audits. |
| **`GoogleChrome/lighthouse`** / **`unlighthouse`** | Automated site-wide Core Web Vitals (`LCP`, `CLS`, `TBT`), SEO metadata, and asset weight scanning across every route in minutes. |
| **`MillionLint/react-scan`** (`aidenybai/react-scan`) | Detects unnecessary React component re-renders and main-thread jank visually during interaction stress-testing. |
