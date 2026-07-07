#!/usr/bin/env python3
"""
Weekly refresh for _data/events.yml.

Runs in CI (see .github/workflows/refresh-events.yml). Asks Claude — with the
server-side web_search tool — to re-research semiconductor / RTL / physical-
design / ASIC / EDA events that are EITHER online OR in-person within ~1hr of
San Jose, CA, then rewrites _data/events.yml as weekly (Mon-Sun) buckets.

The events.html page is a pure template over this file, so we only ever touch
this one data file. If Claude returns nothing usable, the existing file is left
untouched (the workflow then commits nothing).

Env:
  ANTHROPIC_API_KEY   required
  EVENTS_MODEL        optional, defaults to a current Claude model
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import yaml
from anthropic import Anthropic

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EVENTS_PATH = os.path.join(REPO_ROOT, "_data", "events.yml")

MODEL = os.environ.get("EVENTS_MODEL", "claude-sonnet-5")

# The comment header is the schema contract for the file. Kept here so the
# generated file is always self-documenting and stable.
HEADER = """\
# =============================================================================
# events.yml  —  data source for the Industry Events page (/events.html)
# -----------------------------------------------------------------------------
# AUTO-GENERATED WEEKLY by .github/workflows/refresh-events.yml. Manual edits to
# the `events:` list below will be OVERWRITTEN on the next Monday refresh. To
# change what gets pulled, edit .github/scripts/refresh_events.py instead.
#
# CADENCE: WEEKLY. The feed is organized into weekly buckets (Mon-Sun). Each
# event carries a `week_of` (the Monday of its week, ISO). events.html groups
# events under a "Week of <date>" header; the bucket matching `this_week` is
# badged "This week".
#
# INCLUSION FILTER: an event is listed ONLY IF it is EITHER
#   (a) online / virtual / livestreamed, OR
#   (b) in-person within ~1hr driving of San Jose, CA (San Jose, Santa Clara,
#       Sunnyvale, Palo Alto, Milpitas, Fremont, San Francisco, Berkeley,
#       Mountain View, Cupertino ...).
# Past weeks are dropped. RTL / verification / physical design / ASIC / EDA /
# architecture / semiconductor-process relevance preferred. Sorted soonest-first.
#
# SCHEMA per event: name, date (YYYY-MM-DD), week_of (Monday YYYY-MM-DD),
#   date_display (human), mode (online|local), location, url, desc,
#   tags [rtl,pd,asic,verif,arch,eda,papers], tentative (optional bool).
# ============================================================================="""

REQUIRED_FIELDS = ("name", "date", "week_of", "mode", "location", "url", "desc")
VALID_TAGS = {"rtl", "pd", "asic", "verif", "arch", "eda", "papers"}


def monday_of(d):
    return d - timedelta(days=d.weekday())


def build_prompt(this_monday):
    weeks = [this_monday + timedelta(weeks=i) for i in range(6)]
    week_lines = "\n".join(
        f"  - Week of {w.isoformat()} ({w.strftime('%b %d')})" for w in weeks
    )
    return f"""\
You are refreshing the industry-events feed for a chip-design personal site.
Today's Monday (the current week) is {this_monday.isoformat()}.

Use web_search to find REAL, CURRENTLY-SCHEDULED events. Do NOT invent events,
dates, or URLs. Every url must be a real organizer landing page you can justify
from search results (an events/webinars index page is fine; do not fabricate
deep links).

INCLUSION FILTER — include an event ONLY IF it is EITHER:
  (a) online / virtual / livestreamed, OR
  (b) in-person within ~1 hour of San Jose, CA (San Jose, Santa Clara,
      Sunnyvale, Palo Alto, Milpitas, Fremont, San Francisco, Berkeley,
      Mountain View, Cupertino).
Topic relevance (strongly preferred): RTL design, functional verification,
physical design / PnR / STA, ASIC/SoC, EDA tools (Synopsys/Cadence/Siemens EDA),
open silicon (OpenROAD/Efabless/RISC-V/Chipyard), computer architecture,
semiconductor process & packaging.

CADENCE — populate the next several weeks so the near-term feed feels full.
Aim for 3-5 events in EACH of these weeks, soonest first:
{week_lines}
You may also include a few marquee later conferences (Hot Chips, SEMICON West,
RISC-V Summit, ISSCC, DVCon, etc.) if they fit the filter, each in its own
later weekly bucket.

Each event's `week_of` MUST be the Monday of the week its `date` falls in, and
MUST NOT be earlier than {this_monday.isoformat()}.

Return ONLY a JSON array (no prose, no markdown fence) of event objects:
[
  {{
    "name": "string",
    "date": "YYYY-MM-DD",
    "week_of": "YYYY-MM-DD",     // Monday of that event's week
    "date_display": "Jul 07, 2026 · online",
    "mode": "online" | "local",
    "location": "Venue, City" or "Online",
    "url": "https://...",
    "desc": "one concise sentence",
    "tags": ["eda","pd"],        // subset of rtl,pd,asic,verif,arch,eda,papers
    "tentative": true            // include ONLY if the date is unconfirmed
  }}
]"""


