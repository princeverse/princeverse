# Princeverse — Etsy Digital Products

A working repo for building and launching digital products for an Etsy shop.
Start here: **[`strategy/ETSY_STRATEGY.md`](strategy/ETSY_STRATEGY.md)** for
the full market research, positioning, pricing, and 6-month roadmap.

## What's in here

```
strategy/
  ETSY_STRATEGY.md          — full strategy: research, pricing, SEO, roadmap
products/
  budget-planner-bundle/    — Product #1: ready to publish
    Balance-and-Bloom-Budget-Planner-Bundle.pdf   ← upload this as the digital file
    listing-thumbnail.png                          ← upload this as the main photo
    listing-copy.md                                ← title/tags/description, paste-ready
    html/                                           ← editable source (colors, text, new pages)
    pdf/                                             ← individual page PDFs
scripts/
  build_pdfs.py    — renders html/*.html → print-ready PDFs + assembles the bundle
  build_mockup.py  — composites the Etsy listing thumbnail from page renders
```

## Quick start: publish Product #1

1. Open `products/budget-planner-bundle/listing-copy.md`.
2. In Etsy Shop Manager → Listings → Add a listing, upload:
   - **Digital file:** `products/budget-planner-bundle/Balance-and-Bloom-Budget-Planner-Bundle.pdf`
   - **Photo 1:** `products/budget-planner-bundle/listing-thumbnail.png`
3. Copy the title, tags, description, and price straight from `listing-copy.md`.
4. Publish.

## Regenerating or editing a product

Edit the HTML/CSS in `products/<name>/html/`, then rebuild:

```bash
pip install playwright pypdf cffi Pillow --quiet
python3 scripts/build_pdfs.py     # renders pages + assembles the bundle PDF
python3 scripts/build_mockup.py   # rebuilds the listing thumbnail
```

Chromium is expected at `/opt/pw-browsers/chromium` (already available in
Claude Code's remote environment).

## No Etsy account access

Nothing in this repo can publish to Etsy directly — there's no Etsy API
connector attached to this environment. Every product is built to the point
of "upload and hit publish," but that last step is manual, by design.
