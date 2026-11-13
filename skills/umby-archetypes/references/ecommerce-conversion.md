# Category Blueprint 2: High-Conversion E-Commerce & Storefronts (Shopify + Amazon Synthesis)

Synthesize **Aesop/Shopify brand elevation** with **Amazon Prime frictionless buying clarity**.

## 1. Product Detail Page (PDP) — The Money Surface

- **Desktop 2-Column Split (`58%` Media Gallery / `42%` Sticky Buy Box):**
  - Gallery: Instant primary image (`fetchpriority="high"`, zero CLS `aspect-[4/5]` or `1/1`), crisp thumbnail rail or vertical editorial stack, pinch/click high-res zoom.
  - Sticky Buy Box (`position: sticky; top: 96px`):
    1. Breadcrumb (`Shop / Coffee / Single Origin`)
    2. Product Title + concise 1-line tasting/function summary
    3. Price (`tabular-nums`) + unit math (`$24.00 · $0.96/oz`) + verified review count anchor link (only if real reviews exist)
    4. URL-synced Variant Swatches (`?color=obsidian&size=M`): unavailable combinations visually crossed out (not hidden, and never selectable into a surprise error)
    5. Size Guide drawer trigger right beside the Size label
    6. Full-width, high-contrast **Primary CTA** (`Add to bag · $24`) with optimistic slide-over cart response in `<100ms`
    7. Concrete Fulfillment & Risk Reversal directly under CTA: shipping threshold (`Free 2-day shipping over $50`), dispatch window, and exact return policy (`30-day free returns`)
    8. Collapsible `1px`-hairline accordions for `Materials & Specs`, `Dimensions & Fit`, and `Shipping & Care`.
- **Mobile (`<768px`) Thumb-Zone Rule:**
  - Horizontal swipeable gallery with subtle `1 / 5` pill counter.
  - Once the inline `Add to bag` button scrolls above the viewport, surface a compact `64px` **Sticky Bottom Buy Bar** showing variant summary, price, and `Add to bag`.

## 2. Slide-Over Cart Drawer (`vaul` / Accessible Dialog)

- Opens immediately on `Add to bag` without hijacking the user away from browsing onto a slow `/cart` page reload.
- Dynamic **Free Shipping Progress Bar** calculated in integer cents (`Add $12.00 more for free express shipping` -> `Unlocked: Free express shipping`).
- Optimistic `+ / - / Remove` quantity steppers (`tabular-nums`), transparent subtotal (stating *"Shipping & taxes calculated at checkout"* instead of surprise fees), and express checkout button.

## 3. Collection / Category Grid & Search

- **URL-Synced Faceted Filtering:** Price range, size, material, availability (`in_stock=true`), and sort order update URL params shallowly with instant UI response and active filter chips (`Clear all`).
- **Product Card Discipline:** Maximum 3 data lines under image: `Title`, `Subtle Variant/Color Count`, and `Price`. Secondary hover angle image crossfades smoothly on desktop (`@media (hover: hover)`). Zero blinking `"SALE!! 🔥"` circus badges.
