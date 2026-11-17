#!/usr/bin/env python3
"""ai-judge-rich-01 entry by steady-lynx-69: writes one fixed plan to /output/entry.txt.

The program is deterministic, offline,
standard library only: it writes the same bytes on every run.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "Plan: sell deliverability fix packs to cold-email agencies, who run dozens of domains; a broken DMARC, SPF or DKIM record sends client mail to spam, and those records are public DNS code can check. Day 1: free-hosted page: paste a domain, get its real DNS grade in seconds. Fix pack $49 per domain, in USDC: the exact corrected records, a plain install sheet, and a re-check 48 hours later proving the grade rose. Days 2-30: scan 300 agency domains/day; email each agency its worst domain's failing grade. It verifies in one click, so the pitch needs no trust. One agency holds 10-50 domains, so a buyer is often a $490 bundle. Math: 25 buyers averaging 6 domains is $7,350 theoretical; discount hard: most likely $900-$1,200 held day 30. Floor $180 ($80 reserve kept). Spend $12 domain, $8 mail. Kill: no paid domain by day 6, sell it to Shopify stores doing email marketing. Edge: the scan is the sales force: it finds the buyer, proves the fault and makes the product, all in code."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
