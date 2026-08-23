# QA Report — After.9 Product Revision Pass 1
### Truth or Temptation (rebuilt) + How Well Do You Really Know Me? (redesigned)

Status: **Ready for your review.** Nothing has been uploaded or published — both files are attached alongside this report per the "do not publish" instruction.

---

## 1. Environment tested

- **Browser engine:** Chromium (headless, via Playwright), current build in this sandbox.
- **Not tested here:** real Safari/WebKit — no WebKit browser is available in this environment. Both files use only broadly-supported, standard CSS (flexbox, custom properties, `clamp()`, CSS grid, `env(safe-area-inset-*)`, `prefers-reduced-motion`) and vanilla JS with no bleeding-edge APIs, so WebKit compatibility risk is low — but I have not personally confirmed it renders identically in Safari. **Recommend a manual spot-check in real Safari/iOS before launch.**
- **Screen widths tested (required set):** 320px, 360px, 375px, 390px, 414px, 430px — every one, on the cover screen of both files and on full gameplay screens of both files at 320px and 375px specifically.

## 2. Screen sizes — horizontal overflow check

`document.body.scrollWidth > window.innerWidth` checked programmatically at every required width, both files, cover screen:

| Width | Truth or Temptation | How Well Do You Really Know Me? |
|---|---|---|
| 320px | No overflow | No overflow |
| 360px | No overflow | No overflow |
| 375px | No overflow | No overflow |
| 390px | No overflow | No overflow |
| 414px | No overflow | No overflow |
| 430px | No overflow | No overflow |

Also confirmed no overflow at 320px on: the Truth/Temptation choice screen, reveal screen, and confirmation modal; and on How Well's answering screen (all three input formats), predicting screen, and reveal screen — the narrowest width with the most content on screen.

## 3. User flows tested

**Truth or Temptation** — every flow in the brief's checklist, tested via scripted interaction, not just visual inspection:
- Start Playing → choice screen
- Play with Scoring → score chip appears, increments correctly (Truth = 1pt, Temptation = 2pt, verified: 3 Truths + 2 Temptations = 7pts, matched)
- Setup & Rules toggle → opens/closes correctly
- Truth → reveals a Truth prompt
- Temptation → reveals a Temptation prompt
- Skip → redraws a new prompt from the same category without affecting score
- Done / Next Turn → advances turn count, triggers level-up at turn 12 (→ Level 2) and turn 24 (→ Level 3), confirmed via automated playthrough to Level 3 ("After.9")
- End Game (with confirmation modal) → shows result screen with correct final score
- Play Again (with confirmation modal) → clears state, returns to cover
- **Resume flow**: played 5 turns, reloaded the page in the same browser context, confirmed the "Welcome back" screen shows correct progress ("Level 1 · Warm Up — 5 turns played, score 7"), confirmed Resume Game restores the exact score and level
- Start Over → requires confirmation via modal (cannot be triggered accidentally)

**How Well Do You Really Know Me?** — full automated playthrough of all 4 rounds, 36 questions total (9 per round), all three question formats (this-or-that, multiple choice, 1–10 rating):
- Start Playing → Round 1 intro → Begin Round
- Full turn cycle verified for every format: handoff-to-answer → private answer entry → lock in → handoff-to-predict ("no peeking" screen) → prediction entry → lock in → reveal
- Reveal comparison logic verified correct: this-or-that/multiple-choice score "Nailed it!" only on exact match, otherwise "Not even close" (no false partial credit); rating questions score "Nailed it!" (diff ≤1), "Close enough" (diff ≤3), "Not even close" (diff >3) — confirmed with a mismatched test case ("Plan ahead" vs. "Wing it" correctly returned "Not even close")
- Turn alternation confirmed: Partner A answers turn 1, Partner B answers turn 2, etc., continuing across round boundaries
- Round transitions (1→2→3) confirmed, each with distinct teaser copy
- **Consent checkpoint before Round 4** confirmed: appears automatically after Round 3 completes, before Round 4 ("After.9") begins, with a "Continue to After.9" button — cannot be skipped past accidentally
- Skip → redraws a different, unused question from the round's full bank
- Final result screen confirmed: 100% compatibility run produced "You know each other better than most couples ever will..." tier copy; scoring math verified correct
- **Resume flow**: played 1 full question, reloaded, confirmed "Welcome back" screen shows accurate progress ("You Should Know This — question 2 of 9, compatibility 2/2"), confirmed Resume restores to the correct next screen
- Start Over → confirmation modal required, confirmed working; declining (via overlay click or Cancel) leaves progress untouched

## 4. Bugs found and fixed

