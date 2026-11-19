#!/usr/bin/env python3
"""Draw the GTA 6 launch-week meme for make.fun's gta6-meme-x-01 bounty.

The joke: the 13-year wait. Top panel, 2013: a young fan on the couch,
sure GTA 6 is a couple of years away. Bottom panel, 2026: the same fan,
now old with a grey beard, on the same couch on GTA VI launch day.
make.fun's ghost mascot floats beside him holding its magenta star coin,
and the make.fun name sits at the bottom.

Everything here is drawn from scratch with PIL shapes, gradients and
text, plus the make.fun ghost mark from the press kit (assets/mark-1024.png).
No Rockstar art, no logo, no copied meme. Output: meme.png, 1080x1080.
"""

import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
MID = 540  # split between the two panels

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vgrad(size, top, bottom):
    """Vertical gradient image."""
    img = Image.new("RGB", size)
    d = ImageDraw.Draw(img)
    for y in range(size[1]):
        d.line([(0, y), (size[0], y)], fill=lerp(top, bottom, y / max(1, size[1] - 1)))
    return img


def text_center(d, cx, y, s, f, fill, outline=None, width=4):
    """Draw text centred on cx at height y, with an optional outline."""
    w = d.textlength(s, font=f)
    x = cx - w / 2
    if outline is not None:
        d.text((x, y), s, font=f, fill=outline, stroke_width=width, stroke_fill=outline)
    d.text((x, y), s, font=f, fill=fill)


def star(d, cx, cy, r, fill):
    """A four-pointed sparkle star."""
    pts = []
    for i in range(8):
        ang = math.pi / 2 + i * math.pi / 4
        rr = r if i % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
    d.polygon(pts, fill=fill)


def skyline(d, y_base, height, color, seed, lit):
    """A row of dark buildings with a few lit windows."""
    rnd = random.Random(seed)
    x = 0
    while x < W:
        bw = rnd.randint(46, 110)
        bh = rnd.randint(int(height * 0.35), height)
        d.rectangle([x, y_base - bh, x + bw, y_base], fill=color)
        for _ in range(rnd.randint(2, 7)):
            wx = rnd.randint(x + 6, x + bw - 12)
            wy = rnd.randint(y_base - bh + 8, y_base - 12)
            d.rectangle([wx, wy, wx + 6, wy + 8], fill=lit)
        x += bw + rnd.randint(2, 10)


def palm(d, x, y, s, color):
    """A simple palm silhouette: curved trunk, drooping frond blades, coconuts."""
    d.line([(x, y), (x + 10 * s, y - 95 * s)], fill=color, width=int(10 * s))
    cx, cy = x + 10 * s, y - 95 * s
    for ang in (-155, -120, -85, -50, -15, 20):
        a = math.radians(ang)
        mid = (cx + 34 * s * math.cos(a), cy + 26 * s * math.sin(a) - 10 * s)
        tip = (cx + 66 * s * math.cos(a), cy + 52 * s * math.sin(a) + 6 * s)
        d.line([(cx, cy), mid, tip], fill=color, width=int(8 * s), joint="curve")
    d.ellipse([cx - 6 * s, cy - 2 * s, cx + 12 * s, cy + 12 * s], fill=color)
    d.ellipse([cx - 14 * s, cy + 4 * s, cx, cy + 16 * s], fill=color)


