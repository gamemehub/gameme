"""
Steam Wishlist Ranking Scraper (SteamSpy API版)
================================================
SteamSpy APIからゲームランキングデータを取得

必要なライブラリ:
    pip install requests

使い方:
    python steam_wishlist_scraper.py
    python steam_wishlist_scraper.py --count 100 --output json --file data/rankings_new.json
"""

import argparse
import csv
import json
import sys
import time
from dataclasses import asdict, dataclass
from typing import Optional

import requests

STEAMSPY_API = "https://steamspy.com/api.php"
STEAM_APP_URL = "https://store.steampowered.com/app"
REQUEST_INTERVAL = 1.5

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
}


@dataclass
class GameEntry:
    rank: int
    app_id: str
    name: str
    release_date: str
    price: str
    review_summary: str
    review_count: str
    owners: str = ""
    url: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class SteamSpyScraper:
    def __init__(self, interval: float = REQUEST_INTERVAL):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.interval = interval

    def _fetch_top100(self, request_type: str = "top100in2weeks") -> dict:
        params = {"request": request_type}
        try:
            resp = self.session.get(STEAMSPY_API, params=params, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"[ERROR] {request_type} 取得失敗: {e}", file=sys.stderr)
            return {}

    def _parse_price(self, price_cents) -> str:
        try:
            p = int(price_cents)
        except (TypeError, ValueError):
            return "未発表"
        if p == 0:
            return "無料"
        if p < 0:
            return "未発表"
        return f"${p / 100:.2f}"

    def _parse_owners(self, owners_str: str) -> str:
        try:
            parts = owners_str.replace(",", "").split("..")
            low = int(parts[0].strip())
            high = int(parts[1].strip())
            def fmt(n):
                if n >= 1_000_000:
                    return f"{n//1_000_000}M"
                if n >= 1_000:
                    return f"{n//1_000}K"
                return str(n)
            return f"{fmt(low)}〜{fmt(high)}"
        except Exception:
            return owners_str

    def _calc_review(self, positive: int, negative: int) -> str:
        total = positive + negative
        if total == 0:
            return ""
        pct = int(positive / total * 100)
        if pct >= 95: return "圧倒的に好評"
        if pct >= 80: return "非常に好評"
        if pct >= 70: return "好評"
        if pct >= 40: return "賛否両論"
        return "不評"

    def fetch(self, total: int = 100) -> list:
        print("[INFO] SteamSpy TOP100 取得中...")
        data = self._fetch_top100("top100in2weeks")
        if not data:
            print("[INFO] フォールバック: top100forever")
            data = self._fetch_top100("top100forever")
        if not data:
            return []

        entries = []
        for rank, (app_id, info) in enumerate(list(data.items())[:total], start=1):
            positive = info.get("positive", 0)
            negative = info.get("negative", 0)
            total_reviews = positive + negative
            entry = GameEntry(
                rank=rank,
                app_id=str(app_id),
                name=info.get("name", "不明"),
                release_date=info.get("initiallyreleased", ""),
                price=self._parse_price(info.get("price", -1)),
                review_summary=self._calc_review(positive, negative),
                review_count=f"{total_reviews:,}" if total_reviews > 0 else "",
                owners=self._parse_owners(info.get("owners", "")),
                url=f"{STEAM_APP_URL}/{app_id}",
            )
            entries.append(entry)

        print(f"[INFO] 合計 {len(entries)} 件取得完了")
        return entries


def output_table(entries):
    print("\n" + "=" * 90)
    print(f"{'順位':^4} {'タイトル':^35} {'価格':^10} {'レビュー':^12} {'所有者数':^15}")
    print("=" * 90)
    for e in entries:
        title = e.name[:33] + ".." if len(e.name) > 35 else e.name
        print(f"{e.rank:>4}  {title:<35} {e.price:<10} {e.review_summary:<12} {e.owners}")
    print("=" * 90)


def output_json(entries, filepath=None):
    data = [e.to_dict() for e in entries]
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[INFO] JSON保存: {filepath}")
    else:
        print(text)


def output_csv(entries, filepath=None):
    if not entries:
        return
    fieldnames = list(entries[0].to_dict().keys())
    rows = [e.to_dict() for e in entries]
    if filepath:
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"[INFO] CSV保存: {filepath}")
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--count",    type=int,   default=100)
    p.add_argument("--output",   choices=["table", "json", "csv"], default="table")
    p.add_argument("--file",     type=str,   default=None)
    p.add_argument("--interval", type=float, default=1.5)
    return p.parse_args()


def main():
    args = parse_args()
    scraper = SteamSpyScraper(interval=args.interval)
    entries = scraper.fetch(total=args.count)
    if not entries:
        print("[ERROR] データが取得できませんでした", file=sys.stderr)
        sys.exit(1)
    if args.output == "table":
        output_table(entries)
    elif args.output == "json":
        output_json(entries, filepath=args.file)
    elif args.output == "csv":
        output_csv(entries, filepath=args.file)


if __name__ == "__main__":
    main()
