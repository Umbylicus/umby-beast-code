# Category Blueprint 4: Authenticated Web Apps, Dashboards & Pro Workbenches (Linear / Midday / Figma Caliber)

## 1. Chrome Recedes, User Data Leads

- **Density Profile:** Body/table text at `13px–14px` (`0.8125rem–0.875rem`), row heights at `36px–44px`, compact `28px–32px` toolbar controls, `1px` hairline structural dividers instead of floating cards with `24px` gaps everywhere.
- **Navigation Shell:** Collapsible `220px–240px` left rail (`Cmd+\` toggle) + `Cmd+K` global command palette (`cmdk`) + breadcrumb header bar (`48px` height) with contextual primary action on the far right.

## 2. Data Tables, Lists & Charts That Feel Native

- **Tables:** Sticky column headers, right-aligned numeric/currency columns with `tabular-nums`, monospace IDs/hashes, row hover highlight, keyboard `j/k` or arrow navigation where power-user speed matters, bulk-selection action bar appearing cleanly on selection, and URL-persisted filters/sort.
- **Charts:** Zero 3D pies or rainbow gradients. Use 1 primary brand/ink stroke + subtle area fill (`8%` alpha) + crisp crosshair hover tooltip showing exact date and delta.
- **Empty & Zero States:** Never render a blank white box with `"No data found"`. Render a quiet architectural illustration or sample schema preview explaining *what will appear here* plus one primary button (`Connect Stripe account` / `Create first invoice` / `Load sample dataset`).

## 3. Speed & Perceived Zero-Latency

- Optimistic local updates on status toggles, archive/delete, and inline renames.
- Exact-geometry skeleton placeholders only when cold cache exceeds `150ms` (avoid flashing skeletons for `<100ms` reads).
- Preserve scroll position and filter state across detail-drawer opens (`?inspect=inv_8921`).
