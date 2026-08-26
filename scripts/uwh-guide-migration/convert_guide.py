#!/usr/bin/env python3
"""Convert Wayback Google Sites UWH beginner guide HTML dump → Hugo Markdown."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag
import html2text

GUIDE_SRC = Path("/Users/matt/Projects/uwh-beginners-guide")
HUGO = Path("/Users/matt/Projects/hugo-site")
CONTENT = HUGO / "content" / "beginners-guide"
STATIC = HUGO / "static" / "beginners-guide"
WAYBACK_PAGES = HUGO / "scripts" / "uwh-guide-migration" / "wayback" / "pages"

CHROME_IMAGES = {
    "logo-sfuwh-simple-nowater-med.png",
    "88x31.png",
    "widgetOL.png",
    "book-lend.png",
    "blue_silhouette96-0.png",
    "librivoxaudio.jpg",
    "consolelivingroom.jpg",
    "internetarcade.jpg",
    "tv.jpg",
    "etree.jpg",
    "metropolitanmuseumofart-gallery.jpg",
    "911.jpg",
    "clevelandart.jpg",
    "apple-touch-icon.png",
    "loading.gif",
    "wayback-toolbar-logo-200.png",
    "wm_tb_nxt_on.png",
    "wm_tb_prv_on.png",
    "favicon.ico",
    "cleardot.gif",
}

# Local HTML dump → Hugo page metadata
PAGES = [
    {
        "src": "Underwater Hockey Beginner’s Guide - San Franc.html",
        "out": "_index.md",
        "title": "Underwater Hockey Beginner's Guide",
        "weight": 0,
        "slug": None,
        "is_index": True,
    },
    {
        "src": "00. What is Underwater Hockey_ - San Francisco.html",
        "out": "00-what-is-it.md",
        "title": "What is Underwater Hockey?",
        "weight": 1,
        "slug": "what-is-it",
        "aliases": ["/uwh-beginner-guide/what-is-it"],
    },
    {
        "src": "01. Rules - San Francisco Sea Lions Underwater.html",
        "out": "01-rules.md",
        "title": "Rules",
        "weight": 2,
        "slug": "rules",
        "aliases": ["/uwh-beginner-guide/rules"],
    },
    {
        "src": "02. Equipment - San Francisco Sea Lions Underw.html",
        "out": "02-equipment.md",
        "title": "Equipment",
        "weight": 3,
        "slug": "equipment",
        "aliases": ["/uwh-beginner-guide/equipment"],
    },
    {
        "src": "03. Individual Skills - San Francisco Sea Lion.html",
        "out": "03-skills.md",
        "title": "Individual Skills",
        "weight": 4,
        "slug": "skills",
        "aliases": ["/uwh-beginner-guide/skills"],
    },
    {
        "src": "04. Underwater Hockey Positions - San Francisc.html",
        "out": "04-positions.md",
        "title": "Underwater Hockey Positions",
        "weight": 5,
        "slug": "positions",
        "aliases": ["/uwh-beginner-guide/positions"],
    },
    {
        "src": "05. Underwater Hockey Formations - San Francis.html",
        "out": "05-formations.md",
        "title": "Underwater Hockey Formations",
        "weight": 6,
        "slug": "formations",
        "aliases": ["/uwh-beginner-guide/formations"],
    },
    {
        "src": "06. Underwater Hockey Zones - San Francisco Se.html",
        "out": "06-zones.md",
        "title": "Underwater Hockey Zones",
        "weight": 7,
        "slug": "zones",
        "aliases": ["/uwh-beginner-guide/zones"],
    },
    {
        "src": "07. Position Alignment In The 3-3 Formation - .html",
        "out": "07-positioning.md",
        "title": "Position Alignment In The 3-3 Formation",
        "weight": 8,
        "slug": "positioning",
        "aliases": ["/uwh-beginner-guide/positioning"],
    },
    {
        "src": "08. Scenario Alignment In The 3-3 Formation - .html",
        "out": "08-positioning-by-scenario.md",
        "title": "Scenario Alignment In The 3-3 Formation",
        "weight": 11,
        "slug": "positioning-by-scenario",
        "aliases": ["/uwh-beginner-guide/positioning-by-scenario"],
    },
    {
        "src": "09. Scoring a Goal - San Francisco Sea Lions U.html",
        "out": "09-scoring.md",
        "title": "Scoring a Goal",
        "weight": 12,
        "slug": "scoring",
        "aliases": ["/uwh-beginner-guide/scoring"],
    },
    {
        "src": "10. Subbing Out - San Francisco Sea Lions Unde.html",
        "out": "10-subbing.md",
        "title": "Subbing Out",
        "weight": 13,
        "slug": "subbing",
        "aliases": ["/uwh-beginner-guide/subbing"],
    },
    {
        "src": "11. Cycling and Breakaways - San Francisco Sea.html",
        "out": "11-cycling-breakaways.md",
        "title": "Cycling and Breakaways",
        "weight": 14,
        "slug": "cycling-breakaways",
        "aliases": ["/uwh-beginner-guide/cycling-breakaways"],
    },
    {
        "src": "12. How to Execute in a Two-on-One Situation -.html",
        "out": "12-two-on-one.md",
        "title": "How to Execute in a Two-on-One Situation",
        "weight": 15,
        "slug": "2-1",
        "aliases": ["/uwh-beginner-guide/2-1"],
    },
    {
        "src": "13. How to Execute in a Two-on-Two Situation -.html",
        "out": "13-two-on-two.md",
        "title": "How to Execute in a Two-on-Two Situation",
        "weight": 16,
        "slug": "2-2",
        "aliases": ["/uwh-beginner-guide/2-2"],
    },
    {
        "src": "14. Set Play - San Francisco Sea Lions Underwa.html",
        "out": "14-set-play.md",
        "title": "Set Play",
        "weight": 17,
        "slug": "set-play",
        "aliases": ["/uwh-beginner-guide/set-play"],
    },
    {
        "src": "15. Tournament Checklist - San Francisco Sea L.html",
        "out": "15-tournament-checklist.md",
        "title": "Tournament Checklist",
        "weight": 18,
        "slug": "tournament-checklist",
        "aliases": ["/uwh-beginner-guide/tournament-checklist"],
    },
]

# Map old guide path slug → hugo relative path for refs
SLUG_TO_FILE = {
    "": "_index.md",
    "uwh-beginner-guide": "_index.md",
    "what-is-it": "00-what-is-it.md",
    "rules": "01-rules.md",
    "equipment": "02-equipment.md",
    "skills": "03-skills.md",
    "positions": "04-positions.md",
    "formations": "05-formations.md",
    "zones": "06-zones.md",
    "positioning": "07-positioning.md",
    "positioning/backs-in-the-3-3": "07a-backs-in-the-3-3.md",
    "positioning/forwards-in-the-3-3": "07b-forwards-in-the-3-3.md",
    "positioning-by-scenario": "08-positioning-by-scenario.md",
    "scoring": "09-scoring.md",
    "subbing": "10-subbing.md",
    "cycling-breakaways": "11-cycling-breakaways.md",
    "2-1": "12-two-on-one.md",
    "2-2": "13-two-on-two.md",
    "set-play": "14-set-play.md",
    "tournament-checklist": "15-tournament-checklist.md",
    "rules-and-refereeing-instruction": "16-rules-and-refereeing.md",
}

NEAR_MISS = {
    "25861_1430781897994_1486268786_1116570_4169062_n.jpg": "25861_1430781897994_1486268786_1116570_4169062_.jpg",
}


def collect_images() -> dict[str, Path]:
    """basename(lower) → preferred Path (top-level GIFs win)."""
    found: dict[str, Path] = {}
    # page dirs first
    for p in GUIDE_SRC.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".gif", ".png", ".jpg", ".jpeg", ".webp"}:
            continue
        key = p.name.lower()
        if key in {c.lower() for c in CHROME_IMAGES}:
            continue
        found[key] = p
    # top-level overrides
    for p in GUIDE_SRC.iterdir():
        if p.is_file() and p.suffix.lower() in {".gif", ".png", ".jpg", ".jpeg", ".webp"}:
            key = p.name.lower()
            if key not in {c.lower() for c in CHROME_IMAGES}:
                found[key] = p
    return found


def copy_static_images(images: dict[str, Path]) -> None:
    STATIC.mkdir(parents=True, exist_ok=True)
    for key, src in images.items():
        dest = STATIC / src.name
        # Prefer original casing from src
        if not dest.exists() or src.stat().st_mtime >= dest.stat().st_mtime:
            shutil.copy2(src, dest)
    # Explicit extras
    for extra in ["GoalDefense3.gif", "GoalDefense4.gif", "GoalDefense5.gif"]:
        src = GUIDE_SRC / extra
        if src.exists():
            shutil.copy2(src, STATIC / extra)


def youtube_id_from_src(src: str) -> str | None:
    # local wrapper like .../cZb2Hkg8dQs.html or youtube embed URL
    name = Path(src.split("?")[0]).stem
    if re.fullmatch(r"[-A-Za-z0-9_]{11}", name):
        return name
    m = re.search(r"(?:embed/|v=|youtu\.be/)([-A-Za-z0-9_]{11})", src)
    return m.group(1) if m else None


def resolve_image_basename(src: str, images: dict[str, Path]) -> str | None:
    bn = Path(src.split("?")[0]).name
    if bn.lower() in {c.lower() for c in CHROME_IMAGES}:
        return None
    if bn in NEAR_MISS:
        bn = NEAR_MISS[bn]
    key = bn.lower()
    if key in images:
        return images[key].name
    # try without _n suffix variants already handled
    return None


def rewrite_guide_href(href: str) -> str | None:
    if not href:
        return None
    href = href.strip()
    # strip wayback prefix
    href = re.sub(r"^https?://web\.archive\.org/web/\d+[a-z_]*/", "", href)
    m = re.search(r"sfuwh\.org/uwh-beginner-guide(/[^?#]*)?", href)
    if not m:
        # relative guide links
        if href.startswith("#"):
            return href
        if "uwh-beginner-guide" in href:
            m = re.search(r"uwh-beginner-guide(/[^?#]*)?", href)
        else:
            return None
    path = (m.group(1) or "").strip("/")
    # drop attachment query paths that aren't pages
    if path.endswith((".jpg", ".png", ".gif", ".jpeg", ".JPG", ".PNG")):
        return None
    # fragment
    frag = ""
    if "#" in href:
        frag = "#" + href.split("#", 1)[1]
    # map path
    if path in SLUG_TO_FILE:
        target = SLUG_TO_FILE[path]
        return f'{{{{< ref "{target}" >}}}}{frag}'
    # unknown internal
    if path.startswith("home/") or path == "home":
        return None  # external club page dropped
    return None


def extract_content_div(soup: BeautifulSoup) -> Tag | None:
    main = soup.find(id="sites-canvas-main-content")
    if not main:
        return None
    tile = main.select_one(".sites-tile-name-content-1") or main.select_one(
        ".sites-layout-tile"
    )
    return tile or main


def clean_content(tile: Tag, images: dict[str, Path]) -> BeautifulSoup:
    fragment = BeautifulSoup(str(tile), "lxml")
    root = fragment.body if fragment.body else fragment

    for c in root.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()

    for toc in root.select(".sites-embed-type-toc, .goog-toc"):
        parent = toc.find_parent(class_=re.compile(r"sites-embed"))
        (parent or toc).decompose()

    for iframe in root.find_all("iframe"):
        src = iframe.get("src") or ""
        yid = youtube_id_from_src(src)
        if yid:
            iframe.replace_with(fragment.new_string(f"\n\nHUGOYOUTUBE:{yid}\n\n"))
        else:
            iframe.decompose()

    for img in root.find_all("img"):
        src = img.get("src") or ""
        name = resolve_image_basename(src, images)
        alt = img.get("alt") or ""
        if name:
            marker = fragment.new_string(f"\n\nHUGOIMG:{name}|{alt}\n\n")
            parent = img.parent
            if parent and parent.name == "a":
                parent.replace_with(marker)
            else:
                img.replace_with(marker)
        else:
            img.decompose()

    for a in root.find_all("a"):
        href = a.get("href") or ""
        rewritten = rewrite_guide_href(href)
        text = a.get_text(" ", strip=True)
        if rewritten and rewritten.startswith("{{"):
            a["href"] = f"HUGOREF:{rewritten}"
        elif rewritten and rewritten.startswith("#"):
            a["href"] = rewritten
        elif "sfuwh.org" in href or "web.archive.org" in href:
            if text:
                a.replace_with(text)
            else:
                a.decompose()

    for tag in root.find_all(["script", "style", "noscript"]):
        tag.decompose()

    return fragment


def html_to_markdown(fragment: BeautifulSoup) -> str:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = True  # we already replaced with markers
    h.protect_links = False
    h.unicode_snob = True
    html = str(fragment.body) if fragment.body else str(fragment)
    md = h.handle(html)

    # Restore youtube
    md = re.sub(
        r"HUGOYOUTUBE:([-A-Za-z0-9_]{11})",
        r"{{< youtube \1 >}}",
        md,
    )
    # Restore images
    def img_repl(m):
        name, alt = m.group(1), m.group(2)
        alt = alt.strip() or Path(name).stem
        if len(alt) > 80:
            alt = Path(name).stem
        return f"![{alt}](/beginners-guide/{name})"

    md = re.sub(r"HUGOIMG:([^|\n]+)\|([^\n]*)", img_repl, md)

    # Restore refs (with optional <> wrapping from html2text)
    md = re.sub(
        r"\[([^\]]*)\]\(<?HUGOREF:(\{\{< ref \"[^\"]+\" >\}\}(?:#[^)]*)?)>?\)",
        r"[\1](\2)",
        md,
    )
    md = md.replace("HUGOREF:", "")
    md = re.sub(
        r"\[([^\]]*)\]\(<({{< ref \"[^\"]+\" >}}(?:#[^)]*)?)>\)",
        r"[\1](\2)",
        md,
    )

    # Drop prev/next chrome lines (arrow navigation)
    cleaned_lines = []
    for line in md.splitlines():
        stripped = line.strip()
        if ("ref " in stripped or "HUGOREF" in stripped) and (
            "<--" in stripped or "-->" in stripped or "<\\--" in stripped or "&lt;--" in stripped
        ):
            continue
        if re.search(r"\[<?\\?--", stripped) and "-->" in stripped:
            continue
        cleaned_lines.append(line)
    md = "\n".join(cleaned_lines)

    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"&nbsp;", " ", md)
    md = re.sub(r"^_\s*$", "", md, flags=re.M)
    return md.strip() + "\n"


def front_matter(meta: dict, is_index: bool = False) -> str:
    lines = ["---", f'title: "{meta["title"]}"']
    if not is_index:
        lines.append(f"weight: {meta['weight']}")
        if meta.get("slug"):
            lines.append(f'slug: "{meta["slug"]}"')
        if meta.get("aliases"):
            lines.append("aliases:")
            for a in meta["aliases"]:
                lines.append(f'  - "{a}"')
    lines.extend(
        [
            'type: "beginners-guide"',
            "comments: false",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def convert_file(src: Path, meta: dict, images: dict[str, Path]) -> str:
    raw = src.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(raw, "lxml")
    tile = extract_content_div(soup)
    if not tile:
        raise RuntimeError(f"No content tile in {src}")
    cleaned = clean_content(tile, images)
    md = html_to_markdown(cleaned)
    return front_matter(meta, is_index=meta.get("is_index", False)) + md


INDEX_INTRO = """This guide was originally published for the San Francisco Sea Lions Underwater Hockey club.
It is reproduced here as a first-class section of this site.

