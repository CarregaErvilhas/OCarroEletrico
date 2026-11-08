#!/usr/bin/env python3
"""Regenerates the raster images from the SVG drawings in site/base.html and site/static/icon.svg:
site/static/og.png (1200x630, link previews), apple-touch-icon.png (180) and favicon.ico (48).
Needs Playwright and Pillow, which the build does not: run it by hand when the mascot or icon changes
and commit the PNG/ICO."""
import base64, io, os, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "site" / "static"
base = (ROOT / "site" / "base.html").read_text(encoding="utf-8")
reporter = re.search(r'<symbol id="reporter"[^>]*>(.*?)</symbol>', base, re.S).group(1)
grad = re.search(r'<linearGradient id="shineC".*?</linearGradient>', base, re.S).group(0)
icon = (STATIC / "icon.svg").read_text(encoding="utf-8")
font = "data:font/woff2;base64," + base64.b64encode((STATIC / "fonts" / "nunito-latin.woff2").read_bytes()).decode()

OG = f"""<style>@font-face{{font-family:N;src:url({font}) format("woff2");font-weight:400 900}}
body{{margin:0;width:1200px;height:630px;background:#fbfaf5;font-family:N;color:#14203a;position:relative;overflow:hidden}}
.blob{{position:absolute;right:70px;top:80px;width:470px;height:470px;border-radius:50%;background:radial-gradient(circle at 38% 34%,#fdf3c4,#ffe4d6 70%)}}
svg{{position:absolute;right:120px;top:90px;width:400px;height:445px}}
h1{{position:absolute;left:80px;top:170px;margin:0;font-size:92px;line-height:1.02;font-weight:900;letter-spacing:-2px;width:600px}}
p{{position:absolute;left:80px;top:430px;margin:0;font-size:34px;line-height:1.3;width:610px;color:#56627a;font-weight:600}}</style>
<div class="blob"></div>
<svg viewBox="0 0 270 300"><defs>{grad}</defs>{reporter}</svg>
<h1>O Carro Elétrico</h1><p>Carro elétrico em Portugal, sem mitos.</p>"""

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    pg.set_content(OG); pg.evaluate("document.fonts.ready.then(() => document.fonts.size)"); pg.wait_for_timeout(300)
    pg.screenshot(path=str(STATIC / "og.png"))
    def render(size):
        p = b.new_page(viewport={"width": size, "height": size})
        p.set_content(f'<body style="margin:0;background:#fbfaf5;display:grid;place-items:center;width:{size}px;height:{size}px">'
                      + icon.replace("<svg ", f'<svg width="{int(size*.8)}" height="{int(size*.68)}" ', 1))
        data = p.screenshot(); p.close(); return Image.open(io.BytesIO(data)).convert("RGB")
    render(180).save(STATIC / "apple-touch-icon.png", optimize=True)
    render(96).resize((48, 48), Image.LANCZOS).save(STATIC / "favicon.ico", sizes=[(48, 48)])
    b.close()
print("og.png, apple-touch-icon.png, favicon.ico written to", STATIC)
