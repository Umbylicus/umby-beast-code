# The 30 Instant Visual Tells of AI-Generated UI (Eliminate on Sight)

Every item below signals an unedited LLM template. Replace immediately with the paired engineering fix.

| # | AI-Slop Pattern | Exact Replacement |
| :--- | :--- | :--- |
| 1 | Indigo-to-purple-to-pink gradients (`from-indigo-500 via-purple-500 to-pink-500`) | Solid high-conviction brand accent or subtle 2-stop directional OKLCH surface light. |
| 2 | Floating blurred neon blobs behind every hero (`blur-3xl opacity-30 bg-purple-600`) | Clean typographic tension, architectural `1px` grid lines, photography, or an interactive product stage. |
| 3 | Emojis used as feature icons, nav items, or headings (`🚀 Fast`, `✨ AI-Powered`, `🔒 Secure`) | Uniform `1.5px`-stroke SVG icon family (`Lucide` / `Phosphor`) or crisp typographic labels with zero icons. |
| 4 | Sparkle icon (`✨`) slapped onto every button and badge | Name the actual action (`Generate SQL query`, `Summarize 14 threads`) without novelty sparkles. |
| 5 | Three identical rounded cards in a row with tinted icon squares ("Icon Tile Theater") | Asymmetric split showcase, live interactive demo, specification table, or narrative 2-column editorial proof. |
| 6 | Numbered `"01 / 02 / 03 — How It Works"` generic boxes | One connected workflow diagram, interactive stepper, or concrete before-and-after artifact. |
| 7 | Cards nested inside cards inside cards with competing borders + shadows + fills | Group with whitespace or `1px` hairlines; maximum one card depth per module. |
| 8 | Every single section centered with identical vertical padding (`py-20 text-center` x 7) | Alternate left-aligned asymmetric splits, full-bleed stages, dense tables, and focused conversion moments. |
| 9 | Stock unmodified `shadcn/ui` default `slate`/`zinc` variables and default pill badges everywhere | Custom OKLCH token ramp, bespoke font pair, customized button height/radius/press physics. |
| 10 | Rainbow gradient text (`bg-clip-text text-transparent bg-gradient-to-r`) on headlines | Solid high-contrast ink; create emphasis via scale, weight, or italic serif contrast—never rainbow text. |
| 11 | Fake social proof (`"Trusted by 10,000+ teams"`, `"4.9/5 from 2,000+ reviews"`, `Acme Corp` logos) | Real verified proof only, or omit vanity counters completely and show a real interactive product artifact. |
| 12 | Stock AI-generated smiling avatar circles (`Jane Doe, CEO at TechCorp`) | Real named customer quotes with permission, or concrete architectural capability breakdowns. |
| 13 | `"Get Started"` and `"Learn More"` repeated 4+ times on one page | Specific outcome verbs (`Start sandbox`, `Read security whitepaper`, `Compare API plans`). |
| 14 | Glassmorphism (`backdrop-blur-md bg-white/10`) over solid empty backgrounds | Use translucency *only* on sticky navbars/overlays where real content scrolls visibly underneath. |
| 15 | Pure `#000000` background with `#ffffff` text and neon `#00ffcc` borders | Perceptual OKLCH obsidian (`oklch(0.14 0.008 H)`) with `oklch(0.96 0.005 H)` ink and `8%` alpha hairlines. |
| 16 | Gray text on gray cards failing WCAG contrast (`#71717a` on `#27272a`) | Verify `>=4.5:1` contrast for all body/helper copy; step ink lightness up cleanly. |
| 17 | `transition-all duration-300` slapped onto interactive elements | Transition explicit properties only (`transition-[transform,opacity,background-color] duration-150`) with custom ease-out. |
| 18 | Scroll-jacked fade-up (`opacity-0 translate-y-8`) delaying reading on every single paragraph | Keep body copy immediately readable; reserve scroll choreography for meaningful stage transitions. |
| 19 | Equal-radius nested elements (`rounded-2xl` image inside `rounded-2xl p-4` card causing pinched corners) | Concentric math: outer `rounded-2xl` (`16px`) - `p-2` (`8px`) = inner `rounded-lg` (`8px`). |
| 20 | Four different font weights and seven arbitrary `text-[15px]`/`text-[19px]` sizes in one view | Strict 5–6 token type scale and at most 2–3 weights (`400`, `500`, `600`). |
| 21 | Wide 110-character full-width body paragraphs spanning `1280px` | Constrain prose blocks to `max-w-[65ch]` (`max-w-2xl`) even inside wide layouts. |
| 22 | Jittering numbers in sliders, pricing toggles, and counters | Enforce `font-variant-numeric: tabular-nums` (`tabular-nums`). |
| 23 | Pricing page with 3 identical tiers where `"Pro — Most Popular"` bounces 16px taller with a neon ring | Subtle surface elevation or hairline accent + crisp differential table listing only what actually changes per tier. |
| 24 | Footer with 5 columns of dead `#` placeholder links (`Careers`, `Press`, `Investors`, `Blog`) | Link only real, working routes or honest contact endpoints; compact single-row footer if the site has 3 pages. |
| 25 | `<div onClick={...}>` fake buttons invisible to keyboard `Tab` and screen readers | Semantic `<button type="button">` or `<a href="...">` with visible `:focus-visible` ring. |
| 26 | Layout jump (`CLS > 0.1`) when web fonts, hero images, or async data load | Explicit `width`/`height` or `aspect-ratio`, preloaded primary font, and exact-height skeletons. |
| 27 | Desktop navbar cramming 7 links onto 2 wrapped rows on `375px` mobile | Clean mobile header (`Logo` + primary compact CTA + accessible sheet/drawer menu via `vaul` or `<dialog>`). |
| 28 | Heavy blurred black drop shadows (`shadow-2xl`) on dark mode cards (invisible or muddy) | `1px` top specular highlight + slightly lighter surface step (`oklch(+0.04 L)`). |
| 29 | Overly busy charts with 6 gridline axes, legends, gradients, and tooltips blocking data | Tufte minimalism: muted dashed horizontal baseline only, direct inline value readout, crisp single series stroke. |
| 30 | Generic pill badge above every single section heading (`[ FEATURES ]`, `[ TESTIMONIALS ]`, `[ FAQ ]`) | Let strong H2 headings speak directly; use an eyebrow label at most once or twice where category context truly helps. |
