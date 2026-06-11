#!/usr/bin/env python3
"""Build a single self-contained HTML site from docs/wiki.

Usage: python3 docs/wiki-site/build.py
Output: docs/wiki-site/index.html

Requires pandoc on PATH (markdown -> HTML conversion).
"""

import posixpath
import re
import subprocess
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
OUT = Path(__file__).resolve().parent / "index.html"

SITE_TITLE = "The Claude Fable Starter Kit Wiki"

# (section label, [(relative path, slug, nav title), ...])
SECTIONS = [
    ("", [
        ("README.md", "home", "Home"),
    ]),
    ("Start here", [
        ("00-start-here/which-tool-when.md", "which-tool-when", "Which tool when"),
        ("00-start-here/quick-start.md", "quick-start", "Quick start"),
        ("00-start-here/managing-usage-and-cost.md", "managing-usage-and-cost", "Managing usage & cost"),
        ("00-start-here/glossary.md", "glossary", "Glossary"),
    ]),
    ("Claude Code basics", [
        ("01-claude-code-basics/installation-setup.md", "installation-setup", "Installation & setup"),
        ("01-claude-code-basics/claude-md-and-memory.md", "claude-md-and-memory", "CLAUDE.md & memory"),
        ("01-claude-code-basics/settings-and-permissions.md", "settings-and-permissions", "Settings & permissions"),
        ("01-claude-code-basics/slash-commands.md", "slash-commands", "Slash commands"),
    ]),
    ("Power features", [
        ("02-power-features/skills.md", "skills", "Skills"),
        ("02-power-features/subagents-and-orchestration.md", "subagents-and-orchestration", "Subagents & orchestration"),
        ("02-power-features/hooks.md", "hooks", "Hooks"),
        ("02-power-features/mcp.md", "mcp", "MCP"),
        ("02-power-features/claude-desktop.md", "claude-desktop", "Claude Desktop"),
    ]),
    ("Author workflows", [
        ("03-author-workflows/drafting-and-revision.md", "drafting-and-revision", "Drafting & revision"),
        ("03-author-workflows/research-and-worldbuilding.md", "research-and-worldbuilding", "Research & worldbuilding"),
        ("03-author-workflows/publishing-ops.md", "publishing-ops", "Publishing ops"),
        ("03-author-workflows/marketing-and-launch.md", "marketing-and-launch", "Marketing & launch"),
        ("03-author-workflows/adopting-and-sharing-tools.md", "adopting-and-sharing-tools", "Adopting & sharing tools"),
    ]),
    ("Reference", [
        ("04-reference/use-case-catalog.md", "use-case-catalog", "Use-case catalog"),
    ]),
]

PAGES = [(path, slug, title) for _, pages in SECTIONS for path, slug, title in pages]
# wiki-relative path -> slug, for cross-page link rewriting
PATH_TO_SLUG = {path: slug for path, slug, _ in PAGES}
# links to a section directory go to that section's first page
DIR_TO_SLUG = {posixpath.dirname(pages[0][0]): pages[0][1] for _, pages in SECTIONS}


def pandoc(md_path: Path) -> str:
    return subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html", "--wrap=none", str(md_path)],
        check=True, capture_output=True, text=True,
    ).stdout


def rewrite_page(html: str, page_rel: str, slug: str) -> str:
    page_dir = posixpath.dirname(page_rel)

    # Namespace ids so the same heading on two pages can't collide.
    html = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{slug}--{m.group(1)}"', html)

    def fix_href(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:")):
            return f'href="{href}" target="_blank" rel="noopener"'
        if href.startswith("#"):  # same-page anchor
            return f'href="#{slug}/{href[1:]}"'
        target, frag = (href.split("#", 1) + [""])[:2]
        resolved = posixpath.normpath(posixpath.join(page_dir, target))
        if resolved in PATH_TO_SLUG:
            tslug = PATH_TO_SLUG[resolved]
            return f'href="#{tslug}/{frag}"' if frag else f'href="#{tslug}"'
        if resolved in DIR_TO_SLUG:
            return f'href="#{DIR_TO_SLUG[resolved]}"'
        # Outside the wiki (e.g. ../../fable-documentation/...): point at the
        # repo file relative to docs/wiki-site/.
        repo_rel = posixpath.normpath(posixpath.join("..", "wiki", page_dir, href))
        return f'href="{repo_rel}"'

    html = re.sub(r'href="([^"]+)"', fix_href, html)

    # Collect h2s for the on-page TOC before anchor markup is injected.
    toc = [(hid.split("--", 1)[1], re.sub(r"<[^>]+>", "", inner))
           for hid, inner in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)]

    # Hover-revealed anchor links on h2/h3 for shareable deep links.
    def add_anchor(m):
        level, hid, inner = m.groups()
        frag = hid.split("--", 1)[1]
        return (f'<h{level} id="{hid}">{inner}'
                f'<a class="hanchor" href="#{slug}/{frag}" aria-label="Link to this section">#</a>'
                f'</h{level}>')

    html = re.sub(r'<h([23]) id="([^"]+)">(.*?)</h\1>', add_anchor, html)
    # Wide tables (the use-case catalog) need their own scrollbar.
    html = html.replace("<table>", '<div class="table-wrap"><table>')
    html = html.replace("</table>", "</table></div>")
    return html, toc


