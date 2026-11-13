# Stack Decision Matrix & Reference Repository Patterns

Choose the lightest stack that satisfies the product's interactivity, SEO, and deployment requirements:

| Website / App Category | Recommended Primary Stack | UI & Motion Layer | Gold-Standard Reference Repos to Emulate |
| :--- | :--- | :--- | :--- |
| **Marketing Site, Launch Page, Agency Studio, Portfolio, SEO Content Hub** | **Astro 5+** (Islands) or **Next.js App Router** (Static/RSC) + TypeScript | Tailwind CSS v4 (OKLCH tokens) + Motion / GSAP + Lenis (optional) | `withastro/astro`, `darkroomengineering/lenis`, `ibelick/motion-primitives` |
| **B2B SaaS Marketing + Authenticated Dashboard App** | **Next.js App Router** + TypeScript + Drizzle/Prisma + Postgres + Auth | Radix / Base UI (owned source via shadcn pattern, heavily customized) + `cmdk` + `sonner` + `vaul` | `dubinc/dub`, `midday-ai/midday`, `calcom/cal.com`, `nextjs/saas-starter` |
| **Headless E-Commerce Storefront (Shopify / DTC)** | **Next.js App Router** (`vercel/commerce` pattern) or **Shopify Hydrogen** | Tailwind CSS v4 + React Aria / Radix + `vaul` mobile cart sheet + URL search-param facets | `vercel/commerce`, `Shopify/hydrogen`, `blazity/enterprise-commerce` |
| **Self-Hosted Custom Commerce / Editorial Brand Store** | **Next.js** + **Medusa v2** or **Payload CMS 3.0** + Stripe | Custom OKLCH token system + accessible headless primitives | `medusajs/nextjs-starter-medusa`, `payloadcms/payload` |
| **Developer Documentation, API Reference & Technical Blog** | **Fumadocs** (Next.js) or **Astro Starlight** + MDX + Shiki | Dual-theme syntax highlighting + sticky scrollspy TOC + `Cmd+K` search | `fuma-nama/fumadocs`, `withastro/starlight` |
| **Interactive 3D Hardware / Configurator Showcase** | **Next.js** or **Vite** + **React Three Fiber** (`@react-three/fiber` + `drei`) | Static high-res AVIF/WebP LCP poster + adaptive DPR `[1, 1.5]` + GSAP ScrollTrigger | `pmndrs/react-three-fiber`, `pmndrs/drei`, `darkroomengineering/satus` |
| **Lightweight Standalone Tool / Landing Page (No Framework Requested)** | Semantic HTML5 + Modern CSS (`@layer`, `clamp()`, OKLCH, CSS Grid, View Transitions) + Vanilla TS/ESM | Zero external bloat; ships in `<25KB` total with instant `100` Lighthouse score | Native Web Platform APIs |
