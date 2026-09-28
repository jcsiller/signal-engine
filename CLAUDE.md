# Project rules

This is a learning project. The owner doesn't code; they direct Claude.
The goal is to learn to READ code by watching small pieces get built and explained.

## What this project is

This repo is a from-scratch learning project that becomes the Signal Engine:
a GTM tool that finds US startups hiring LATAM engineers. It is separate from
CEVE. Never reference or copy from CEVE. Current progress lives in ROADMAP.md.

## Rules for this whole repo

- Before writing or changing any file, explain in plain language what you're
  about to do and why. Wait for an OK.
- Keep code simple and flat: one file, no classes, no abstractions, no frameworks.
- Python standard library only (urllib, json). No pip installs.
- After writing code, walk through it line by line in plain English.
- Before running anything, ask the owner to predict what it will print. Then run
  it, and compare the output to the prediction.
- Build one stage at a time. Don't start the next until the current one works.
- Log cost per run from day one (starting with the first paid API call).

## Layout

- `weekN/dayN_name.py`: one standalone script per day. Each day starts as a copy
  of the previous day plus that day's new piece.
- `LEARNING.md`: the owner's notes, in their own words. Don't write notes there
  for them.
