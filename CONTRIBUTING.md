# Contributing to docaviv2026

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
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── docaviv2026.skill          the distributable single-file bundle (committed)
└── VERSION
```

## Editing the skill instructions

The skill prompt lives in [`skills/docaviv2026/SKILL.md`](skills/docaviv2026/SKILL.md). Open it, make your changes, commit, and push. The data files under `data/` are refreshed periodically by the maintainer.

## Installing for local development (Claude Code)

```bash
git clone https://github.com/internet-and-sons/docaviv2026 ~/.claude/plugins/docaviv2026
```

Restart Claude Code. The skill auto-triggers on Docaviv / Tel Aviv documentary context.

## License

Plugin code (SKILL.md) is MIT. Film data belongs to [Docaviv](https://www.docaviv.co.il/) — redistributed here for non-commercial viewing-planning purposes only.
