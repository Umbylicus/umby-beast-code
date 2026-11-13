#!/usr/bin/env bash
# Umby Beast Code Universal Skill Tree Installer
# Safely links (or copies) every skill and subagent into Claude Code,
# Gemini/Antigravity, Cursor, Codex/Fable, Grok CLI, ~/.agents, or a target repo.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="${ROOT_DIR}/skills"
AGENTS_SRC="${ROOT_DIR}/agents"

DRY_RUN=0
USE_COPY=0
FORCE=0
DO_ALL=0
DO_CLAUDE=0
DO_GEMINI=0
DO_CURSOR=0
DO_CODEX=0
DO_GROK=0
DO_AGENTS_GLOBAL=0
PROJECT_DIR=""

usage() {
  cat <<EOF
Usage: ./install.sh [options]

Options:
  --dry-run            Show planned links/copies without touching disk
  --copy               Copy directories instead of symlinking (useful for Git repos)
  --force              Also replace symlinks that point somewhere other than this folder
                       (the old link is renamed to <name>.replaced-<timestamp>, never deleted)
  --all                Install into all detected global agent directories on this machine
  --claude             Install into ~/.claude/skills (and ~/.claude/agents)
  --gemini             Install into ~/.gemini/config/skills
  --cursor             Install into ~/.cursor/skills (and ~/.cursor/agents)
  --codex              Install into ~/.codex/skills
  --grok               Install into ~/.grok/skills
  --agents             Install into ~/.agents/skills
  --project <dir>      Install into <dir>/.agents/skills (universal workspace root)
  -h, --help           Show this help
EOF
}

if [[ $# -eq 0 ]]; then
  usage
  exit 0
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --copy) USE_COPY=1; shift ;;
    --force) FORCE=1; shift ;;
    --all) DO_ALL=1; shift ;;
    --claude) DO_CLAUDE=1; shift ;;
    --gemini) DO_GEMINI=1; shift ;;
    --cursor) DO_CURSOR=1; shift ;;
    --codex) DO_CODEX=1; shift ;;
    --grok) DO_GROK=1; shift ;;
    --agents) DO_AGENTS_GLOBAL=1; shift ;;
    --project)
      PROJECT_DIR="${2:-}"
      if [[ -z "${PROJECT_DIR}" ]]; then
        echo "[ERROR] --project requires a directory path" >&2
        exit 1
      fi
      shift 2
      ;;
    -h|--help) usage; exit 0 ;;
    *)
      echo "[ERROR] Unknown flag: $1" >&2
      usage
      exit 1
      ;;
  esac
done

install_item() {
  local src="$1"
  local dest="$2"

  if [[ -L "${dest}" ]]; then
    local current
    current="$(readlink "${dest}")"
    if [[ "${current}" == "${src}" && "${USE_COPY}" -eq 0 ]]; then
      echo "[OK]      ${dest} already links to this folder (nothing to do)."
    elif [[ "${current}" != "${src}" && "${FORCE}" -eq 0 ]]; then
      echo "[SKIP]    ${dest} is a symlink to ${current} (not this folder). Left alone; re-run with --force to replace it."
    elif [[ "${DRY_RUN}" -eq 1 ]]; then
      echo "[DRY-RUN] Replace symlink: ${dest} (was -> ${current}) with ${src}"
    else
      if [[ "${current}" != "${src}" ]]; then
        local kept
        kept="${dest}.replaced-$(date +%Y%m%d-%H%M%S)"
        mv "${dest}" "${kept}"
        echo "[KEPT]    old link saved as ${kept}"
      else
        rm "${dest}"
      fi
      if [[ "${USE_COPY}" -eq 1 ]]; then
        cp -R "${src}" "${dest}"
        echo "[COPIED]  ${dest}"
      else
        ln -s "${src}" "${dest}"
        echo "[LINKED]  ${dest} -> ${src}"
      fi
    fi
  elif [[ -e "${dest}" ]]; then
    echo "[SKIP]    ${dest} already exists as a real file/folder (skipped to protect existing user files)."
  else
    if [[ "${DRY_RUN}" -eq 1 ]]; then
      if [[ "${USE_COPY}" -eq 1 ]]; then
        echo "[DRY-RUN] Copy: ${src} -> ${dest}"
      else
        echo "[DRY-RUN] Symlink: ${dest} -> ${src}"
      fi
    else
      mkdir -p "$(dirname "${dest}")"
      if [[ "${USE_COPY}" -eq 1 ]]; then
        cp -R "${src}" "${dest}"
        echo "[COPIED]  ${dest}"
      else
        ln -s "${src}" "${dest}"
        echo "[LINKED]  ${dest} -> ${src}"
      fi
    fi
  fi
}

install_skills_into() {
  local target_skills_dir="$1"
  echo "=== Target Skills Directory: ${target_skills_dir} ==="
  for skill_path in "${SKILLS_SRC}"/*; do
    [[ -d "${skill_path}" ]] || continue
    local skill_name
    skill_name="$(basename "${skill_path}")"
    install_item "${skill_path}" "${target_skills_dir}/${skill_name}"
  done
}

install_agents_into() {
  local target_agents_dir="$1"
  echo "=== Target Subagents Directory: ${target_agents_dir} ==="
  for agent_file in "${AGENTS_SRC}"/*.md; do
    [[ -f "${agent_file}" ]] || continue
    local agent_name
    agent_name="$(basename "${agent_file}")"
    install_item "${agent_file}" "${target_agents_dir}/${agent_name}"
  done
}

if [[ "${DO_ALL}" -eq 1 ]]; then
  [[ -d "${HOME}/.claude" ]] && DO_CLAUDE=1
  [[ -d "${HOME}/.gemini" ]] && DO_GEMINI=1
  [[ -d "${HOME}/.cursor" ]] && DO_CURSOR=1
  [[ -d "${HOME}/.codex" ]] && DO_CODEX=1
  [[ -d "${HOME}/.grok" ]] && DO_GROK=1
  [[ -d "${HOME}/.agents" ]] && DO_AGENTS_GLOBAL=1
fi

if [[ "${DO_CLAUDE}" -eq 1 ]]; then
  install_skills_into "${HOME}/.claude/skills"
  install_agents_into "${HOME}/.claude/agents"
fi

if [[ "${DO_GEMINI}" -eq 1 ]]; then
  install_skills_into "${HOME}/.gemini/config/skills"
fi

if [[ "${DO_CURSOR}" -eq 1 ]]; then
  install_skills_into "${HOME}/.cursor/skills"
  install_agents_into "${HOME}/.cursor/agents"
fi

if [[ "${DO_CODEX}" -eq 1 ]]; then
  install_skills_into "${HOME}/.codex/skills"
fi

if [[ "${DO_GROK}" -eq 1 ]]; then
  install_skills_into "${HOME}/.grok/skills"
fi

if [[ "${DO_AGENTS_GLOBAL}" -eq 1 ]]; then
  install_skills_into "${HOME}/.agents/skills"
fi

if [[ -n "${PROJECT_DIR}" ]]; then
  install_skills_into "${PROJECT_DIR}/.agents/skills"
fi

echo "Done."
