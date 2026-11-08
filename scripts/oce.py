"""What build.py, check.py and rewrite.py share: where things live, the pages in content/, the small
Markdown renderer, the facts from Voltaria and the "## Fontes" of each skill.

Stdlib only. Voltaria is the folder voltaria/ (a git submodule), never a copy.
"""
import datetime as dt
import hashlib
import html
import importlib.util
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOLTARIA = ROOT / "voltaria"
CONTENT = ROOT / "content"
SITE_URL = "https://ocarroeletrico.com"
VOLTARIA_URL = "https://github.com/CarregaErvilhas/voltaria"
SITE_REPO_URL = "https://github.com/CarregaErvilhas/OCarroEletrico"
LANGS = ("pt", "en")

# Skills that don't get a page. regime-2010 is the revoked regime: useful to an assistant answering
# about the old model, noise for someone who wants to charge today.
SKIP = {"regime-2010"}

# The home page groups, in order. A published skill missing from here fails check.py.
GROUPS = [
    ("casa", ["carregar-em-casa", "instalacao-eletrica", "sub-cpe"]),
    ("rua", ["carregamento-publico", "autonomia"]),
    ("carro", ["baterias", "garantias-de-origem"]),
    ("dinheiro", ["incentivos", "empresas-e-frotas"]),
    ("pro", ["afir", "afir-nap", "tarifas-de-acesso", "tecnologia-de-carregamento"]),
]

TOOLS = {
    "ohmigo": "https://ohmigo.ocarroeletrico.com/",
    "ceme": "https://ceme.ocarroeletrico.com/",
    "nap": "https://nap.ocarroeletrico.com/",
    "simuladores": "https://simuladores.ocarroeletrico.com/",
}
# Which tools each page points to at the end. Everything else gets ohmigo.
PAGE_TOOLS = {
    "carregar-em-casa": ["ohmigo", "simuladores"],
    "carregamento-publico": ["ohmigo", "ceme", "nap"],
    "autonomia": ["ohmigo", "nap"],
    "incentivos": ["simuladores", "ohmigo"],
    "empresas-e-frotas": ["simuladores", "ceme"],
    "sub-cpe": ["ohmigo", "simuladores"],
    "afir-nap": ["nap", "ohmigo"],
}

FACT_KINDS = {"apoio", "fiscal", "municipal", "mercado"}
FACT_STATES = {"aberto", "anunciado", "fechado", "futuro", "todos"}
STALE_DAYS = 180


class PageError(Exception):
    pass


# ---------------------------------------------------------------- Voltaria

