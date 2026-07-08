# Cold Outreach Playbook for B2B SaaS

A synthesized, opinionated playbook built from the ten practitioners in
[`research/sources.md`](research/sources.md). This is the "so what" layer on top of the raw
research: every play below is attributed to the operator(s) it came from, so it's auditable
and easy to go deeper on.

> Scope: outbound to book qualified meetings for a B2B SaaS product. Assumes a defined ICP.

---

## 1. Operating principles (where the ten agree)

1. **Signals > volume.** Start from a buying signal, not a list. Connectivity of signals
   across systems is the real bottleneck, not the model or the sequencer. *(Florin Tatulea,
   Tito Bohrt, Jed Mahrle)*
2. **Earn the right.** Relevance and manners are a moat because the bar is so low. *(Leslie
   Venetz, Samantha McKenna, Josh Braun)*
3. **Multichannel, phone-anchored.** As automated email degrades, the phone and in-person
   are the least-crowded channels. *(Jason Bay, Tito Bohrt)*
4. **Personalize by economics.** Deep 1:1 personalization for high-ACV/enterprise; invest in
   product-marketing-grade messaging for SMB volume. *(Will Allred)*
5. **Human-in-the-loop AI.** Use AI for list-building, research, and QA — not to fully
   automate sending, which is just repackaged spray-and-pray. *(Tito Bohrt, Jed Mahrle,
   Jason Bay)*

---

## 2. The sequence (≈14 touches over ~15 business days)

A multichannel cadence combining email, phone, and LinkedIn. Trigger it off a signal
(job change, hiring, funding, tech-stack, content engagement), not a static list.

| Day | Channel | Play | Source |
|-----|---------|------|--------|
| 1 | LinkedIn | Connect, **no pitch** (optionally a "Show Me You Know Me" note referencing something specific) | Samantha McKenna |
| 1 | Email #1 | Problem → hypothesis → (mock-up/demo), soft close "does this sound interesting?" + a **secondary CTA** | Josh Braun, Will Allred, Jed Mahrle |
| 2 | Call #1 | "Heard-the-name-tossed-around" opener → **Problem Proposition**; leave a voicemail if no pickup | Armand Farrokh, Tito Bohrt |
| 3 | LinkedIn | Genuinely engage with their recent post (comment, not pitch) | Samantha McKenna |
| 4 | Call #2 | Different time of day; use local-presence + person/company caller ID | Tito Bohrt |
| 6 | Email #2 | New angle: "companies like yours" proof or a specific insight; keep it short, "founder tone" if you're small | Jed Mahrle |
| 8 | Call #3 + LinkedIn | Call, then a short LinkedIn message/voice note | Jason Bay |
| 10 | Email #3 | Soft "should I close your file?" with the **check-back** secondary CTA | Jed Mahrle |
| 12 | Multithread | Reach a second stakeholder; **Recap & Roll** what you've learned; find a warm path via Sales Nav "Connections Of" | Armand Farrokh, Samantha McKenna |
| 14 | Call #4 + LinkedIn | Final call + break-up note | — |

**Rule that beats better copy:** the moment anyone gives *any* signal — accepts a connection,
replies to an email (even neutrally), gets referred — **call them**, then keep following up
across channels. *(Jed Mahrle)*

---

## 3. Copy frameworks

### Cold email
- **Structure (Josh Braun's 4-T / problem-led):** Trigger → Think (a hypothesis about their
  world) → Third-party credibility → Talk (soft ask). Or: *uncover a problem → offer a
  hypothesis → show a mock-up/loom* rather than describe.
- **Lead with demand creation, not just capture (Will Allred):** "If [pain] is true, would
  it help if you could [outcome]?" reaches the ~95% who aren't in-market yet.
- **Secondary CTA (Jed Mahrle):** after the main ask, add a low-friction option — "Or want a
  90-sec video of why I reached out?" / "Happy to share examples of similar companies." /
  "Mind if I check back in a few months?"
- **Deliverability is copy's twin (Becc Holland):** warm the domain, keep volume sane, and
  keep the "spam cannon" away from tier-1 accounts (Will Allred).

### Cold call
- **Opener (Armand Farrokh):** pattern-interrupt + permission — e.g., "Hey Jane, it's Armand
  from [X], heard our name tossed around?" Avoid "is now a bad time?"
- **Problem Proposition:** name the specific pain the persona feels, then a one-line value +
  soft ask ("open to seeing an example?").

### When they object or brush you off
- **Objections are information (Josh Braun):** label the thinking instead of overcoming it.
  "Too expensive" → "Sounds like there's a ceiling on what you'd want to invest."
- **Referral reply (Samantha McKenna):** "not the right person" → gratitude + EQ + offer
  logic + anticipate confidentiality + close with appreciation → turns a dead-end into a
  warm internal intro.

---

## 4. Discovery (once they engage)
- **Layered questions (Armand Farrokh):** drop a POV into a situation → a multiple-choice
  question to surface the operational problem → a "magic-moment" question for business impact
  ("when did you realize this was a problem?").
- **Keep questions neutral (Becc Holland):** if your discovery question contains adjectives
  or adverbs ("low win rates," "long cycles"), you're selling, not helping.

---

## 5. Systems & deliverability (make it land)
- **Connect-rate levers (Tito Bohrt):** power-dial one number at a time (no parallel
  dialing), get through AI screeners (call again days apart + change the message), person +
  company caller ID, area code matched to persona. Target 6%+ vs. the 1.5–3% norm.
- **List-building with a human gate (Jed Mahrle):** agent/Claude/Clay builds the list against
  ICP docs; a human QAs before it enters the sequencer.
- **Tier your effort (Will Allred):** automate low-ACV volume; hand-craft tier-1 accounts.

---

## 6. Measurement & debugging
- **Track:** connect rate, positive-reply rate, meetings booked/week, and pipeline created —
  not send volume.
- **Judge personalization by outcomes (Leslie Venetz):** if AI "personalization" doesn't move
  open/reply/conversion, it's reputational risk, not value.
- **Debug in this order — BSMS (Tito Bohrt / Jason Bay):** **B**ehaviors → **S**ystems →
  **M**essaging → **S**kills. Most teams train skills first; fix behavior and deliverability
  before touching scripts.
- **Outbound dies in the last 1% (Tito Bohrt):** each fix creates a downstream problem
  (more signals → can't sequence → parallel dialers → domain reputation → "spam likely" →
  untracked missed calls). Winners just out-detail everyone.

---

## 7. First 3 things I'd test (my POV)
1. **Signal-triggered sequences** over static lists — even a simple "job-change + hiring"
   trigger, measured against a control.
2. **Phone re-prioritized** with local presence + caller ID, since it's the least-crowded
   channel right now.
3. **Secondary CTAs** on every email — the cheapest reply-rate lift in the research.

_Sources for every play: [`research/sources.md`](research/sources.md) and the collected
posts in [`research/linkedin-posts/`](research/linkedin-posts)._
