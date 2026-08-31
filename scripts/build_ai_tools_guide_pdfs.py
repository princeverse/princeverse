#!/usr/bin/env python3
"""
Build script for the "Signal Stack" AI Tools for Sales & Marketing guide.
Renders each HTML page to a print-ready US Letter PDF via headless Chromium,
then assembles the full bundle PDF.

Usage:
    python3 scripts/build_ai_tools_guide_pdfs.py
"""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_DIR = ROOT / "products" / "ai-sales-tools-guide"
HTML_DIR = PRODUCT_DIR / "html"
PDF_DIR = PRODUCT_DIR / "pdf"
CHROMIUM_PATH = "/opt/pw-browsers/chromium"

# Ordered pages: (html filename, output pdf filename)
PAGES = [
    ("00_cover.html", "00_Cover.pdf"),
    ("01_how_to_use.html", "01_How_To_Use_This_Guide.pdf"),
    ("02_visitor_intel.html", "02_Website_Visitor_ID_And_Intent.pdf"),
    ("03_data_enrichment.html", "03_Data_Enrichment_And_Waterfalls.pdf"),
    ("04_ai_outbound.html", "04_AI_SDRs_And_Outbound_Sequencing.pdf"),
    ("05_ai_voice.html", "05_AI_Voice_And_Conversational_Sales.pdf"),
    ("06_comparison_table.html", "06_Tool_Comparison_At_A_Glance.pdf"),
    ("07_build_your_stack.html", "07_Build_Your_Stack.pdf"),
    ("08_thankyou.html", "08_Thank_You.pdf"),
]


def find_chromium():
    candidates = [
        CHROMIUM_PATH,
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    # fall back: let playwright find its own installed browser
    return None


def render_all():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    chromium_path = find_chromium()

    with sync_playwright() as p:
        launch_kwargs = {}
        if chromium_path:
            launch_kwargs["executable_path"] = chromium_path
        browser = p.chromium.launch(**launch_kwargs)
        page = browser.new_page()

        individual_pdfs = []
        for html_name, pdf_name in PAGES:
            html_path = HTML_DIR / html_name
            pdf_path = PDF_DIR / pdf_name
            page.goto(f"file://{html_path}")
            page.pdf(
                path=str(pdf_path),
                format="Letter",
                print_background=True,
                margin={"top": "0in", "bottom": "0in", "left": "0in", "right": "0in"},
            )
            individual_pdfs.append(pdf_path)
            print(f"Rendered {pdf_path.name}")

        browser.close()

    # Assemble full bundle
    writer = PdfWriter()
    for pdf_path in individual_pdfs:
        writer.append(str(pdf_path))
    bundle_path = PRODUCT_DIR / "Signal-Stack-AI-Sales-Marketing-Tools-Guide.pdf"
    with open(bundle_path, "wb") as f:
        writer.write(f)
    print(f"Bundle written to {bundle_path}")


if __name__ == "__main__":
    render_all()
