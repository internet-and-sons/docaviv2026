# Project context — docaviv2026

This file is auto-loaded as project context whenever Claude Code is opened in this repo.

## What this repo is

A Claude Code plugin that helps users explore and schedule films at the Docaviv 2026 documentary festival. It ships as a drop-in plugin (clone into `~/.claude/plugins/docaviv2026/`) providing two slash commands (`/docaviv:start`, `/docaviv:update`) and a skill (`docaviv2026`). The skill reads a bundled `films.json` dataset and uses a stdlib-only Python helper (`plan.py`) for all time-based calculations. No external dependencies required.

## Companion files

Read these before any task that touches the area they cover:

- **`CONTRIBUTING.md`** — setup, version-bump flow, what not to change without coordination
- **`TODO.md`** — pending work and deferred decisions
- **`LEARNINGS.md`** — non-obvious gotchas discovered in development

Org-wide rules live in [`internet-and-sons/.github/CONTRIBUTING.md`](https://github.com/internet-and-sons/.github/blob/main/CONTRIBUTING.md).

## Hard rules

1. **Every change goes through a PR.** No direct pushes to `main`.
2. **Ask before opening a PR.** Plan approval ≠ PR approval — ask again when the branch is ready to push.
3. **When bumping a version:** update `VERSION`, `.docaviv-manifest.json` (version field), and `plugin.json` (version field) in the same commit. These three must always agree.
4. **Never propose a schedule with overlapping screenings.** Always verify with `plan.py conflicts` or `plan.py schedule` before presenting a plan to the user.
5. **`films.json` is the source of truth for screening data.** Don't hardcode film names, dates, or venues in SKILL.md or commands — always read from the data file.

## Quick orientation

| Path | What it is |
| --- | --- |
| `commands/start.md` | `/docaviv:start` slash command |
| `commands/update.md` | `/docaviv:update` slash command |
| `skills/docaviv2026/SKILL.md` | AI skill instructions (Hebrew-first) |
| `skills/docaviv2026/data/films.json` | 124 films, 185 screenings, compact JSON |
| `skills/docaviv2026/scripts/plan.py` | Time-math CLI: `list`, `search`, `day`, `single`, `pairs`, `conflicts`, `schedule` |
| `skills/docaviv2026/scripts/update.py` | Self-updater, fetches from `internet-and-sons/docaviv2026` on GitHub |
| `VERSION` | Semver string — single source of version truth (along with plugin.json + manifest) |
| `.docaviv-manifest.json` | Files synced by `update.py` on self-update |
| `tools/` | Gitignored authoring tools: scraper (`crawl.js`) and raw data intermediates |

## Need help?

Open an issue at https://github.com/internet-and-sons/docaviv2026/issues
