# Contributing — docaviv2026

> **Org-wide rules:** [`internet-and-sons/.github/CONTRIBUTING.md`](https://github.com/internet-and-sons/.github/blob/main/CONTRIBUTING.md). PR template: [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md). This file covers what's specific to docaviv2026.

Read `CLAUDE.md` first for the architectural picture and the safety rules.

## Setup (per clone)

1. Clone into the Claude Code plugins directory:
   ```bash
   git clone https://github.com/internet-and-sons/docaviv2026 ~/.claude/plugins/docaviv2026
   ```
2. Restart Claude Code.
3. No dependencies to install — Python 3.8+ stdlib is all that's needed.

## Workflow

**For skill/command/data changes:**
1. Branch off `main` (`git checkout -b feat/your-description`)
2. Make changes
3. Test with the slash commands in Claude Code
4. For data changes: run `python3 skills/docaviv2026/scripts/plan.py list` to verify JSON parses correctly
5. Ask before opening a PR (Hard rule #2 in CLAUDE.md)

**For releasing a new version:**
1. Update `VERSION` (the semver string)
2. Update `"version"` in `.docaviv-manifest.json`
3. Update `"version"` in `.claude-plugin/plugin.json`
4. These three files must be in the same commit

## What NOT to change without coordination

- **`skills/docaviv2026/data/films.json` field names** — `plan.py` and `update.py` reference specific keys (`datetime`, `hall`, `order`, `url_en`, etc.). Renaming breaks everything silently.
- **The path `skills/docaviv2026/scripts/update.py`** — hardcoded in `commands/update.md` and relied on by users who have installed the plugin.
- **`GITHUB_OWNER`, `GITHUB_REPO`, `GITHUB_BRANCH` constants in `update.py`** — changing these breaks self-update for all existing installs.

## Help

Open an issue at https://github.com/internet-and-sons/docaviv2026/issues
