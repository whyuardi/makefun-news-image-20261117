#!/usr/bin/env python3
"""Composite the 17 Nov 2026 news image: resize the generated base art to
1024x1024, then overlay exact-text caption bars (PIL, DejaVu Sans Bold) so
every word is spelled right and legible.

Layout (1024x1024, measured off the base art):
  TL aid trucks     -> "GAZA AID PLEA"
  TR damaged bridge -> "CRIMEAN BRIDGE HIT"
  MR burning tanker -> "HORMUZ TANKER MINED"
  BL summit hall    -> "COP31 CLIMATE DEAL"
  BC fighter jets   -> "JAPAN SCRAMBLES JETS"
  BR three leaders  -> "XI-TRUMP-PUTIN SUMMIT"
  (ML jets panel is left uncaptioned: the same jets story, already
  captioned at BC, and jets need no label to be read as jets.)
Footer band: "TUESDAY 17 NOVEMBER 2026 - THE WORLD IN ONE DAY".

Output: comp.jpg (JPEG, quality 88), must stay <= 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "media-generation-news-17nov-base-0-627ef97b-40e8-4c53-ba12-25d09456f53d.jpg"
OUT = "comp.jpg"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# (label, bar x0, y0, x1, y1)
CAPTIONS = [
    ("GAZA AID PLEA", 83, 239, 499, 275),
    ("CRIMEAN BRIDGE HIT", 544, 278, 1024, 314),
    ("HORMUZ TANKER MINED", 717, 572, 1024, 608),
    ("COP31 CLIMATE DEAL", 26, 924, 333, 960),
    ("JAPAN SCRAMBLES JETS", 352, 940, 691, 976),
    ("XI-TRUMP-PUTIN SUMMIT", 710, 924, 1024, 960),
]
FOOTER = "TUESDAY 17 NOVEMBER 2026  -  THE WORLD IN ONE DAY"


def fit_font(draw, text, max_w, start=30, floor=20):
    size = start
    while size > floor:
        f = ImageFont.truetype(BOLD, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 1
    return ImageFont.truetype(BOLD, floor)


def main():
    im = Image.open(SRC).convert("RGB")
    im = im.resize((1024, 1024), Image.LANCZOS)
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)

    for label, x0, y0, x1, y1 in CAPTIONS:
        od.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 175))

    # Footer band naming the day.
    od.rectangle([0, 986, 1024, 1024], fill=(8, 22, 40, 255))
    im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(im)

    # Text goes on AFTER the composite, or the dark bars dim it.
    for label, x0, y0, x1, y1 in CAPTIONS:
        f = fit_font(draw, label, (x1 - x0) - 24)
        th = f.getbbox(label)[3] - f.getbbox(label)[1]
        draw.text((x0 + 12, y0 + (y1 - y0 - th) // 2 - 2), label,
                  font=f, fill=(255, 255, 255))

    f = fit_font(draw, FOOTER, 1024 - 40, start=30)
    tw = draw.textlength(FOOTER, font=f)
    th = f.getbbox(FOOTER)[3] - f.getbbox(FOOTER)[1]
    draw.text(((1024 - tw) // 2, 986 + (38 - th) // 2 - 2), FOOTER,
              font=f, fill=(255, 255, 255))

    im.save(OUT, "JPEG", quality=88)
    import os
    print(f"{OUT}: {im.size}, {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
