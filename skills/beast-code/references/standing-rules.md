# Standing Rules

These rules apply to every build, update, or fix made with any skill in this tree: websites, apps, internal tools, games, and automations. They outrank every playbook step and every autonomy grant. "The operator" means the person running the session.

If a file named `standing-rules.local.md` sits beside this one, read it too. It holds the operator's private rules (deploy route, client logging, protected code areas). Where the two files disagree, the local file wins. The local file is never committed or published.

If a rule cannot be followed (no preview hosting, no git remote, no access to the log), stop and say so. Never skip a rule silently.

## 1. Approval gates: research, then mockups, then build

Work moves through three gates in order. Stop at the end of each one and wait for the operator's explicit go before starting the next.

1. **Research.** Recon, discovery answers, comparable products, and on a rebuild the route and SEO inventory. Deliver a short written summary.
2. **Mockups.** A direction the operator can look at: static mockups, a rendered screen, a playable slice, or a bakeoff. No production code yet.
3. **Build.** Only after the mockups are approved.

A phrase like "run autonomously" or "don't ask" lets you choose defaults inside the current gate. It does not skip a gate. A gate is skipped only when the operator names it ("skip mockups, go straight to build").

Small fixes the operator asks for directly (a typo, a broken link, one bug) skip the research and mockup gates. The rest of these rules still apply.

## 2. Nothing goes live without an explicit go

- Never deploy to production, merge to the main branch, or publish anything publicly without the operator's explicit go for that specific change. An earlier go does not carry over.
- Use the deploy route the operator has set up. If none is named, hand over a ready-to-deploy branch and stop.
- Never send messages, emails, or posts to other people on your own.

## 3. Feature branch with a preview

- Work on a feature branch, never directly on the main branch.
- Give the operator a preview URL, or a runnable build for apps and games, before asking for a go. If the project has no preview hosting, say so and offer local screenshots or a recording.

## 4. Stay out of protected code

- Some areas are off limits unless the task names them: billing, auth, customer data stores, and anything the operator lists as protected.
- Do not edit, refactor, restyle, or "clean up" protected code as a side effect of other work. Cleanup skills in this tree skip it too.
- If the task seems to need a change there, stop and ask first, naming the exact files.

## 5. Keep or redirect every existing URL on a rebuild

- Before a rebuild, list every existing URL from the live site and the sitemap, not only the repo routes.
- Each URL either stays at the same path or gets a permanent `301` to its closest replacement. None is dropped, and none is pointed at the homepage just to get rid of it.
- Show the old-to-new URL map before launch and re-check every old URL on the preview.

## 6. Real proof only, white-hat only

- Use only real reviews, ratings, testimonials, logos, photos, numbers, and client names that the operator supplied. With no real proof, leave the section out or show something true instead.
- Structured data must describe what is visibly on the page. No review or rating markup without real on-page reviews.
- Never build doorway pages, stuff keywords, join link schemes, cloak content, or use someone else's trademark to mislead.
- No lorem ipsum or filler copy in anything shown to the operator or their customers.
- Games and apps are original work. A reference product sets a quality bar. Its names, characters, art, music, levels, and look are never copied.

## 7. Log the work

- Every significant piece of work gets a dated entry: what was done, when it finished, who asked for it, and when they asked.
- Use the log the operator names. With none named, append to `.beast/work-log.md` in the project.
- If you cannot reach the log, write the exact entry in your handoff and say it still needs adding.

## Definition of done for any build task

1. The gate it belongs to was approved.
2. The work is on a feature branch with a preview, or the operator was told why not.
3. `verify` passed, including its numbers gate where it applies.
4. No protected code changed unless asked.
5. On a rebuild, the old-to-new URL map is complete.
6. The work is logged.
7. Nothing was merged to the main branch or deployed.
