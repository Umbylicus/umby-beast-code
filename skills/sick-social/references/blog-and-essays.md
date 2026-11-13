# Long-Form Blog Posts, Essays & Changelogs Playbook

Model long-form writing on **Paul Graham, Patrick McKenzie (patio11), Stripe Engineering, Linear Method essays, and Dan Luu**—clear thinking, high information density per paragraph, unexpected examples, and zero filler headings.

---

## 1. Structural Rules That Separate Great Essays from AI Blog Slop

1. **Kill the Wikipedia Intro:** Never open an essay by defining the topic (*"Web performance refers to how fast websites load, and it has never been more important..."*). Drop the reader straight into a puzzle, a failure mode, a surprising measurement, or a sharp thesis they haven't heard phrased that way before.
2. **Headings State Claims, Not Labels:**
   - *AI Slop Heading:* `## The Importance of State Management` / `## Challenges and Solutions` / `## Conclusion`
   - *Human Essay Heading:* `## Boolean flags rot faster than schemas` / `## Why our first two fixes made latency worse`
   - Never write a `## Conclusion` or `## Final Thoughts` heading at the end of a blog post.
3. **Never Repeat the Heading in Sentence One:** After `## Why caches hide bad queries`, do not start with *"Caches often hide bad database queries."* Advance immediately to the evidence or mechanism.
4. **Prose Over Bullet Soup:** AI turns every blog post into 8 bulleted lists of bold-colon labels (`- **Scalability:** ...`). Write connected paragraphs that build an argument. Use a list **only** when enumerating discrete steps, specifications, or data points that genuinely belong in a table/list.
5. **Earned Specificity & Tangents:** Real writers include exact edge cases, parenthetical asides (`(we learned this the hard way when a Safari 17 update broke our checkout drawer at 2 a.m.)`), and honest uncertainty (*"I'm still not convinced this holds above 50 engineers, though"*). Keep those rough human edges; never sand everything down to sterile corporate certainty.
6. **Abrupt, High-Impact Endings:** Once your last argument lands, stop on a concrete implication or sharp final image. Do not summarize the essay.

---

## 2. Product Changelogs & Launch Announcements

- **Headline = What the User Can Now Do:** `"Export 12 months of ledger history to NetSuite in one click"` beats `"Introducing Enhanced Accounting Integrations 2.0"`.
- **Show, Then Explain in 120 Words:** Lead with the interactive demo / crisp cropped capture, state the exact customer pain that drove it, name 2–3 specific technical details (e.g., keyboard shortcut `G then E`, CSV + JSON webhook support), and link directly to the live route or docs.
