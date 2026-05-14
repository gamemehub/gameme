"""
Steam Ranking Scraper (SteamSpy API版)
"""

import argparse, csv, json, sys
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional
import requests

STEAMSPY_API  = "https://steamspy.com/api.php"
STEAM_APP_URL = "https://store.steampowered.com/app"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# メジャーパブリッシャー一覧
MAJOR_PUBLISHERS = {
    "valve", "electronic arts", "ea sports", "activision", "blizzard entertainment",
    "activision blizzard", "ubisoft", "2k", "2k games", "take-two interactive",
    "bethesda softworks", "bethesda game studios", "square enix", "bandai namco",
    "bandai namco entertainment", "capcom", "konami", "sega", "atlus",
    "sony interactive entertainment", "microsoft studios", "xbox game studios",
    "warner bros. games", "warner bros. interactive entertainment", "thq nordic",
    "deep silver", "koch media", "focus home interactive", "focus entertainment",
    "paradox interactive", "devolver digital", "team17", "505 games",
    "ncsoft", "nexon", "netmarble", "krafton",
}

def is_major(publisher: str) -> bool:
    if not publisher:
        return False
    return publisher.strip().lower() in MAJOR_PUBLISHERS

def check_released(date_str: str) -> bool:
    """リリース済みかどうか判定"""
    if not date_str:
        return True  # 日付不明 = リリース済み扱い（top100は全て発売済み）
    try:
        for fmt in ("%b %d, %Y", "%Y-%m-%d", "%d %b, %Y", "%B %d, %Y"):
            try:
                dt = datetime.strptime(date_str.strip(), fmt)
                return dt <= datetime.now()
            except ValueError:
                continue
        return True  # パース失敗 = リリース済み扱い
    except Exception:
        return True


@dataclass
class GameEntry:
    rank: int
    app_id: str
    name: str
    developer: str
    publisher: str
    is_major: bool
    release_date: str
    price: str
    review_summary: str
    review_count: str
    is_released: bool = True
    owners: str = ""
    url: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class SteamSpyScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def _fetch_top100(self, request_type="top100in2weeks") -> dict:
        try:
            resp = self.session.get(STEAMSPY_API, params={"request": request_type}, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"[ERROR] {request_type}: {e}", file=sys.stderr)
            return {}

    def _parse_price(self, price_cents) -> str:
        try:
            p = int(price_cents)
        except (TypeError, ValueError):
            return "未発表"
        if p == 0: return "無料"
        if p < 0:  return "未発表"
        return f"${p/100:.2f}"

    def _parse_owners(self, s: str) -> str:
        try:
            parts = s.replace(",","").split("..")
            lo, hi = int(parts[0].strip()), int(parts[1].strip())
            def fmt(n): return f"{n//1_000_000}M" if n>=1_000_000 else f"{n//1_000}K" if n>=1_000 else str(n)
            return f"{fmt(lo)}〜{fmt(hi)}"
        except: return s

    def _calc_review(self, pos, neg) -> str:
        total = pos + neg
        if total == 0: return ""
        pct = int(pos / total * 100)
        if pct >= 95: return "圧倒的に好評"
        if pct >= 80: return "非常に好評"
        if pct >= 70: return "好評"
        if pct >= 40: return "賛否両論"
        return "不評"

    def fetch(self, total=100) -> list:
        print("[INFO] SteamSpy TOP100 取得中...")
        data = self._fetch_top100("top100in2weeks") or self._fetch_top100("top100forever")
        if not data:
            return []

        entries = []
        for rank, (app_id, info) in enumerate(list(data.items())[:total], start=1):
            pos = info.get("positive", 0)
            neg = info.get("negative", 0)
            pub = info.get("publisher", "")
            dev = info.get("developer", "")
            entries.append(GameEntry(
                rank=rank,
                app_id=str(app_id),
                name=info.get("name", "不明"),
                developer=dev,
                publisher=pub,
                is_major=is_major(pub),
                release_date=info.get("initiallyreleased", ""),
                is_released=check_released(info.get("initiallyreleased", "")),
                price=self._parse_price(info.get("price", -1)),
                review_summary=self._calc_review(pos, neg),
                review_count=f"{pos+neg:,}" if pos+neg > 0 else "",
                review_score=int(pos/(pos+neg)*100) if pos+neg > 0 else None,
                owners=self._parse_owners(info.get("owners", "")),
                url=f"{STEAM_APP_URL}/{app_id}",
            ))

        print(f"[INFO] {len(entries)}件取得完了")
        return entries


def output_json(entries, filepath=None):
    data = [e.to_dict() for e in entries]
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f: f.write(text)
        print(f"[INFO] JSON保存: {filepath}")
    else:
        print(text)

def output_csv(entries, filepath=None):
    if not entries: return
    fieldnames = list(entries[0].to_dict().keys())
    rows = [e.to_dict() for e in entries]
    if filepath:
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames); w.writeheader(); w.writerows(rows)
        print(f"[INFO] CSV保存: {filepath}")
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=fieldnames); w.writeheader(); w.writerows(rows)

def output_table(entries):
    print("\n" + "="*95)
    print(f"{'順位':^4} {'タイトル':^30} {'パブリッシャー':^20} {'価格':^10} {'メジャー':^6}")
    print("="*95)
    for e in entries:
        t = e.name[:28]+".." if len(e.name)>30 else e.name
        p = e.publisher[:18]+".." if len(e.publisher)>20 else e.publisher
        print(f"{e.rank:>4}  {t:<30} {p:<20} {e.price:<10} {'✓' if e.is_major else ''}")
    print("="*95)

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--count",  type=int, default=100)
    p.add_argument("--output", choices=["table","json","csv"], default="table")
    p.add_argument("--file",   type=str, default=None)
    return p.parse_args()

def main():
    args = parse_args()
    entries = SteamSpyScraper().fetch(total=args.count)
    if not entries:
        print("[ERROR] データ取得失敗", file=sys.stderr); sys.exit(1)
    if args.output == "table":   output_table(entries)
    elif args.output == "json":  output_json(entries, args.file)
    elif args.output == "csv":   output_csv(entries, args.file)

if __name__ == "__main__":
    main()
