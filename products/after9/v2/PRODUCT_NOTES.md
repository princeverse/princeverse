# Product Notes — After.9

---

## Truth or Temptation

**Product summary**
A choice-driven couples' game: every turn, one partner picks Truth (answer honestly) or Temptation (a mutual invitation to try something together). The game escalates automatically across three heat levels, ending at "After.9." Built as a self-contained interactive web app, not a printable or a flat card list.

**Target audience**
Adults 21–40, dating or partnered, looking for a date-night experience with more momentum than a passive Truth-or-Dare deck — couples who want built-in escalation and a little structure, not just a prompt list they have to manage themselves.

**Expected playing time**
25–40 minutes for a full arc through all three heat levels; the "End the game here" option means it never has to run longer than a couple wants.

**Number of prompts**
104 total (54 Truth, 50 Temptation) across 3 levels — see QA_REPORT.md §9 for the exact breakdown.

**Replayability**
No-repeat guaranteed within a single session (up to bank exhaustion, extremely unlikely in normal play). Because prompt order reshuffles fresh each session and the bank is large relative to a typical playthrough, replays feel genuinely different rather than mechanically identical.

**Recommended price (CAD)**
**$19 CAD.** This is the brand's recommended first product — pricing it as the flagship rather than the cheaper of the two signals confidence in it without overreaching for a digital impulse-buy category.

**Suggested Shopify title**
Truth or Temptation | After.9 Couples Game

**Suggested product subtitle**
Choose carefully. Both options escalate.

**Five key benefits**
1. Built-in escalation — you never have to decide "should we go further," the game paces it for you
2. Every Temptation can become a Truth instead — control stays with both partners, always
3. Optional shared scoring turns it into something you build together, not a competition
4. Progress saves automatically — pick up exactly where you left off, even after closing the app
5. Instant access, works on any phone or tablet, no install required

**What the buyer receives**
One self-contained HTML file (`TruthorTemptation.html`) — opens directly in any modern browser, works offline after the first load, no account or login.

**Suggested product-page FAQ**
- *Is this explicit?* No — flirty and escalating, never graphic. Every prompt was written and reviewed to stay tasteful.
- *What if we want to stop or slow down?* Every prompt can be skipped, any time, no explanation needed — and Temptations can always be swapped for a Truth.
- *Do we need anything else to play?* No — just the device you're reading this on.
- *Does our progress save if we close the app?* Yes — reopen it and you'll be offered "Resume Game."

---

## How Well Do You Really Know Me?

**Product summary**
A genuine prediction-and-reveal game, not a shared conversation deck: one partner privately answers, the other predicts what they picked, then you reveal together and see how close the guess was. Builds a shared "compatibility score" across four rounds, ending at "After.9."

**Target audience**
Same core audience as Truth or Temptation, with slightly more appeal to couples who enjoy a game with actual mechanics and a sense of "winning together" over a pure conversation-starter format.

**Expected playing time**
45–60 minutes for all four rounds (36 questions total); naturally splits into ~10–15 minute chunks per round if a couple prefers to play it across more than one sitting (progress saves automatically either way).

**Number of prompts**
80 in the full library; each session randomly draws 9 per round (36 total played per session) — see QA_REPORT.md §9 for the format breakdown.

**Replayability**
Strong — each session uses less than half the full question bank, so replays reliably surface a meaningfully different set of questions rather than the same 36 every time.

**Recommended price (CAD)**
**$16 CAD** at launch, positioned as the second product in the collection. Revisit upward once it has reviews — this is a substantially more mechanically rich product than a typical prompt-deck and can likely support the same $19 CAD as Truth or Temptation once proven.

**Suggested Shopify title**
How Well Do You Really Know Me? | After.9 Prediction Game

**Suggested product subtitle**
A prediction game, not just a conversation.

**Five key benefits**
1. A real game mechanic — predict, reveal, score — not just a list of questions to read aloud
2. Every answer stays private until both of you choose to reveal it together
3. Collaborative scoring — you're building a compatibility score together, never competing against each other
4. A built-in consent checkpoint before the most intimate round, so nothing sneaks up on either partner
5. Replayable — most sessions surface a different set of questions than the last

