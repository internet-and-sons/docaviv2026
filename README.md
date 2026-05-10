# docaviv2026

A free, fan-made Claude Code plugin that helps you explore and plan your schedule for the Docaviv 2026 documentary film festival (28 May – 6 June 2026, Tel Aviv Cinematheque).

Ask it to recommend films based on your taste, build a conflict-free day plan, find back-to-back pairings, or surface single-screening films before they disappear. Works primarily in Hebrew.

> **Data credit & disclaimer.** All film titles, descriptions, schedules, venues, and order links come from the official festival site at [docaviv.co.il](https://www.docaviv.co.il/). Huge thanks to the Docaviv team for organising the festival and publishing the data that makes this planner possible. This is an **independent, non-commercial fan project** — not affiliated with or endorsed by Docaviv. For ticketing and the most up-to-date schedule, always go to [docaviv.co.il](https://www.docaviv.co.il/).

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

## Acknowledgments

- **[דוקאביב / Docaviv](https://www.docaviv.co.il/)** — for the festival itself, and for publishing the film catalogue, descriptions, and screening schedule that this planner reads. Festival programming, curation, and venue logistics are 100% theirs; this project just helps viewers navigate the lineup.
- The Tel Aviv Cinematheque, where the festival lives.
- Documentary filmmakers everywhere — without whom there's nothing to plan around.

## License & terms

The plugin code (SKILL.md, plan.py, build scripts, update logic) is released under the MIT license — see [LICENSE](./LICENSE). Free to use, fork, modify, redistribute.

The bundled film data (titles, descriptions, schedules, venue and ticket links) is sourced from [docaviv.co.il](https://www.docaviv.co.il/) and remains the property of the Docaviv festival. This project redistributes it for the limited purpose of helping viewers plan their attendance — please respect the festival's [terms of use](https://www.docaviv.co.il/terms-of-use/) and don't repurpose the data commercially.

---

*Built with ❤️ for documentary lovers.*
