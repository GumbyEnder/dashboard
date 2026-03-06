#!/usr/bin/env python3
"""Carry the significant-move brief to Discord three times per trading day."""

import argparse
import csv
import io
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

YAHOO_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json,text/plain,*/*",
}

WORKSPACE = Path(__file__).parent.parent
POSITIONS_F = WORKSPACE / "portfolio-positions.json"
DATA_F = WORKSPACE / "veanox-dashboard" / "portfolio-data.json"
ET = ZoneInfo("America/New_York")
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    )
}
SIGNIFICANCE_PCT = 5.0
DISCORD_CHANNEL = "discord"
DISCORD_TARGET = "channel:1478135368053166183"
SLOT_LABELS = {
    "morning": "Morning check",
    "midday": "Midday check",
    "close": "Close check",
}


def fetch_stooq(symbol: str):
    for suffix in (".US", ""):
        try:
            url = f"https://stooq.com/q/l/?s={symbol}{suffix}&f=sd2t2ohlcv&h&e=csv"
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code != 200:
                continue
            reader = csv.DictReader(io.StringIO(resp.text))
            for row in reader:
                close = row.get("Close")
                if not close or close == "N/D":
                    continue
                open_price = row.get("Open")
                price = float(close)
                o = float(open_price) if open_price and open_price != "N/D" else price
                change = price - o
                pct = (change / o * 100) if o else 0
                return price, change, pct
        except Exception:
            pass
    return None


def fetch_all_prices(symbols):
    prices = {}
    for sym in symbols:
        result = fetch_stooq(sym)
        if result:
            price, change, pct = result
            prices[sym] = {"price": price, "change": change, "change_pct": pct}
            if price >= 1:
                price_label = f"${price:,.2f}"
            else:
                price_label = f"${price:.4f}"
            print(f"  {sym}: {price_label} ({pct:+.2f}%)")
        else:
            print(f"  {sym}: unavailable")
        time.sleep(0.5)
    return prices


def fetch_index_change(symbol: str, label: str):
    """Return (label, last_close, prev_close, pct_change) using Yahoo chart API."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=10d"
    try:
        resp = requests.get(url, headers=YAHOO_HEADERS, timeout=12)
        if resp.status_code != 200:
            return None
        payload = resp.json()
        result = payload.get("chart", {}).get("result", [])
        if not result:
            return None
        closes = result[0].get("indicators", {}).get("quote", [{}])[0].get("close", [])
        cleaned = [c for c in closes if c is not None]
        if len(cleaned) < 2:
            return None
        prev_close = float(cleaned[-2])
        last_close = float(cleaned[-1])
        pct_change = ((last_close - prev_close) / prev_close * 100) if prev_close else 0.0
        return (label, last_close, prev_close, pct_change)
    except Exception:
        return None


def load_positions():
    return json.loads(POSITIONS_F.read_text())


def load_shared_data():
    if DATA_F.exists():
        data = json.loads(DATA_F.read_text())
    else:
        data = {}
    data.setdefault("last_prices_for_updates", {})
    data.setdefault("last_total_value", {"value": 0.0, "date": None})
    data.setdefault("last_slot", None)
    data.setdefault("last_run", None)
    return data


def save_shared_data(data):
    DATA_F.write_text(json.dumps(data, indent=2))


def get_symbols(positions):
    return sorted(
        {
            pos["symbol"]
            for account in positions["accounts"].values()
            for pos in account["positions"]
        }
    )


def compute_total_value(positions, prices):
    total = 0.0
    for account in positions["accounts"].values():
        total += account.get("cash", 0)
        for pos in account["positions"]:
            sym = pos["symbol"]
            share_price = prices.get(sym, {}).get("price")
            if share_price is None:
                continue
            total += share_price * pos.get("shares", 0)
    return total


def format_price(value):
    if value is None:
        return "N/A"
    if value >= 1:
        return f"${value:,.2f}"
    return f"${value:.4f}"


def format_currency(value):
    return f"{value:+,.2f}"


def send_discord_message(message):
    try:
        result = subprocess.run(
            [
                "openclaw",
                "message",
                "send",
                "--channel",
                DISCORD_CHANNEL,
                "--target",
                DISCORD_TARGET,
                "--message",
                message,
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            print("⚠️ Discord send failed:", result.stderr.strip())
    except Exception as exc:
        print("⚠️ Discord send error:", exc)


def build_message(slot, significant, total_value, change_delta, change_pct, prev_total_known, market_changes):
    now = datetime.now(ET)
    slot_label = SLOT_LABELS[slot]
    header = f"{slot_label} — {now.strftime('%I:%M %p ET')}"
    lines = [header, ""]
    if significant:
        lines.append(f"Significant moves (±{SIGNIFICANCE_PCT:.0f}%) since last check:")
        for sym, last_price, price, pct in significant:
            lines.append(
                f"- {sym}: {pct:+.1f}% ({format_price(last_price)} → {format_price(price)})"
            )
    else:
        lines.append(
            "No ±5% moves were detected since the previous slot; prices are saved for the next run."
        )
    if slot == "close":
        lines.append("")
        lines.append("End-of-day summary:")
        lines.append(f"- Total portfolio value: ${total_value:,.2f}")
        if prev_total_known:
            lines.append(
                f"- Change vs last close: {format_currency(change_delta)} ({change_pct:+.2f}%)"
            )
        else:
            lines.append("- Change vs last close: N/A (first close measurement)")

        lines.append("- Market indexes (daily):")
        if market_changes:
            for label, last_close, _prev_close, pct in market_changes:
                lines.append(f"  - {label}: {pct:+.2f}% (close {last_close:,.2f})")
        else:
            lines.append("  - Nasdaq: unavailable")
            lines.append("  - NYSE Composite: unavailable")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Send portfolio significant-move snapshots to Discord.")
    parser.add_argument(
        "--slot",
        choices=("morning", "midday", "close"),
        default="morning",
        help="Which update window is running",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the outgoing message but do not call OpenClaw.")
    args = parser.parse_args()

    positions = load_positions()
    symbols = get_symbols(positions)
    if not symbols:
        print("No symbols configured in portfolio-positions.json. Exiting.")
        sys.exit(1)

    print(f"Fetching {len(symbols)} prices...")
    prices = fetch_all_prices(symbols)
    if not prices:
        print("No prices fetched; aborting.")
        sys.exit(1)

    data = load_shared_data()
    last_prices = data["last_prices_for_updates"]
    prev_total_data = data["last_total_value"]

    significant = []
    for sym in symbols:
        bucket = prices.get(sym)
        if not bucket:
            continue
        price = bucket["price"]
        baseline = last_prices.get(sym)
        if baseline and baseline > 0:
            pct_change = (price - baseline) / baseline * 100
            if abs(pct_change) >= SIGNIFICANCE_PCT:
                significant.append((sym, baseline, price, pct_change))
        last_prices[sym] = price

    total_value = None
    change_delta = 0.0
    change_pct = 0.0
    prev_total_known = False

    if args.slot == "close":
        total_value = compute_total_value(positions, prices)
        prev_value = prev_total_data.get("value") or 0.0
        if prev_value > 0:
            change_delta = total_value - prev_value
            change_pct = (change_delta / prev_value) * 100
            prev_total_known = True
        prev_total_data["value"] = total_value
        prev_total_data["date"] = datetime.now(ET).strftime("%Y-%m-%d")
        data["last_total_value"] = prev_total_data
    else:
        total_value = 0.0

    market_changes = []
    if args.slot == "close":
        for symbol, label in (("%5EIXIC", "Nasdaq Composite"), ("%5ENYA", "NYSE Composite")):
            snap = fetch_index_change(symbol, label)
            if snap:
                market_changes.append(snap)

    data["last_slot"] = args.slot
    data["last_run"] = datetime.now(ET).isoformat()
    save_shared_data(data)

    message = build_message(
        args.slot,
        significant,
        total_value,
        change_delta,
        change_pct,
        prev_total_known,
        market_changes,
    )

    print("--- Message preview ---")
    print(message)
    print("-----------------------")

    if args.dry_run:
        print("Dry run: skipping Discord deliverable.")
    else:
        send_discord_message(message)


if __name__ == "__main__":
    main()