**What the buyer receives**
One self-contained HTML file (`HowWellDoYouReallyKnowMe.html`) — same delivery model as Truth or Temptation.

**Suggested product-page FAQ**
- *How is this different from a typical "get to know you" card game?* Those games are just questions you both answer out loud. This one is a real guessing game — one of you answers privately, the other predicts it, and you score how well you actually know each other.
- *Can my partner see my answer before I reveal it?* Not through the app — you'll get a clear "pass the phone, no peeking" moment between answering and predicting. (See QA_REPORT.md §6 for the honest limit of what a single shared device can and can't protect.)
- *Is there pressure to "perform" or get every answer right?* No — this is explicitly framed as collaborative, and the final result is written to feel warm regardless of the score.
- *Does progress save if we stop partway?* Yes, at any point, with a Resume option on reopening.

---

## Delivery method recommendation (applies to both products)

Comparing the three options you asked about:

| | Downloadable HTML file | Hosted access link | Unique purchase code/token |
|---|---|---|---|
| **Customer convenience** | High — double-click, opens in any browser, works offline | High — no file to manage, just revisit the link | Lower — extra step to find and enter a code |
| **Link-sharing risk** | High — nothing stops forwarding the file | High, and arguably easier to share than a file (zero friction) unless access-controlled | Lowest, but only if codes are enforced single-use/device-bound — otherwise just as leaky |
| **Maintenance** | Low effort to update the master; already-downloaded copies never get fixes | Easy — push an update, every buyer sees it immediately | Highest — needs real backend infrastructure |
| **Updating past purchases** | Not possible without the buyer manually re-downloading | Easy — same link, updated content behind it | Easy, once the infrastructure exists |
| **Privacy** | Best of the three — nothing ever leaves the buyer's device, nothing to collect | Good if hosting is static/logless; degrades if you add accounts or analytics later | Depends entirely on implementation — a validation backend inherently logs something |
| **Shopify compatibility** | Native — works today with the free Digital Downloads app | Needs custom app/fulfillment setup beyond Digital Downloads | Not natively supported; needs a custom or third-party licensing app |

**Recommendation: launch with the downloadable HTML file (option 1), via Shopify's free Digital Downloads app.** It's the only option that requires zero new infrastructure, stays fully within "no accounts, payments, auth, databases, hosting until approved," and — somewhat counterintuitively — has the strongest privacy story of the three, since there's nothing to collect in the first place. The link-sharing risk is real, but it's the same risk essentially every small digital-download shop accepts at this stage, and it's the trade every downloadable-PDF or downloadable-template competitor in this broader category already makes.

The one real weakness of this approach — you can't push a fix to a bug or add new content to something someone already bought — is worth revisiting once there's real sales volume to justify building a lightweight hosted-link system. That's a "when it's earned it" upgrade, not a launch requirement.

## Required product screenshots (for the Shopify listing)

For each product, recommend capturing:
1. The cover/title screen (establishes brand and premium aesthetic immediately)
2. One mid-game screen showing an actual prompt/question card
3. One screen showing the escalation mechanic visually (heat-level indicator for Truth or Temptation; the reveal/compatibility screen for How Well)
4. The final result screen
5. One screen shown at a "flat lay" or in-hand mockup style for the listing's primary image (I can produce clean in-app screenshots on request; a styled device-mockup composite is a separate follow-up task)

## Recommended launch order

1. **Truth or Temptation first**, per the brief's own priority call — it's simpler to explain in a single product photo/description and has the more immediately legible hook ("choose Truth or Temptation").
2. **How Well Do You Really Know Me? second**, once its redesigned mechanic has your sign-off — it's a slightly harder concept to explain at a glance (needs the product page to clearly communicate "this is a prediction game," not just another Q&A deck), so benefits from Truth or Temptation already having proven the store converts.
3. Unhide the store's Featured Products collection once Truth or Temptation is live, per the existing storefront plan noted in your brief.
