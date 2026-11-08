#!/usr/bin/env python3
"""Checks the site's links against a build: internal ones (files and #anchors) in --site DIR, and
external ones over HTTP. Stdlib only. Usage:
    scripts/build.py --out _site && scripts/check_links.py --site _site [--no-external]
Exits 1 if an internal link or anchor is broken. External links only warn: a server that refuses
robots answers 403 without being broken."""
import argparse, html.parser, pathlib, sys, urllib.parse, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

class P(html.parser.HTMLParser):
    def __init__(s):
        super().__init__(); s.links = []; s.ids = set()
    def handle_starttag(s, tag, a):
        a = dict(a)
        if a.get("id"): s.ids.add(a["id"])
        if tag == "a" and a.get("name"): s.ids.add(a["name"])
        for k in ("href", "src"):
            if a.get(k): s.links.append(a[k])

def target(root, base, href):
    u = urllib.parse.urlsplit(urllib.parse.urljoin(base, href))
    p = urllib.parse.unquote(u.path)
    f = root / p.lstrip("/")
    if f.is_dir(): f = f / "index.html"
    return f, urllib.parse.unquote(u.fragment)

def external(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link-check)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r: return url, r.status
    except urllib.error.HTTPError as e: return url, e.code
    except Exception as e: return url, str(e)[:60]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--site", required=True)
    ap.add_argument("--no-external", action="store_true"); a = ap.parse_args()
    root = pathlib.Path(a.site).resolve(); bad = []; ext = set(); parsed = {}
    for f in root.rglob("*.html"):
        p = P(); p.feed(f.read_text(errors="ignore")); parsed[f] = p
    for f, p in parsed.items():
        base = "/" + str(f.relative_to(root))
        for h in p.links:
            if h.startswith(("mailto:", "tel:", "data:", "javascript:")): continue
            if h.startswith(("http://", "https://")):
                if urllib.parse.urlsplit(h).hostname != "ocarroeletrico.com": ext.add(h)
                continue
            t, frag = target(root, base, h)
            if not t.exists(): bad.append(f"{base}: {h} (file does not exist)"); continue
            if frag and t in parsed and frag not in parsed[t].ids: bad.append(f"{base}: {h} (anchor does not exist)")
    for b in sorted(bad): print("BROKEN", b)
    if not a.no_external:
        with ThreadPoolExecutor(8) as ex:
            for url, st in sorted(ex.map(external, sorted(ext))):
                if st != 200: print("EXTERNAL", st, url)
    print(f"{len(parsed)} pages, {len(bad)} broken internal links")
    return 1 if bad else 0
sys.exit(main())
