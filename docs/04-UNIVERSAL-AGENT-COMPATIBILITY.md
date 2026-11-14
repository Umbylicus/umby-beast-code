# Universal Agent Compatibility Guide (Claude, Gemini, Fable/Codex, Grok, Cursor & More)

Every skill in `skills/` adheres strictly to the **open `SKILL.md` standard** (`name` + `description` YAML frontmatter, relative markdown links to sibling skills `../<skill>/SKILL.md`, self-contained `references/`, and zero-dependency Python 3 `scripts/`). No proprietary vendor lock-in, hardcoded model IDs, or single-IDE tool names exist anywhere in the tree.

---

## One-Command Installation (`install.sh`)

From inside this folder, preview or install the entire skill tree across all your agents using `./install.sh`:

```bash
cd umby-beast-code

# 1. Dry-run preview (shows exact target paths, changes nothing)
./install.sh --dry-run --all

# 2. Install globally for ALL detected local agents (Claude, Gemini/Antigravity, Cursor, Codex/Fable, Grok, ~/.agents)
./install.sh --all

# 3. Or install into a specific website repository you are working on
./install.sh --project /path/to/your/website-repo
```

By default, `./install.sh` uses clean symlinks so any edit you make inside this master folder on your Desktop propagates everywhere immediately (pass `--copy` if you prefer standalone file copies for committing into a Git repo).

---

## Platform-Specific Setup & Invocation Reference

### 1. Claude Code (Claude Opus 5.5 / Sonnet)
* **Skill Path:** `~/.claude/skills/<skill-name>/SKILL.md` (global) or `<repo>/.claude/skills/` (project)
* **Subagents Path:** `~/.claude/agents/` (`builder.md`, `design-critic.md`, `comment-slicer.md`)
* **Root Adapter:** Copy `adapters/CLAUDE.md` into your project root if you want `beast-code` standards active on every turn automatically.
* **How to Invoke:** Type `/beast-code`, `/sick-social`, `/comment-slicer`, or ask naturally (*"Use beast-code to redesign our pricing page"*).

### 2. Google Antigravity & Gemini CLI (Gemini 4 Carbon)
* **Skill Path:** `~/.gemini/config/skills/<skill-name>/SKILL.md` (global) or `<workspace>/.agents/skills/<skill-name>/SKILL.md` (workspace)
* **Root Adapter:** Copy `adapters/GEMINI.md` to `<workspace>/GEMINI.md`.
* **Built-In Superpowers Unlocked Automatically:**
  * `verify` uses Antigravity's native `browser` subagent (or Playwright CLI) for live multi-viewport visual inspection.
  * `arena` uses native `invoke_subagent` / `swarm` tools for parallel candidate generation and fresh-context `comment-slicer` / `design-critic` reviews.
  * Combine with `/plan`, `/grill-me`, `/goal`, or `/boost` slash commands when running multi-hour flagship builds.

### 3. OpenAI Codex / Fable 5.2 / ChatGPT Projects
* **Skill Path:** `~/.codex/skills/<skill-name>/SKILL.md` or `<repo>/.agents/skills/<skill-name>/SKILL.md`
* **Root Adapter:** Copy `adapters/AGENTS.md` to `<repo>/AGENTS.md`.
* **How to Invoke in CLI/Desktop:** Type `$beast-code`, `$sick-social`, `$comment-slicer`, or name the skill in your prompt.
* **Web / Chat-Only Surfaces (Fable Web, ChatGPT Projects, Claude Projects):** Paste `adapters/system-prompt-universal.md` into Project Instructions and attach the relevant `SKILL.md` files (`beast-code`, `craft`, `sick-social`) as project knowledge. Note: when running in a web chat with no shell/browser access, the skills automatically report verification commands for you to run locally rather than faking browser screenshots.

### 4. Cursor IDE & Cursor CLI (Multi-Model: Claude + Gemini + Grok + Fable)
* **Skill Path:** `~/.cursor/skills/<skill-name>/SKILL.md` (personal) or `<repo>/.agents/skills/` (project)
* **Subagents Path:** `~/.cursor/agents/` (`builder.md`, `design-critic.md`, `comment-slicer.md`)
* **How to Invoke:** Select `/beast-code` from the `/` menu (press `Option+Enter` on macOS to pin `beast-code` as a persistent custom mode across the entire session!).

### 5. Grok Build CLI
* **Skill Path:** `~/.grok/skills/<skill-name>/SKILL.md`
* **Verification:** Run `grok inspect` to confirm discovery, then invoke `/beast-code` or `/sick-social` directly in your build session.

---

## Multi-Agent Handshake Workflow (Using Two Frontier Agents Together)

Want maximum quality on an ultra-high-stakes flagship launch? Run this two-agent relay on the same repository:

1. **Pass 1 — Architecture, Creative Direction & Build (Agent A, e.g., Gemini 4 Carbon or Claude Opus 5.5):**
   Run `beast-code` to lock the brief, generate the OKLCH design system, write copy via `sick-social`, and implement the full responsive vertical slice.
2. **Pass 2 — Cross-Family Adversarial Audit (Agent B, a *different* model family, e.g., Fable 5.2, Claude Opus 5.5, or Grok):**
   Open the same repo in Agent B and run:
   > *"Run `comment-slicer` and `verify` on the current branch. Break the UI across 375px and 1440px, audit copy with `sick_social_lint.py`, and report only defects proven by running code or rendered screenshots."*
3. **Pass 3 — Root-Cause Fix & Final Gate:**
   Fix every proven finding at the token or component-model root, re-run the static and browser checks, and ship.