def couch(d, x, y, w, h, color, dark):
    """A simple sofa: base, back, two cushions, two armrests."""
    d.rounded_rectangle([x, y - h * 0.55, x + w, y + h * 0.45], radius=18, fill=color)
    d.rounded_rectangle([x + 14, y - h * 0.28, x + w // 2 - 6, y + h * 0.42], radius=12, fill=dark)
    d.rounded_rectangle([x + w // 2 + 6, y - h * 0.28, x + w - 14, y + h * 0.42], radius=12, fill=dark)
    d.rounded_rectangle([x - 8, y - h * 0.28, x + 22, y + h * 0.45], radius=12, fill=color)
    d.rounded_rectangle([x + w - 22, y - h * 0.28, x + w + 8, y + h * 0.45], radius=12, fill=color)


def character(d, cx, base_y, s, skin, hair, shirt, old=False):
    """A seated fan holding a controller. Old version: grey beard and glasses."""
    # torso
    d.rounded_rectangle([cx - 52 * s, base_y - 108 * s, cx + 52 * s, base_y - 8 * s],
                        radius=22, fill=shirt)
    # head
    d.ellipse([cx - 46 * s, base_y - 196 * s, cx + 46 * s, base_y - 104 * s], fill=skin)
    # hair
    if old:
        d.pieslice([cx - 48 * s, base_y - 200 * s, cx + 48 * s, base_y - 128 * s],
                   start=180, end=360, fill=(210, 210, 210))
        # grey beard
        d.rounded_rectangle([cx - 40 * s, base_y - 152 * s, cx + 40 * s, base_y - 96 * s],
                            radius=16, fill=(215, 215, 215))
        # eyes behind glasses
        d.ellipse([cx - 30 * s, base_y - 178 * s, cx - 8 * s, base_y - 156 * s],
                  outline=(30, 30, 30), width=3)
        d.ellipse([cx + 8 * s, base_y - 178 * s, cx + 30 * s, base_y - 156 * s],
                  outline=(30, 30, 30), width=3)
        d.line([(cx - 8 * s, base_y - 167 * s), (cx + 8 * s, base_y - 167 * s)],
               fill=(30, 30, 30), width=3)
    else:
        d.pieslice([cx - 48 * s, base_y - 200 * s, cx + 48 * s, base_y - 132 * s],
                   start=180, end=360, fill=hair)
        d.ellipse([cx - 48 * s, base_y - 168 * s, cx - 30 * s, base_y - 130 * s], fill=hair)
        d.ellipse([cx + 30 * s, base_y - 168 * s, cx + 48 * s, base_y - 130 * s], fill=hair)
        # eyes and a big grin
        d.ellipse([cx - 28 * s, base_y - 176 * s, cx - 12 * s, base_y - 160 * s], fill=(25, 25, 25))
        d.ellipse([cx + 12 * s, base_y - 176 * s, cx + 28 * s, base_y - 160 * s], fill=(25, 25, 25))
        d.arc([cx - 24 * s, base_y - 156 * s, cx + 24 * s, base_y - 122 * s],
              start=15, end=165, fill=(25, 25, 25), width=4)
    # arms down to the controller
    d.line([(cx - 44 * s, base_y - 96 * s), (cx - 22 * s, base_y - 40 * s)],
           fill=shirt, width=int(20 * s))
    d.line([(cx + 44 * s, base_y - 96 * s), (cx + 22 * s, base_y - 40 * s)],
           fill=shirt, width=int(20 * s))
    # controller
    d.rounded_rectangle([cx - 42 * s, base_y - 52 * s, cx + 42 * s, base_y - 8 * s],
                        radius=12, fill=(35, 35, 45))
    d.ellipse([cx - 30 * s, base_y - 44 * s, cx - 14 * s, base_y - 28 * s], fill=(90, 200, 120))
    d.ellipse([cx + 14 * s, base_y - 44 * s, cx + 30 * s, base_y - 28 * s], fill=(240, 90, 120))


def star_coin(d, cx, cy, r):
    """make.fun's magenta coin: a magenta disc with a white star."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(226, 0, 122))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=4)
    star(d, cx, cy, r * 0.62, (255, 255, 255))


def build():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- top panel: 2013, warm Vice City sunset ----
    top = vgrad((W, MID - 8), (255, 150, 60), (255, 80, 140))
    img.paste(top, (0, 0))
    d = ImageDraw.Draw(img)
    # big low sun, off to the left so it never sits behind the fan's head
    d.ellipse([120, 170, 280, 330], fill=(255, 235, 160))
    # skyline and palms along the bottom of the top panel
    skyline(d, MID - 8, 120, (120, 40, 90), seed=7, lit=(255, 210, 120))
    palm(d, 60, MID - 8, 1.1, (70, 20, 55))
    palm(d, 960, MID - 8, 0.95, (70, 20, 55))
    # headline and punchline
    text_center(d, W // 2, 26, "2013: GTA V just dropped", font(FONT_BOLD, 62),
                (255, 255, 255), outline=(30, 10, 40), width=5)
    text_center(d, W // 2, 100, "GTA 6 will be out in a couple years, right?",
                font(FONT_BOLD, 40), (255, 255, 255), outline=(30, 10, 40), width=4)
    # young fan on the couch
    couch(d, 330, 470, 420, 90, (150, 60, 60), (110, 40, 45))
    character(d, 540, 430, 1.0, (245, 200, 160), (90, 55, 30), (30, 160, 140))

    # ---- divider ----
    d.rectangle([0, MID - 8, W, MID + 8], fill=(255, 255, 255))
    d.rectangle([0, MID - 8, W, MID - 4], fill=(20, 20, 30))

    # ---- bottom panel: 2026, neon Vice City night ----
    bot = vgrad((W, H - MID - 8), (18, 12, 60), (80, 20, 110))
    img.paste(bot, (0, MID + 8))
    d = ImageDraw.Draw(img)
    rnd = random.Random(11)
    for _ in range(70):
        x = rnd.randint(10, W - 10)
        y = rnd.randint(MID + 20, MID + 240)
        r = rnd.randint(1, 3)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))
    skyline(d, H - 60, 150, (12, 8, 40), seed=21, lit=(0, 220, 255))
    skyline(d, H - 60, 100, (25, 12, 70), seed=33, lit=(255, 60, 200))
    # headline and punchline
    text_center(d, W // 2, MID + 28, "2026: GTA VI LAUNCH DAY", font(FONT_BOLD, 62),
                (255, 255, 255), outline=(10, 5, 25), width=5)
    text_center(d, W // 2, MID + 102, "13 years. Worth it.", font(FONT_BOLD, 42),
                (255, 255, 255), outline=(10, 5, 25), width=4)
    # the same fan, now old, on the same couch, lifted so the name fits below
    couch(d, 300, 965, 420, 90, (150, 60, 60), (110, 40, 45))
    character(d, 510, 925, 1.0, (245, 200, 160), (90, 55, 30), (60, 90, 160), old=True)
    # make.fun ghost floats in from the right, holding its star coin
    ghost = Image.open("assets/mark-1024.png").convert("RGBA").resize((215, 215))
    img.paste(ghost, (800, 700), ghost)
    star_coin(d, 968, 852, 38)
    # the make.fun name, big and readable, bottom centre
    text_center(d, W // 2, 1018, "make.fun", font(FONT_BOLD, 52),
                (255, 255, 255), outline=(10, 5, 25), width=4)

    return img


if __name__ == "__main__":
    meme = build()
    meme.save("meme.png")
    print("wrote meme.png", meme.size)
