# Aspect library

Pick one aspect per critic. Start from the top of the list for the category and stop when you run out of critics. Rename an aspect to fit the build when that makes it clearer. For games, use `../../game-mode/references/ten-aspects.md` instead.

Each line gives the aspect and what its critic checks.

## Websites (marketing, local business, storefront)

1. **First-screen clarity.** Within five seconds: what this is, who it is for, and the one next step.
2. **Visual design.** Hierarchy, spacing, type, color, and consistency. No template look.
3. **Copy.** Specific, true, human. One idea per section. No filler or unproven claims.
4. **Mobile experience.** Layout, tap targets, and speed at 375 and 430 wide.
5. **Conversion path.** How few steps from landing to call, booking, order, or purchase, and what gets in the way.
6. **Performance.** Measured load and interaction numbers on a phone profile.
7. **Accessibility.** Keyboard use, contrast, labels, focus, reduced motion.
8. **Search readiness.** Titles, descriptions, headings, structured data that matches the page, crawlable links.
9. **Trust and proof.** Real reviews, photos, credentials, and policies, placed where doubt appears.
10. **Motion and polish.** States, transitions, empty and error screens, and the small details.

## Apps and internal tools (dashboards, CRMs, ordering apps, automations)

1. **Core task flow.** The main job a user came to do, counted in steps and seconds.
2. **Data model and correctness.** States that cannot contradict each other, validation at the edges, right answers in edge cases.
3. **Reliability.** Behavior on slow network, failed request, double submit, refresh, and back button.
4. **Interface design.** Density, hierarchy, consistency, and readable tables and forms.
5. **States.** Loading, empty, error, partial, and overflow, each designed.
6. **Performance.** Time to first useful screen and response time on common actions, measured.
7. **Security and privacy.** Auth, permissions, input handling, secrets, and what data is exposed to whom.
8. **Accessibility.** Keyboard paths, labels, contrast, screen reader output on the main flow.
9. **Code quality.** Structure a new developer can follow, tests on behavior, no dead code.
10. **Onboarding and help.** How a first-time user learns it without a manual.

## Anything else (documents, APIs, CLIs, libraries)

Build the list from these questions, one aspect per answer:

- What is the main job, and how well is it done?
- What does a first-time user hit in the first minute?
- What happens when input is wrong or something fails?
- How fast is it, measured?
- How easy is it to read, learn, and change?
- What would an expert in this field check first?
- What could harm a user (security, data loss, wrong output)?
