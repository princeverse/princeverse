# QA Notes — The Kamasutra Guide (draft 1)

Status: **Draft, not uploaded or published.** Updated after a real headless-browser
pass (Playwright + the pre-installed Chromium) — see "Browser QA" below. Static
checks from the first pass are unchanged and still hold.

## Browser QA (Chromium, headless, via Playwright)

33 automated checks, all passing:

- **No horizontal overflow** at all six required widths (320/360/375/390/414/430px), on the cover, browse, and detail screens — 18 checks, all pass.
- **Full interaction flow**, scripted end to end: info box toggle, entering the browse screen, filtering by energy/flexibility/experience individually and in combination, a contradictory filter combo (Intense + High + Beginner, which has zero real matches) correctly shows the empty state instead of breaking, resetting filters restores all 36, search narrows correctly ("lotus" → exactly "The Lotus Circle," alt name "Yab-Yum" displayed correctly), favoriting from the detail screen, favorites-only filter, **favorite state survives a full page reload** (localStorage round-trip confirmed), Surprise Me opens a detail screen, and a live-DOM check confirms zero `div[onclick]` pseudo-buttons.
- Full script and raw output available on request if you want to see it directly.

**Not tested:** real Safari/WebKit (same limitation as the After.9 products — no WebKit engine available in this environment; the CSS uses the same broadly-supported patterns already used there, so risk is low but unconfirmed).

## What was checked (static pass)

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

- No Safari/WebKit check (see above).
- No human read-through of the 36 entries for tone/accuracy — this is now the main open item.

## Recommendation

Structure, data integrity, and interaction are all verified. The one thing
left before this is launch-ready is your read-through of the actual content
and a sign-off on the $22 CAD price point — nothing further to test on my end
until then.
