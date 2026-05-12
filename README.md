# docaviv2026

A free, fan-made Claude Code plugin that helps you explore and plan your schedule for the **Docaviv 2026** documentary film festival (28 May – 6 June 2026, Tel Aviv Cinematheque + Tel Aviv Museum).

This skill bundles the **entire festival catalog as searchable markdown files** inside the plugin — 122 films, 185 screenings, 18 sections, all queryable with `grep` and `cat`. No binary to install, no external API calls at runtime, works in any Claude environment with shell access (Claude Code, Claude Desktop, claude.ai web upload).

Ask in Hebrew or English: recommend films by taste, build a conflict-free day plan, find back-to-back pairings, surface single-screening films before they disappear.

> **Data credit & disclaimer.** All film titles, descriptions, schedules, venues, and order links come from the official festival site at [docaviv.co.il](https://www.docaviv.co.il/). Huge thanks to the Docaviv team for organising the festival and publishing the data that makes this planner possible. This is an **independent, non-commercial fan project** — not affiliated with or endorsed by Docaviv. For ticketing and the most up-to-date schedule, always go to [docaviv.co.il](https://www.docaviv.co.il/).

## How it's built (progressive disclosure)

Rather than a single 78 KB JSON file (slow for Claude to scan), the festival data is pre-split into 143 small markdown files keyed by access pattern, following [Anthropic's recommended progressive-disclosure pattern](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices):

```
data/
├── INDEX.md            ~10 KB — one line per film, grep-friendly catalog
├── schedule.md         ~30 KB — one line per screening, sorted by date+time
├── films/              122 detail pages, ~2 KB each (loaded only when asked about a specific film)
└── sections/           18 selection-track pages, ~3 KB each
```

When a user asks "what's playing 30.5?", Claude greps `schedule.md` for that date and reads only ~1 KB of context. When asked "tell me about Holofiction," it `cat`s `films/holofiction.md` — 2 KB. The other 363 KB stay on disk, costing zero tokens.

## Install

### Claude Code — git clone

```bash
git clone https://github.com/internet-and-sons/docaviv2026 ~/.claude/plugins/docaviv2026
```

Restart Claude Code. The skill triggers automatically when you mention Docaviv or ask about Tel Aviv documentary screenings.

### Claude Code — marketplace

Paste `https://github.com/internet-and-sons/docaviv2026` into Customize → Add marketplace. Sync, install the `docaviv` plugin.

### Claude.ai web — single-file upload

Download [`docaviv2026.skill`](https://github.com/internet-and-sons/docaviv2026/raw/main/docaviv2026.skill) (about 200 KB) and upload via Customize → Skills → Upload skill.

## Usage

Just ask in Hebrew or English — the skill triggers on context.

- *"מה כדאי לי לראות בדוקאביב?"*
- *"תכנן לי 3 סרטים ב-30 במאי בלי חפיפות"*
- *"אילו סרטים מוקרנים פעם אחת בלבד?"*
- *"מצא לי זיווג גב-אל-גב ב-2 ביוני"*
- *"recommend a Holocaust documentary on Friday night"*

## Updates

The bundled data is a snapshot. Docaviv keeps publishing films and screenings in the lead-up to the festival; new versions of this plugin ship periodically.

| What | Where | How to update |
| --- | --- | --- |
| The plugin | This repo | `cd ~/.claude/plugins/docaviv2026 && git pull`, or re-download `.skill` |

## How the snapshot is built (for maintainers)

The pipeline is:

```bash
# 1. Sync live data with the docaviv-pp-cli binary (kept in a separate repo)
docaviv-pp-cli sync                  # pulls WP REST → SQLite
docaviv-pp-cli screenings sync       # scrapes the schedule page

# 2. Regenerate the markdown tree
python3 scripts/build-skill-data.py  # SQLite → data/INDEX.md + data/schedule.md + data/films/*.md + data/sections/*.md

# 3. Rebuild the single-file bundle
python3 scripts/build-skill.py       # zips everything into docaviv2026.skill

# 4. Bump VERSION, commit, push, GitHub release
echo "0.X.0" > VERSION
git add . && git commit -m "Refresh data for X" && git push
```

The `docaviv-pp-cli` binary lives at https://github.com/internet-and-sons/docaviv-pp-cli — it's only needed by maintainers (the human running these refresh scripts), not end users of the plugin.

## License & terms

The plugin code (SKILL.md, build scripts) is released under the MIT license — see [LICENSE](./LICENSE).

The film data bundled inside the plugin is sourced from [docaviv.co.il](https://www.docaviv.co.il/) and remains the property of the Docaviv festival. Redistributed here for the limited purpose of helping viewers plan their attendance — please respect the festival's [terms of use](https://www.docaviv.co.il/terms-of-use/) and don't repurpose the data commercially.

## Acknowledgments

- **[דוקאביב / Docaviv](https://www.docaviv.co.il/)** — for the festival, and for publishing the data this planner reads.
- The Tel Aviv Cinematheque, where the festival lives.
- Documentary filmmakers everywhere.

---

*Built with ❤️ for documentary lovers.*