def _load_check_skills():
    """voltaria/scripts/check-skills.py, for its glossary and frontmatter parsers: one parser for
    the skills and for these pages."""
    path = VOLTARIA / "scripts" / "check-skills.py"
    spec = importlib.util.spec_from_file_location("check_skills", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


check_skills = _load_check_skills()


def frontmatter(text):
    fields, errors = check_skills.frontmatter(text)
    if errors:
        raise PageError("; ".join(errors))
    body = text[text.find("\n---\n", 4) + 5:]
    return fields, body


def glossary_terms():
    return check_skills.glossary_terms(str(VOLTARIA / "glossario.md"))


def skill_names():
    """Every skill in Voltaria, published or not."""
    return sorted(p.parent.name for p in (VOLTARIA / "skills").glob("*/SKILL.md"))


def published():
    return [s for s in skill_names() if s not in SKIP]


def skill_path(name):
    return VOLTARIA / "skills" / name / "SKILL.md"


def skill_text(name):
    return skill_path(name).read_text(encoding="utf-8")


def skill_sha(name):
    return hashlib.sha256(skill_path(name).read_bytes()).hexdigest()


def voltaria_commit():
    return _git("rev-parse", "HEAD")


def voltaria_date():
    """Date of the Voltaria commit the site is built from (YYYY-MM-DD)."""
    return _git("log", "-1", "--format=%cs")


def _git(*args):
    return subprocess.run(["git", "-C", str(VOLTARIA), *args], check=True, capture_output=True,
                          text=True).stdout.strip()


def facts():
    data = json.loads((VOLTARIA / "knowledge" / "incentives.json").read_text(encoding="utf-8"))
    return data["entries"]


def fact_state(entry, today):
    """aberto (in force or open), anunciado, fechado (history) or futuro (published, not yet valid)."""
    if entry.get("status") == "anunciado":
        return "anunciado"
    if entry.get("validTo") and entry["validTo"] < today:
        return "fechado"
    if entry.get("validFrom") and entry["validFrom"] > today:
        return "futuro"
    return "aberto"


# ---------------------------------------------------------------- pages

def page_path(lang, slug):
    return CONTENT / lang / f"{slug}.md"


def load_page(lang, slug):
    """(fields, body) of content/<lang>/<slug>.md, or None if it doesn't exist."""
    path = page_path(lang, slug)
    if not path.exists():
        return None
    return frontmatter(path.read_text(encoding="utf-8"))


def pages(lang):
    """Published skills that have a page in this language, in group order."""
    out = []
    for _, slugs in GROUPS:
        out += [s for s in slugs if page_path(lang, s).exists()]
    return out


def news(lang):
    """The briefs in content/<lang>/novidades/*.md, newest first: (slug, fields, body)."""
    out = []
    for path in (CONTENT / lang / "novidades").glob("*.md"):
        fields, body = frontmatter(path.read_text(encoding="utf-8"))
        out.append((path.stem, fields, body))
    return sorted(out, key=lambda n: (n[1].get("date", ""), n[0]), reverse=True)


# ---------------------------------------------------------------- dates

MONTHS_PT = "jan. fev. mar. abr. maio jun. jul. ago. set. out. nov. dez.".split()
MONTHS_EN = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def fmt_date(iso, lang):
    d = dt.date.fromisoformat(iso)
    if lang == "pt":
        return f"{d.day} {MONTHS_PT[d.month - 1]} {d.year}"
    return f"{d.day} {MONTHS_EN[d.month - 1]} {d.year}"


# ---------------------------------------------------------------- Markdown

BOXES = {"essencial", "aviso"}
CODE_RE = re.compile(r"`([^`\n]+)`")
LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
URL_RE = re.compile(r"https://[^\s<>\"]+[^\s<>\".,;:)]")
FACTS_RE = re.compile(r"^\{\{factos((?:\s+\w+=[\w-]+)*)\s*\}\}$")
UNIT_NBSP_RE = re.compile(r"(\d) (%|mm²|mA|kWh|kVA|kW|VA|V|A|km|dias|days|anos|years|meses|months|horas|hours)(?![\w-])")
INTERNAL_RE = re.compile(r"^/(?:([a-z0-9-]+)/)?(#[\w-]+)?$")


def slugify(text):
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).lower()
    table = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçñ", "aaaaaeeeeiiiiooooouuuucn")
    text = text.translate(table)
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-") or "s"


