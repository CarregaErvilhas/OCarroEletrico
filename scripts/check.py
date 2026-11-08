#!/usr/bin/env python3
"""Checks the pages in content/ against Voltaria, so the agent can't quietly change the law.

Errors (exit 1):
- every published skill has a page in pt and en, from the current SKILL.md (sourceSha);
- every diploma number (93/2025, 2023/1804, 128/2026/1, ...) and every article number in a page
  appears in the skill (or in Voltaria's facts);
- every number with a unit (30 dias, 41,4 kVA, 10 A, 30 mA, ...) and, in pt, every date appears in
  the skill: the agent may leave numbers out, never change them;
- no money (€, euros) in the prose: amounts come from the facts, injected by the build;
- no glossary "Evitar" term in pt; no assistant voice ("o utilizador", "skill", ohmigo's tool names);
  no emojis;
- the site builds (Markdown subset, links, {{factos}} markers).

Warnings: tone (agent/TOM.md: banned phrases, exclamation marks, long sentences), a page much shorter
than its skill, a missing "O essencial" box.

Usage: scripts/check.py [--partial]   (--partial: missing pages are warnings, for work in progress)
"""
import argparse
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import oce  # noqa: E402

REQUIRED = ("source", "sourceCommit", "sourceSha", "title", "description", "updated")
URL_RE = re.compile(r"https?://\S+")
CODE_RE = re.compile(r"`[^`\n]+`")
DIPLOMA_RE = re.compile(r"\b(\d{1,4}(?:-[A-Z])?/\d{4}(?:/\d+)?|\d{4}/\d{1,5})\b")
# "art. 23.º", "arts. 13.º, 14.º e 34.º", "arts. 9.º a 11.º", "Articles 21 and 22": every number counts.
ARTICLE_RE = re.compile(r"\b(?:art(?:igos?|s?\.)|articles?)\s*((?:\d+(?:\.?\s?º)?(?:-[A-Z])?(?:\s*(?:,|e|a|and|to)\s*(?=\d))?)+)", re.I)


def articles(text):
    return {n for m in ARTICLE_RE.findall(text) for n in re.findall(r"\d+", re.sub(r"-[A-Z]", "", m))}
UNITS = {"dias": "dias", "days": "dias", "meses": "meses", "months": "meses", "anos": "anos", "years": "anos",
         "horas": "horas", "hours": "horas", "minutos": "minutos", "minutes": "minutos",
         "A": "A", "mA": "mA", "kW": "kW", "kWh": "kWh", "kVA": "kVA", "VA": "VA", "V": "V", "mm²": "mm²",
         "%": "%", "km": "km"}
UNIT_RE = re.compile(r"(?<![\w.,])(\d+(?:[.,]\d+)?)\s?(%|mm²|(?:dias|days|meses|months|anos|years|horas|hours|minutos|minutes|mA|kWh|kVA|kW|VA|km|A|V)\b)")
DATE_RE = re.compile(r"\b(\d{1,2})-(\d{1,2})-(\d{4})\b")
MONEY_RE = re.compile(r"€|\bEUR\b|\beuros?\b", re.I)
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿]")
VOICE = {
    "pt": [r"\bassistente\b", r"\bskills?\b", r"\b(?:o|ao|do|pelo|no) utilizador\b", r"\bEscrito para ti\b",
           r"\bglossário\b", r"\bVoltaria\b"],
    "en": [r"\bassistant\b", r"\bskills?\b", r"\bthe user\b", r"\bglossary\b", r"\bVoltaria\b"],
}
TOOLS_RE = re.compile(r"\b(estimate_charging_cost|find_cheapest_charging|find_chargers|lookup_charger|"
                      r"list_ceme_tariffs|list_operators|ev_rules_portugal|get_guide|get_facts)\b")
BANNED = {
    "pt": ["neste artigo", "nesta página vamos", "é importante referir", "é importante notar", "é de salientar",
           "em suma", "em conclusão", "vamos ver", "sem dúvida", "você", "de forma a", "tudo o que precisa"],
    "en": ["in this article", "it is important to note", "it's important to note", "in conclusion",
           "in summary", "delve", "everything you need to know", "without a doubt"],
}
BOX_RE = re.compile(r"^:::essencial\s*$(.*?)^:::\s*$", re.M | re.S)


