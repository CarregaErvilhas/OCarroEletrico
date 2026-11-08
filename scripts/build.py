#!/usr/bin/env python3
"""Builds ocarroeletrico.com into _site/ (or --out DIR). pages.yml publishes it on GitHub Pages.

- content/<lang>/<skill>.md: the prose for people, written by the agent from Voltaria's skill
  (agent/SYSTEM.md). One page per published skill, Portuguese at /<skill>/, English at /en/<skill>/.
- {{factos ...}} lines become the facts from voltaria/knowledge/incentives.json, as of the build
  date. Amounts and dates never come from the agent.
- The "Fontes" of each page come from the skill's "## Fontes".
- site/base.html is the one template, site/strings.json the site's own text in pt and en.
- Also: the home page per language, 404.html, sitemap.xml, robots.txt, llms.txt, site/static/.

Usage: scripts/build.py [--out DIR] [--today YYYY-MM-DD]   (stdlib only; run from anywhere)
"""
import argparse
import html
import json
import re
import shutil
import sys
import datetime as dt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import oce  # noqa: E402

SITE = oce.ROOT / "site"
KEY_RE = re.compile(r"\{\{([\w.-]+)\}\}")
OG_LOCALE = {"pt": "pt_PT", "en": "en_GB"}
HTML_LANG = {"pt": "pt-PT", "en": "en"}


def esc(s):
    return html.escape(s, quote=True)


def lang_prefix(lang):
    return "" if lang == "pt" else "/en"


def url_for(lang, slug=None):
    path = f"{lang_prefix(lang)}/" + (f"{slug}/" if slug else "")
    return oce.SITE_URL + path


