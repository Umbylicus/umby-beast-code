# Playbook: Feature Vertical Slice

Use when adding a new interactive feature, page, dashboard workflow, checkout step, or stateful UI module.

## Mandatory Checklist

1. **Subsystem Grounding:** Trace how surrounding routes, auth, API handlers, and design tokens currently work. Never invent a parallel styling or state convention when the repo already has a clean one.
2. **Domain Model & Interface Sketch (`../../architect/SKILL.md`):** Define the exact TypeScript discriminated union / statechart, URL search-param contract, and boundary validation schema before writing JSX. Design two candidate component APIs if the boundary crosses multiple modules; pick the deeper, simpler surface.
3. **Complete State Matrix (`../../craft/SKILL.md`):** Specify exact visuals and microcopy for: `idle`, `loading`, `empty`, `populated`, `optimistic-pending`, `validation-error`, `network-error` (with retry), and `overflow` (long names, 0 items, 1,000 items).
4. **Vertical Implementation & Physics (`../../motion/SKILL.md`):** Implement end-to-end from boundary schema through accessible UI controls (`Radix` / `Base UI` / `React Aria` or semantic HTML). Keep high-frequency transitions under `150ms` on `transform`/`opacity`.
5. **Microcopy & Clarity Pass (`../../sick-social/SKILL.md` + `../../comment-slicer/SKILL.md`):** Make button labels concrete verbs (*"Create API key"*, *"Export 14 invoices"*). Run `slicer_scan.py` and `audit_ui_slop.py` on touched files.
6. **Behavioral Test & Live Surface Proof (`../../verify/SKILL.md`):** Write user-observable behavioral tests (asserting roles, visible states, and mutations—never internal hook implementation) and exercise every state in a real browser across mobile and desktop viewports.
