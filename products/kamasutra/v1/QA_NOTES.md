# QA Notes — The Kamasutra Guide (draft 1)

Status: **Draft, not uploaded or published.** Static checks only — no headless
browser was available in this environment for this pass (After.9's QA_REPORT.md
used Playwright; that isn't installed here). Recommend a real-device or
browser check before this goes live, the same way a Safari spot-check was
flagged as outstanding for the After.9 products.

## What was checked

- **JS syntax** — inline script extracted and validated with `node --check`. Passed. (One bug — a stray Python-style ternary left over from drafting — was caught and fixed before this check.)
- **HTML structure** — parsed with Python's `html.parser`; no unclosed or mismatched tags.
- **Element wiring** — every DOM id referenced by the script (`cover`, `browse`, `detail`, filter chip containers, detail fields, etc.) exists exactly once in the markup.
- **Data integrity** — 36 entries, all unique ids, all unique names, 12/12/12 split across chapters, 12/12/12 split across each of energy/flexibility/experience, no missing required fields.
- **Brand consistency** — "After.9" used correctly throughout (zero instances of "After 9" without the period).
- **Content register** — scanned for the same coercive-phrasing patterns flagged in the After.9 QA pass ("no matter what," "no complaints," "whatever your partner," "must/has to/owe," etc.) — none present. Scanned separately for explicit/clinical/graphic terms — none present; content stays descriptive throughout.
- **Accessibility basics** — every interactive element is a real `<button>`; no `<div onclick>` pseudo-buttons.
- **No network dependency beyond Google Fonts** — same pattern as the rest of the collection; declares system-font fallbacks.
- **No data collection** — only `localStorage` write is the favorites list (an array of position ids); no other storage, no analytics, no external calls.

## Not yet done

- No visual/overflow testing at the required screen widths (320–430px) — the CSS reuses the exact patterns already QA'd for that in Truth or Temptation (`clamp()` typography, `env(safe-area-inset-*)`, `overflow-x: hidden`, flexible card/button layout), so risk is low, but this hasn't been independently confirmed the way the After.9 files were.
- No manual click-through of every filter combination, search, favorite-toggle, and Surprise Me path — only the data layer and DOM wiring were verified, not the full interaction flow end to end.
- No Safari/WebKit check.

## Recommendation

Content and structure are ready for your read-through. Before publishing,
I'd like to either get a real headless-browser pass (I can try installing
Playwright if you want that now) or have you click through it once yourself
on a phone — whichever you'd rather do.