def call_claude(prompt):
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        sys.exit(
            "ERROR: ANTHROPIC_API_KEY is empty. Set the repo secret "
            "(Settings -> Secrets and variables -> Actions) to a real key."
        )
    client = Anthropic(api_key=key)
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 8}],
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(
        block.text for block in resp.content if getattr(block, "type", None) == "text"
    )


def extract_json_array(text):
    # Prefer a fenced block if present, else the outermost [ ... ].
    fenced = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.DOTALL)
    raw = fenced.group(1) if fenced else None
    if raw is None:
        start, end = text.find("["), text.rfind("]")
        if start == -1 or end == -1 or end <= start:
            raise ValueError("no JSON array found in model output")
        raw = text[start : end + 1]
    return json.loads(raw)


def clean(events, this_monday):
    out = []
    for e in events:
        if not isinstance(e, dict):
            continue
        if any(not e.get(f) for f in REQUIRED_FIELDS):
            continue
        if e["mode"] not in ("online", "local"):
            continue
        try:
            date = datetime.strptime(e["date"], "%Y-%m-%d").date()
            week_of = datetime.strptime(e["week_of"], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        if not str(e["url"]).startswith("http"):
            continue
        # Normalize week_of to the true Monday of `date`, and drop past weeks.
        week_of = monday_of(date)
        if week_of < this_monday:
            continue
        item = {
            "name": str(e["name"]).strip(),
            "date": date.isoformat(),
            "week_of": week_of.isoformat(),
            "date_display": str(e.get("date_display") or date.strftime("%b %d, %Y")),
            "mode": e["mode"],
            "location": str(e["location"]).strip(),
            "url": str(e["url"]).strip(),
            "desc": str(e["desc"]).strip(),
        }
        tags = [t for t in (e.get("tags") or []) if t in VALID_TAGS]
        if tags:
            item["tags"] = tags
        if e.get("tentative") is True:
            item["tentative"] = True
        out.append(item)

    # De-dupe by (name, date), then sort soonest-first.
    seen, deduped = set(), []
    for e in out:
        key = (e["name"].lower(), e["date"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(e)
    deduped.sort(key=lambda e: (e["date"], e["name"].lower()))
    return deduped


def render(events, this_monday):
    lines = [HEADER, "", f'refreshed: "{this_monday.isoformat()}"',
             f'this_week: "{this_monday.isoformat()}"', "", "events:"]
    current_week = None
    for e in events:
        if e["week_of"] != current_week:
            current_week = e["week_of"]
            label = datetime.strptime(current_week, "%Y-%m-%d").date().strftime("%b %d, %Y")
            suffix = "  (current)" if current_week == this_monday.isoformat() else ""
            lines.append(f"  # --- Week of {label}{suffix} " + "-" * 12)
        body = yaml.safe_dump([e], sort_keys=False, allow_unicode=True, width=100)
        lines.append(re.sub(r"^", "  ", body.rstrip("\n"), flags=re.MULTILINE))
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def main():
    today = datetime.now(timezone.utc).date()
    this_monday = monday_of(today)

    prompt = build_prompt(this_monday)
    text = call_claude(prompt)

    try:
        raw = extract_json_array(text)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"::warning::could not parse model output ({exc}); leaving events.yml unchanged")
        print("---- model output (first 2000 chars) ----")
        print(text[:2000])
        return 0

    events = clean(raw, this_monday)
    if len(events) < 6:
        print(f"::warning::only {len(events)} valid events after filtering; "
              "leaving events.yml unchanged to avoid emptying the feed")
        return 0

    out = render(events, this_monday)
    # Validate the file we're about to write actually parses.
    parsed = yaml.safe_load(out)
    assert isinstance(parsed.get("events"), list) and parsed["events"], "render sanity check failed"

    with open(EVENTS_PATH, "w") as fh:
        fh.write(out)
    weeks = sorted({e["week_of"] for e in events})
    print(f"Wrote {len(events)} events across {len(weeks)} weeks ({weeks[0]} … {weeks[-1]}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
