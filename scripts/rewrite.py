#!/usr/bin/env python3
"""Which pages need rewriting after Voltaria changed, and the bookkeeping after you rewrite them.
It never calls a model: the rewriting is done by a Claude Code session (CLAUDE.md, agent/SYSTEM.md).

  scripts/rewrite.py                 status of every published skill: ok, stale or missing
  scripts/rewrite.py diff SKILL      what changed in that SKILL.md since its page was written
  scripts/rewrite.py stamp SKILL...  after rewriting: records the Voltaria commit, the SKILL.md sha256
                                     and today's date in the pt and en pages

stamp refuses unless both pages exist, so pt and en always come from the same SKILL.md.
"""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import oce  # noqa: E402


def status():
    rows = []
    for slug in oce.published():
        page = oce.load_page("pt", slug)
        if page is None:
            rows.append((slug, "missing", ""))
            continue
        fields, _ = page
        if fields.get("sourceSha") == oce.skill_sha(slug):
            rows.append((slug, "ok", fields.get("updated", "")))
        else:
            stat = _git_diff(fields.get("sourceCommit"), slug, "--stat")
            rows.append((slug, "stale", stat.strip().splitlines()[-1] if stat.strip() else "changed"))
    width = max(len(r[0]) for r in rows)
    for slug, state, note in rows:
        print(f"{slug:<{width}}  {state:<7}  {note}")
    todo = [r[0] for r in rows if r[1] != "ok"]
    print(f"\n{len(todo)} to write: {' '.join(todo)}" if todo else "\nall pages are current")


def _git_diff(commit, slug, *flags):
    if not commit:
        return ""
    path = f"skills/{slug}/SKILL.md"
    r = subprocess.run(["git", "-C", str(oce.VOLTARIA), "diff", *flags, commit, "HEAD", "--", path],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else f"(no diff: {r.stderr.strip()})"


def diff(slug):
    page = oce.load_page("pt", slug)
    if page is None:
        sys.exit(f"{slug}: no page yet, write it from the whole SKILL.md")
    out = _git_diff(page[0].get("sourceCommit"), slug)
    print(out or "no changes")


def stamp(slugs):
    commit, sha_today = oce.voltaria_commit(), dt.date.today().isoformat()
    for slug in slugs:
        if slug not in oce.published():
            sys.exit(f"{slug}: not a published skill")
        paths = [oce.page_path(lang, slug) for lang in oce.LANGS]
        missing = [str(p.relative_to(oce.ROOT)) for p in paths if not p.exists()]
        if missing:
            sys.exit(f"{slug}: write both pages first; missing {', '.join(missing)}")
        values = {"source": slug, "sourceCommit": commit, "sourceSha": oce.skill_sha(slug), "updated": sha_today}
        for p in paths:
            text = p.read_text(encoding="utf-8")
            end = text.find("\n---\n", 4)
            if not text.startswith("---\n") or end < 0:
                sys.exit(f"{p}: no frontmatter")
            head = text[4:end].split("\n")
            for key, value in values.items():
                line = f'{key}: "{value}"'
                idx = next((i for i, l in enumerate(head) if re.match(rf"{key}\s*:", l)), None)
                if idx is None:
                    head.append(line)
                else:
                    head[idx] = line
            p.write_text("---\n" + "\n".join(head) + text[end:], encoding="utf-8")
        print(f"{slug}: stamped {commit[:7]}")


def main():
    args = sys.argv[1:]
    if not args:
        status()
    elif args[0] == "diff" and len(args) == 2:
        diff(args[1])
    elif args[0] == "stamp" and len(args) > 1:
        stamp(args[1:])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
