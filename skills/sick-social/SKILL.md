---
name: sick-social
description: Writes magnetic, unmistakably human social media posts (Facebook, Instagram, Google Business Profile, X/Twitter, LinkedIn, Threads, Reddit, Hacker News), long-form blog posts, founder essays, changelogs, and high-converting website copy with zero AI slop. Enforces high sentence burstiness, concrete lived details, spiky points of view, platform-native pacing, and a strict ban on AI vocabulary, em-dash chains, 'not X but Y' contrasts, LinkedIn broetry, and generic throat-clearing—verified deterministically by 'sick_social_lint.py'. Use directly via '/sick-social' or whenever drafting any social post, blog article, or website copy.
license: MIT
major: true
metadata:
  version: "1.1.0"
  tree: "beast-code"
  role: orchestrator
---

# Sick Social: Human-Cadence Social, Blog & Web Copy Engine

## Skill selection (every task)

Follow the shared procedure in [`../beast-code/references/select-skills.md`](../beast-code/references/select-skills.md) using [`../beast-code/SKILLS-INDEX.md`](../beast-code/SKILLS-INDEX.md) before drafting. State the roster. Load `discover` when the brief has no raw material, `archetypes` for landing-page structure, `craft` when the copy lives in a UI, `comment-slicer` if you also touch code, `verify` if the words ship on a page, `ship` if this task opens a PR.

Language models default to the statistical midpoint of corporate blogs and LinkedIn hustle threads: uniform 15-word sentences, hollow contrast formulas (*"It's not about X. It's about Y."*), em-dashes everywhere, safe opinions nobody could disagree with, and neat TED-talk endings.

`sick-social` overrides that statistical pull at the root. Whether you are writing a 40-word X post, a 1,800-word technical essay, or hero copy for a flagship storefront, every line must read like a sharp, observant human practitioner wrote it at a keyboard.

Load the reference guide matching your target surface:
- **Social Media Posts, Threads & Community Launches (Facebook, Instagram, Google Business Profile, X, LinkedIn, Threads, HN, Reddit):** [`references/social-platforms.md`](references/social-platforms.md)
- **Blog Posts, Founder Essays, Postmortems & Changelogs:** [`references/blog-and-essays.md`](references/blog-and-essays.md)
- **Website Headlines, Landing Pages, Pricing & UI Microcopy:** [`references/web-conversion-copy.md`](references/web-conversion-copy.md)

---

## Step 1: Extract Raw Friction & Voice First (Never Invent Fake Stories)

Great writing starts from **specifics, friction, and a point of view**, never abstract topics.

1. **Voice Sample Check:** If the user provided sample posts or articles in their voice, study their exact sentence length, capitalization, humor, punctuation habits, and openings—**their real voice sample overrides default punctuation bans** (for example, if they genuinely use lowercase or occasional dashes, match their exact rate).
2. **Raw Material Gate:** Look at what the user gave you.
   - If they gave raw notes, metrics, a bug story, or product facts: extract the **sharpest concrete detail** (the `410ms -> 28ms` drop, the deleted Redis cluster, the angry Tuesday support ticket) and build around it.
   - If they gave only a naked topic (*"Write a blog post / LinkedIn post about why design matters"*) and did not ask for autonomous drafting, ask **2–3 fast, pointed questions** before drafting:
     1. *What specific mistake, scar, or counter-intuitive belief triggered this post?*
     2. *What is one real number, tool, or concrete example we can anchor on (so we invent zero facts)?*
     3. *Who is the exact reader, and what should they stop or start doing after reading?*
3. **Strict Honesty Rule:** Never fabricate personal anecdotes, fake customer quotes, or invented statistics. When writing without personal stories, use concrete technical mechanisms, observable industry examples, or crisp operational logic.

---

## Step 2: Enforce the 7 Laws of Unmistakably Human Prose

Draft from scratch with all seven laws active simultaneously:

