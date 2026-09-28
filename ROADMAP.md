# Roadmap

## Rules while building

- Build one stage at a time. Don't start the next until the current one works.
- Claude explains every change before it's accepted. That's where the
  code-reading skill develops.
- Log cost per run from day one.

## Week 1: Read code by building tiny things

Each day is one small script, built and explained line by line. Predict the
output before running it.

- [x] **Day 1:** Call one public job-board API and print 10 engineering jobs.
  *HTTP request, JSON, variables.* → `week1/day1_fetch_jobs.py`
- [ ] **Day 2:** Filter those jobs to US companies hiring remote or LATAM.
  *Conditionals, loops, lists.*
- [ ] **Day 3:** Save the results to a file, then load them back.
  *Files, data structures.*
- [ ] **Day 4:** Break it on purpose (a wrong API key, a missing field) and read
  the error trace. *Debugging and logs. The most important day.*
- [ ] **Day 5:** First Claude API call: classify one job post as fit or not fit.
  *API auth, prompts, token cost.*

**Deliverable:** ☐ A ~50-line script you can explain top to bottom without help.
It becomes stage 1 (Ingest) of the Signal Engine.

## Week 2: Data and APIs

- [ ] SQL basics on SQLBolt
- [ ] 15 real queries against this project's Supabase data (the jobs collected
  in Week 1): filters, joins, counts, grouping by date
- [ ] APIs: endpoints, auth headers, rate limits, webhooks (read Anthropic's
  tool-use docs as the example)
- [ ] Read Anthropic's "Building Effective Agents" (when to use a workflow vs.
  an agent)

**Deliverable:** ☐ A Supabase schema for the Signal Engine (companies, signals,
contacts, messages, outcomes), designed by you and built by Claude Code.

## Week 3: GTM engineering fundamentals

- [ ] **ICP:** write down exactly who converted for CodrSpot (US startups under
  300 people, scaling engineering, already open to LATAM)
- [ ] **Signals:** engineer job posts, funding rounds, new CTO/VP Engineering
  hires, headcount growth, US companies posting "remote LATAM" roles
- [ ] **Enrichment:** finding the right contact and a verified email (Clay
  University, free)
- [ ] **Deliverability:** separate sending domain, SPF/DKIM/DMARC, warmup,
  volume limits

**Deliverable:** ☐ A written ICP and a ranked list of 5 signals with how to
detect each.

## Weeks 4–5: Build v1

One stage at a time:

- [ ] **1. Ingest:** pull job posts and funding news for the ICP into Supabase daily
- [ ] **2. Qualify:** rule-based filtering in Python first, then Haiku scores
  each company against the ICP
- [ ] **3. Enrich:** find the hiring manager or founder and verify the email
- [ ] **4. Draft:** Sonnet writes an opener citing the specific signal
- [ ] **5. Approve and send:** Telegram message to approve or edit, then send
  through the sequencer and log to Supabase

A human stays in the loop on every send for v1. Autonomy comes after the evals
prove the quality.

## Week 6: Evals and proof

- [ ] **Qualifier eval:** hand-label 50 companies as fit or not fit, then measure
  agreement with Haiku. Fix the prompt until agreement is high.
- [ ] **Draft eval:** blind-rate 20 AI drafts against 20 of your own messages
- [ ] **Business metrics:** reply rate against baseline, cost per qualified
  conversation, hours saved per week

**Deliverable:** ☐ A one-page case study plus a 3-minute recorded demo.
