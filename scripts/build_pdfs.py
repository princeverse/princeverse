#!/usr/bin/env python3
"""
Build script for the "Balance & Bloom" Budget Planner Bundle.
Renders each HTML page to a print-ready US Letter PDF via headless Chromium,
then assembles the full bundle PDF.

Usage:
    python3 scripts/build_pdfs.py
"""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_DIR = ROOT / "products" / "budget-planner-bundle"
HTML_DIR = PRODUCT_DIR / "html"
PDF_DIR = PRODUCT_DIR / "pdf"
CHROMIUM_PATH = "/opt/pw-browsers/chromium"

# Ordered pages: (html filename, output pdf filename)
PAGES = [
    ("00_cover.html", "00_Cover.pdf"),
    ("01_monthly_budget.html", "01_Monthly_Budget_Tracker.pdf"),
    ("02_debt_payoff.html", "02_Debt_Payoff_Tracker.pdf"),
    ("03_savings_goal.html", "03_Savings_Goal_Tracker.pdf"),
    ("04_bill_tracker.html", "04_Annual_Bill_Tracker.pdf"),
    ("05_expense_log.html", "05_Weekly_Expense_Log.pdf"),
    ("06_thankyou.html", "06_Thank_You_Guide.pdf"),
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

    # Assemble full bundle (skip the thank-you page duplicate ordering not needed, include all in order)
    writer = PdfWriter()
    for pdf_path in individual_pdfs:
        writer.append(str(pdf_path))
    bundle_path = PRODUCT_DIR / "Balance-and-Bloom-Budget-Planner-Bundle.pdf"
    with open(bundle_path, "wb") as f:
        writer.write(f)
    print(f"Bundle written to {bundle_path}")


if __name__ == "__main__":
    render_all()
