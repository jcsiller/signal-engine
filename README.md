# Signal Engine

A GTM tool, built from scratch, that finds US startups hiring LATAM engineers.
It pulls hiring signals (job posts, funding rounds, new engineering leaders),
qualifies companies against an ICP, and drafts outreach for human approval.

It's also a learning log: every line was built step by step and explained,
so the author can read and explain the whole system. See
[ROADMAP.md](ROADMAP.md) for the plan and [LEARNING.md](LEARNING.md) for notes.

## Run the scripts

Needs Python 3 only, with no installs.

```
python week1/day1_fetch_jobs.py
python week1/day2_filter_jobs.py
```

- Day 1 prints the first 10 software-dev jobs.
- Day 2 prints only the jobs open to LATAM candidates.

Job data comes from [Remotive](https://remotive.com). Please respect their rate
limit: no more than a few runs per day.
