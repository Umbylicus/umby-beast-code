# Category Blueprint 5: Documentation, Knowledge Hubs, Blogs & Changelogs (Stripe Docs / Fumadocs / Press Caliber)

## 1. Documentation & API References

- **3-Column Desktop Shell:** Left navigation tree (`240px–260px`, collapsible groups, active route indicator) + Center prose column (`max-w-[68ch]`, generous `48px` gutter) + Right `On this page` scrollspy TOC (`200px`, hidden below `1280px`).
- **Diátaxis Information Clarity:** Never mix a 5-minute *Quickstart* with an exhaustive *Configuration Reference*.
  - **Quickstart:** Copy-pasteable working path to first green output in `<3` minutes.
  - **Concept Guide:** Architectural mental model + clean SVG/Mermaid diagram.
  - **API Reference:** Sticky two-column Stripe layout (prose parameters & error codes on left; pinned request/response code examples on right).
- **Code Block Craft:** Filename header bar, language badge, 1-click copy button with checkmark morph, highlighted diff/focus lines, horizontal scroll (never ugly mid-token line wrapping).

## 2. Long-Form Editorial Blogs & Changelogs

- Pair layout tokens here with [`../../sick-social/SKILL.md`](../../sick-social/SKILL.md) (`references/blog-and-essays.md`) so prose quality matches typographic quality.
- **Reading Comfort:** `17px–18px` body font, `1.65–1.72` line-height, `62–66ch` measure, clear author/date/reading-time metadata line, footnotes/sidenotes instead of cluttered parenthetical tangents, and crisp captioned figures (`<figure>` + `<figcaption>`).
- **Changelogs:** Reverse-chronological stream with sticky date rail on the left, real product video/interactive embeds (`aspect-video` rounded concentric frame), and direct links to live docs—zero filler release-note fluff.
