---
name: architect
description: Designs domain data structures, explicit UI state machines, URL-synced state contracts, server/client boundaries, and stack choices before implementation begins. Uses structural two-candidate sketching to prevent boolean prop soup, hydration bugs, and leaky abstractions. Use before building stateful components, multi-route architectures, data flows, or selecting a web stack.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Architect: Domain Modeling, State & Stack Architecture

> **Standing rules apply.** Before changing anything, read [`../beast-code/references/standing-rules.md`](../beast-code/references/standing-rules.md): approval gates, no deploy or merge without an explicit go, feature branch with a preview, protected code, keep or redirect every URL, real proof only, and the work log.

Bad websites rot from the inside out: boolean flags multiply (`isLoading && !isError && isSubmitted`), state drifts out of sync with the URL, client bundles balloon because `"use client"` sits at the layout root, and components expose 19 optional props instead of composable slots.

Follow this 4-phase architecture protocol before writing complex logic or multi-file features.

---

## Phase 1: Select the Right Stack & Reference Blueprint

For greenfield builds or stack migrations, consult [`references/stack-and-repo-matrix.md`](references/stack-and-repo-matrix.md). Pick the **simplest architecture that delivers sub-second speed and maintainability**:
- **80%+ Content, Marketing, Portfolio, Editorial, or SEO Hub:** Prefer **Astro 5+** (with isolated React/Svelte islands only where stateful interactivity lives) or static/ISR **Next.js App Router** shipping minimal client JS.
- **Interactive SaaS App, Authenticated Dashboard, or Hybrid App+Marketing:** **Next.js App Router** (or **TanStack Start** / **Remix**) with Server Components for data reads, validated Server Actions / typed RPC at mutation boundaries, and unstyled accessible primitives (`Radix` / `Base UI` / `React Aria`).
- **Headless Storefront:** **Next.js Commerce** (`vercel/commerce` pattern) or **Shopify Hydrogen** for Shopify backends; **Medusa v2** or **Payload 3** when full Postgres/CMS ownership is required.
- **Zero-Build / Single-Artifact Prototype:** Clean semantic HTML5 + modern CSS custom properties (`@layer`, OKLCH, CSS Grid, View Transitions) + modular ES modules when no framework build chain is requested.

---

## Phase 2: Model the Domain First (Make Illegal States Unrepresentable)

Read [`references/state-and-boundary-patterns.md`](references/state-and-boundary-patterns.md) and write the core TypeScript types and state transitions **before** writing JSX:

1. **Discriminated Unions Over Boolean Soup:**
   Replace `{ loading: boolean; error?: string; data?: Order }` with an explicit tagged state:
   ```ts
   type CheckoutState =
     | { status: "idle"; cart: CartSnapshot }
     | { status: "validating"; cart: CartSnapshot }
     | { status: "payment_failed"; cart: CartSnapshot; reason: PaymentFailureCode; retryable: boolean }
     | { status: "confirmed"; orderId: OrderId; receiptUrl: string };
   ```
2. **Declarative Registries Over Branching Chains:** Encode pricing tiers, navigation trees, filter facets, keyboard shortcuts, and feature comparison matrices as typed readonly data tables rather than 300-line `if/else` JSX trees.
3. **URL-First State:** Decide upfront which states belong in URL search params (`?plan=annual&currency=EUR`, `?category=outerwear&size=M&sort=price-asc`, `?tab=security`) vs. ephemeral UI state (dropdown open/closed).
4. **Server vs. Client Leaf Split:** Push `"use client"` down to the smallest interactive leaf (`<PricingSlider />`, `<MobileMenuDrawer />`, `<AddToBagButton />`) so static copy, SVG diagrams, and SEO content render on the server at zero client bundle cost.

---

## Phase 3: Design It Twice (Boundary Sketching)

Whenever designing a shared component library primitive, cross-module state store, or API contract:
1. Write **caller usage first** (how a parent page actually renders and wires the component in 10 lines).
2. Sketch **two structurally distinct shapes** (for example: *Compound Slot Components* `<PricingTable><PricingTier /></PricingTable>` vs. *Typed Configuration Schema* `<PricingMatrix plans={PLANS} />`).
3. Prefer the candidate with **deeper interface simplicity**: hide complex keyboard, focus, aria, and layout math inside the module behind a tiny, hard-to-misuse prop contract. Assume the next engineer or agent only reads the call site.

---

## Phase 4: Scrap Early If Workarounds Multiply

During implementation, treat friction as an architectural alarm:
- If you need `as any`, `useEffect` chains syncing derived state that could be computed during render, `setTimeout(..., 0)` timing hacks, or prop-drilling across 4 layers, **stop**.
- Do not bolt guards onto a broken shape. Redesign the data model from first principles so downstream UI code becomes obvious.
