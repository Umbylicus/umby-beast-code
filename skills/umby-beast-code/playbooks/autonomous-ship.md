# Playbook: Autonomous Multi-Phase Ship

Use when the user grants long-running autonomy (*"run until complete"*, *"going to sleep, finish all pages"*, `/goal` or `/loop` workflows).

## Mandatory Checklist

1. **Acceptance Contract & Decision Log Setup:** Create `.umby/decisions.tsv` (`timestamp\tphase\tdecision\trationale\treversibility_note`) to record every non-trivial assumption so the user has a crystal-clear audit trail upon return.
2. **Phase Partitioning:** Order work strictly by dependency:
   - **Phase 1 (Blocking Shared Foundation):** Stack config, root OKLCH tokens, typography, shared layout shell (Navbar/Footer), domain types, and route skeleton. Verify build green before any fan-out.
   - **Phase 2 (Disjoint Route/Feature Slices):** Implement and verify each route or feature slice to full completion (desktop + mobile + states + `sick-social` copy) one verifiable unit at a time—or in parallel subagents owning strictly disjoint route directories.
   - **Phase 3 (Cross-Cutting Integration):** Wire navigation links, search/filtering, sitemap/metadata, and shared transitions.
3. **Continuous Hygiene Gates:** Run `slicer_scan.py`, `audit_ui_slop.py`, and `sick_social_lint.py` at the end of every slice so technical and visual debt never compounds across 10 routes.
4. **Full-Site Browser Sweep (`../../umby-verify/SKILL.md`):** Walk every route in a real browser across `375px` and `1440px`, verify zero `404`s, zero console/hydration errors, keyboard reachability, and passing production build (`npm run build` + `verify_surface_readiness.py`).
5. **Respect Hard Safety Stops:** Never push to shared branches, deploy to production, run destructive DB migrations against live environments, or incur paid external charges unless explicitly pre-authorized in the user's prompt. Leave a clean resumable summary and link `.umby/decisions.tsv`.