def validate(sections_html: dict):
    ids = set()
    for h in sections_html.values():
        ids.update(re.findall(r'\bid="([^"]+)"', h))
    bad = []
    for slug, h in sections_html.items():
        for href in re.findall(r'href="#([^"]+)"', h):
            page, _, frag = href.partition("/")
            if page not in PATH_TO_SLUG.values():
                bad.append((slug, href, "unknown page"))
            elif frag and f"{page}--{frag}" not in ids:
                bad.append((slug, href, "missing anchor"))
    for slug, href, why in bad:
        print(f"  warn: {slug} -> #{href} ({why})", file=sys.stderr)
    return bad


CSS = """
:root {
  --bg: #ffffff;
  --text: #161616;
  --muted: #6e6e6e;
  --faint: #9b9b9b;
  --hairline: #e7e7e7;
  --code-bg: #f5f5f5;
  --link: #a8471d;
  --panel: #fafafa;
  --quote-text: #3d3d3d;
  --nav-text: #3c3c3c;
  --nav-label: #767676;
  --sidebar-w: 252px;
  --font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #151515;
    --text: #e6e6e6;
    --muted: #a0a0a0;
    --faint: #828282;
    --hairline: #2c2c2c;
    --code-bg: #222222;
    --link: #e08e63;
    --panel: #1d1d1d;
    --quote-text: #c4c4c4;
    --nav-text: #cfcfcf;
    --nav-label: #8e8e8e;
    color-scheme: dark;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
:focus-visible { outline: 2px solid var(--link); outline-offset: 2px; }
[id] { scroll-margin-top: 24px; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 400 15.5px/1.65 -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", system-ui, sans-serif;
  letter-spacing: -0.006em;
}

/* ---- sidebar ---- */
nav {
  position: fixed;
  inset: 0 auto 0 0;
  width: var(--sidebar-w);
  overflow-y: auto;
  border-right: 1px solid var(--hairline);
  padding: 28px 20px 40px 28px;
}
nav .site-title {
  display: block;
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 600;
  line-height: 1.45;
  color: var(--text);
  text-decoration: none;
  margin-bottom: 6px;
}
nav .site-sub {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--nav-label);
  margin: 0 0 28px;
}
nav .section {
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--nav-label);
  margin: 26px 0 8px;
}
nav a.page {
  display: block;
  padding: 4px 0 4px 10px;
  margin-left: -12px;
  border-left: 2px solid transparent;
  font-size: 13.5px;
  color: var(--nav-text);
  text-decoration: none;
  transition: color 0.12s ease;
}
nav a.page:hover { color: var(--text); }
nav a.page.active { color: var(--text); font-weight: 600; border-left-color: var(--link); }

/* ---- content ---- */
main {
  margin-left: var(--sidebar-w);
  padding: 56px 56px 96px;
}
main > section { display: none; max-width: 42.5rem; }
main > section.active { display: block; }

h1 {
  font-size: 27px;
  font-weight: 650;
  letter-spacing: -0.022em;
  line-height: 1.2;
  margin: 0 0 20px;
}
h2 {
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -0.014em;
  line-height: 1.3;
  margin: 44px 0 12px;
  padding-top: 24px;
  border-top: 1px solid var(--hairline);
}
h3 { font-size: 16px; font-weight: 600; letter-spacing: -0.01em; margin: 30px 0 8px; }
h4 { font-size: 14.5px; font-weight: 600; margin: 24px 0 6px; }
p { margin: 0 0 14px; }
ul, ol { margin: 0 0 14px; padding-left: 22px; }
li { margin: 4px 0; }
li > ul, li > ol { margin-bottom: 0; }
hr { border: 0; border-top: 1px solid var(--hairline); margin: 36px 0; }

a {
  color: var(--link);
  text-decoration: underline;
  text-decoration-color: color-mix(in srgb, var(--link) 30%, transparent);
  text-underline-offset: 2.5px;
  transition: text-decoration-color 0.12s ease;
}
a:hover { text-decoration-color: currentColor; }

blockquote {
  margin: 0 0 18px;
  padding: 2px 0 2px 18px;
  border-left: 2px solid var(--text);
  color: var(--quote-text);
}
blockquote p:last-child { margin-bottom: 0; }
/* The "In plain words" opener every page leads with. */
h1 + blockquote {
  background: var(--panel);
  border: 1px solid var(--hairline);
  border-radius: 8px;
  padding: 16px 20px;
  margin-bottom: 28px;
}

.hanchor {
  margin-left: 8px;
  color: var(--faint);
  font-weight: 400;
  text-decoration: none;
  opacity: 0;
  transition: opacity 0.12s ease;
}
h2:hover .hanchor, h3:hover .hanchor, .hanchor:focus-visible { opacity: 1; }
.hanchor:hover { color: var(--link); }

code, kbd {
  font-family: var(--font-mono);
  font-size: 0.86em;
}
code { background: var(--code-bg); border-radius: 4px; padding: 1.5px 5px; }
pre {
  background: var(--code-bg);
  border-radius: 6px;
  padding: 14px 16px;
  overflow-x: auto;
  margin: 0 0 16px;
  line-height: 1.55;
}
pre code { background: none; padding: 0; font-size: 13px; }
kbd {
  background: var(--panel);
  border: 1px solid var(--hairline);
  border-bottom-width: 2px;
  border-radius: 4px;
  padding: 1px 5px;
  font-size: 0.8em;
}

.table-wrap { overflow-x: auto; margin: 0 0 18px; }
.table-wrap.fits { overflow: visible; }
table { border-collapse: separate; border-spacing: 0; width: 100%; font-size: 13.5px; line-height: 1.5; }
th {
  position: sticky;
  top: 0;
  z-index: 1;
  background: var(--bg);
  text-align: left;
  font-family: var(--font-mono);
  font-size: 10.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
  padding: 8px 14px 8px 0;
  box-shadow: inset 0 -1px 0 var(--text);
}
td {
  vertical-align: top;
  padding: 9px 14px 9px 0;
  border-bottom: 1px solid var(--hairline);
}
tbody tr:hover td { background: var(--panel); }

.pager {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  margin-top: 56px;
  padding-top: 20px;
  border-top: 1px solid var(--hairline);
  font-size: 13.5px;
}
.pager a { text-decoration: none; color: var(--text); max-width: 48%; }
.pager a:hover .pager-title { text-decoration: underline; }
.pager .label { display: block; font-family: var(--font-mono); font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--faint); margin-bottom: 3px; }
.pager .next { margin-left: auto; text-align: right; }

footer.colophon {
  margin-top: 28px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--faint);
}

/* ---- on-page TOC (wide screens only) ----
   Breakpoint is em-based and main reserves right padding so the fixed
   rail can never sit over the text column, whatever the root font size. */
.toc { display: none; }
@media (min-width: 80em) {
  main { padding-right: 268px; }
  .toc {
    display: block;
    position: fixed;
    top: 56px;
    right: 28px;
    width: 204px;
    max-height: calc(100vh - 112px);
    overflow-y: auto;
  }
  .toc-label {
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--nav-label);
    margin-bottom: 8px;
  }
  .toc a {
    display: block;
    padding: 3px 0 3px 10px;
    margin-left: -12px;
    border-left: 2px solid transparent;
    font-size: 12.5px;
    line-height: 1.45;
    color: var(--muted);
    text-decoration: none;
    transition: color 0.12s ease;
  }
  .toc a:hover { color: var(--text); }
  .toc a.active { color: var(--text); border-left-color: var(--link); }
}

.to-top {
  position: fixed;
  right: 28px;
  bottom: 28px;
  z-index: 2;
  padding: 7px 12px;
  background: var(--bg);
  border: 1px solid var(--hairline);
  border-radius: 6px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--muted);
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.12s ease, color 0.12s ease;
}
.to-top.show { opacity: 1; pointer-events: auto; }
.to-top:hover { color: var(--text); }

/* ---- small screens ---- */
.menu-toggle { display: none; }
@media (max-width: 880px) {
  .menu-toggle {
    display: block;
    position: fixed;
    top: 14px;
    right: 16px;
    z-index: 3;
    background: var(--bg);
    border: 1px solid var(--hairline);
    border-radius: 6px;
    padding: 6px 12px;
    font: 600 12.5px/1 inherit;
    font-family: inherit;
    color: var(--text);
    cursor: pointer;
  }
  nav {
    width: min(320px, 86vw);
    background: var(--bg);
    z-index: 2;
    transform: translateX(-100%);
    transition: transform 0.2s ease;
  }
  body.nav-open nav { transform: none; box-shadow: 8px 0 24px rgba(0,0,0,0.06); }
  main { margin-left: 0; padding: 56px 22px 80px; }
}
"""

