# Brownfield Migration, URL & SEO Safety Guardrails

## 1. Zero Silent URL Breakage
- Never rename an indexable public URL slug (`/features/automation` -> `/platform/workflows`) without **both** explicit user approval **and** a permanent `301`/`308` redirect rule in `next.config.*` / `vercel.json` / `_redirects` / `astro.config.*`.
- Preserve URL query parameter contracts (`?utm_*`, `?ref=`, `?plan=`, `?variant=`) when refactoring navigation or client routers.

## 2. Form, Webhook & Checkout Contract Integrity
- When restyling lead-capture, login, or checkout forms, preserve exact `<input name="...">` keys, validation semantics, CSRF/honeypot fields, and API endpoint payloads unless also migrating the backend handler in the same tested slice.

## 3. Incremental Styling Coexistence (Large Codebases Only)
- If the user scopes a redesign strictly to *one* landing page inside a massive legacy app (e.g., Bootstrap/SCSS monolith), scope new CSS variables to a root wrapper attribute (`[data-beast-surface="marketing"]`) rather than mutating global `body` / `button` resets that could break unvisited admin screens—and test at least one untouched legacy route to confirm zero bleed.
