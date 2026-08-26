# UWH Beginner's Guide migration

## Paths

| Role | Path |
|------|------|
| **Tiell HTTrack mirror (primary)** | `scripts/uwh-guide-migration/tiell-mirror/` ([source](https://tiell.com/SFUWH/WIN/www.sfuwh.org/uwh-beginner-guide.html)) |
| Offline Wayback “Save Page As” dump | `/Users/matt/Projects/uwh-beginners-guide` (outside this repo) |
| Hugo guide content | `content/beginners-guide/` |
| Served images | `static/beginners-guide/` |
| PDF source (2005-era manual) | `content/beginners-guide/UFNewMembersManual.pdf` |
| PDF image review extract | `scripts/uwh-guide-migration/pdf-extract/all-images/` |
| Optional recovered HTML | `scripts/uwh-guide-migration/wayback/pages/` |
| Atlantis wiki offline mirror | `scripts/uwh-guide-migration/atlantis-wiki/` |
| Modernization gap list | [MODERNIZATION_RECS.md](MODERNIZATION_RECS.md) |
| Local extras catalog | [local-docs-extract/CATALOG.md](local-docs-extract/CATALOG.md) |

## Atlantis wiki mirror

```bash
python3 scripts/uwh-guide-migration/scrape_atlantis_wiki.py
```

Fetches all **published** pages listed by Wiki.js GraphQL, saves HTML + text under `atlantis-wiki/`. See [MODERNIZATION_RECS.md](MODERNIZATION_RECS.md) for beginner-guide update/add/delete recommendations (analysis only—no wholesale republish).


## Re-run HTML → Markdown conversion

```bash
cd /Users/matt/Projects/hugo-site
./scripts/uwh-guide-migration/.venv/bin/python scripts/uwh-guide-migration/convert_guide.py
hugo
```

Do **not** re-run conversion blindly over edited Markdown chapters; it overwrites generated pages. Prefer copying recovered assets into `static/beginners-guide/` and wiring them by hand (or only re-convert pages you still treat as disposable).

---

## Tiell mirror (recommended image source)

Full HTTrack backup of the live Google Sites guide (Mar 2023):

```bash
cd /Users/matt/Projects/hugo-site
python3 scripts/uwh-guide-migration/mirror_tiell_guide.py   # crawl → tiell-mirror/
python3 scripts/uwh-guide-migration/restore_tiell_images.py  # backpick placeholders only
```

- **Restored from mirror:** `backpick1–3.png`, `uwh-1-1-a/b`, `uwh-2-2a/b` (2014 guide originals)
- Compare originals archived under `static/beginners-guide/original/` and in `tiell-mirror/`; not shown on pages

Manifest: `tiell-mirror/MANIFEST.json`

---

## Restore missing images from Wayback

### Why the local dump is incomplete

The dump under `uwh-beginners-guide` is a browser “Save Page As” of Archive.org captures of the Google Sites guide (`sfuwh.org` / `www2.sfuwh.org`).

Many image files in the dump’s `*_files/` folders are **not images**. Google Sites / accounts redirects returned HTML login pages; the browser saved those as `.jpg` / `.png` / `.gif` with the right names.

Quick check:

```bash
file "/Users/matt/Projects/uwh-beginners-guide/"*/*/*.png \
     "/Users/matt/Projects/uwh-beginners-guide/"*/*.jpg 2>/dev/null | grep -i html
```

Anything reported as `HTML document` is a failed download. The same bad files were copied into `static/beginners-guide/` for some assets (`backpick1.png`, `backpick2.png`, `uwh-1-1-a.PNG`, `uwh-1-1-b.PNG`, etc.).

Diagram GIFs dated **2011** in the dump root (e.g. `LeftForward.gif`, `GoodPassing.gif`) are often real and were preferred over the failed `*_files/` copies.

### What is still missing (site-era assets)

These appear in the HTML dump and/or Markdown, but are fake HTML or absent from the PDF:

| Asset | Chapter | Notes |
|-------|---------|--------|
| `backpick1.png` | Positioning | Fake HTML in static + dump |
| `backpick2.png` | Positioning | Fake HTML in static + dump |
| `backpick3.png` | Positioning | Referenced in dump HTML; may not be wired in MD |
| `uwh-1-1-a.PNG` | 2-on-1 | Fake HTML in static + dump |
| `uwh-1-1-b.PNG` | 2-on-1 | Fake HTML in static + dump |
| `uwh-2-2a.PNG` | 2-on-2 | Not in PDF; missing from dump `*_files/` |
| `uwh-2-2b.PNG` | 2-on-2 | Same |
| `[MISSING DIAGRAM: GOOD POSITIONING]` | Positioning | Likely `GoodPassing2.gif` (real copy already in static); confirm against page |

Equipment photos (`image001.jpg` glove / `image002.jpg` sticks) failed in the dump the same way; sticks was later restored from a local `content/beginners-guide/sticks.webp`, glove from the PDF extract.

### Find the Archive.org URL

1. Open the chapter HTML in the dump (e.g. `13. How to Execute in a Two-on-Two Situation -.html`).
2. Search for the filename. Prefer:
   - `og:image` / `itemprop="image"` meta tags (often already `…/web/TIMESTAMP**im_**/http://www.sfuwh.org/_/rsrc/…`)
   - `href` on the image anchor (`…/uwh-beginner-guide/…/file.PNG?attredirects=0`)
3. Build an **image** playback URL with the `im_` (or `if_`) flag after the timestamp:

```text
https://web.archive.org/web/<TIMESTAMP>im_/<ORIGINAL_URL>
```

Strip `?attredirects=0` and HTML entities (`&amp;` → `&`). Prefer `/_/rsrc/<id>/…` URLs when present; they are the stored binary.

Known starting points (May 2022 captures):

```text
https://web.archive.org/web/20220522211137im_/http://www.sfuwh.org/uwh-beginner-guide/positioning/backpick1.png
https://web.archive.org/web/20220522211137im_/http://www.sfuwh.org/uwh-beginner-guide/positioning/backpick2.png
https://web.archive.org/web/20220522211137im_/http://www.sfuwh.org/uwh-beginner-guide/positioning/backpick3.png

https://web.archive.org/web/20220522205040im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-1/uwh-1-1-a.PNG
https://web.archive.org/web/20220522205040im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-1/uwh-1-1-b.PNG

https://web.archive.org/web/20220522203718im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-2/uwh-2-2a.PNG
https://web.archive.org/web/20220522203718im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-2/uwh-2-2b.PNG
```

If a timestamp 404s, resolve via CDX (when Archive.org is up):

```bash
curl -sL "https://web.archive.org/cdx/search/cdx?url=www.sfuwh.org/uwh-beginner-guide/2-2/uwh-2-2a.PNG&output=json&fl=timestamp,original,statuscode,mimetype,length&filter=statuscode:200&limit=20"

# Also try the rsrc form and www2.sfuwh.org
curl -sL "https://web.archive.org/cdx/search/cdx?url=www.sfuwh.org/_/rsrc/*/uwh-beginner-guide/2-2/uwh-2-2a.PNG&output=json&fl=timestamp,original,statuscode,mimetype,length&limit=20"
```

Pick a `200` row whose `mimetype` is an image (`image/png`, `image/jpeg`, …). Replay:

```text
https://web.archive.org/web/<timestamp>im_/<original>
```

### Download and validate

Archive.org often returns **503** under load. Retry later; do not treat HTML error bodies as success.

```bash
OUT="/Users/matt/Projects/hugo-site/static/beginners-guide"
URL="https://web.archive.org/web/20220522203718im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-2/uwh-2-2a.PNG"
DEST="$OUT/uwh-2-2a.PNG"

curl -L --fail --retry 5 --retry-delay 10 -A 'Mozilla/5.0' -o "$DEST" "$URL"
file "$DEST"
# Expect: PNG image data / JPEG image data / GIF image data
# Reject: HTML document, ASCII text

# Optional: reject tiny/error payloads
python3 - <<'PY'
from pathlib import Path
p = Path("/Users/matt/Projects/hugo-site/static/beginners-guide/uwh-2-2a.PNG")
b = p.read_bytes()[:64]
assert not b.lstrip().lower().startswith((b"<!doctype", b"<html")), "got HTML, not an image"
print("ok", p.stat().st_size, "bytes")
PY
```

Batch pattern for several URLs (skip failures, leave existing good files alone):

```bash
OUT="/Users/matt/Projects/hugo-site/static/beginners-guide"
download() {
  local url="$1" name="$2"
  local dest="$OUT/$name"
  echo "→ $name"
  if curl -L --fail --retry 5 --retry-delay 10 -A 'Mozilla/5.0' -o "$dest.tmp" "$url"; then
    if file "$dest.tmp" | grep -qiE 'PNG image|JPEG image|GIF image|Web/P'; then
      mv "$dest.tmp" "$dest"
      echo "  ok $(file -b "$dest")"
    else
      echo "  REJECT (not an image): $(file -b "$dest.tmp")"
      rm -f "$dest.tmp"
    fi
  else
    echo "  FAIL curl"
    rm -f "$dest.tmp"
  fi
}

download "https://web.archive.org/web/20220522211137im_/http://www.sfuwh.org/uwh-beginner-guide/positioning/backpick1.png" "backpick1.png"
download "https://web.archive.org/web/20220522211137im_/http://www.sfuwh.org/uwh-beginner-guide/positioning/backpick2.png" "backpick2.png"
download "https://web.archive.org/web/20220522205040im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-1/uwh-1-1-a.PNG" "uwh-1-1-a.PNG"
download "https://web.archive.org/web/20220522205040im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-1/uwh-1-1-b.PNG" "uwh-1-1-b.PNG"
download "https://web.archive.org/web/20220522203718im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-2/uwh-2-2a.PNG" "uwh-2-2a.PNG"
download "https://web.archive.org/web/20220522203718im_/http://www.sfuwh.org/_/rsrc/1449216181212/uwh-beginner-guide/2-2/uwh-2-2b.PNG" "uwh-2-2b.PNG"
```

### Wire into Markdown

Most chapters already reference the expected filenames under `/beginners-guide/…`. After a good file lands in `static/beginners-guide/`, a Hugo rebuild is enough.

For 2-on-2, replace the note in `content/beginners-guide/13-two-on-two.md` with:

```markdown
![Two-on-two diagram A](/beginners-guide/uwh-2-2a.PNG)

…

![Two-on-two diagram B](/beginners-guide/uwh-2-2b.PNG)
```

For `[MISSING DIAGRAM: GOOD POSITIONING]` in `07-positioning.md`, compare the live Wayback page to `GoodPassing2.gif` before inventing a new asset name.

### Inventory check

```bash
cd /Users/matt/Projects/hugo-site
python3 - <<'PY'
import re
from pathlib import Path
static = Path("static/beginners-guide")
for md in Path("content/beginners-guide").glob("*.md"):
    for ref in re.findall(r"!\[[^\]]*\]\((/beginners-guide/[^)]+)\)", md.read_text()):
        p = static / Path(ref).name
        if not p.exists():
            print("MISSING", md.name, ref)
            continue
        head = p.read_bytes()[:80].lstrip().lower()
        if head.startswith((b"<!doctype", b"<html")):
            print("FAKE HTML", md.name, ref)
PY
```

---

## PDF images (separate from Wayback)

The PDF predates some website diagrams. Extracted embeds are under `pdf-extract/all-images/`.

Raw `pdfimages` output is often **vertically flipped** relative to the page (Word→PDF transform). Corrected review copies were fixed with: rotate 180°, then flip left-right (net effect: vertical flip only). Prefer the `pages/` renders when unsure of orientation.

```bash
# Re-extract + contact sheet
PDF="content/beginners-guide/UFNewMembersManual.pdf"
OUT="scripts/uwh-guide-migration/pdf-extract/all-images"
mkdir -p "$OUT/png" "$OUT/pages"
pdfimages -png "$PDF" "$OUT/png/img"
pdftoppm -png -r 150 "$PDF" "$OUT/pages/page"
```

---

## Recover missing Wayback *pages* (HTML)

When archive.org is healthy, save HTML into:

- `scripts/uwh-guide-migration/wayback/pages/backs-in-the-3-3.html`
- `scripts/uwh-guide-migration/wayback/pages/forwards-in-the-3-3.html`
- `scripts/uwh-guide-migration/wayback/pages/rules-and-refereeing-instruction.html`

Copy recovered images into `static/beginners-guide/`. Only then consider re-running `convert_guide.py` for those extras (`maybe_convert_wayback_extras`).
