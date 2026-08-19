#!/usr/bin/env python3
"""Composite a square Etsy listing thumbnail mockup from rendered page screenshots.
No external AI image generation used — pure PIL compositing, zero cost.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_DIR = ROOT / "products" / "budget-planner-bundle"
OUT = PRODUCT_DIR / "listing-thumbnail.png"

SIZE = 2000
BG = (248, 244, 236)       # ivory
ACCENT = (124, 143, 110)   # sage
ACCENT_DARK = (86, 99, 74)
INK = (63, 58, 52)


def load_font(bold=False, italic=False, size=40):
    candidates = []
    if bold:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
        ]
    elif italic:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
        ]
    else:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
        ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def load_sans(size=28, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def drop_shadow(size, radius=30, opacity=90):
    shadow = Image.new("RGBA", (size[0] + radius * 4, size[1] + radius * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(shadow)
    d.rectangle([radius * 2, radius * 2, radius * 2 + size[0], radius * 2 + size[1]], fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius))
    return shadow


def paste_rotated_card(canvas, img_path, center, target_w, angle, border=10):
    img = Image.open(img_path).convert("RGB")
    w, h = img.size
    scale = target_w / w
    img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    img = ImageOps.expand(img, border=border, fill=(255, 255, 255))
    img = ImageOps.expand(img, border=2, fill=(207, 199, 180))
    img = img.convert("RGBA")  # so rotation fills new corners with transparency, not black

    shadow = drop_shadow(img.size, radius=24, opacity=70).rotate(-angle, expand=True, resample=Image.BICUBIC)
    rotated = img.rotate(-angle, expand=True, resample=Image.BICUBIC, fillcolor=(0, 0, 0, 0))

    sx = center[0] - shadow.width // 2 + 14
    sy = center[1] - shadow.height // 2 + 22
    canvas.paste(shadow, (sx, sy), shadow)

    rx = center[0] - rotated.width // 2
    ry = center[1] - rotated.height // 2
    canvas.paste(rotated, (rx, ry), rotated)


def main():
    canvas = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(canvas)

    # soft background texture: large faint circle accents
    overlay = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([-400, -400, 700, 700], fill=ACCENT + (18,))
    od.ellipse([SIZE - 700, SIZE - 700, SIZE + 400, SIZE + 400], fill=ACCENT + (18,))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)

    # fanned page cards
    paste_rotated_card(canvas, "/tmp/hires_03_savings_goal.png", (SIZE // 2 - 330, SIZE // 2 + 260), 620, -9)
    paste_rotated_card(canvas, "/tmp/hires_01_monthly_budget.png", (SIZE // 2 + 340, SIZE // 2 + 280), 620, 8)
    paste_rotated_card(canvas, "/tmp/hires_00_cover.png", (SIZE // 2, SIZE // 2 + 150), 660, 0)

    # top kicker + title band
    draw.rectangle([0, 0, SIZE, 330], fill=BG)
    kicker_font = load_sans(size=30, bold=True)
    title_font = load_font(bold=False, size=92)
    sub_font = load_sans(size=32)

    kicker = "B A L A N C E   &   B L O O M"
    kw = draw.textlength(kicker, font=kicker_font)
    draw.text(((SIZE - kw) / 2, 60), kicker, font=kicker_font, fill=ACCENT_DARK)

    title1 = "Budget & Savings"
    title2 = "Planner Bundle"
    t1w = draw.textlength(title1, font=title_font)
    t2w = draw.textlength(title2, font=title_font)
    draw.text(((SIZE - t1w) / 2, 115), title1, font=title_font, fill=INK)
    draw.text(((SIZE - t2w) / 2, 215), title2, font=title_font, fill=INK)

    # bottom badge strip
    badge_font = load_sans(size=30, bold=True)
    badge_text = "6 PRINTABLE PAGES  •  INSTANT DOWNLOAD  •  US LETTER PDF"
    bw = draw.textlength(badge_text, font=badge_font)
    pad = 30
    bx0 = (SIZE - bw) / 2 - pad
    by0 = SIZE - 150
    bx1 = (SIZE + bw) / 2 + pad
    by1 = SIZE - 90
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=30, fill=ACCENT)
    draw.text(((SIZE - bw) / 2, by0 + 14), badge_text, font=badge_font, fill=(255, 255, 255))

    canvas.save(OUT, quality=95)
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
