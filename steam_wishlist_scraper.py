"""
Steam Wishlist Ranking Scraper
==============================
Steamのウィッシュリストランキングを取得するスクリプト

必要なライブラリ:
    pip install requests beautifulsoup4

使い方:
    python steam_wishlist_scraper.py
    python steam_wishlist_scraper.py --count 50 --output csv
    python steam_wishlist_scraper.py --count 100 --output json --file results.json
"""

import argparse
import csv
import json
import sys
import time
from dataclasses import asdict, dataclass, field
from typing import Optional

import requests
from bs4 import BeautifulSoup

# ─────────────────────────────────────────────
# 定数
# ─────────────────────────────────────────────
STEAM_SEARCH_API = "https://store.steampowered.com/search/results/"
STEAM_APP_URL = "https://store.steampowered.com/app"
REQUEST_INTERVAL = 1.0  # 秒（サーバー負荷対策）

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ─────────────────────────────────────────────
# データモデル
# ─────────────────────────────────────────────
@dataclass
class GameEntry:
    rank: int
    app_id: str
    name: str
    release_date: str
    price: str
    review_summary: str
    review_count: str
    tags: list[str] = field(default_factory=list)
    url: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["tags"] = ", ".join(self.tags)
        return d


# ─────────────────────────────────────────────
# フェッチ
# ─────────────────────────────────────────────
class SteamWishlistScraper:
    def __init__(self, interval: float = REQUEST_INTERVAL):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.interval = interval

    def _fetch_page(self, start: int, count: int) -> Optional[str]:
        """Steam検索APIからHTMLを取得"""
        params = {
            "filter": "wishlist",
            "start": start,
            "count": count,
        }
        try:
            resp = self.session.get(STEAM_SEARCH_API, params=params, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            return data.get("results_html", "")
        except requests.RequestException as e:
            print(f"[ERROR] ページ取得失敗 (start={start}): {e}", file=sys.stderr)
            return None
        except json.JSONDecodeError:
            # JSONでない場合はHTMLとして処理
            return resp.text

    def _parse_html(self, html: str, start_rank: int) -> list[GameEntry]:
        """HTMLをパースしてゲームリストを返す"""
        soup = BeautifulSoup(html, "html.parser")
        entries = []

        rows = soup.select("a.search_result_row")
        for i, row in enumerate(rows):
            rank = start_rank + i + 1

            # App ID
            app_id = row.get("data-ds-appid", "")

            # タイトル
            name_el = row.select_one(".title")
            name = name_el.get_text(strip=True) if name_el else "不明"

            # リリース日
            date_el = row.select_one(".search_released")
            release_date = date_el.get_text(strip=True) if date_el else ""

            # 価格
            price_el = row.select_one(".discount_final_price") or row.select_one(".search_price")
            price = price_el.get_text(strip=True) if price_el else "未発表"

            # レビュー
            review_el = row.select_one("[data-tooltip-html]")
            review_text = ""
            review_count = ""
            if review_el:
                tooltip = review_el.get("data-tooltip-html", "")
                # "好評 (1,234 件のレビュー)" のような形式
                review_text = tooltip.split("<br>")[0] if "<br>" in tooltip else tooltip

            # タグ (data属性から)
            tags_raw = row.get("data-ds-tagids", "[]")
            try:
                tag_ids = json.loads(tags_raw)
            except json.JSONDecodeError:
                tag_ids = []

            url = f"{STEAM_APP_URL}/{app_id}" if app_id else ""

            entries.append(GameEntry(
                rank=rank,
                app_id=app_id,
                name=name,
                release_date=release_date,
                price=price,
                review_summary=review_text,
                review_count=review_count,
                url=url,
            ))

        return entries

    def fetch(self, total: int = 50, page_size: int = 25) -> list[GameEntry]:
        """ウィッシュリストランキングを取得"""
        all_entries: list[GameEntry] = []
        fetched = 0

        print(f"[INFO] Steam ウィッシュリストランキング取得開始 (目標: {total}件)")

        while fetched < total:
            batch = min(page_size, total - fetched)
            print(f"[INFO] {fetched + 1}〜{fetched + batch} 位を取得中...", end=" ", flush=True)

            html = self._fetch_page(start=fetched, count=batch)
            if html is None:
                print("スキップ")
                break

            entries = self._parse_html(html, start_rank=fetched)
            if not entries:
                print("データなし → 終了")
                break

            all_entries.extend(entries)
            fetched += len(entries)
            print(f"取得: {len(entries)}件")

            if fetched < total:
                time.sleep(self.interval)

        print(f"[INFO] 合計 {len(all_entries)} 件取得完了")
        return all_entries


# ─────────────────────────────────────────────
# 出力
# ─────────────────────────────────────────────
def output_table(entries: list[GameEntry]) -> None:
    """ターミナルに表形式で表示"""
    print("\n" + "=" * 90)
    print(f"{'順位':^4} {'タイトル':^35} {'価格':^10} {'リリース':^12} {'レビュー':^20}")
    print("=" * 90)
    for e in entries:
        title = e.name[:33] + ".." if len(e.name) > 35 else e.name
        review = e.review_summary[:18] + ".." if len(e.review_summary) > 20 else e.review_summary
        print(f"{e.rank:>4}  {title:<35} {e.price:<10} {e.release_date:<12} {review}")
    print("=" * 90)


def output_json(entries: list[GameEntry], filepath: Optional[str] = None) -> None:
    data = [e.to_dict() for e in entries]
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[INFO] JSON保存: {filepath}")
    else:
        print(text)


def output_csv(entries: list[GameEntry], filepath: Optional[str] = None) -> None:
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


# ─────────────────────────────────────────────
# エントリーポイント
# ─────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(description="Steam ウィッシュリストランキング スクレイパー")
    p.add_argument("--count",  type=int, default=50,     help="取得件数 (デフォルト: 50)")
    p.add_argument("--output", choices=["table", "json", "csv"], default="table",
                   help="出力形式 (デフォルト: table)")
    p.add_argument("--file",   type=str, default=None,   help="保存先ファイルパス")
    p.add_argument("--interval", type=float, default=1.0, help="リクエスト間隔(秒) (デフォルト: 1.0)")
    return p.parse_args()


def main():
    args = parse_args()

    scraper = SteamWishlistScraper(interval=args.interval)
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
