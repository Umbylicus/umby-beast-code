# Claude Code Configuration — Umby Beast Code Standard

Use the installed **`beast-code`** skill tree (`~/.claude/skills/` or `.claude/skills/`) as the default engineering, design, and writing workflow for websites and applications:

- Invoke **`/beast-code`** at the start of any greenfield build, brownfield website upgrade, UI feature, conversion pass, or performance/CWV task.
- Invoke **`/sick-social`** (and run `sick_social_lint.py`) for all social media posts, launch threads, blog articles, changelogs, and landing page copy.
- Invoke **`/comment-slicer`** (and dispatch the read-only `comment-slicer` subagent + `slicer_scan.py`) after every code-writing batch before committing or presenting work.
- Delegate scoped disjoint file slices to `builder` and fresh visual screenshot audits (`375px`, `768px`, `1440px`, `1920px`) to `design-critic`. Never declare UI done without inspecting rendered pixels.
