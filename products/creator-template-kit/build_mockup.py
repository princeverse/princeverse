from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from pathlib import Path

OUT = Path("/home/user/princeverse/products/creator-template-kit/listing-thumbnail.png")
SIZE = 2000
BG = (248, 244, 236)
ACCENT = (124, 143, 110)
ACCENT_DARK = (86, 99, 74)
GOLD = (200, 162, 74)
INK = (63, 58, 52)

def load_font(bold=False, size=40):
    c = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    return ImageFont.truetype(c, size)

def load_sans(size=28, bold=False):
    c = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(c, size)

def drop_shadow(size, radius=28, opacity=80):
    shadow = Image.new("RGBA", (size[0]+radius*4, size[1]+radius*4), (0,0,0,0))
    d = ImageDraw.Draw(shadow)
    d.rectangle([radius*2, radius*2, radius*2+size[0], radius*2+size[1]], fill=(0,0,0,opacity))
    return shadow.filter(ImageFilter.GaussianBlur(radius))

def paste_card(canvas, img_path, center, target_w, angle, border=10):
    img = Image.open(img_path).convert("RGB")
    w, h = img.size
    scale = target_w / w
    img = img.resize((int(w*scale), int(h*scale)), Image.LANCZOS)
    img = ImageOps.expand(img, border=border, fill=(255,255,255))
    img = ImageOps.expand(img, border=2, fill=(207,199,180))
    img = img.convert("RGBA")
    shadow = drop_shadow(img.size).rotate(-angle, expand=True, resample=Image.BICUBIC)
    rotated = img.rotate(-angle, expand=True, resample=Image.BICUBIC, fillcolor=(0,0,0,0))
    sx = center[0]-shadow.width//2+12
    sy = center[1]-shadow.height//2+20
    canvas.paste(shadow, (sx, sy), shadow)
    rx = center[0]-rotated.width//2
    ry = center[1]-rotated.height//2
    canvas.paste(rotated, (rx, ry), rotated)

canvas = Image.new("RGB", (SIZE, SIZE), BG)
overlay = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
od = ImageDraw.Draw(overlay)
od.ellipse([-400,-400,700,700], fill=ACCENT+(18,))
od.ellipse([SIZE-700,SIZE-700,SIZE+400,SIZE+400], fill=GOLD+(20,))
canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
draw = ImageDraw.Draw(canvas)

paste_card(canvas, "/tmp/kit_tips.png", (SIZE//2-340, SIZE//2+270), 620, -8)
paste_card(canvas, "/tmp/kit_brand.png", (SIZE//2+340, SIZE//2+290), 620, 8)
paste_card(canvas, "/tmp/kit_quote.png", (SIZE//2, SIZE//2+160), 660, 0)

draw.rectangle([0,0,SIZE,320], fill=BG)
kicker_font = load_sans(30, bold=True)
title_font = load_font(bold=False, size=88)

kicker = "B L O O M   C R E A T O R   K I T"
kw = draw.textlength(kicker, font=kicker_font)
draw.text(((SIZE-kw)/2, 60), kicker, font=kicker_font, fill=ACCENT_DARK)

t1, t2 = "Instagram Post", "Template Kit"
t1w = draw.textlength(t1, font=title_font)
t2w = draw.textlength(t2, font=title_font)
draw.text(((SIZE-t1w)/2, 115), t1, font=title_font, fill=INK)
draw.text(((SIZE-t2w)/2, 215), t2, font=title_font, fill=INK)

badge_font = load_sans(28, bold=True)
badge_text = "7 POST TEMPLATES + BRAND KIT  •  CANVA + POWERPOINT  •  INSTANT DOWNLOAD"
bw = draw.textlength(badge_text, font=badge_font)
pad = 30
bx0 = (SIZE-bw)/2 - pad
by0 = SIZE-150
bx1 = (SIZE+bw)/2 + pad
by1 = SIZE-90
draw.rounded_rectangle([bx0,by0,bx1,by1], radius=30, fill=GOLD)
draw.text(((SIZE-bw)/2, by0+14), badge_text, font=badge_font, fill=(255,255,255))

canvas.save(OUT, quality=95)
print(f"Saved {OUT}")
