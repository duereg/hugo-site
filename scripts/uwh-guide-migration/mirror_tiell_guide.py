#!/usr/bin/env python3
"""Mirror the tiell.com HTTrack backup of the SFUWH beginner guide."""

from __future__ import annotations

import json
import mimetypes
import re
import subprocess
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen

BASE_URL = "https://tiell.com/SFUWH/WIN/www.sfuwh.org/"
OUT_ROOT = Path(__file__).resolve().parent / "tiell-mirror" / "www.sfuwh.org"

GUIDE_PAGES = [
    "uwh-beginner-guide.html",
    "uwh-beginner-guide/what-is-it.html",
    "uwh-beginner-guide/rules.html",
    "uwh-beginner-guide/equipment.html",
    "uwh-beginner-guide/skills.html",
    "uwh-beginner-guide/positions.html",
    "uwh-beginner-guide/formations.html",
    "uwh-beginner-guide/zones.html",
    "uwh-beginner-guide/positioning.html",
    "uwh-beginner-guide/positioning/forwards-in-the-3-3.html",
    "uwh-beginner-guide/positioning/backs-in-the-3-3.html",
    "uwh-beginner-guide/positioning-by-scenario.html",
    "uwh-beginner-guide/scoring.html",
    "uwh-beginner-guide/subbing.html",
    "uwh-beginner-guide/cycling-breakaways.html",
    "uwh-beginner-guide/2-1.html",
    "uwh-beginner-guide/2-2.html",
    "uwh-beginner-guide/set-play.html",
    "uwh-beginner-guide/tournament-checklist.html",
    "uwh-beginner-guide/rules-and-refereeing-instruction.html",
    "uwh-beginner-guide/index.html",
]

SKIP_HOSTS = {"www.gstatic.com", "www.google.com", "www.youtube.com", "youtube.com"}
HTML_MARKERS = ("HTML document", "ASCII text", "UTF-8 Unicode text", "XML document")


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        for key in ("href", "src"):
            val = attr.get(key)
            if val:
                self.links.add(val)


def normalize_url(url: str, page_url: str) -> str | None:
    url = url.strip().split("#", 1)[0]
    if not url or url.startswith(("mailto:", "javascript:", "data:")):
        return None
    abs_url = urljoin(page_url, url)
    parsed = urlparse(abs_url)
    if parsed.netloc and parsed.netloc not in ("tiell.com", "www.tiell.com"):
        return None
    path = parsed.path
    if not path.startswith("/SFUWH/WIN/www.sfuwh.org/"):
        return None
    clean = urlunparse(
        (
            parsed.scheme or "https",
            parsed.netloc or "tiell.com",
            path,
            "",
            "",
            "",
        )
    )
    return clean


def local_path(url: str) -> Path:
    rel = urlparse(url).path.removeprefix("/SFUWH/WIN/www.sfuwh.org/")
    return OUT_ROOT / rel


def sniff_mime(path: Path) -> str:
    try:
        out = subprocess.check_output(["file", "-b", "--mime-type", str(path)], text=True).strip()
        return out or "application/octet-stream"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return mimetypes.guess_type(str(path))[0] or "application/octet-stream"


def is_html_file(path: Path) -> bool:
    try:
        desc = subprocess.check_output(["file", "-b", str(path)], text=True).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return any(m in desc for m in HTML_MARKERS) and "image" not in desc.lower()


def fetch(url: str, dest: Path) -> dict:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = Request(url, headers={"User-Agent": "uwh-guide-mirror/1.0"})
    with urlopen(req, timeout=60) as resp:
        data = resp.read()
    dest.write_bytes(data)
    mime = sniff_mime(dest)
    if is_html_file(dest) and not url.endswith(".html"):
        dest.unlink(missing_ok=True)
        raise ValueError(f"HTML body for non-HTML URL: {url}")
    return {
        "source_url": url,
        "local_path": str(dest.relative_to(OUT_ROOT.parent.parent)),
        "bytes": len(data),
        "mime": mime,
    }


def crawl() -> list[dict]:
    manifest: list[dict] = []
    seen_urls: set[str] = set()
    queue: list[str] = [urljoin(BASE_URL, p) for p in GUIDE_PAGES]

    while queue:
        url = queue.pop(0)
        if url in seen_urls:
            continue
        seen_urls.add(url)

        dest = local_path(url)
        if dest.exists() and dest.stat().st_size > 0:
            entry = {
                "source_url": url,
                "local_path": str(dest.relative_to(OUT_ROOT.parent.parent)),
                "bytes": dest.stat().st_size,
                "mime": sniff_mime(dest),
                "cached": True,
            }
            manifest.append(entry)
            html = dest.read_text(encoding="utf-8", errors="replace")
        else:
            try:
                time.sleep(0.15)
                entry = fetch(url, dest)
                manifest.append(entry)
                html = dest.read_text(encoding="utf-8", errors="replace")
            except Exception as exc:  # noqa: BLE001
                print(f"SKIP {url}: {exc}")
                continue

        if not url.endswith(".html"):
            continue

        parser = LinkParser()
        parser.feed(html)
        for link in parser.links:
            norm = normalize_url(link, url)
            if not norm:
                continue
            if norm.endswith(".html") or "/_/rsrc/" in norm:
                if norm not in seen_urls:
                    queue.append(norm)

    return manifest


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = crawl()
    manifest_path = OUT_ROOT.parent / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest)} entries to {manifest_path}")


if __name__ == "__main__":
    main()
