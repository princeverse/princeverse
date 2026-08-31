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
  ai-sales-tools-guide/     — Product #2: ready to publish
    Signal-Stack-AI-Sales-Marketing-Tools-Guide.pdf ← upload this as the digital file
    listing-thumbnail.png                          ← upload this as the main photo
    listing-copy.md                                ← title/tags/description, paste-ready
    html/                                           ← editable source (colors, text, new pages)
    pdf/                                             ← individual page PDFs
scripts/
  build_pdfs.py                  — renders budget-planner-bundle html/*.html → PDFs + bundle
  build_mockup.py                — composites the budget-planner-bundle listing thumbnail
  build_ai_tools_guide_pdfs.py   — renders ai-sales-tools-guide html/*.html → PDFs + bundle
  build_ai_tools_guide_mockup.py — composites the ai-sales-tools-guide listing thumbnail
```

## Quick start: publish a product

1. Open `products/<name>/listing-copy.md` (e.g. `products/budget-planner-bundle/`
   or `products/ai-sales-tools-guide/`).
2. In Etsy Shop Manager → Listings → Add a listing, upload:
   - **Digital file:** the bundle PDF in that product's folder
   - **Photo 1:** that product's `listing-thumbnail.png`
3. Copy the title, tags, description, and price straight from `listing-copy.md`.
4. Publish.

## Regenerating or editing a product

Edit the HTML/CSS in `products/<name>/html/`, then rebuild with that
product's own build scripts:

```bash
pip install playwright pypdf cffi Pillow --quiet

# budget-planner-bundle
python3 scripts/build_pdfs.py     # renders pages + assembles the bundle PDF
python3 scripts/build_mockup.py   # rebuilds the listing thumbnail

# ai-sales-tools-guide
python3 scripts/build_ai_tools_guide_pdfs.py     # renders pages + assembles the bundle PDF
python3 scripts/build_ai_tools_guide_mockup.py   # rebuilds the listing thumbnail
```

Chromium is expected at `/opt/pw-browsers/chromium` (already available in
Claude Code's remote environment).

## No Etsy account access

Nothing in this repo can publish to Etsy directly — there's no Etsy API
connector attached to this environment. Every product is built to the point
of "upload and hit publish," but that last step is manual, by design.

## Note on compiled files

The compiled PDF/PNG outputs (the actual bundle PDFs, individual page PDFs,
and listing thumbnails) are committed to this repo so a listing can be
published straight from a fresh clone. If you edit a product's HTML source,
re-run that product's build scripts (above) and commit the regenerated
outputs alongside your source changes.
