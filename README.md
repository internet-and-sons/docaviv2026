# docaviv2026

A Claude Code plugin that helps you explore and plan your schedule for the Docaviv 2026 documentary film festival (28 May – 6 June 2026, Tel Aviv Cinematheque).

Ask it to recommend films based on your taste, build a conflict-free day plan, find back-to-back pairings, or surface single-screening films before they disappear. Works primarily in Hebrew.

## What's in here

| Path | What it is |
| --- | --- |
| `commands/start.md` | `/docaviv:start` — loads the planner, checks for updates |
| `commands/update.md` | `/docaviv:update` — self-update from this repo |
| `skills/docaviv2026/SKILL.md` | Skill instructions for the AI agent |
| `skills/docaviv2026/data/films.json` | 124 films, 185 screenings (compact JSON) |
| `skills/docaviv2026/scripts/plan.py` | Time-math helper (back-to-back, conflict detection, day view) |
| `skills/docaviv2026/scripts/update.py` | Self-updater — fetches latest from this repo, stdlib only |
| `VERSION` | Current plugin version (semver) |
| `.docaviv-manifest.json` | Files synced by the updater |

## Getting started

Pick your installation flavor:

### Claude Code (CLI) — full plugin with slash commands

1. Install Python 3.8+ (already on Mac/Linux; download from python.org on Windows)
2. Clone into your Claude Code plugins directory:
   ```bash
   git clone https://github.com/internet-and-sons/docaviv2026 ~/.claude/plugins/docaviv2026
   ```
3. Restart Claude Code.
4. Use `/docaviv:start` to begin, `/docaviv:update` to refresh.

### Claude Desktop (Customize → Add marketplace)

Paste `https://github.com/internet-and-sons/docaviv2026` into the *Add marketplace* dialog. Sync, then install the `docaviv` plugin.

### Claude.ai web — standalone skill upload

Download [`docaviv2026.skill`](https://github.com/internet-and-sons/docaviv2026/raw/main/docaviv2026.skill) (the file at the root of this repo), then upload it via *Customize → Skills → Upload skill*. No slash commands, but the planner triggers automatically when you mention Docaviv or ask about Tel Aviv documentary screenings.

## Usage

Just ask in Hebrew or English — the skill triggers on context. Examples:

- *"מה כדאי לי לראות בדוקאביב?"*
- *"תכנן לי 3 סרטים ב-30 במאי בלי חפיפות"*
- *"אילו סרטים מוקרנים פעם אחת בלבד?"*
- *"מצא לי זיווג גב-אל-גב ב-2 ביוני"*

## Help

Open an issue at https://github.com/internet-and-sons/docaviv2026/issues

---

*Licensed under MIT. See [LICENSE](./LICENSE).*
