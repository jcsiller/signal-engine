# Learning notes

<!--
Template: copy this for each new day.

## Day N: <title>

**What I built:**

**Predicted vs. what happened:**

**In my own words:**

**How to read what went wrong (if anything did):**

**What still confuses me:**

**Can I answer without looking?**
1.
2.
3.

**Question for next time:**
-->

## Day 1: Fetch jobs from an API

**Can I answer without looking?**
1. Which single line in the script actually contacts the internet?
2. If Remotive renamed `company_name` to `company`, which line would break, and what might the error say?
3. Why did the total say 16, not 10?

**Answers** (rewritten after the originals were lost):
1. `with urllib.request.urlopen(request) as response:` is the only line that
   goes out to the internet. Everything before it just prepares the request;
   everything after works on data already on my computer.
2. The `print(...)` line inside the loop, because it asks for
   `job["company_name"]`. Python would stop with `KeyError: 'company_name'`,
   meaning "you asked for a label that isn't in this job".
3. Remotive only sent 16 jobs in total. `jobs[:10]` limits what gets *printed*,
   but `len(jobs)` counts everything that came back.


## Day 2: Filter jobs open to LATAM

*(Written by Claude from my answers in the session, at my request.)*

**What I built:** `week1/day2_filter_jobs.py`. Same fetch as Day 1, then a loop
that keeps only jobs whose location mentions a LATAM keyword (latam, latin
america, americas, mexico, argentina, brazil, colombia, chile, peru). I decided
NOT to count "Worldwide": it means "anyone", which isn't a real LATAM signal.

**Predicted vs. what happened:**
- I predicted 4 jobs would pass. **7 passed.** I missed the 2 A.Team jobs
  ("Americas, Europe, Israel") and 1 iMerit job that lists Mexico among 6
  random countries. I was filtering with my judgment; the code only checks
  whether the letters appear.
- "USA, Canada, USA timezones" doesn't pass. ✅ Correct.
- "Northern America, LATAM…" *does* pass, but because of `latam`, not
  `americas`. "Northern America" has no "s", so it doesn't match. The computer
  matches exact letters, not meaning.

**In my own words:**
- A **list** is items in square brackets, in order.
- A **for loop** repeats the indented block once per item.
- A **loop inside a loop** checks every keyword for every job.
- **`if word in location`** asks "does this text appear inside that text?" and
  the answer is True or False.
- **`.append()`** adds to a list. **`break`** stops the inner loop once one
  keyword matched.
- The data has no "company country" field, so I can filter on where the
  *candidate* can live, not where the *company* is. A signal is only as good
  as the fields the source gives you.

**Can I answer without looking?**
1. What happens without `break`? → The list grows from 7 to 9, i.e. **2 more**,
   not 3. KoboToolbox appears 3 times (Argentina, Mexico, Peru), but one of
   those was already counted. Careful with "3 copies" vs "3 extra".
2. Why `.lower()`? → Without it, "LATAM" wouldn't match "latam", and I'd lose
   the 3 Lemon.io jobs.
3. Which keyword removes iMerit? → `mexico` (KoboToolbox stays via Argentina and
   Peru). But I won't remove it: Mexico is exactly what I'm looking for. The
   problem isn't the word; it's that a keyword can't tell a LATAM-focused job
   from a job listing Mexico among countries worldwide.

**Question for next time:**
- How do I weed out "random country list" jobs like iMerit? Options: a smarter
  rule (e.g. drop jobs listing countries on 3+ continents), or let Haiku judge
  in the Qualify stage. For now, cast a wide net and let later stages clean up.
