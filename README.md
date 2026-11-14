# Umby Beast Code

A skill tree for AI coding agents that builds websites, apps, internal tools, backends, automations, and games to a professional standard, and checks its own work with independent critics before it calls anything done.

It works in any agent that loads `SKILL.md` folders: Claude Code, Cursor, Codex, Gemini CLI, Grok CLI, and others.

## Install

```bash
git clone https://github.com/Umbylicus/umby-beast-code.git
cd umby-beast-code

# Preview what will be linked. Changes nothing.
./install.sh --dry-run --all

# Link every skill and subagent into the agent folders found on this machine.
./install.sh --all
```

The installer only creates symlinks (or copies with `--copy`). It never overwrites a real file or folder, and it leaves a symlink that points somewhere else alone unless you pass `--force`. Use `--claude`, `--cursor`, `--codex`, `--gemini`, `--grok`, `--agents`, or `--project <dir>` to pick targets. Reruns refresh `SKILLS-INDEX.md` and remove legacy `umby-*` skills and subagents **this repo used to install**, so you do not keep duplicates after a rename. Other `umby-*` skills (for example from a different repo) are left alone.

## The modes you start with

| Type this | For |
| :--- | :--- |
| `/beast-code` | Building or changing anything. It replies `BEAST CODE {ON}-OFF`, reads the skill index, states which skills apply, picks a playbook, loads every relevant skill, and ends with one round of critics. |
| `/critic-mode` | Scoring a build against the best in its category and looping fix-then-recritique until it clears the bar you choose. |
| `/game-mode` | Making an original game. It grills you on engine, platform, loop, and scope until you agree a plan in `docs/game-plan.md`, then scaffolds, builds, and runs a ten-critic loop. |
| `/sick-social` | Social posts, blog posts, and website copy that read like a person wrote them. |
| `/comment-slicer` | Cutting comments that do not earn their place, without changing what the code does. |
| `/skill-router` | Finding the right skill, or sharpening a rough prompt before you build. |

## Quality levels (Critic Mode and Game Mode)

| Level | Passes when | Cost |
| :--- | :--- | :--- |
| **A. Best in class** | every aspect scores 9 or higher | High. Many rounds, a full panel each round. |
| **B. Great** | every aspect scores 7 or higher | Medium. |
| **C. Critique only** | one round, nothing changed | Low. |

Each critic owns one aspect, compares it with the best-regarded product in the same category for that aspect, says why it is not a 10, and gives the next writer specific fixes. Scores are logged every round to `.beast/critic/graph.html`, which you can leave open in a browser.

The loop stops on a pass. It also stops and asks you when scores stall for two rounds or the round cap is reached, so it cannot run forever. A score is a measurement, not a promise: the mode raises quality, and it tells you honestly where the build still falls short.

## Skill map

```text
beast-code       orchestrator (reads SKILLS-INDEX.md every task)
  discover       intake questions and a creative brief
  build-plan     plan and decision log kept in files
  architect      data shape, state, and stack before code
  backend        schemas, migrations, APIs, jobs, integrations
  craft          design tokens, hierarchy, states, UI slop scanner
  motion         interaction timing and scroll choreography
  archetypes     page blueprints by site category
  evolve         safe upgrades to existing sites
  arena          parallel candidates and adversarial review (major)
  debug          reproduce, find the cause, failing check, fix
  secure         security and privacy review
  verify         real-browser checks, Lighthouse, accessibility, links
  ship           commits, pull requests, review comments
critic-mode      critic panel loop with a live score graph (major)
game-mode        planning interview, agreed plan, scaffold, ten-critic loop (major)
sick-social      human-sounding writing with a linter (major)
comment-slicer   comment and silencer review that never breaks a build
skill-router     router and prompt sharpener
```

Subagents live in `agents/`: `builder`, `design-critic`, and `comment-slicer`. Drop-in project files for different tools are in `adapters/`. Background reading is in `docs/`. The generated catalog is `SKILLS-INDEX.md` (installed as `beast-code/SKILLS-INDEX.md`); major skills read it at the start of a task and follow `beast-code/references/select-skills.md`.

## Standing rules

`skills/beast-code/references/standing-rules.md` sets the defaults every skill obeys: approval gates (research, then mockups, then build), nothing merged or deployed without an explicit go, feature branches, protected code, keeping or redirecting every URL on a rebuild, real proof only, and a work log.

To add your own private rules (your deploy route, your client log, your protected folders), create `standing-rules.local.md` beside that file. It is read after the public rules, wins where they differ, and is ignored by git.

## Bundled tools

All are plain Python 3 with no dependencies.

| Tool | What it does |
| :--- | :--- |
| `beast-code/scripts/preflight_recon.py` | Summarizes a web project before work starts |
| `craft/scripts/audit_ui_slop.py` | Flags generic UI patterns, fake proof, and placeholder text |
| `verify/scripts/verify_surface_readiness.py` | Checks HTML landmarks, metadata, and dead links |
| `sick-social/scripts/sick_social_lint.py` | Lints copy for AI tells and flat rhythm |
| `comment-slicer/scripts/slicer_scan.py` | Lists comment candidates and marks tool-read comments as protected |
| `critic-mode/scripts/critic_graph.py` | Logs critic rounds, decides pass or stall, draws the graph |
| `game-mode/scripts/game_scaffold.py` | Creates a game folder layout and checks the asset manifest |

Check the whole tree at any time:

```bash
python3 scripts/generate_skills_index.py --check
python3 scripts/validate_skill_tree.py
```

## License

MIT. See `LICENSE`.