class Site:
    def __init__(self, out, today):
        self.out = out
        self.today = today
        self.strings = json.loads((SITE / "strings.json").read_text(encoding="utf-8"))
        self.template = (SITE / "base.html").read_text(encoding="utf-8")
        self.facts = oce.facts()
        self.vdate = oce.voltaria_date()
        self.pages = {lang: oce.pages(lang) for lang in oce.LANGS}
        self.meta = {lang: {s: oce.load_page(lang, s)[0] for s in self.pages[lang]} for lang in oce.LANGS}
        self.news = {lang: oce.news(lang) for lang in oce.LANGS}
        self.sitemap = {}
        self.anchors = {}

    def s(self, lang, key, **kw):
        text = self.strings[lang][key]
        for k, v in kw.items():
            text = text.replace("{" + k + "}", v)
        return text

    # ------------------------------------------------------------ the frame
    def render(self, lang, main, *, title, desc, slug=None, jsonld, og_type="website", robots=""):
        canonical = url_for(lang, slug) if slug != "404" else oce.SITE_URL + "/404.html"
        has = lambda l, x: x is None or x in self.pages[l] or x == "novidades"  # noqa: E731
        both = slug == "404" or all(has(l, slug) for l in oce.LANGS)
        if slug == "404":
            alternates = ""
        else:
            alternates = "\n".join(
                f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url_for(l, slug)}">'
                for l in oce.LANGS if has(l, slug))
            if both:
                alternates += f'\n<link rel="alternate" hreflang="x-default" href="{url_for("pt", slug)}">'
        other_slug = None if slug in (None, "404") else slug
        P = {
            "page.lang": HTML_LANG[lang],
            "page.title": esc(title),
            "page.desc": esc(desc),
            "page.robots": robots,
            "page.canonical": canonical,
            "page.alternates": alternates,
            "page.og.type": og_type,
            "page.og.locale": OG_LOCALE[lang],
            "page.jsonld": json.dumps(jsonld, ensure_ascii=False).replace("<", "\\u003c"),
            "page.home": f"{lang_prefix(lang)}/",
            "page.href.pt": "/" + (f"{other_slug}/" if other_slug and has("pt", other_slug) else ""),
            "page.href.en": "/en/" + (f"{other_slug}/" if other_slug and has("en", other_slug) else ""),
            "page.feed": f'<link rel="alternate" type="application/atom+xml" href="{lang_prefix(lang)}/novidades/feed.xml" title="{esc(self.s(lang, "news.title"))}">',
            "page.current.pt": 'aria-current="page"' if lang == "pt" else "",
            "page.current.en": 'aria-current="page"' if lang == "en" else "",
            "page.credit": self.s(lang, "foot.credit", date=oce.fmt_date(self.vdate, lang)),
            "page.main": main,
        }

        def fill(m):
            key = m.group(1)
            if key.startswith("s."):
                if key[2:] not in self.strings[lang]:
                    raise SystemExit(f"base.html: no string {key[2:]!r} in {lang}")
                return self.strings[lang][key[2:]]
            if key not in P:
                raise SystemExit(f"base.html: unknown key {key!r}")
            return P[key]

        return KEY_RE.sub(fill, self.template)

    def write(self, rel, text):
        path = self.out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    # ------------------------------------------------------------ facts
    def facts_html(self, lang, attrs):
        if "id" in attrs:
            if set(attrs) != {"id"}:
                raise oce.PageError("{{factos id=...}} takes no other attributes")
            match = [e for e in self.facts if e["id"] == attrs["id"]]
            if not match:
                raise oce.PageError(f"{{{{factos}}}}: no fact with id {attrs['id']!r}")
            return f'<div class="facts">{self.fact_card(lang, match[0])}</div>'
        kind = attrs.get("kind")
        if kind not in oce.FACT_KINDS:
            raise oce.PageError(f"{{{{factos}}}}: kind must be one of {sorted(oce.FACT_KINDS)}, not {kind!r}")
        estado = attrs.get("estado", "aberto")
        if estado not in oce.FACT_STATES:
            raise oce.PageError(f"{{{{factos}}}}: estado must be one of {sorted(oce.FACT_STATES)}, not {estado!r}")
        extra = set(attrs) - {"kind", "estado", "series"}
        if extra:
            raise oce.PageError(f"{{{{factos}}}}: unknown attributes {sorted(extra)}")
        today = self.today
        series = attrs.get("series")
        if series and not any(e.get("series") == series for e in self.facts):
            raise oce.PageError(f"{{{{factos}}}}: no fact has series {series!r}")
        rows = [e for e in self.facts if e["kind"] == kind
                and (not series or e.get("series") == series)
                and (estado == "todos" or oce.fact_state(e, today) == estado)]
        if estado == "fechado":
            rows.sort(key=lambda e: e.get("validTo") or "", reverse=True)
        D = lambda iso: oce.fmt_date(iso, lang)  # noqa: E731
        asof = f'<p class="facts-asof">{esc(self.s(lang, "facts.asof", date=D(today)))}</p>'
        if not rows:
            return f'<p class="facts-none">{esc(self.s(lang, "facts.none." + estado, date=D(today)))}</p>'
        if kind == "municipal":
            head = "".join(f"<th>{esc(self.s(lang, 'facts.mun.' + k))}</th>" for k in ("municipio", "beneficio", "detalhe", "oficial"))
            body = ""
            for e in sorted(rows, key=lambda e: e["municipality"]):
                off = e.get("official") or {}
                link = f'<a href="{esc(off["url"])}" rel="noopener">{esc(off.get("name", "") or off["url"])}</a>' if off.get("url") else ""
                body += (f"<tr><td><strong>{esc(e['municipality'])}</strong></td>"
                         f"<td>{esc(self.s(lang, 'facts.benefit.' + e['benefit']))}</td>"
                         f"<td>{esc(e['text'][lang])}</td><td>{link}</td></tr>")
            src = rows[0]["source"]
            checked = max(e["checkedAt"] for e in rows)
            note = self.s(lang, "facts.mun.source", name=f'<a href="{esc(src["url"])}" rel="noopener">{esc(src["name"].split(",")[0])}</a>', date=D(checked))
            return (f'{asof}<div class="table"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
                    f'<p class="fact-meta">{note}</p>')
        items = [self.fact_card(lang, e) for e in rows]
        return f'{asof}<div class="facts">{"".join(items)}</div>'

    def fact_card(self, lang, e):
        today = self.today
        D = lambda iso: oce.fmt_date(iso, lang)  # noqa: E731
        state = oce.fact_state(e, today)
        tag = ""
        if state == "fechado":
            tag = self.s(lang, "facts.closed", date=D(e["validTo"]))
        elif state == "anunciado" and not e["text"][lang].lower().startswith(("anunciado", "announced")):
            tag = self.s(lang, "facts.announced")
        elif state == "futuro":
            tag = self.s(lang, "facts.future", date=D(e["validFrom"]))
        stale = state == "aberto" and (dt.date.fromisoformat(today) - dt.date.fromisoformat(e["checkedAt"])).days > oce.STALE_DAYS
        if stale:
            tag = self.s(lang, "facts.stale")
        tag_html = f'<span class="fact-tag">{esc(tag)}</span>' if tag else ""
        cls = " closed" if state == "fechado" else ""
        src = e["source"]
        return (f'<article class="fact{cls}">{tag_html}<p>{esc(e["text"][lang])}</p>'
                f'<p class="fact-meta">{esc(self.s(lang, "facts.source"))}: <a href="{esc(src["url"])}" rel="noopener">{esc(src["name"])}</a>'
                f' · {esc(self.s(lang, "facts.checked", date=D(e["checkedAt"])))}</p></article>')

    # ------------------------------------------------------------ pages
    def group_of(self, slug):
        return next(g for g, slugs in oce.GROUPS if slug in slugs)

    def article(self, lang, slug):
        fields, body = oce.load_page(lang, slug)
        r = oce.Renderer(lang, oce.published(), facts_fn=lambda a: self.facts_html(lang, a),
                         box_titles={b: self.s(lang, "box." + b) for b in oce.BOXES},
                         existing=self.pages[lang])
        try:
            prose = r.render(body)
        except oce.PageError as e:
            raise SystemExit(f"content/{lang}/{slug}.md: {e}")
        self.anchors[(lang, slug)] = (set(r.ids), list(r.links))
        fr = oce.Renderer(lang, oce.published(), autolink=True, existing=self.pages[lang])
        fr._lide = True
        fontes = fr.render(oce.fontes_md(slug), toc=False)
        toc = "".join(f'<li><a href="#{hid}">{text}</a></li>' for hid, text in r.headings)
        group = self.group_of(slug)
        tools = "".join(
            f'<li><a href="{oce.TOOLS[t]}"><b>{self.s(lang, f"tool.{t}.name")}</b><span>{self.s(lang, f"tool.{t}.desc")}</span></a></li>'
            for t in oce.PAGE_TOOLS.get(slug, ["ohmigo"]))
        updated = fields.get("updated") or self.today
        main = f"""<article>
<div class="wrap">
  <header class="art-head">
    <a class="eyebrow" href="{lang_prefix(lang)}/#{group}">{self.s(lang, "group." + group)}</a>
    <h1>{esc(fields["title"])}</h1>
    <p class="meta">{esc(self.s(lang, "art.updated", date=oce.fmt_date(updated, lang)))} · <a href="{oce.VOLTARIA_URL}/blob/main/skills/{slug}/SKILL.md">{self.s(lang, "art.based")}</a></p>
  </header>
  <div class="art-grid">
    <nav class="toc" aria-label="{esc(self.s(lang, "art.toc"))}"><b>{self.s(lang, "art.toc")}</b><ol>{toc}</ol></nav>
    <div class="prose">
{prose}
    </div>
  </div>
  <aside class="art-tools">
    <h2>{self.s(lang, "art.tools")}</h2>
    <p>{self.s(lang, "art.tools.lead")}</p>
    <ul>{tools}</ul>
  </aside>
  <a class="back" href="{lang_prefix(lang)}/#temas">← {self.s(lang, "art.home")}</a>
</div>
<section class="fontes" id="fontes">
  <div class="wrap"><div class="fontes-inner">
    <h2>{self.s(lang, "art.fontes")}</h2>
    <p>{self.s(lang, "art.fontes.note")}</p>
{fontes}
  </div></div>
</section>
</article>"""
        jsonld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": fields["title"],
            "description": fields["description"],
            "inLanguage": HTML_LANG[lang],
            "dateModified": updated,
            "url": url_for(lang, slug),
            "isBasedOn": f"{oce.VOLTARIA_URL}/blob/main/skills/{slug}/SKILL.md",
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "publisher": {"@type": "Organization", "name": "O Carro Elétrico", "url": oce.SITE_URL},
        }
        page = self.render(lang, main, title=f'{fields["title"]} | O Carro Elétrico', desc=fields["description"],
                           slug=slug, jsonld=jsonld, og_type="article")
        self.write(f"{lang_prefix(lang).lstrip('/')}/{slug}/index.html".lstrip("/"), page)
        self.sitemap[slug] = max(updated, self.sitemap.get(slug, ""))

    def home(self, lang):
        S = lambda k: self.s(lang, k)  # noqa: E731
        groups = ""
        for g, slugs in oce.GROUPS:
            cards = ""
            for slug in slugs:
                m = self.meta[lang].get(slug)
                if m:
                    cards += (f'<li class="topic"><a href="{lang_prefix(lang)}/{slug}/"><b>{esc(m["title"])}</b>'
                              f'<span>{esc(m["description"])}</span></a></li>')
            if not cards:
                continue
            groups += f'<div class="group" id="{g}"><h3>{S("group." + g)}</h3><ul class="topics">{cards}</ul></div>'
        tools = "".join(
            f'<li class="tool {t}"><a href="{u}"><b>{S(f"tool.{t}.name")}</b><span>{S(f"tool.{t}.desc")}</span><i>{S("tool.open")} →</i></a></li>'
            for t, u in oce.TOOLS.items())
        main = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <span class="eyebrow">{S("hero.eyebrow")}</span>
      <h1>{S("hero.title")}</h1>
      <p class="lead">{S("hero.lead")}</p>
      <div class="ctas">
        <a class="btn btn-main" href="#temas">{S("hero.cta1")}</a>
        <a class="btn btn-go" href="{oce.TOOLS["ohmigo"]}">{S("hero.cta2")}</a>
      </div>
    </div>
    <div class="stage">
      <div class="blob"></div>
      <svg class="mascot" viewBox="0 0 270 300" role="img" aria-label="{esc(S("mascot.alt"))}"><use href="#reporter"/></svg>
      <p class="bubble">{S("hero.bubble")}</p>
    </div>
  </div>
