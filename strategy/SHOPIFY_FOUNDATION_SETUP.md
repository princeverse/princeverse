# Shopify Foundation Setup — Account Checklist

Do these in order. Tier 1 blocks everything I can build; Tiers 2-3 can happen
in parallel or slightly after.

---

## Tier 1 — Blocks me completely. Do this first.

### 1. Create the Shopify store
- Go to shopify.com → Start free trial
- Store name: use your Etsy shop name if you want one consistent brand
  across both, or tell me what to use — I don't have it yet
- Use noblewavemarketing@gmail.com (or your dedicated business email) as
  the account email — keep this consistent across every platform below,
  it matters for payout verification later

### 2. Generate my API access
Settings → Apps and sales channels → Develop apps → Create an app → name
it "Claude Automation" → Configure Admin API scopes → enable at minimum:
```
write_products, read_products
write_inventory, read_inventory
write_content, read_content
write_orders, read_orders
```
→ Install app → reveal **Admin API access token** → send it to me here.

This one token is what turns everything from here on into "I build it,"
not "here's a brief for you to execute."

### 3. Set up payment processing
Settings → Payments → Shopify Payments (if available in your country) or
PayPal as fallback. This requires your identity/bank details — I can't do
this step, and Shopify won't let orders complete without it, so it's not
skippable even though it feels like admin busywork.

---

## Tier 2 — Needed within a few days, for the organic push

### 4. Pinterest Business account (free)
pinterest.com/business/create — claim it under the same email. This is
your highest-leverage free channel for this niche per the research. Once
it exists, tell me and I'll start producing pin graphics from the
templates we already built.

### 5. Meta Business Suite + Facebook Page + Instagram
business.facebook.com → create a Business Portfolio → create a Page
("Balance & Bloom" or your chosen name) → connect/create an Instagram
account. Do this now even though the ad boost is later — installing the
Meta Pixel on the store from day one means it's already collecting
data by the time we spend the $100, which makes that one boosted day
target better instead of firing blind.

---

## Tier 3 — Only needed right before the $100 boost day

### 6. Meta ad account + payment method
Inside Business Suite → Ads Manager → create an ad account, add a card.
We'll do this together closer to the actual boost so the card details are
fresh and you're not holding an idle ad account for weeks.

---

## What I'm doing in parallel right now (no dependency on the above)

Drafting the store's required policy pages (refund, privacy, terms) so
they're ready to paste in the moment the store exists — see
`shopify-policy-pages/` in this repo.