def norm(text):
    """Collapses whitespace (a number and its unit can sit on two lines), joins thousands written with
    a space (3 680), for comparing."""
    text = re.sub(r"[\s\u00a0\u202f]+", " ", text)
    return re.sub(r"(?<=\d) (?=\d{3}\b)", "", text)


def prose_of(body):
    """The page without URLs and code, which the checks below don't apply to."""
    return CODE_RE.sub(" ", URL_RE.sub(" ", body))


def units(text):
    return {(n.replace(",", "."), UNITS[u]) for n, u in UNIT_RE.findall(norm(text))}


def facts_text():
    out = []
    for e in oce.facts():
        out += [e["text"]["pt"], e["text"]["en"], e["source"]["name"]]
    return "\n".join(out)


def sentences(text):
    """Sentences of the prose: headings, tables and box markers out, every list item on its own, and
    "art." not taken for the end of a sentence."""
    blocks = []
    for line in text.split("\n"):
        s = line.strip()
        if not s or s.startswith(("#", "|", ":::", "{{")):
            blocks.append("")
        elif re.match(r"(- |\d+\. )", s):
            blocks += ["", re.sub(r"^(- |\d+\. )", "", s)]
        else:
            blocks.append(s)
    out = []
    for block in re.split(r"\n{2,}", "\n".join(blocks)):
        block = re.sub(r"\b(art|arts|n|p)\. ", r"\1_ ", re.sub(r"\s+", " ", block))
        out += [x for x in re.split(r"(?<=[.!?;])\s+", block) if len(x.split()) > 2]
    return out