</section>
<section class="alt" id="temas">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{S("temas.eyebrow")}</span><h2>{S("temas.title")}</h2><p class="lead">{S("temas.lead")}</p></div>
    {groups}
  </div>
</section>
{self.news_home(lang)}<section id="ferramentas">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{S("tools.eyebrow")}</span><h2>{S("tools.title")}</h2><p class="lead">{S("tools.lead")}</p></div>
    <ul class="tools">{tools}</ul>
  </div>
</section>
<section class="alt" id="sobre">
  <div class="wrap sobre">
    <span class="eyebrow">{S("sobre.eyebrow")}</span>
    <h2>{S("sobre.title")}</h2>
    <p class="lead">{S("sobre.text")}</p>
    <div class="ctas">
      <a class="btn btn-main" href="https://m.me/OCarroEletricoDotCom">{S("sobre.messenger")}</a>
      <a class="btn" href="mailto:info@ocarroeletrico.com">{S("sobre.email")}</a>
    </div>
  </div>
</section>"""
        jsonld = {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "O Carro Elétrico",
            "url": url_for(lang),
            "inLanguage": HTML_LANG[lang],
            "description": S("meta.home.desc"),
            "publisher": {"@type": "Organization", "name": "O Carro Elétrico", "url": oce.SITE_URL,
                          "email": "info@ocarroeletrico.com"},
        }
        page = self.render(lang, main, title=S("meta.home.title"), desc=S("meta.home.desc"), jsonld=jsonld)
        self.write(f"{lang_prefix(lang).lstrip('/')}/index.html".lstrip("/"), page)

    # ------------------------------------------------------------ news
    def news_items(self, lang):
        """(slug, fields, html) of every brief, rendered once for the page, the feed and the home."""
        cache = self.__dict__.setdefault("_news_html", {})
        if lang not in cache:
            out = []
            for slug, fields, body in self.news[lang]:
                for key in ("title", "date"):
                    if not fields.get(key):
                        raise SystemExit(f"content/{lang}/novidades/{slug}.md: frontmatter has no {key!r}")
                r = oce.Renderer(lang, oce.published(), facts_fn=lambda a: self.facts_html(lang, a),
                                 box_titles={b: self.s(lang, "box." + b) for b in oce.BOXES},
                                 existing=self.pages[lang])
                r._lide = True
                try:
                    html_body = r.render(body, toc=False)
                except oce.PageError as e:
                    raise SystemExit(f"content/{lang}/novidades/{slug}.md: {e}")
                if "<h2" in html_body or "<h3" in html_body:
                    raise SystemExit(f"content/{lang}/novidades/{slug}.md: a brief has no headings")
                self.anchors[(lang, f"novidades/{slug}")] = (set(), list(r.links))
                out.append((slug, fields, html_body))
            cache[lang] = out
        return cache[lang]

    def news_page(self, lang):
        S = lambda k: self.s(lang, k)  # noqa: E731
        items = "".join(
            f'<article class="brief" id="{slug}"><p class="meta"><time datetime="{f["date"]}">{oce.fmt_date(f["date"], lang)}</time></p>'
            f'<h2><a href="#{slug}">{esc(f["title"])}</a></h2><div class="prose">{h}</div></article>'
            for slug, f, h in self.news_items(lang))
        main = f"""<div class="wrap news">
  <header class="art-head">
    <span class="eyebrow">{S("nav.novidades")}</span>
    <h1>{S("news.title")}</h1>
    <p class="lead">{S("news.lead")}</p>
    <p class="meta"><a href="{lang_prefix(lang)}/novidades/feed.xml">{S("news.feed")}</a></p>
  </header>
  <div class="briefs">{items}</div>
  <a class="back" href="{lang_prefix(lang)}/#temas">← {S("art.home")}</a>