JS = """
const sections = document.querySelectorAll('main > section');
const navLinks = document.querySelectorAll('nav a.page');

function route() {
  const raw = decodeURIComponent(location.hash.slice(1)) || 'home';
  const [slug, anchor] = raw.split('/');
  let found = false;
  sections.forEach(s => {
    const on = s.dataset.page === slug;
    s.classList.toggle('active', on);
    if (on) found = true;
  });
  if (!found) { location.hash = '#home'; return; }
  navLinks.forEach(a => a.classList.toggle('active', a.dataset.page === slug));
  const active = document.querySelector('nav a.page.active');
  document.title = (active && slug !== 'home' ? active.textContent + ' · ' : '') + SITE_TITLE;
  document.body.classList.remove('nav-open');
  // Tables that fit their column lose the scroll wrapper so sticky headers work.
  document.querySelectorAll('main > section.active .table-wrap:not([data-measured])').forEach(w => {
    w.dataset.measured = '1';
    if (w.scrollWidth <= w.clientWidth) w.classList.add('fits');
  });
  if (anchor) {
    const el = document.getElementById(slug + '--' + anchor);
    if (el) { el.scrollIntoView(); spy(); return; }
  }
  window.scrollTo(0, 0);
  spy();
}

const toTop = document.querySelector('.to-top');
function spy() {
  const sec = document.querySelector('main > section.active');
  if (!sec) return;
  let cur = null;
  sec.querySelectorAll('h2[id]').forEach(h => {
    if (h.getBoundingClientRect().top <= 96) cur = h;
  });
  const curHash = cur ? '#' + cur.id.replace('--', '/') : null;
  sec.querySelectorAll('.toc a').forEach(a =>
    a.classList.toggle('active', a.getAttribute('href') === curHash));
  toTop.classList.toggle('show', window.scrollY > window.innerHeight * 1.5);
}
let rafPending = false;
window.addEventListener('scroll', () => {
  if (rafPending) return;
  rafPending = true;
  requestAnimationFrame(() => { rafPending = false; spy(); });
}, { passive: true });
toTop.addEventListener('click', () => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
});

window.addEventListener('hashchange', route);
document.querySelector('.menu-toggle').addEventListener('click', () => {
  document.body.classList.toggle('nav-open');
});
route();
"""