def check_page(lang, slug, fields, body, skill, ftext, errors, warnings):
    where = f"content/{lang}/{slug}.md"
    E = lambda msg: errors.append(f"{where}: {msg}")  # noqa: E731
    W = lambda msg: warnings.append(f"{where}: {msg}")  # noqa: E731
    for key in REQUIRED:
        if not fields.get(key):
            E(f"frontmatter has no {key!r}")
    if fields.get("source") != slug:
        E(f"source is {fields.get('source')!r}, expected {slug!r}")
    if fields.get("sourceSha") and fields["sourceSha"] != oce.skill_sha(slug):
        E("written from an older SKILL.md (sourceSha): rewrite it, then scripts/rewrite.py stamp " + slug)
    if len(fields.get("description", "")) > 170:
        W("description is over 170 characters (search results cut it)")

    prose = prose_of(body)
    source = skill
    # A page that shows facts may name the diplomas behind them (a Despacho, an aviso); its numbers,
    # dates and articles still have to come from the skill.
    src = norm(skill + ("\n" + ftext if "{{factos" in body else ""))

    for d in sorted(set(DIPLOMA_RE.findall(prose))):
        if d not in src:
            E(f"cites {d!r}, which is not in the skill" + (" or the facts" if "{{factos" in body else ""))
    for a in sorted(articles(prose) - articles(source), key=int):
        E(f"cites article {a}, which the skill never cites")
    for n, u in sorted(units(prose) - units(source)):
        E(f"has '{n} {u}', which is not in the skill")
    if lang == "pt":
        src_dates = {tuple(int(x) for x in m) for m in DATE_RE.findall(source)}
        for m in DATE_RE.findall(prose):
            if tuple(int(x) for x in m) not in src_dates:
                E(f"has the date {'-'.join(m)}, which is not in the skill")
    if MONEY_RE.search(prose):
        E("has money in the prose; amounts come from {{factos}}")
    if EMOJI_RE.search(body):
        E("has emojis")
    for pat in VOICE[lang]:
        for m in re.finditer(pat, prose, re.I):
            E(f"assistant voice or internal name: {m.group(0)!r}")
    for m in TOOLS_RE.finditer(body):
        E(f"names an ohmigo tool: {m.group(0)!r}")
    if lang == "pt":
        for term, avoid, pat in oce.glossary_terms():
            if pat.search(prose):
                E(f"uses {avoid!r}; the glossary says {term!r}")

    low = prose.lower()
    for phrase in BANNED[lang]:
        if phrase in low:
            W(f"tone: {phrase!r}")
    if prose.count("!") > 1:
        W(f"tone: {prose.count('!')} exclamation marks (at most one per page)")
    sents = sentences(prose)
    if sents:
        avg = sum(len(s.split()) for s in sents) / len(sents)
        if avg > 22:
            W(f"tone: sentences average {avg:.0f} words (aim for under 20)")
        for s in sents:
            if len(s.split()) > 45:
                W(f"tone: a {len(s.split())}-word sentence: {s[:70]}…")
    first = next((l.strip() for l in body.split("\n") if l.strip()), "")
    if first.startswith(("#", ":::", "-", "|", "{{")):
        W("the page doesn't open with a paragraph (the lide)")
    box = BOX_RE.search(body)
    if not box:
        W("no :::essencial box")
    elif not 3 <= len(re.findall(r"^\s*- ", box.group(1), re.M)) <= 4:
        W(":::essencial should have 3 points")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--partial", action="store_true", help="missing pages are warnings")
    a = ap.parse_args()
    errors, warnings = [], []

    grouped = [s for _, slugs in oce.GROUPS for s in slugs]
    for s in sorted(set(oce.published()) - set(grouped)):
        errors.append(f"oce.py GROUPS: {s!r} is published but in no group")
    for s in sorted(set(grouped) - set(oce.published())):
        errors.append(f"oce.py GROUPS: {s!r} is not a published skill")
    for lang in oce.LANGS:
        for p in sorted((oce.CONTENT / lang).glob("*.md")):
            if p.stem not in oce.published():
                errors.append(f"{p.relative_to(oce.ROOT)}: no published skill with that name")

    ftext = facts_text()
    for slug in oce.published():
        skill = oce.skill_text(slug)
        shas = {}
        for lang in oce.LANGS:
            try:
                page = oce.load_page(lang, slug)
            except oce.PageError as e:
                errors.append(f"content/{lang}/{slug}.md: {e}")
                continue
            if page is None:
                (warnings if a.partial else errors).append(f"content/{lang}/{slug}.md: missing")
                continue
            fields, body = page
            shas[lang] = fields.get("sourceSha")
            check_page(lang, slug, fields, body, skill, ftext, errors, warnings)
        if len(shas) == 2 and shas["pt"] != shas["en"]:
            errors.append(f"{slug}: pt and en were written from different versions of the skill")

    # News briefs: the same honesty rules, against the whole of Voltaria (a brief can be about any
    # skill or fact). They may name Voltaria, since saying what changed there is their job.
    every_skill = "\n".join(oce.skill_text(x) for x in oce.skill_names())
    slugs = {lang: {n[0] for n in oce.news(lang)} for lang in oce.LANGS}
    for s_ in sorted(slugs["pt"] ^ slugs["en"]):
        errors.append(f"novidades/{s_}.md: exists in one language only")
    for lang in oce.LANGS:
        for slug, fields, body in oce.news(lang):
            where = f"content/{lang}/novidades/{slug}.md"
            if not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+$", slug):
                errors.append(f"{where}: name it YYYY-MM-DD-slug.md")
            if fields.get("date") != slug[:10]:
                errors.append(f"{where}: date {fields.get('date')!r} doesn't match the file name")
            errs = []
            check_page(lang, slug, {**fields, "source": slug, "sourceCommit": "-", "sourceSha": None,
                                    "description": "", "updated": "-"}, body, every_skill, ftext, errs, [])
            errors += [e.replace(f"content/{lang}/{slug}.md", where) for e in errs
                       if "Voltaria" not in e and "frontmatter has no" not in e and "source is" not in e]

    import build  # noqa: E402
    with tempfile.TemporaryDirectory() as tmp:
        try:
            build.Site(Path(tmp) / "_site", build.dt.date.today().isoformat()).build()
        except SystemExit as e:
            errors.append(f"build: {e}")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    n = sum(1 for lang in oce.LANGS for s in oce.published() if oce.page_path(lang, s).exists())
    print(f"{n} pages, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
