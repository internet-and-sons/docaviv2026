# Project context — docaviv2026

This file is auto-loaded as project context whenever Claude Code is opened in this repo. Read it first, then read the companion files below as the task requires.

## What this repo is

A free, fan-made Claude Code plugin that helps users explore and plan their schedule for the **Docaviv 2026** documentary film festival (28 May – 6 June 2026, Tel Aviv Cinematheque + Tel Aviv Museum). It ships 122 films and 185 screenings as a grep-friendly markdown tree inside a `.skill` bundle — no external API calls at runtime. Public repo, MIT-licensed code, festival data credited to [docaviv.co.il](https://www.docaviv.co.il/).

The companion private repo [`internet-and-sons/docaviv-pp-cli`](https://github.com/internet-and-sons/docaviv-pp-cli) handles the data pipeline (WP REST API → SQLite). Build scripts live locally at `~/docaviv-scripts/` — they are not in this repo.

## Companion files

Read the companion files below before any task that touches the area they cover.

- **`CONTRIBUTING.md`** — how to edit the skill prompt and how to install locally for development.
- **`TODO.md`** — pending work and deferred decisions. Read when continuing in-flight work.
- **`LEARNINGS.md`** — non-obvious gotchas. Read before editing areas where past issues have lived.

Org-wide rules live in [`internet-and-sons/.github/CONTRIBUTING.md`](https://github.com/internet-and-sons/.github/blob/main/CONTRIBUTING.md). Read that once; it covers branching, PRs, and the merge policy.

## Hard rules (always apply, never override)

1. **Every change goes through a PR.** No direct pushes to `main`. See org CONTRIBUTING for the full policy.
2. **Ask before opening a PR.** Don't open one autonomously. Plan approval doesn't imply PR approval — ask again when the branch is ready.
3. **Never edit `skills/docaviv2026/data/` files by hand.** They are generated output. The data pipeline lives in `~/docaviv-scripts/` and is run by the maintainer only.
4. **Don't rename `SKILL.md` or move files it references.** The `.skill` bundle and Claude Desktop both depend on stable paths.
5. **The README is user-facing and Hebrew-first.** Don't rewrite it in English or add technical content — keep it welcoming and simple.

## Working agreements

- **Ask clarifying questions before complex tasks.** Surface ambiguities before starting.
- **Make minimal changes.** Stay in the lane the task asked for; flag anything else as a follow-up.
- **Atomic commits.** One commit per logical change. No catch-all commits.
- **PRs are batched commits, reviewed as a whole.**
- **Never silently choose between two viable approaches.** Lay out the tradeoffs and wait for the human to pick.

## Quick orientation

| Path | What it is |
| --- | --- |
| `skills/docaviv2026/SKILL.md` | The skill prompt — what Claude reads when the skill fires |
| `skills/docaviv2026/data/INDEX.md` | One-line catalog of all 122 films, grep-friendly |
| `skills/docaviv2026/data/schedule.md` | One line per screening, sorted by date+time |
| `skills/docaviv2026/data/films/` | 122 per-film detail pages (~2 KB each) |
| `skills/docaviv2026/data/sections/` | 18 section/track pages |
| `docaviv2026.skill` | The distributable zip bundle — rebuilt after any data or SKILL.md change |
| `assets/banner.jpeg` | Repo banner image |
| `.claude-plugin/plugin.json` | Plugin metadata (name, version) |
| `.claude-plugin/marketplace.json` | Enables install via Claude Desktop marketplace |

## Need help?

If you're unsure whether a change is safe — especially anything touching data files, SKILL.md paths, or the README — stop and ask.
