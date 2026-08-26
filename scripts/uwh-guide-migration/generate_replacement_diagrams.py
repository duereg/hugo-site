#!/usr/bin/env python3
"""Generate replacement tactical diagrams for missing beginners-guide assets."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[2] / "static" / "beginners-guide"

# Palette matched to existing GIF diagrams (BadPass2, SevenFormation, etc.)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)  # on-bottom teammates (BadPass2.gif)
GRAY = (120, 120, 120)
DARK = (40, 40, 40)
GREEN = (0, 128, 0)
YELLOW = (255, 220, 0, 90)


def font(size: int = 12):
    for name in ("Helvetica.ttc", "Arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_dashed_line(draw: ImageDraw.ImageDraw, p1, p2, fill=RED, width=2, dash=8):
    x1, y1 = p1
    x2, y2 = p2
    length = math.hypot(x2 - x1, y2 - y1)
    if length == 0:
        return
    dx, dy = (x2 - x1) / length, (y2 - y1) / length
    dist = 0
    while dist < length:
        start = (x1 + dx * dist, y1 + dy * dist)
        end_dist = min(dist + dash, length)
        end = (x1 + dx * end_dist, y1 + dy * end_dist)
        draw.line([start, end], fill=fill, width=width)
        dist += dash * 2


def draw_dashed_hline(draw, y, x1, x2, **kwargs):
    draw_dashed_line(draw, (x1, y), (x2, y), **kwargs)


def draw_pool_frame(draw, box, goal_depth=18, wall_left=False):
    x0, y0, x1, y1 = box
    draw.rectangle(box, outline=BLACK, width=2, fill=WHITE)
    cx = (x0 + x1) // 2
    gw = max(24, (x1 - x0) // 3)
    # opponent goal (top)
    draw.polygon(
        [(cx - gw, y0), (cx + gw, y0), (cx + gw - 8, y0 + goal_depth), (cx - gw + 8, y0 + goal_depth)],
        outline=BLACK,
        fill=WHITE,
    )
    # our goal (bottom)
    draw.polygon(
        [(cx - gw, y1), (cx + gw, y1), (cx + gw - 8, y1 - goal_depth), (cx - gw + 8, y1 - goal_depth)],
        outline=BLACK,
        fill=WHITE,
    )
    if wall_left:
        draw.line([(x0, y0), (x0, y1)], fill=BLACK, width=4)
    h = y1 - y0
    draw_dashed_hline(draw, y0 + h // 3, x0 + 2, x1 - 2)
    draw_dashed_hline(draw, y0 + 2 * h // 3, x0 + 2, x1 - 2)


def player(draw, xy, label, team="white", r=11):
    x, y = xy
    fill = WHITE if team == "white" else GRAY
    outline = BLACK
    draw.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=2)
    f = font(11)
    bbox = draw.textbbox((0, 0), label, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x - tw / 2, y - th / 2 - 1), label, fill=BLACK, font=f)


def draw_pool_badpass2(draw: ImageDraw.ImageDraw, box):
    """Pool frame matching BadPass2.gif: border = walls, trapezoid goals, red zone dashes."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, outline=BLACK, width=2, fill=WHITE)
    cx = (x0 + x1) // 2
    gw = max(18, (x1 - x0) // 3)
    gd = 12
    draw.polygon(
        [(cx - gw, y0), (cx + gw, y0), (cx + gw - 6, y0 + gd), (cx - gw + 6, y0 + gd)],
        outline=BLACK,
        fill=WHITE,
    )
    draw.polygon(
        [(cx - gw, y1), (cx + gw, y1), (cx + gw - 6, y1 - gd), (cx - gw + 6, y1 - gd)],
        outline=BLACK,
        fill=WHITE,
    )
    h = y1 - y0
    draw_dashed_hline(draw, y0 + h // 3, x0 + 2, x1 - 2)
    draw_dashed_hline(draw, y0 + 2 * h // 3, x0 + 2, x1 - 2)


def teammate(draw, xy, label, *, on_bottom=True, r=9):
    """Good-guy circle: cyan when on bottom (BadPass2 convention)."""
    x, y = xy
    fill = CYAN if on_bottom else WHITE
    draw.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=BLACK, width=1)
    f = font(8)
    bbox = draw.textbbox((0, 0), label, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x - tw / 2, y - th / 2 - 1), label, fill=BLACK, font=f)


def opponent_at_puck(draw, puck_xy, toward_xy, *, size=10):
    """Opponent triangle: apex on puck, pointing toward target (e.g. LB)."""
    px, py = puck_xy
    tx, ty = toward_xy
    ang = math.atan2(ty - py, tx - px)
    apex = (px, py)
    back_x = px - size * 1.15 * math.cos(ang)
    back_y = py - size * 1.15 * math.sin(ang)
    perp = ang + math.pi / 2
    half = size * 0.88
    base1 = (back_x + half * math.cos(perp), back_y + half * math.sin(perp))
    base2 = (back_x - half * math.cos(perp), back_y - half * math.sin(perp))
    draw.polygon([apex, base1, base2], outline=BLACK, fill=WHITE)


def puck(draw, xy, r=3):
    x, y = xy
    draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def arrow(draw, p1, p2, fill=BLACK, width=2):
    draw.line([p1, p2], fill=fill, width=width)
    x1, y1 = p1
    x2, y2 = p2
    ang = math.atan2(y2 - y1, x2 - x1)
    size = 8
    for da in (2.6, -2.6):
        ax = x2 - size * math.cos(ang + da)
        ay = y2 - size * math.sin(ang + da)
        draw.line([(x2, y2), (ax, ay)], fill=fill, width=width)


def backpick_panel(scene: int) -> Image.Image:
    """Left-wall backpick sequence — styled like BadPass2.gif (90×320)."""
    w, h = 90, 320
    img = Image.new("RGB", (w, h), WHITE)
    draw = ImageDraw.Draw(img)
    box = (6, 14, w - 6, h - 14)
    draw_pool_badpass2(draw, box)
    wall_x = box[0] + 10  # left wall

    if scene == 1:
        # Black attacks down the left wall toward LB; LF closes from behind on the wall.
        puck_xy = (wall_x + 2, 132)
        lb_xy = (wall_x + 28, 150)
        lf_xy = (wall_x, 108)  # behind triangle (up-wall from puck)
        opponent_at_puck(draw, puck_xy, lb_xy, size=9)
        puck(draw, puck_xy)
        teammate(draw, lb_xy, "LB")
        teammate(draw, lf_xy, "LF")
        arrow(draw, puck_xy, (puck_xy[0], puck_xy[1] + 28), fill=BLACK, width=1)
        arrow(draw, (lb_xy[0] - 6, lb_xy[1] - 4), puck_xy, fill=BLACK, width=1)
        arrow(draw, lf_xy, (lf_xy[0], lf_xy[1] + 22), fill=BLACK, width=1)
    elif scene == 2:
        # LB turns black toward LF; LF waits behind on the wall for the curl.
        puck_xy = (wall_x + 2, 168)
        lb_xy = (wall_x + 28, 152)
        lf_xy = (wall_x, 142)
        opponent_at_puck(draw, puck_xy, lb_xy, size=9)
        puck(draw, puck_xy)
        teammate(draw, lb_xy, "LB")
        teammate(draw, lf_xy, "LF")
        arrow(draw, (lb_xy[0] - 8, lb_xy[1] + 2), puck_xy, fill=BLACK, width=1)
        draw.arc([wall_x - 4, 148, wall_x + 26, 192], start=80, end=175, fill=BLACK, width=1)
    else:
        # LF steals; body between black player and puck (apex still on puck, aimed at LB).
        puck_xy = (wall_x + 2, 218)
        lb_xy = (wall_x + 26, 168)
        lf_xy = (wall_x, 198)  # behind triangle on the wall
        opponent_at_puck(draw, puck_xy, lb_xy, size=9)
        puck(draw, puck_xy)
        teammate(draw, lf_xy, "LF")
        teammate(draw, lb_xy, "LB")
        draw.line([(wall_x + 10, 210), lf_xy], fill=BLACK, width=1)

    return img


def two_on_one_dsz() -> Image.Image:
    """Pass around vs through defender swat zone."""
    w, h = 520, 420
    img = Image.new("RGB", (w, h), WHITE)
    draw = ImageDraw.Draw(img)
    box = (40, 50, w - 40, h - 40)
    draw_pool_frame(draw, box)
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    draw.text((cx - 70, y0 - 28), "Through DSZ (good)", fill=GREEN, font=font(12))
    draw.text((x0, y1 + 8), "Wide around DSZ (slow — help arrives)", fill=RED, font=font(11))

    # last defender
    dx, dy = cx, y0 + 130
    player(draw, (dx, dy), "D", team="black", r=13)
    # DSZ fan toward goal (top)
    draw.pieslice([dx - 55, dy - 55, dx + 55, dy + 55], start=200, end=340, fill=(255, 200, 200), outline=RED)
    draw.text((dx - 18, dy - 42), "DSZ", fill=RED, font=font(10))

    # passer and receiver
    player(draw, (cx - 90, y0 + 230), "P", team="white")
    puck(draw, (cx - 82, y0 + 242))
    player(draw, (cx + 70, y0 + 210), "R", team="white")

    # good: short pass through DSZ
    arrow(draw, (cx - 82, y0 + 242), (cx + 55, y0 + 205), fill=GREEN, width=3)
    # bad: wide arc
    draw.arc([cx - 160, y0 + 80, cx + 160, y0 + 320], start=300, end=20, fill=RED, width=2)
    arrow(draw, (cx - 82, y0 + 242), (cx + 120, y0 + 120), fill=RED, width=2)

    return img


def two_on_one_receiver() -> Image.Image:
    """Receiver body reduces DSZ."""
    w, h = 520, 420
    img = Image.new("RGB", (w, h), WHITE)
    draw = ImageDraw.Draw(img)
    box = (40, 50, w - 40, h - 40)
    draw_pool_frame(draw, box)
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    draw.text((cx - 95, y0 - 28), "Receiver seals DSZ", fill=GREEN, font=font(12))

    dx, dy = cx, y0 + 150
    player(draw, (dx, dy), "D", team="black", r=14)
    # stick arm toward passer
    draw.line([(dx - 8, dy + 8), (dx - 45, dy + 35)], fill=BLACK, width=3)
    draw.pieslice([dx - 60, dy - 20, dx + 40, dy + 80], start=210, end=320, fill=(255, 220, 220), outline=RED)
    draw.text((dx - 52, dy + 45), "blocked", fill=RED, font=font(9))

    player(draw, (cx - 95, y0 + 240), "P", team="white")
    puck(draw, (cx - 88, y0 + 252))
    # receiver tight on defender stick side
    player(draw, (dx - 28, dy + 38), "R", team="white", r=13)
    draw.ellipse([dx - 42, dy + 20, dx - 8, dy + 58], outline=CYAN, width=2)
    arrow(draw, (cx - 88, y0 + 252), (dx - 20, dy + 45), fill=GREEN, width=3)
    draw.text((x0 + 10, y1 + 8), "R body blocks defender stick moving back", fill=BLACK, font=font(10))

    return img


def two_on_two_predictable() -> Image.Image:
    """Typical readable 2-on-2 — both defenders read the pass."""
    w, h = 520, 420
    img = Image.new("RGB", (w, h), WHITE)
    draw = ImageDraw.Draw(img)
    box = (40, 50, w - 40, h - 40)
    draw_pool_frame(draw, box)
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    draw.text((cx - 110, y0 - 28), "Predictable 2-on-2 (bad)", fill=RED, font=font(12))

    player(draw, (cx - 60, y0 + 200), "O1", team="white", r=12)
    puck(draw, (cx - 52, y0 + 212))
    player(draw, (cx + 80, y0 + 170), "O2", team="white", r=12)
    player(draw, (cx - 20, y0 + 150), "D1", team="black", r=12)
    player(draw, (cx + 40, y0 + 130), "D2", team="black", r=12)

    arrow(draw, (cx - 52, y0 + 212), (cx + 70, y0 + 175), fill=BLACK, width=2)
    arrow(draw, (cx + 40, y0 + 130), (cx + 75, y0 + 168), fill=RED, width=2)
    draw.text((cx - 20, y1 + 8), "D2 reads pass — easy switch", fill=RED, font=font(10))

    return img


def two_on_two_commit() -> Image.Image:
    """Attack second defender — both commit, teammate open."""
    w, h = 520, 420
    img = Image.new("RGB", (w, h), WHITE)
    draw = ImageDraw.Draw(img)
    box = (40, 50, w - 40, h - 40)
    draw_pool_frame(draw, box)
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    draw.text((cx - 120, y0 - 28), "Swim at 2nd defender (good)", fill=GREEN, font=font(12))

    player(draw, (cx - 30, y0 + 210), "O1", team="white", r=12)
    puck(draw, (cx - 22, y0 + 222))
    player(draw, (cx + 100, y0 + 240), "O2", team="white", r=12)
    player(draw, (cx - 70, y0 + 160), "D1", team="black", r=12)
    player(draw, (cx + 10, y0 + 150), "D2", team="black", r=12)

    arrow(draw, (cx - 22, y0 + 222), (cx + 5, y0 + 165), fill=GREEN, width=3)
    arrow(draw, (cx - 70, y0 + 160), (cx - 35, y0 + 195), fill=RED, width=2)
    arrow(draw, (cx + 10, y0 + 150), (cx - 15, y0 + 195), fill=RED, width=2)
    draw.ellipse([cx + 75, y0 + 220, cx + 125, y0 + 270], outline=GREEN, width=2)
    draw.text((cx + 78, y0 + 248), "open", fill=GREEN, font=font(10))
    draw.text((x0 + 10, y1 + 8), "Both defenders on O1 — O2 finds hole", fill=BLACK, font=font(10))

    return img


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    outputs = {
        "backpick1.png": backpick_panel(1),
        "backpick2.png": backpick_panel(2),
        "backpick3.png": backpick_panel(3),
        "uwh-1-1-a.PNG": two_on_one_dsz(),
        "uwh-1-1-b.PNG": two_on_one_receiver(),
        "uwh-2-2a.PNG": two_on_two_predictable(),
        "uwh-2-2b.PNG": two_on_two_commit(),
    }

    for name, image in outputs.items():
        path = OUT / name
        image.save(path, optimize=True)
        print(f"wrote {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
