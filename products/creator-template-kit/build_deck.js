const pptxgen = require("pptxgenjs");

// ---- Palette (matches the Balance & Bloom store aesthetic, extended with a gold accent) ----
const INK = "3F3A34";
const ACCENT = "7C8F6E";       // sage
const ACCENT_DARK = "56634A";
const BG = "F8F4EC";           // ivory
const GOLD = "C8A24A";
const WHITE = "FFFFFF";
const LINE = "CFC7B4";
const PLACEHOLDER = "E7E1D3";  // soft neutral for photo placeholders

const HEAD_FONT = "Cambria";
const BODY_FONT = "Calibri";

function newDeck() {
  const pres = new pptxgen();
  pres.defineLayout({ name: "INSTA_SQUARE", width: 10, height: 10 });
  pres.layout = "INSTA_SQUARE";
  return pres;
}

function badge(slide, num) {
  slide.addShape("ellipse", { x: 0.5, y: 0.5, w: 0.55, h: 0.55, fill: { color: ACCENT }, line: { type: "none" } });
  slide.addText(String(num).padStart(2, "0"), {
    x: 0.5, y: 0.5, w: 0.55, h: 0.55, align: "center", valign: "middle",
    fontFace: BODY_FONT, fontSize: 13, bold: true, color: WHITE, margin: 0,
  });
}

function kicker(slide, text) {
  slide.addText(text, {
    x: 1.25, y: 0.62, w: 7, h: 0.35, fontFace: BODY_FONT, fontSize: 11,
    color: ACCENT_DARK, bold: true, charSpacing: 2, margin: 0,
  });
}

function photoPlaceholder(slide, x, y, w, h, label) {
  slide.addShape("roundRect", {
    x, y, w, h, rectRadius: 0.12, fill: { color: PLACEHOLDER }, line: { color: LINE, width: 1 },
  });
  slide.addShape("ellipse", {
    x: x + w / 2 - 0.35, y: y + h / 2 - 0.55, w: 0.7, h: 0.7,
    fill: { color: WHITE }, line: { color: ACCENT, width: 1.5 },
  });
  slide.addText("+", {
    x: x + w / 2 - 0.35, y: y + h / 2 - 0.55, w: 0.7, h: 0.7,
    align: "center", valign: "middle", fontFace: BODY_FONT, fontSize: 28, color: ACCENT, margin: 0,
  });
  slide.addText(label || "Replace with your photo", {
    x: x, y: y + h / 2 + 0.25, w: w, h: 0.4, align: "center",
    fontFace: BODY_FONT, fontSize: 11, italic: true, color: ACCENT_DARK, margin: 0,
  });
}

const pres = newDeck();

// ---------------------------------------------------------------------------
// Slide 1 — Quote Post
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: BG };
  badge(s, 1);
  kicker(s, "BLOOM CREATOR KIT  ·  QUOTE POST");

  s.addText(`“Your quote or caption\ngoes right here —\nswap this text for\nyour own words.”`, {
    x: 0.8, y: 3.0, w: 8.4, h: 3.6, align: "center", valign: "middle",
    fontFace: HEAD_FONT, italic: true, fontSize: 34, color: INK, lineSpacing: 42, margin: 0,
  });

  s.addText("@youraccount", {
    x: 0.8, y: 8.4, w: 8.4, h: 0.5, align: "center",
    fontFace: BODY_FONT, fontSize: 13, color: ACCENT_DARK, bold: true, charSpacing: 1, margin: 0,
  });
}

// ---------------------------------------------------------------------------
// Slide 2 — Product / Service Highlight
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  badge(s, 2);
  kicker(s, "PRODUCT HIGHLIGHT POST");

  photoPlaceholder(s, 0.8, 1.5, 4.2, 6.5, "Product / lifestyle photo");

  s.addText("New\nArrival", {
    x: 5.3, y: 2.0, w: 4.0, h: 1.8, fontFace: HEAD_FONT, fontSize: 40, color: INK, bold: false, lineSpacing: 42, margin: 0,
  });
  s.addText("A short, benefit-driven description of the product goes here — keep it to two lines.", {
    x: 5.3, y: 3.9, w: 3.9, h: 1.3, fontFace: BODY_FONT, fontSize: 14, color: INK, lineSpacing: 20, margin: 0,
  });
  s.addText("$00", {
    x: 5.3, y: 5.4, w: 3.9, h: 0.6, fontFace: HEAD_FONT, fontSize: 26, color: ACCENT_DARK, bold: true, margin: 0,
  });
  s.addShape("roundRect", {
    x: 5.3, y: 6.3, w: 2.6, h: 0.62, rectRadius: 0.12, fill: { color: ACCENT }, line: { type: "none" },
  });
  s.addText("Shop Now →", {
    x: 5.3, y: 6.3, w: 2.6, h: 0.62, align: "center", valign: "middle",
    fontFace: BODY_FONT, fontSize: 13, bold: true, color: WHITE, margin: 0,
  });
}

