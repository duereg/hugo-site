#!/usr/bin/env python3
"""Generate backpick2/3 using hand-made backpick1.png as the pool template."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
STATIC = ROOT / "static" / "beginners-guide"
PUBLIC = ROOT / "public" / "beginners-guide"
REFERENCE = STATIC / "backpick1.png"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)

# Left-wall play cluster only (keeps pool frame + Middle Zone label intact)
PLAY_CLEAR = (20, 126, 58, 240)
ZONE_Y = (142, 143, 248, 249)


def font(size: int = 10):
    for name in ("Helvetica.ttc", "Arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def restore_zone_dashes(draw: ImageDraw.ImageDraw):
    for y in ZONE_Y:
        x = 21
        while x < 58:
            draw.line([(x, y), (min(x + 5, 58), y)], fill=RED, width=1)
            x += 10


def clear_play_cluster(img: Image.Image):
    draw = ImageDraw.Draw(img)
    draw.rectangle(PLAY_CLEAR, fill=WHITE)
    restore_zone_dashes(draw)


def pool_from_reference() -> Image.Image:
    return Image.open(REFERENCE).convert("RGB").copy()


def cyan_player(draw: ImageDraw.ImageDraw, xy, label: str, r: int = 10):
    x, y = xy
    draw.ellipse([x - r, y - r, x + r, y + r], fill=CYAN, outline=BLACK, width=1)
    f = font(10)
    bbox = draw.textbbox((0, 0), label, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x - tw / 2, y - th / 2 - 1), label, fill=BLACK, font=f)


def puck(draw: ImageDraw.ImageDraw, xy):
    x, y = xy
    draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=BLACK)


def triangle_at_puck(draw: ImageDraw.ImageDraw, puck_xy, toward_xy, *, base_dist=18, half_w=7):
    px, py = puck_xy
    tx, ty = toward_xy
    ang = math.atan2(ty - py, tx - px)
    bcx = px - base_dist * math.cos(ang)
    bcy = py - base_dist * math.sin(ang)
    perp = ang + math.pi / 2
    b1 = (bcx + half_w * math.cos(perp), bcy + half_w * math.sin(perp))
    b2 = (bcx - half_w * math.cos(perp), bcy - half_w * math.sin(perp))
    draw.polygon([puck_xy, b1, b2], fill=WHITE, outline=BLACK)


def between_players(lf_xy, lb_xy) -> tuple[int, int]:
    """Puck/triangle midpoint on the left wall between LF (above) and LB (below)."""
    x = lf_xy[0] + 1
    y = (lf_xy[1] + lb_xy[1]) // 2
    return (x, y)


def scene2() -> Image.Image:
    """LB engages and turns attacker toward LF; LF low on wall for the curl."""
    img = pool_from_reference()
    clear_play_cluster(img)
    draw = ImageDraw.Draw(img)

    lf = (34, 150)
    lb = (34, 218)
    puck_xy = between_players(lf, lb)

    cyan_player(draw, lf, "LF")
    triangle_at_puck(draw, puck_xy, lf)
    puck(draw, puck_xy)
    cyan_player(draw, lb, "LB")
    draw.arc([22, puck_xy[1] - 18, 50, puck_xy[1] + 18], start=200, end=305, fill=BLACK, width=1)
    return img


def scene3() -> Image.Image:
    """LF steals with body between opponent and puck."""
    img = pool_from_reference()
    clear_play_cluster(img)
    draw = ImageDraw.Draw(img)

    lf = (34, 155)
    lb = (34, 225)
    puck_xy = between_players(lf, lb)

    cyan_player(draw, lf, "LF")
    triangle_at_puck(draw, puck_xy, lb)
    puck(draw, puck_xy)
    cyan_player(draw, lb, "LB")
    draw.line([lf, puck_xy], fill=BLACK, width=1)
    return img


def main():
    for n, factory in ((2, scene2), (3, scene3)):
        img = factory()
        for d in (STATIC, PUBLIC):
            d.mkdir(parents=True, exist_ok=True)
            path = d / f"backpick{n}.png"
            img.save(path, optimize=True)
            print(f"wrote {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
