# Domain State, React Composition & Boundary Discipline Patterns

## 1. Zero Derived-State `useEffect` Anti-Patterns

Never store values in `useState` and sync them inside `useEffect` when they derive deterministically from props, URL params, or existing state.
- **Wrong:** `useEffect(() => { setFilteredItems(items.filter(...)); }, [items, query]);` (causes double render, stale frame flashes, and cascading state bugs).
- **Right:** Compute `const filteredItems = useMemo(...)` (or plain inline calculation) directly during render, and reset child state cleanly via a semantic `key={selectedAccountId}` prop when identity changes.

## 2. Compound Components Over Boolean Prop Proliferation

Never build a `<Card isCompact hasHeaderBorder showFooterAction isHighlighted isClickable />` monster.
Build composable semantic slots with `data-slot` attributes and shared CSS token styling:
```tsx
<Surface elevation="raised" interactive>
  <SurfaceHeader>
    <SurfaceTitle>Treasury Yield</SurfaceTitle>
    <Badge tone="positive">4.92% APY</Badge>
  </SurfaceHeader>
  <SurfaceBody>...</SurfaceBody>
</Surface>
```

## 3. Boundary Validation & Branded Primitives

- Validate all external inputs (form `FormData`, query parameters, JSON responses, webhook payloads, `.env` configuration) at the system edge using a schema validator (`zod`, `valibot`, or a small explicit parser function).
- Represent money in **integer minor units** (`cents: number` + explicit `currency: CurrencyCode`), never floating-point dollars (`19.99 * 3 === 59.970000000000006`).
- Handle network cancellation and rapid user clicking idempotently: disable duplicate non-idempotent form submissions while in flight (`aria-busy="true"`), or pass an idempotency key / `AbortSignal` for search and filter queries.

## 4. Optimistic UI With Honest Rollback

On interactive apps and storefronts (adding to bag, toggling bookmarks, reordering rows, archiving items):
1. Apply the optimistic state immediately (`<50ms` perceived latency).
2. Reconcile against the authoritative server response.
3. If the mutation fails, roll back cleanly to the prior snapshot and surface a specific, actionable recovery toast/inline message—never claim `"Saved!"` before confirmation unless rollback is wired.