1. **Start Mid-Thought (*In Media Res*):** Delete your first throat-clearing paragraph. Start directly inside the tension, the number, the mistake, or the concrete claim (*"We deleted 14,000 lines of caching code on Thursday and our p99 latency dropped by half."*—never *"In today's modern engineering landscape, caching is often seen as essential."*).
2. **High Burstiness (Asymmetric Sentence Physics):** Break uniform rhythm ruthlessly. Pair a blunt 3-to-6-word sentence with a 20-to-28-word observational sentence that unpacks the mechanism. Vary paragraph heights (a 1-sentence turn followed by a 4-sentence proof block, never five identical 3-line paragraphs).
3. **The Checkability Test (Nouns & Verbs Over Adjectives):** Replace vague claims (*"significant growth"*, *"seamless onboarding"*, *"world-class speed"*) with concrete mechanisms or checkable numbers (*"cut signup from 6 screens to 1 OAuth redirect"*). If a sentence could paste unchanged into a competitor's post, delete it.
4. **Spiky Point of View:** Avoid hedging both sides into mush (*"While X has merits, Y is also important"*). Take a clear, defensible stance and name the exact tradeoff honestly, including where your stance *doesn't* apply.
5. **Zero Structural AI Formulas:**
   - **Ban `"Not X, it's Y"`** (*"It's not just a tool, it's a teammate"*, *"This isn't about speed; it's about trust"*). State what the thing actually does.
   - **Ban Forced Triads** (listing adjectives, examples, or parallel sentences in neat groups of three). Use 1 strong example, 2 contrasting ones, or 4 specific items.
   - **Ban Em-Dashes (`—` and ` -- `)** unless matching an explicit user writing sample. Choose the real logical connector: a period, comma, parentheses, or `because`.
   - **Ban Staged Openers & Mic-Drop Closers:** Never write *"Let's dive in"*, *"Here's the thing:"*, *"Honestly?"*, *"Read that again"*, *"Let that sink in"*, *"And that changes everything"*, or *"The future belongs to..."*
   - **Ban LinkedIn Broetry & Threadboi Clichés:** Never put every single sentence on its own double-spaced line for 15 lines straight, and never open X threads with `"🧵 1/10 Most people get X completely wrong:"` or `🚀` / `💡` emoji bullets.
6. **Plain Words Beat Corporate Dress-Up:** Say `use` (never *utilize* or *leverage*), `is` or `has` (never *serves as*, *stands as*, *boasts*), `help` (never *facilitate* or *empower*), and ban the AI lexicon (*delve, tapestry, landscape, seamless, unlock, unleash, supercharge, elevate, testament, pivotal, crucial, intricate, foster, underscore, realm, beacon, game-changer, synergy*).
7. **End on the Last Sharp Fact:** Stop the moment the point lands. Never append a summary paragraph restating what the reader just read three scrolls ago.

---

## Step 3: Mandatory Deterministic Lint Gate (`sick_social_lint.py`)

Never hand a social post, blog draft, or landing page copy file to the user before running the voice linter:

```bash
python3 <path-to-sick-social>/scripts/sick_social_lint.py <draft-file.md>
# Or pipe text via stdin:
python3 <path-to-sick-social>/scripts/sick_social_lint.py --stdin <<'EOF'
<your draft here>
EOF
```

- If `sick_social_lint.py` outputs **`FAIL`**, rewrite the flagged lines from the paragraph level (do not just swap one synonym while leaving the robotic sentence skeleton intact) and re-run until **`PASS`**.
- Read the final draft aloud internally once: if any line sounds like a keynote teleprompter or a press release, cut it in half and make it conversational.

---

## Step 4: Post Rules & Approval Gate (Every Social Post)

Check each post against these before handing it over:

1. **Hook First:** The first line carries the most specific, interesting fact in the post. It must make sense on its own, because most platforms cut the rest off.
2. **One Idea Per Post:** Each post makes one point. If the draft covers two (a new service *and* a holiday schedule), split it into two posts.
3. **Fits the Platform:** Length, line breaks, hashtags, and link handling follow the matching section of [`references/social-platforms.md`](references/social-platforms.md). Never paste the same text across platforms unchanged.
4. **One CTA That Matches the Goal:** Name the post's goal first (calls, bookings, online orders, foot traffic, reviews, awareness), then give exactly one next step that serves it. A post aimed at bookings ends with how to book, not "follow us for more". If the goal is awareness only, no CTA is fine.
5. **No Hype, No Fake Claims:** No "best in town", "#1", "guaranteed", or superlatives the business cannot prove. Every fact, number, review quote, and customer story must come from the owner or client. Mark anything you could not confirm as `[CONFIRM: ...]` instead of guessing.
6. **No Prices or Offers Without the Owner's OK:** Never include a price, discount, deal, promo code, or deadline unless the owner supplied or approved that exact figure in this conversation. If a post would be stronger with one, leave a `[PRICE: needs OK]` slot and say so.
7. **Drafts Only, Never Post:** Deliver drafts for review. Never publish, schedule, boost, or send a post, reply, or message on any account without the owner's explicit OK for that specific post.

**Definition of done:** `sick_social_lint.py` prints `PASS`, all seven rules above hold, every unconfirmed fact is flagged, and the handoff says plainly that nothing has been posted.