def build():
    sections_html = {}
    tocs = {}
    for path, slug, _ in PAGES:
        sections_html[slug], tocs[slug] = rewrite_page(pandoc(WIKI / path), path, slug)

    validate(sections_html)

    nav = [f'<a class="site-title" href="#home">{SITE_TITLE}</a>',
           '<p class="site-sub">For fiction authors, terminal optional</p>']
    for label, pages in SECTIONS:
        if label:
            nav.append(f'<div class="section">{label}</div>')
        for _, slug, title in pages:
            if slug == "home":
                continue
            nav.append(f'<a class="page" data-page="{slug}" href="#{slug}">{title}</a>')

    body = []
    for i, (_, slug, title) in enumerate(PAGES):
        pager = []
        if i > 0:
            _, pslug, ptitle = PAGES[i - 1]
            pager.append(f'<a href="#{pslug}"><span class="label">Previous</span><span class="pager-title">{ptitle}</span></a>')
        if i < len(PAGES) - 1:
            _, nslug, ntitle = PAGES[i + 1]
            pager.append(f'<a class="next" href="#{nslug}"><span class="label">Next</span><span class="pager-title">{ntitle}</span></a>')
        toc_html = ""
        if len(tocs[slug]) >= 3:
            items = "".join(f'<a href="#{slug}/{frag}">{text}</a>' for frag, text in tocs[slug])
            toc_html = f'<aside class="toc"><div class="toc-label">On this page</div>{items}</aside>\n'
        body.append(
            f'<section data-page="{slug}">\n{toc_html}{sections_html[slug]}\n'
            f'<div class="pager">{"".join(pager)}</div>\n'
            '<footer class="colophon">Generated from docs/wiki · verified against official Anthropic docs 2026-06-10</footer>\n'
            '</section>'
        )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{SITE_TITLE}</title>
<style>{CSS}</style>
</head>
<body>
<button class="menu-toggle" aria-label="Toggle navigation">Menu</button>
<nav>
{chr(10).join(nav)}
</nav>
<main>
{chr(10).join(body)}
</main>
<button class="to-top" aria-label="Back to top">&#8593; Top</button>
<script>const SITE_TITLE = {SITE_TITLE!r};{JS}</script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB, {len(PAGES)} pages)")


if __name__ == "__main__":
    build()
