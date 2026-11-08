# CLAUDE.md

ocarroeletrico.com: the site for people built from Voltaria's skills (`voltaria/`, a git submodule of
`CarregaErvilhas/voltaria`). Voltaria writes for assistants; this site rewrites the same knowledge for
drivers, in pt-PT and English. ohmigo (`CarregaErvilhas/ohmigo-mcp`) serves the same skills over MCP.

## How it fits together

- `content/<lang>/<skill>.md`: one page per published skill, written by an agent following
  `agent/SYSTEM.md` and `agent/TOM.md`. Checked in, reviewed in a PR.
- `scripts/build.py`: renders `content/` with `site/base.html` and `site/strings.json` into `_site/`.
  Amounts and dates of incentives come from `voltaria/knowledge/incentives.json` through
  `{{factos ...}}` markers, as of the build date. Each page's "Fontes" comes from the skill.
- `scripts/check.py`: what keeps the agent honest. Every diploma, article, number with a unit and
  (pt) date in a page must be in the skill; no money in the prose; glossary; no assistant voice;
  pages current with their SKILL.md (`sourceSha`). Tone problems are warnings.
- `scripts/oce.py`: shared code. `SKIP` (skills without a page: `regime-2010`), `GROUPS` (home page),
  `PAGE_TOOLS` (which tools each page points to).
- `pages.yml` builds and publishes on every push to `main` and every Monday, so open and closed
  incentives follow the calendar without a new commit.

Stdlib Python only. No CI step calls a model: there is no Claude key in CI.

## Rewriting after Voltaria changes (by hand, locally)

When Voltaria has significant changes:

1. `git -C voltaria fetch origin && git -C voltaria checkout origin/main` (the submodule pointer
   moves; commit it with the pages).
2. `scripts/rewrite.py`: which pages are stale or missing. `scripts/rewrite.py diff <skill>`: what
   changed in that SKILL.md since its page was written.
3. For each stale or missing skill, one subagent: it reads `agent/SYSTEM.md`, `agent/TOM.md`, the
   SKILL.md, the glossary and the current page, and writes `content/pt/<skill>.md`, then
   `content/en/<skill>.md` from the pt page. A rewrite changes only what the skill changed.
4. `scripts/rewrite.py stamp <skill>...`. Then the news: one brief per change a driver cares about
   (`content/{pt,en}/novidades/YYYY-MM-DD-slug.md`, rules in `agent/SYSTEM.md`, "Novidades"). It
   feeds `/novidades/`, its Atom feed and the home page. Then `scripts/check.py` until there are no
   errors.
5. Read each changed page next to its skill: no rule lost, none invented.
6. One PR. Merge is Fernando's.

Changing the voice means changing `agent/TOM.md` first, then the pages, never a page alone.

## Commands

```sh
scripts/build.py                 # _site/, facts as of today (--today YYYY-MM-DD to test dates)
scripts/check.py                 # what CI runs; --partial while pages are still being written
scripts/rewrite.py               # page status against the submodule
python3 -m http.server -d _site 8000   # preview (links are root-relative)
```

## Rules

- Never edit `voltaria/` here. Fixes to the knowledge go to Voltaria by PR; this repo only moves the
  submodule pointer.
- Never write a price, amount or incentive deadline in `content/`. Use `{{factos}}`.
- Content is CC-BY-4.0 (derived from Voltaria). The credit line in the footer is required by the
  licence: don't remove it.
- The mascot (the orange reporter car), the name and the icons are the site's brand, outside the licences.
- Every commit is signed off (`git commit -s`, DCO; `dco.yml` checks PRs). No CLA. Content fixes go to Voltaria, not here (CONTRIBUTING.md).