// ---------------------------------------------------------------------------
// Slide 3 — Tips / Listicle
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: BG };
  badge(s, 3);
  kicker(s, "TIPS / LISTICLE POST");

  s.addText("3 Tips For\n[Your Topic]", {
    x: 0.8, y: 1.4, w: 8.4, h: 1.7, fontFace: HEAD_FONT, fontSize: 36, color: INK, lineSpacing: 40, margin: 0,
  });

  const tips = [
    ["Tip headline one", "One or two lines expanding on the first tip goes here."],
    ["Tip headline two", "One or two lines expanding on the second tip goes here."],
    ["Tip headline three", "One or two lines expanding on the third tip goes here."],
  ];
  let ty = 3.55;
  tips.forEach((tip, i) => {
    s.addShape("ellipse", { x: 0.8, y: ty, w: 0.55, h: 0.55, fill: { color: GOLD }, line: { type: "none" } });
    s.addText(String(i + 1), {
      x: 0.8, y: ty, w: 0.55, h: 0.55, align: "center", valign: "middle",
      fontFace: BODY_FONT, fontSize: 15, bold: true, color: WHITE, margin: 0,
    });
    s.addText(tip[0], {
      x: 1.6, y: ty - 0.05, w: 7.0, h: 0.4, fontFace: BODY_FONT, fontSize: 17, bold: true, color: INK, margin: 0,
    });
    s.addText(tip[1], {
      x: 1.6, y: ty + 0.38, w: 7.0, h: 0.6, fontFace: BODY_FONT, fontSize: 13, color: ACCENT_DARK, lineSpacing: 17, margin: 0,
    });
    ty += 1.55;
  });
}

// ---------------------------------------------------------------------------
// Slide 4 — Testimonial
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  badge(s, 4);
  kicker(s, "TESTIMONIAL POST");

  s.addText("“", {
    x: 0.6, y: 1.6, w: 2.0, h: 2.0, fontFace: HEAD_FONT, fontSize: 120, color: GOLD, margin: 0,
  });

  s.addText("This is where a short, glowing customer testimonial goes — two to three sentences works best.", {
    x: 1.0, y: 3.5, w: 8.0, h: 2.2, align: "center", valign: "middle",
    fontFace: HEAD_FONT, italic: true, fontSize: 26, color: INK, lineSpacing: 34, margin: 0,
  });

  s.addShape("ellipse", { x: 4.4, y: 6.3, w: 0.8, h: 0.8, fill: { color: PLACEHOLDER }, line: { color: ACCENT, width: 1.2 } });
  s.addText("Client Name", {
    x: 2.5, y: 7.25, w: 5.0, h: 0.4, align: "center", fontFace: BODY_FONT, fontSize: 15, bold: true, color: INK, margin: 0,
  });
  s.addText("★ ★ ★ ★ ★", {
    x: 2.5, y: 7.65, w: 5.0, h: 0.4, align: "center", fontFace: BODY_FONT, fontSize: 16, color: GOLD, margin: 0,
  });
}

// ---------------------------------------------------------------------------
// Slide 5 — Announcement / Sale
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: ACCENT_DARK };
  s.addShape("ellipse", { x: 0.5, y: 0.5, w: 0.55, h: 0.55, fill: { color: GOLD }, line: { type: "none" } });
  s.addText("05", {
    x: 0.5, y: 0.5, w: 0.55, h: 0.55, align: "center", valign: "middle",
    fontFace: BODY_FONT, fontSize: 13, bold: true, color: WHITE, margin: 0,
  });
  s.addText("ANNOUNCEMENT POST", {
    x: 1.25, y: 0.62, w: 7, h: 0.35, fontFace: BODY_FONT, fontSize: 11,
    color: BG, bold: true, charSpacing: 2, margin: 0,
  });

  s.addText("Big News\nStarts Today", {
    x: 0.8, y: 3.2, w: 8.4, h: 2.4, align: "center", valign: "middle",
    fontFace: HEAD_FONT, fontSize: 46, color: WHITE, lineSpacing: 52, margin: 0,
  });
  s.addText("A short supporting line about the announcement goes here.", {
    x: 1.3, y: 5.6, w: 7.4, h: 0.6, align: "center",
    fontFace: BODY_FONT, fontSize: 15, color: BG, margin: 0,
  });

  s.addShape("roundRect", {
    x: 3.5, y: 6.6, w: 3.0, h: 0.7, rectRadius: 0.14, fill: { color: GOLD }, line: { type: "none" },
  });
  s.addText("Shop The Sale", {
    x: 3.5, y: 6.6, w: 3.0, h: 0.7, align: "center", valign: "middle",
    fontFace: BODY_FONT, fontSize: 14, bold: true, color: INK, margin: 0,
  });
}

