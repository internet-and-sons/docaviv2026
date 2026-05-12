# Contributing to docaviv2026

Thanks for wanting to help. This document covers the maintainer workflow — how the data is refreshed and how the `.skill` bundle is rebuilt.

## Repository layout

```
.
├── skills/docaviv2026/
│   ├── SKILL.md              skill instructions (what Claude reads)
│   └── data/
│       ├── INDEX.md          one line per film — grep-friendly catalog
│       ├── schedule.md       one line per screening, sorted by date+time
│       ├── films/            122 detail pages (~2 KB each)
│       └── sections/         18 section pages (~3 KB each)
├── scripts/
│   ├── build-skill-data.py   SQLite → markdown tree
│   └── build-skill.py        markdown tree → docaviv2026.skill zip
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── docaviv2026.skill          the distributable single-file bundle (committed)
└── VERSION
```

## Prerequisites

- Python 3.9+
- [`docaviv-pp-cli`](https://github.com/internet-and-sons/docaviv-pp-cli) — the private CLI that pulls data from the Docaviv WordPress REST API into a local SQLite store. Only needed by maintainers refreshing data; end users never need it.

## Refreshing the data

```bash
# 1. Pull latest from Docaviv's WP REST API + scrape the schedule page
docaviv-pp-cli sync
docaviv-pp-cli screenings sync

# 2. Regenerate the markdown tree
python3 scripts/build-skill-data.py

# 3. Rebuild the single-file .skill bundle
python3 scripts/build-skill.py

# 4. Bump version, commit, push
echo "0.X.0" > VERSION
# update version in .claude-plugin/plugin.json to match
git add . && git commit -m "v0.X.0: refresh data for <date>"
git push
```

The committed `docaviv2026.skill` is what end users download and double-click. Always rebuild it when the data changes.

## Editing the skill instructions

The skill prompt lives in [`skills/docaviv2026/SKILL.md`](skills/docaviv2026/SKILL.md). After editing it, rebuild the bundle:

```bash
python3 scripts/build-skill.py
git add docaviv2026.skill skills/docaviv2026/SKILL.md
git commit -m "skill: <describe change>"
```

## Installing for local development (Claude Code)

```bash
git clone https://github.com/internet-and-sons/docaviv2026 ~/.claude/plugins/docaviv2026
```

Restart Claude Code. The skill auto-triggers on Docaviv / Tel Aviv documentary context.

## License

Plugin code (SKILL.md, build scripts) is MIT. Film data belongs to [Docaviv](https://www.docaviv.co.il/) — redistributed here for non-commercial viewing-planning purposes only.