| # | Bug | File | Status |
|---|---|---|---|
| 1 | Consent/footer `<div>` sat outside the `.app` flex container, causing layout issues (the exact bug named in the brief) | Truth or Temptation | **Fixed** — footer moved inside `.app`, given a reserved flex row with its own safe-area padding and a top border, so it never gets pushed off-screen or overlaps content |
| 2 | Brand name displayed twice on the cover (kicker + `<h1>`, both reading "After 9") | Truth or Temptation | **Fixed** — consolidated to a single kicker line; the large title is now the game name, not a second brand repeat |
| 3 | Horizontal overflow risk on narrow screens (fixed-size buttons/text, no safe-area handling, no `overflow-x` guard) | Both | **Fixed** — `clamp()` typography, `env(safe-area-inset-*)` padding, `overflow-x: hidden` on html/body, flexible button sizing with `min-width: 0` on flex children |
| 4 | Brand written inconsistently as "After 9" (no period) throughout | Both | **Fixed** — every instance now reads "After.9"; verified via full-file text search, zero remaining instances of the old form |
| 5 | Coercive-sounding language in Temptation prompts ("no matter what they ask," "no complaints allowed," "no hesitation," "do whatever your partner asks," "don't stop until they pull away," and prompts implying one partner owes the other physical contact) | Truth or Temptation | **Fixed** — every flagged prompt rewritten as a mutual, opt-in invitation (e.g., "Let your partner choose one item of your clothing to remove" → "If you both want to, let your partner choose one item you're comfortable removing"). Verified via full-file phrase search: zero matches remain. |
| 6 | No progress persistence — closing or refreshing lost the whole game | Both | **Fixed** — `localStorage`-based state saved on every phase transition, with a "Welcome back" resume screen offering Resume or Start Over (the latter requires confirmation) |
| 7 | "How Well Do You Really Know Me?" was a shared conversation deck, not a knowledge/prediction game — the title didn't match the mechanic | How Well | **Fixed** — fully redesigned as a private-answer → prediction → reveal game with a shared compatibility score, per the brief's recommended structure |
| 8 | Old How Well content included jealousy-framed-as-love-proof, distrust-of-named-others, and secret-demanding questions | How Well | **Fixed** — entire question bank rewritten from scratch; none of that content exists in the new bank (verified by keyword search for "jealous," "trust," "secret," "argument" — zero matches) |

## 5. Not reproduced

- **"Remove the duplicate level-two Temptation deck declaration"** — I inspected the original `TruthorTemptation.html` before rewriting it and could only find a single `temptation:` key in the `DECK` object; no duplicate declaration was present. I'm noting this rather than claiming a fix for something I couldn't find — if you're aware of a specific duplicate that isn't the one I checked, point me to it and I'll address it directly.

## 6. Remaining limitations (documented, not defects)

- **Privacy during the "answer" step is procedural, not technical.** On a single shared device, there's no way to cryptographically hide one partner's answer from the other — the app relies on a deliberate hand-off screen ("pass the phone, no peeking") the same way real single-device party games (Heads Up!, Psych!, Speak Out) do. This is disclosed rather than oversold as secure.
- **No-repeat guarantee is bounded by bank size.** Truth or Temptation guarantees no repeats within a level until that level's full bank (17–20 prompts per category) is exhausted in one sitting; beyond that, it reshuffles rather than freezing the game — equivalent to running out of physical cards in a real deck. This is very unlikely in a normal single session but is a known, accepted boundary, not a bug.
- **Transient private-answer storage.** How Well's `localStorage` briefly holds the current round's real answer and prediction between "lock in" and "reveal," purely so a refresh mid-question doesn't lose that turn. It is deleted from storage immediately after each reveal — only the aggregate score persists beyond that point. Nothing is ever transmitted anywhere; this stays entirely in the player's own browser. Flagging this as the one deliberate, minimal exception to "don't store answers," per the brief's "unless explicitly approved" clause — happy to remove even this transient storage if you'd rather a refresh mid-question simply lose that one in-flight turn.
- **Safari/WebKit untested directly**, as noted in section 1.

## 7. Consent review

Completed. Every prompt in both files was read individually against the brief's list of banned coercive phrasings and the "mutual invitation" framing requirement. Both rules screens now state explicitly, in the app itself (not just in this report): every prompt is optional, either partner may pass/modify/stop at any time, a Temptation can always become a Truth, and silence or hesitation is not consent. How Well adds a dedicated consent-checkpoint screen immediately before its most intimate round.

## 8. Accessibility review

- Every interactive element is a real `<button>` (verified: zero `<div onclick>` pseudo-buttons in either file — the two grep matches during testing were false positives from buttons nested inside div wrappers).
- `:focus-visible` outlines defined and present on all buttons/links (verified via a keyboard-only spot check: Tab correctly focuses "Start Playing" first, Enter correctly activates it).
- Dynamically generated answer/prediction buttons carry `aria-label` attributes matching their visible text.
- `prefers-reduced-motion` is respected in both files — animations and transitions are disabled for users who request it.
- Text/background contrast uses the cream-on-near-black palette throughout; no low-contrast combinations were introduced. (One screenshot during testing appeared to show near-invisible question text — investigated and confirmed to be a screenshot-timing artifact of the 350ms fade-in animation, not an actual rendering bug; text is fully legible once settled, confirmed with a delayed screenshot.)
- No external dependencies beyond Google Fonts (Fraunces + Inter), which is optional — both files declare system-font fallback stacks, and the sandbox's own network failure loading Google Fonts during testing did not break layout or legibility.
- Neither file makes any network calls other than the font request, collects no personal data, and contains no analytics or tracking of any kind — confirmed by reading both files end to end.

## 9. Prompt / question counts

**Truth or Temptation — 104 total prompts** (was described as "approximately 100" — this is within that range):

| Category | Level 1 (Warm Up) | Level 2 (Heating Up) | Level 3 (After.9) | Total |
|---|---|---|---|---|
| Truth | 17 | 17 | 20 | 54 |
| Temptation | 17 | 17 | 16 | 50 |

**How Well Do You Really Know Me? — 80 total questions**, drawing 9 per round per session:

| Round | This-or-that | Multiple choice | Rating (1-10) | Total in bank |
|---|---|---|---|---|
| 1 — You Should Know This | 8 | 6 | 6 | 20 |
| 2 — Between Us | 8 | 6 | 6 | 20 |
| 3 — Read My Mind | 8 | 6 | 6 | 20 |
| 4 — After.9 | 8 | 6 | 6 | 20 |

## 10. Duplicate check

Programmatically verified (not just visually) for both files: zero duplicate question/prompt IDs, and zero duplicate prompt text (case-insensitive, whitespace-trimmed comparison) across the entire bank in each file.
