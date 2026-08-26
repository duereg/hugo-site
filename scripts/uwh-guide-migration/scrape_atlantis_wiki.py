#!/usr/bin/env python3
"""Mirror public pages from wiki.atlantissports.org (Wiki.js) for offline analysis."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://wiki.atlantissports.org"
OUT = Path(__file__).resolve().parent / "atlantis-wiki"
HTML_DIR = OUT / "html"
TEXT_DIR = OUT / "text"
DELAY_S = 0.35
UA = "Mozilla/5.0 (compatible; uwh-guide-migration/1.0; +local offline mirror)"


class ContentExtractor(HTMLParser):
    """Extract body from Wiki.js SSR HTML (legacy page-contents or template slot)."""

    def __init__(self) -> None:
        super().__init__()
        self._capture = False
        self._depth = 0
        self._parts: list[str] = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_d = {k: (v or "") for k, v in attrs}
        classes = attrs_d.get("class", "")
        if tag == "title":
            self._in_title = True
        if tag == "div" and "page-contents" in classes.split():
            self._capture = True
            self._depth = 1
            return
        if tag == "template" and attrs_d.get("slot") == "contents":
            self._capture = True
            self._depth = 1
            return
        if self._capture:
            if tag in {"div", "template", "section", "article", "ol", "ul", "li", "figure"}:
                self._depth += 1
            if tag in {"h1", "h2", "h3", "h4", "p", "li", "br", "tr"}:
                self._parts.append("\n")
            if tag == "a":
                href = attrs_d.get("href", "")
                if href.startswith("/") or href.startswith(BASE):
                    self._parts.append(f" [{href}] ")
            if tag == "img":
                self._parts.append(f" [img:{attrs_d.get('src', '')}] ")

    def handle_endtag(self, tag: str) -> None:
        if self._in_title and tag == "title":
            self._in_title = False
        if not self._capture:
            return
        if tag in {"div", "template", "section", "article", "ol", "ul", "li", "figure"}:
            self._depth -= 1
            if self._depth <= 0:
                self._capture = False
        if tag in {"p", "li", "h1", "h2", "h3", "h4", "tr"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._capture:
            self._parts.append(data)

    def text(self) -> str:
        raw = "".join(self._parts)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def regex_extract(html: str) -> str:
    m = re.search(r'<template\s+slot="contents">(.*?)</template>', html, re.S | re.I)
    if not m:
        return ""
    chunk = m.group(1)
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</(p|h1|h2|h3|h4|li|tr)>", "\n", chunk, flags=re.I)
    chunk = re.sub(r'<a[^>]+href="([^"]+)"[^>]*>', r" [\1] ", chunk)
    chunk = re.sub(r"<[^>]+>", "", chunk)
    chunk = re.sub(r"&nbsp;", " ", chunk)
    chunk = re.sub(r"&amp;", "&", chunk)
    chunk = re.sub(r"[ \t]+", " ", chunk)
    chunk = re.sub(r"\n{3,}", "\n\n", chunk)
    return chunk.strip()


def graphql_list() -> list[dict]:
    body = json.dumps(
        {"query": "{ pages { list { id path title locale isPublished } } }"}
    ).encode()
    req = urllib.request.Request(
        f"{BASE}/graphql",
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": UA},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    return data["data"]["pages"]["list"]


def url_for_path(path: str) -> str:
    if path in {"home", ""}:
        return f"{BASE}/"
    return f"{BASE}/{path}"


def fetch(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b""


def safe_name(path: str) -> str:
    if path in {"home", ""}:
        return "home"
    return path.strip("/").replace("/", "__")


def main() -> None:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)

    pages = graphql_list()
    published = [p for p in pages if p.get("isPublished")]
    unpublished = [p for p in pages if not p.get("isPublished")]
    print(f"GraphQL list: {len(pages)} total, {len(published)} published")

    index_rows: list[str] = [
        "# Atlantis Sports Underwater Hockey Wiki — offline mirror",
        "",
        f"Source: {BASE}",
        f"Published pages attempted: {len(published)}",
        f"Unpublished (skipped): {len(unpublished)}",
        "",
        "| Status | Path | Title | Local HTML | Local text |",
        "|--------|------|-------|------------|------------|",
    ]

    ok = fail = skip = 0
    for i, page in enumerate(sorted(published, key=lambda p: p["path"])):
        path = page["path"]
        title = page.get("title") or path
        url = url_for_path(path)
        name = safe_name(path)
        html_path = HTML_DIR / f"{name}.html"
        text_path = TEXT_DIR / f"{name}.md"

        status, body = fetch(url)
        time.sleep(DELAY_S)

        if status != 200:
            fail += 1
            index_rows.append(
                f"| {status} | `{path}` | {title} | — | — |"
            )
            print(f"FAIL {status} {path}")
            continue

        html_path.write_bytes(body)
        extractor = ContentExtractor()
        try:
            extractor.feed(body.decode("utf-8", errors="replace"))
        except Exception as e:  # noqa: BLE001
            print(f"parse warn {path}: {e}")

        page_title = (extractor.title.split("|")[0].strip() if extractor.title else title)
        text = extractor.text()
        if len(text) < 40:
            text = regex_extract(body.decode("utf-8", errors="replace"))
        md = (
            f"# {page_title}\n\n"
            f"- URL: {url}\n"
            f"- Path: `{path}`\n\n"
            f"{text}\n"
        )
        text_path.write_text(md, encoding="utf-8")
        ok += 1
        index_rows.append(
            f"| 200 | `{path}` | {page_title} | `html/{name}.html` | `text/{name}.md` |"
        )
        if (i + 1) % 25 == 0:
            print(f"... {i + 1}/{len(published)}")

    index_rows.extend(
        [
            "",
            "## Unpublished (not fetched)",
            "",
        ]
    )
    for p in sorted(unpublished, key=lambda x: x["path"]):
        index_rows.append(f"- `{p['path']}` — {p.get('title')}")
        skip += 1

    index_rows.extend(
        [
            "",
            f"## Summary",
            "",
            f"- OK: {ok}",
            f"- Failed: {fail}",
            f"- Unpublished skipped: {skip}",
            "",
        ]
    )
    (OUT / "INDEX.md").write_text("\n".join(index_rows) + "\n", encoding="utf-8")
    (OUT / "pages.json").write_text(
        json.dumps({"published": published, "unpublished": unpublished}, indent=2),
        encoding="utf-8",
    )
    print(f"Done OK={ok} FAIL={fail} SKIP_UNPUB={skip}")
    print(f"Wrote {OUT / 'INDEX.md'}")


if __name__ == "__main__":
    main()