class Renderer:
    """A small Markdown renderer for the subset the agent is allowed to write. Anything outside it
    raises PageError, so a page can't sneak in raw HTML, images or formats the design doesn't style.

    Blocks: ## and ### headings, paragraphs, "- " and "1. " lists (one level, continuation lines
    indented), pipe tables, :::essencial / :::aviso boxes, and a {{factos ...}} line.
    Inline: **bold**, `code`, [text](link). Internal links are /<slug>/ or /<slug>/#anchor.
    """

    def __init__(self, lang, slugs, facts_fn=None, autolink=False, box_titles=None, existing=None):
        self.lang = lang
        self.existing = None if existing is None else set(existing)
        self.box_titles = box_titles or {}
        self.slugs = set(slugs)
        self.facts_fn = facts_fn
        self.autolink = autolink
        self.headings = []
        self.links = []
        self._ids = set()
        self.ids = self._ids
        self._lide = False

    # inline -----------------------------------------------------------
    def href(self, url):
        if url.startswith("https://"):
            return url
        m = INTERNAL_RE.match(url)
        if not m:
            raise PageError(f"link not allowed: {url!r} (https:// or /<slug>/)")
        slug = m.group(1)
        if slug and slug not in self.slugs:
            raise PageError(f"link to a page that doesn't exist: {url!r}")
        self.links.append(url)
        if slug and self.existing is not None and slug not in self.existing:
            return None  # a published skill whose page isn't written yet: plain text for now
        prefix = "" if self.lang == "pt" else "/en"
        return prefix + url

    def inline(self, text):
        if "![" in text:
            raise PageError("images are not allowed")
        parts = []
        pos = 0
        for m in CODE_RE.finditer(text):
            parts.append(self._inline_text(text[pos:m.start()]))
            parts.append(f"<code>{html.escape(m.group(1))}</code>")
            pos = m.end()
        parts.append(self._inline_text(text[pos:]))
        return "".join(parts)

    def _inline_text(self, text):
        tokens = []

        def keep(s):
            tokens.append(s)
            return f"\x00{len(tokens) - 1}\x00"

        def link(m):
            href = self.href(m.group(2))
            if href is None:
                return keep(self._bold(html.escape(m.group(1))))
            ext = ' rel="noopener"' if href.startswith("https://") else ""
            return keep(f'<a href="{html.escape(href)}"{ext}>{self._bold(html.escape(m.group(1)))}</a>')

        text = LINK_RE.sub(link, text)
        if self.autolink:
            text = URL_RE.sub(lambda m: keep(f'<a href="{html.escape(m.group(0))}" rel="noopener">'
                                             f'{html.escape(m.group(0))}</a>'), text)
        text = self._bold(html.escape(text, quote=False))
        # A number never wraps away from its unit ("16 A", "30 dias", "art. 23.º").
        text = UNIT_NBSP_RE.sub("\\1\u00a0\\2", text)
        return re.sub("\x00(\\d+)\x00", lambda m: tokens[int(m.group(1))], text)

    @staticmethod
    def _bold(text):
        return BOLD_RE.sub(r"<strong>\1</strong>", text)

    # blocks -----------------------------------------------------------
    def render(self, md, toc=True):
        lines = md.replace("\r\n", "\n").split("\n")
        out = []
        i = 0
        while i < len(lines):
            s = lines[i].strip()
            n = i + 1
            if not s:
                i += 1
                continue
            if s.startswith(("```", ">", "<")) or re.match(r"#(?!#)|#{4,}", s):
                raise PageError(f"line {n}: not in the allowed Markdown: {s[:40]!r}")
            m = re.match(r"(#{2,3}) (.+)$", s)
            if m:
                out.append(self._heading(len(m.group(1)), m.group(2), toc))
                i += 1
                continue
            if s.startswith(":::"):
                name = s[3:].strip()
                if name not in BOXES:
                    raise PageError(f"line {n}: unknown box {name!r} (use {sorted(BOXES)})")
                j = i + 1
                while j < len(lines) and lines[j].strip() != ":::":
                    j += 1
                if j == len(lines):
                    raise PageError(f"line {n}: box :::{name} is not closed")
                inner = Renderer(self.lang, self.slugs, self.facts_fn, box_titles=self.box_titles,
                                 existing=self.existing)
                inner._lide = True
                body = inner.render("\n".join(lines[i + 1:j]), toc=False)
                self.links += inner.links
                out.append(f'<aside class="box box-{name}"><p class="box-title">{html.escape(self.box_titles.get(name, ""))}</p>{body}</aside>')
                i = j + 1
                continue
            m = FACTS_RE.match(s)
            if m:
                if not self.facts_fn:
                    raise PageError(f"line {n}: {{{{factos}}}} is not allowed here")
                attrs = dict(a.split("=", 1) for a in m.group(1).split())
                out.append(self.facts_fn(attrs))
                i += 1
                continue
            if s.startswith("{{"):
                raise PageError(f"line {n}: bad marker {s!r} (use {{{{factos kind=... estado=...}}}})")
            if s.startswith("|"):
                j = i
                while j < len(lines) and lines[j].strip().startswith("|"):
                    j += 1
                out.append(self._table(lines[i:j], n))
                i = j
                continue
            if re.match(r"(- |\d+\. )", s):
                i = self._list(lines, i, out)
                continue
            j = i
            para = []
            while j < len(lines) and lines[j].strip() and not re.match(r"(#{2,3} |:::|\||- |\d+\. |\{\{)", lines[j].strip()):
                para.append(lines[j].strip())
                j += 1
            cls = ""
            if not self._lide:
                cls, self._lide = ' class="lide"', True
            out.append(f"<p{cls}>{self.inline(' '.join(para))}</p>")
            i = j
        return "\n".join(out)

    def _heading(self, level, text, toc):
        m = re.match(r"^(.*?)\s*\{#([a-z0-9-]+)\}$", text)
        if m:
            text, base = m.group(1), m.group(2)
            if base in self._ids:
                raise PageError(f"heading id {base!r} is used twice")
        else:
            base = slugify(text)
        hid, k = base, 2
        while hid in self._ids:
            hid, k = f"{base}-{k}", k + 1
        self._ids.add(hid)
        inner = self.inline(text)
        if toc and level == 2:
            self.headings.append((hid, inner))
        return f'<h{level} id="{hid}">{inner}</h{level}>'

    def _list(self, lines, i, out):
        ordered = bool(re.match(r"\d+\. ", lines[i].strip()))
        marker = r"\d+\. " if ordered else r"- "
        items = []
        while i < len(lines):
            raw = lines[i]
            s = raw.strip()
            if not s:
                break
            if re.match(marker, s) and not raw.startswith(" "):
                items.append([re.sub("^" + marker, "", s)])
            elif raw.startswith(" ") and items:
                if re.match(r"(- |\d+\. )", s):
                    raise PageError(f"line {i + 1}: nested lists are not allowed")
                items[-1].append(s)
            else:
                break
            i += 1
        tag = "ol" if ordered else "ul"
        lis = "".join(f"<li>{self.inline(' '.join(it))}</li>" for it in items)
        out.append(f"<{tag}>{lis}</{tag}>")
        return i

    def _table(self, rows, n):
        cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
        if len(cells) < 3 or not all(re.match(r"^:?-{3,}:?$", c) for c in cells[1]):
            raise PageError(f"line {n}: a table needs a header, a |---| line and at least one row")
        width = len(cells[0])
        if any(len(r) != width for r in cells):
            raise PageError(f"line {n}: every table row needs {width} cells")
        head = "".join(f"<th>{self.inline(c)}</th>" for c in cells[0])
        body = "".join("<tr>" + "".join(f"<td>{self.inline(c)}</td>" for c in r) + "</tr>" for r in cells[2:])
        return f'<div class="table"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


