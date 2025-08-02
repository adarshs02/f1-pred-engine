#!/usr/bin/env python3
import os, json, datetime, requests, pathlib, sys

API_KEY = os.getenv(ODDS_API_KEY)
SPORT   = "motorsport_f1"
REGION  = "uk"           # EU/UK books usually carry F1 futures
MARKET  = "outrights"    # outright-winner futures
BOOKMAKERS = "betfair,pinnacle,bet365"  # pick your favourites

if not API_KEY:
    sys.exit("❌ ODDS_API_KEY not found in environment.")

url = (
    "https://api.the-odds-api.com/v4/sports/"
    f"{SPORT}/odds"
    f"?regions={REGION}&markets={MARKET}&bookmakers={BOOKMAKERS}"
    f"&apiKey={API_KEY}"
)

print(f"Fetching odds from {url}")
resp = requests.get(url, timeout=10)
resp.raise_for_status()
odds_data = resp.json()

out_dir = pathlib.Path("data")
out_dir.mkdir(exist_ok=True, parents=True)
out_file = out_dir / f"f1_championship_odds_{datetime.date.today()}.json"

with open(out_file, "w") as fp:
    json.dump(odds_data, fp, indent=2, sort_keys=True)

print(f"Saved odds → {out_file}")