</div>"""
        jsonld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": S("news.title"),
                  "url": url_for(lang, "novidades"), "inLanguage": HTML_LANG[lang]}
        page = self.render(lang, main, title=f'{S("news.title")} | O Carro Elétrico', desc=S("news.lead"),
                           slug="novidades", jsonld=jsonld)
        prefix = lang_prefix(lang).lstrip("/")
        self.write(f"{prefix}/novidades/index.html".lstrip("/"), page)
        self.write(f"{prefix}/novidades/feed.xml".lstrip("/"), self.feed(lang))
        items = self.news_items(lang)
        if items:
            self.sitemap["novidades"] = max(items[0][1]["date"], self.sitemap.get("novidades", ""))

    def feed(self, lang):
        """Atom feed of the briefs, full text, absolute links."""
        base = url_for(lang, "novidades")
        items = self.news_items(lang)
        entries = []
        for slug, f, h in items:
            body = re.sub(r'href="/', f'href="{oce.SITE_URL}/', h)
            entries.append(
                f"<entry><id>tag:ocarroeletrico.com,{f['date']}:{lang}/novidades/{slug}</id>"
                f"<title>{esc(f['title'])}</title><link href=\"{base}#{slug}\"/>"
                f"<updated>{f['date']}T00:00:00Z</updated><content type=\"html\">{esc(body)}</content></entry>")
        updated = (items[0][1]["date"] if items else self.vdate) + "T00:00:00Z"
        return ('<?xml version="1.0" encoding="utf-8"?>\n'
                f'<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="{HTML_LANG[lang]}">\n'
                f"<title>O Carro Elétrico: {esc(self.s(lang, 'news.title'))}</title>"
                f'<link href="{base}"/><link rel="self" href="{base}feed.xml"/>'
                f"<id>{base}</id><updated>{updated}</updated><author><name>O Carro Elétrico</name></author>\n"
                + "\n".join(entries) + "\n</feed>\n")

    def news_home(self, lang):
        items = self.news_items(lang)[:3]
        if not items:
            return ""
        S = lambda k: self.s(lang, k)  # noqa: E731
        lis = "".join(
            f'<li><a href="{lang_prefix(lang)}/novidades/#{slug}"><time datetime="{f["date"]}">{oce.fmt_date(f["date"], lang)}</time>'
            f'<b>{esc(f["title"])}</b></a></li>' for slug, f, _ in items)
        return f"""<section id="novidades">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{S("nav.novidades")}</span><h2>{S("news.home.title")}</h2></div>
    <ul class="news-list">{lis}</ul>
    <p class="more"><a href="{lang_prefix(lang)}/novidades/">{S("news.all")} →</a></p>
  </div>