# ---------------------------------------------------------------- the skill's "## Fontes"

def fontes_md(name):
    """The "## Fontes" section of a skill, kept as a list of sources: the ### headings, the items,
    and the short lead-ins that end in ":" ("Da DGEG …, verificado a …:"). Other paragraphs are notes
    to the assistant ("Cita a UVE quando…") and are dropped."""
    text = skill_text(name)
    start = text.find("\n## Fontes\n")
    if start < 0:
        return ""
    rest = text[start + len("\n## Fontes\n"):]
    nxt = re.search(r"^## ", rest, re.M)
    if nxt:
        rest = rest[:nxt.start()]
    keep = []
    for block in re.split(r"\n\s*\n", rest.strip()):
        b = block.strip()
        if b.startswith("### "):
            first, _, after = b.partition("\n")
            keep.append(first)
            b = after.strip()
            if not b:
                continue
        if b.startswith("- "):
            keep.append("\n".join(_fonte_item(it) for it in re.split(r"\n(?=- )", b)))
        elif b.endswith(":"):
            keep.append(b)
    return "\n\n".join(keep)


def _fonte_item(item):
    """"- Label: https://url" becomes a link with the label as its text. The "[DGEG, guia técnico]"
    markers point the assistant to inline citations the pages don't have, so they go; an item that is
    only a marker and a URL keeps the marker as its text."""
    text = " ".join(l.strip() for l in item[2:].split("\n"))
    marker = None
    m = re.match(r"^\[([^\]]+)\]\s*(.*)$", text)
    if m:
        marker, text = m.group(1), m.group(2)
    m = re.match(r"^(.*?):?\s*(https://\S+)$", text)
    if m and "https://" not in m.group(1):
        label = m.group(1).strip() or marker or m.group(2)
        label = label.replace("[", "(").replace("]", ")")
        return f"- [{label}]({m.group(2)})"
    return "- " + text