**License:** [CC BY-NC-ND 3.0](https://creativecommons.org/licenses/by-nc-nd/3.0/).
Attribution to the original authors and contributors (including MB, RW, and Mark P Sullivan).
Originally transcribed from a Word document (~2010) and hosted on Google Sites.

"""

FUTURE_NOTE = """
## Potential future updates

After restoring any remaining gaps from the Wayback Machine, the following local Sea Lions coaching materials are **candidates for refreshing or extending** this guide (especially positioning). They are **not** drop-in replacements for the original beginner chapters — they use a later “Flow” vocabulary (Wing Forward / Pivot / Wing Back / Swing, Inside/Openside) rather than the guide’s Left/Center/Right Forward & Back framing:

- `Position Complete 2016-07-29.docx` (and comments)
- `Swing.docx` / `Pivot.docx` / `swing.txt`
- `Playbook Draft for 2018 v2.pptx` / `v4.pptx`
- `Style of Play version 01.pdf`
- `Advantage pucks 2017.pptx`
- `Drill File 2017v3.pptx`

These files remain in the offline source archive (`uwh-beginners-guide/`). Fitness workouts, beep tests, and foul photo docs are out of scope for the beginner’s guide itself.

"""


def maybe_convert_wayback_extras(images: dict[str, Path]) -> None:
    extras = [
        (
            WAYBACK_PAGES / "backs-in-the-3-3.html",
            {
                "out": "07a-backs-in-the-3-3.md",
                "title": "Backs in the 3-3",
                "weight": 9,
                "slug": "backs-in-the-3-3",
                "aliases": ["/uwh-beginner-guide/positioning/backs-in-the-3-3"],
            },
        ),
        (
            WAYBACK_PAGES / "forwards-in-the-3-3.html",
            {
                "out": "07b-forwards-in-the-3-3.md",
                "title": "Forwards In The 3-3",
                "weight": 10,
                "slug": "forwards-in-the-3-3",
                "aliases": ["/uwh-beginner-guide/positioning/forwards-in-the-3-3"],
            },
        ),
        (
            WAYBACK_PAGES / "rules-and-refereeing-instruction.html",
            {
                "out": "16-rules-and-refereeing.md",
                "title": "Rules and Refereeing Instruction",
                "weight": 19,
                "slug": "rules-and-refereeing-instruction",
                "aliases": ["/uwh-beginner-guide/rules-and-refereeing-instruction"],
            },
        ),
    ]
    for src, meta in extras:
        if not src.exists() or src.stat().st_size < 500:
            print(f"skip missing wayback page: {src.name}")
            continue
        try:
            body = convert_file(src, meta, images)
            # convert_file already includes front matter via meta keys — need out
            (CONTENT / meta["out"]).write_text(body, encoding="utf-8")
            print(f"wrote wayback {meta['out']}")
        except Exception as e:
            print(f"failed wayback {src}: {e}")


def main() -> None:
    CONTENT.mkdir(parents=True, exist_ok=True)
    images = collect_images()
    print(f"collected {len(images)} content images")
    copy_static_images(images)
    print(f"static images in {STATIC}: {len(list(STATIC.iterdir()))}")

    index_meta = None
    for meta in PAGES:
        if meta.get("is_index"):
            index_meta = meta
            continue
        src = GUIDE_SRC / meta["src"]
        if not src.exists():
            print(f"MISSING SRC {meta['src']}")
            continue
        md = convert_file(src, meta, images)
        (CONTENT / meta["out"]).write_text(md, encoding="utf-8")
        print(f"wrote {meta['out']} ({len(md)} chars)")

    maybe_convert_wayback_extras(images)

    if index_meta:
        chapters = [p for p in PAGES if not p.get("is_index")]
        toc = ["## Chapters", ""]
        # Interleave recovered 07a/07b after positioning if they exist
        for p in chapters:
            toc.append(f'- [{p["title"]}]({{{{< ref "{p["out"]}" >}}}})')
            if p["out"] == "07-positioning.md":
                for extra_out, extra_title in [
                    ("07a-backs-in-the-3-3.md", "Backs in the 3-3"),
                    ("07b-forwards-in-the-3-3.md", "Forwards In The 3-3"),
                ]:
                    if (CONTENT / extra_out).exists():
                        toc.append(f'- [{extra_title}]({{{{< ref "{extra_out}" >}}}})')
        if (CONTENT / "16-rules-and-refereeing.md").exists():
            toc.append(
                '- [Rules and Refereeing Instruction]({{< ref "16-rules-and-refereeing.md" >}})'
            )
        body = (
            front_matter(index_meta, is_index=True)
            + INDEX_INTRO
            + "\n".join(toc)
            + "\n"
            + FUTURE_NOTE
        )
        (CONTENT / index_meta["out"]).write_text(body, encoding="utf-8")
        print(f"wrote {index_meta['out']} (clean index)")

    print("done")


if __name__ == "__main__":
    main()