</section>
"""

    def not_found(self):
        parts = []
        for lang in oce.LANGS:
            parts.append(f'<div lang="{HTML_LANG[lang]}" class="head"><h2>{self.s(lang, "404.title")}</h2>'
                         f'<p class="lead">{self.s(lang, "404.text")}</p>'
                         f'<div class="ctas"><a class="btn btn-main" href="{lang_prefix(lang)}/">{self.s(lang, "404.home")}</a></div></div>')
        main = (f'<section><div class="wrap hero-grid"><div class="hero-text">{"".join(parts)}</div>'
                f'<div class="stage"><div class="blob"></div><svg class="mascot" viewBox="0 0 270 300" aria-hidden="true"><use href="#reporter"/></svg></div></div></section>')
        page = self.render("pt", main, title="404 | O Carro Elétrico", desc=self.s("pt", "404.text"), slug="404",
                           jsonld={"@context": "https://schema.org", "@type": "WebPage", "name": "404"},
                           robots='<meta name="robots" content="noindex">')
        self.write("404.html", page)

    def extras(self):
        urls = [(None, self.vdate)] + sorted(self.sitemap.items())
        rows = []
        for slug, mod in urls:
            for lang in oce.LANGS:
                if slug and slug not in self.pages[lang]:
                    continue
                alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url_for(l, slug)}"/>'
                               for l in oce.LANGS if slug is None or slug in self.pages[l])
                rows.append(f"<url><loc>{url_for(lang, slug)}</loc><lastmod>{mod}</lastmod>{alts}</url>")
        self.write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
                   + "\n".join(rows) + "\n</urlset>\n")
        self.write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {oce.SITE_URL}/sitemap.xml\n")
        lines = ["# O Carro Elétrico", "",
                 "> Electric mobility in Portugal for people: charging at home and on the road, condos, installation, "
                 "grants and tax, with the law and sources behind every fact. pt-PT at /, English at /en/.", "",
                 f"Content is adapted from Voltaria ({oce.VOLTARIA_URL}, CC-BY-4.0). For prices and live charger data, "
                 "use the ohmigo MCP server: https://ohmigo.ocarroeletrico.com/mcp", "", "## Pages", ""]
        for lang in oce.LANGS:
            for slug in self.pages[lang]:
                m = self.meta[lang][slug]
                lines.append(f"- [{m['title']}]({url_for(lang, slug)}) ({lang}): {m['description']}")
        self.write("llms.txt", "\n".join(lines) + "\n")

    def check_anchors(self):
        """Every /<slug>/#id link points to a heading that exists on that page, in that language."""
        bad = []
        for (lang, slug), (_, links) in self.anchors.items():
            for url in links:
                m = oce.INTERNAL_RE.match(url)
                target, frag = m.group(1) or None, (m.group(2) or "")[1:]
                if not frag:
                    continue
                if target is None:
                    bad.append(f"content/{lang}/{slug}.md: #{frag} on the home page")
                elif (lang, target) in self.anchors and frag not in self.anchors[(lang, target)][0]:
                    bad.append(f"content/{lang}/{slug}.md: {url} has no heading with id {frag!r}")
        if bad:
            raise SystemExit("; ".join(bad))

    def build(self):
        if self.out.exists():
            shutil.rmtree(self.out)
        shutil.copytree(SITE / "static", self.out)
        for lang in oce.LANGS:
            for slug in self.pages[lang]:
                self.article(lang, slug)
            self.news_page(lang)
            self.home(lang)
        self.not_found()
        self.extras()
        self.check_anchors()
        n = sum(len(v) for v in self.pages.values())
        print(f"built {self.out}: {n} pages + 2 home pages, Voltaria {oce.voltaria_commit()[:7]} ({self.vdate}), facts as of {self.today}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(oce.ROOT / "_site"))
    ap.add_argument("--today", default=dt.date.today().isoformat(), help="date for open/closed facts")
    a = ap.parse_args()
    Site(Path(a.out).resolve(), a.today).build()


if __name__ == "__main__":
    main()
