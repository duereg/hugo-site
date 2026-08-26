#!/usr/bin/env python3
"""Copy tiell mirror backpick assets into Hugo static/."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

MIRROR = Path(__file__).resolve().parent / "tiell-mirror" / "www.sfuwh.org"
STATIC = Path(__file__).resolve().parents[2] / "static" / "beginners-guide"
ORIGINAL = STATIC / "original"


def find_one(pattern: str) -> Path:
    matches = sorted(MIRROR.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No mirror match for {pattern}")
    return matches[0]


def verify_image(path: Path) -> None:
    out = subprocess.check_output(["file", "-b", str(path)], text=True).strip()
    if "image" not in out.lower():
        raise ValueError(f"Not an image: {path} ({out})")


def copy(src: Path, dest: Path) -> None:
    verify_image(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"  {src.name} -> {dest.relative_to(STATIC.parent.parent)}")


def main() -> None:
    priority = [
        (find_one("_/rsrc/*/uwh-beginner-guide/positioning/backpick1*.png"), STATIC / "backpick1.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/positioning/backpick2*.png"), STATIC / "backpick2.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/positioning/backpick3*.png"), STATIC / "backpick3.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/2-1/uwh-1-1-a.png"), STATIC / "uwh-1-1-a.PNG"),
        (find_one("_/rsrc/*/uwh-beginner-guide/2-1/uwh-1-1-b.png"), STATIC / "uwh-1-1-b.PNG"),
        (find_one("_/rsrc/*/uwh-beginner-guide/2-2/uwh-2-2a.png"), STATIC / "uwh-2-2a.PNG"),
        (find_one("_/rsrc/*/uwh-beginner-guide/2-2/uwh-2-2b.png"), STATIC / "uwh-2-2b.PNG"),
    ]

    print("2014 guide restores:")
    for src, dest in priority:
        copy(src, dest)

    # Archive originals for reference (not linked from guide pages)
    archive = [
        (find_one("_/rsrc/*/uwh-beginner-guide/scoring/uwh-scoring-a.png"), ORIGINAL / "uwh-scoring-a.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/scoring/uwh-scoring-b.png"), ORIGINAL / "uwh-scoring-b.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/skills/uwh-bg-01*.png"), ORIGINAL / "uwh-bg-figure8.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/skills/uwh-bg-02*.png"), ORIGINAL / "uwh-bg-rolling.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/skills/uwh-bg-03*.png"), ORIGINAL / "uwh-bg-rolling-v.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/skills/uwh-bg-04*.png"), ORIGINAL / "uwh-bg-body-compare.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/skills/uwh-bg-05*.png"), ORIGINAL / "uwh-bg-wall.png"),
        (find_one("_/rsrc/*/uwh-beginner-guide/equipment/image001.jpg"), ORIGINAL / "equipment-glove.jpg"),
        (find_one("_/rsrc/*/uwh-beginner-guide/equipment/image002.jpg"), ORIGINAL / "equipment-sticks.jpg"),
    ]

    print("\nArchive copies (original/):")
    for src, dest in archive:
        copy(src, dest)


if __name__ == "__main__":
    main()