// ---------------------------------------------------------------------------
// Slide 6 — Behind the Brand / Founder
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: BG };
  badge(s, 6);
  kicker(s, "BEHIND THE BRAND POST");

  photoPlaceholder(s, 0.8, 2.0, 3.8, 3.8, "Founder photo");

  s.addText("Meet The\nMaker", {
    x: 5.0, y: 2.1, w: 4.2, h: 1.6, fontFace: HEAD_FONT, fontSize: 32, color: INK, lineSpacing: 36, margin: 0,
  });
  s.addText("A few warm sentences introducing you or your brand — who you are, what you make, and why it matters to your customer.", {
    x: 5.0, y: 3.75, w: 4.1, h: 2.0, fontFace: BODY_FONT, fontSize: 14, color: INK, lineSpacing: 20, margin: 0,
  });

  s.addText("est. 2026", {
    x: 0.8, y: 6.1, w: 3.8, h: 0.4, align: "center",
    fontFace: BODY_FONT, fontSize: 12, italic: true, color: ACCENT_DARK, margin: 0,
  });
}

// ---------------------------------------------------------------------------
// Slide 7 — Swipe / Carousel Intro
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  badge(s, 7);
  kicker(s, "CAROUSEL INTRO POST");

  s.addText("5 Mistakes\nto Avoid When\n[Doing The Thing]", {
    x: 0.8, y: 2.6, w: 8.4, h: 3.6, align: "center", valign: "middle",
    fontFace: HEAD_FONT, fontSize: 38, color: INK, lineSpacing: 44, margin: 0,
  });

  s.addShape("roundRect", {
    x: 3.65, y: 7.4, w: 2.7, h: 0.62, rectRadius: 0.12, fill: { color: ACCENT }, line: { type: "none" },
  });
  s.addText("Swipe to see more →", {
    x: 3.65, y: 7.4, w: 2.7, h: 0.62, align: "center", valign: "middle",
    fontFace: BODY_FONT, fontSize: 12, bold: true, color: WHITE, margin: 0,
  });
}

// ---------------------------------------------------------------------------
// Slide 8 — Mini Brand Kit / How to Customize
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: BG };
  badge(s, 8);
  kicker(s, "YOUR MINI BRAND KIT");

  s.addText("Color Palette", {
    x: 0.8, y: 1.5, w: 8.4, h: 0.4, fontFace: BODY_FONT, fontSize: 15, bold: true, color: INK, margin: 0,
  });
  const swatches = [
    [INK, "Ink"], [ACCENT, "Sage"], [ACCENT_DARK, "Deep Sage"], [GOLD, "Gold"], [BG, "Ivory"],
  ];
  let sx = 0.8;
  swatches.forEach(([color, label]) => {
    s.addShape("roundRect", { x: sx, y: 2.05, w: 1.4, h: 1.0, rectRadius: 0.08, fill: { color }, line: { color: LINE, width: 1 } });
    s.addText(`${label}\n#${color}`, {
      x: sx, y: 3.1, w: 1.4, h: 0.55, align: "center", fontFace: BODY_FONT, fontSize: 9, color: ACCENT_DARK, lineSpacing: 12, margin: 0,
    });
    sx += 1.6;
  });

  s.addText("Font Pairing", {
    x: 0.8, y: 4.3, w: 8.4, h: 0.4, fontFace: BODY_FONT, fontSize: 15, bold: true, color: INK, margin: 0,
  });
  s.addText("Headline — Cambria", {
    x: 0.8, y: 4.8, w: 8.0, h: 0.55, fontFace: HEAD_FONT, fontSize: 22, color: INK, margin: 0,
  });
  s.addText("Body — Calibri", {
    x: 0.8, y: 5.4, w: 8.0, h: 0.5, fontFace: BODY_FONT, fontSize: 16, color: INK, margin: 0,
  });

  s.addText("Brand Voice", {
    x: 0.8, y: 6.1, w: 8.4, h: 0.4, fontFace: BODY_FONT, fontSize: 15, bold: true, color: INK, margin: 0,
  });
  const words = ["calm", "warm", "honest", "unfussy"];
  let wx = 0.8;
  words.forEach((w) => {
    const width = 0.55 + w.length * 0.12;
    s.addShape("roundRect", { x: wx, y: 6.6, w: width, h: 0.5, rectRadius: 0.25, fill: { color: WHITE }, line: { color: ACCENT, width: 1 } });
    s.addText(w, {
      x: wx, y: 6.6, w: width, h: 0.5, align: "center", valign: "middle", fontFace: BODY_FONT, fontSize: 12, color: ACCENT_DARK, margin: 0,
    });
    wx += width + 0.2;
  });

  s.addText("How to customize: open in PowerPoint, Google Slides, or import into Canva. Click any text box to edit. Right-click a photo placeholder → “Change Picture” to add your own.", {
    x: 0.8, y: 7.6, w: 8.4, h: 1.5, fontFace: BODY_FONT, fontSize: 12, italic: true, color: ACCENT_DARK, lineSpacing: 17, margin: 0,
  });
}

pres.writeFile({ fileName: "Bloom-Creator-Kit-Instagram-Templates.pptx" }).then(() => {
  console.log("Deck written.");
});
