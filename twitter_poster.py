"""
Twitter Auto Poster - Steam Wishlist Ranking
============================================
GitHub Actionsから呼び出されるTwitter投稿スクリプト

環境変数 (GitHub Secrets に設定):
    TWITTER_API_KEY
    TWITTER_API_SECRET
    TWITTER_ACCESS_TOKEN
    TWITTER_ACCESS_TOKEN_SECRET
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import tweepy

# ─────────────────────────────────────────────
# Twitter認証
# ─────────────────────────────────────────────
def get_client() -> tweepy.Client:
    return tweepy.Client(
        consumer_key=os.environ["TWITTER_API_KEY"],
        consumer_secret=os.environ["TWITTER_API_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )


# ─────────────────────────────────────────────
# データ読み込み
# ─────────────────────────────────────────────
def load_rankings(path: str = "data/rankings.json") -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ─────────────────────────────────────────────
# ツイート生成
# ─────────────────────────────────────────────
JST = timezone(timedelta(hours=9))

def make_daily_top10(data: dict) -> str:
    """毎日トップ10ツイート"""
    today = datetime.now(JST).strftime("%Y/%m/%d")
    entries = data["entries"][:10]

    lines = [f"🎮 Steam ウィッシュリスト TOP10（{today}）\n"]
    medals = ["🥇", "🥈", "🥉"]
    for i, e in enumerate(entries):
        medal = medals[i] if i < 3 else f"{i+1}."
        price = e.get("price", "未発表")
        lines.append(f"{medal} {e['name']}　{price}")

    lines.append("\n🔗 詳細 → https://gamemehub.github.io/gameme/")
    lines.append("#Steam #ゲーム #ウィッシュリスト")

    return "\n".join(lines)


def make_movers(data: dict) -> list[str]:
    """順位変動・新着ツイート（複数になることがある）"""
    entries = data["entries"]
    prev = {e["app_id"]: e.get("prev_rank") for e in entries if e.get("prev_rank")}
    tweets = []

    # 新着（前回ランキング外から登場）
    new_entries = [e for e in entries[:20] if e.get("is_new")]
    if new_entries:
        lines = ["🆕 Steam ウィッシュリスト 新着ランクイン！\n"]
        for e in new_entries[:5]:
            lines.append(f"▶ {e['name']}（{e['rank']}位）")
        lines.append("\n#Steam #新作ゲーム")
        tweets.append("\n".join(lines))

    # 急上昇（10位以上アップ）
    risers = [
        e for e in entries[:30]
        if e.get("prev_rank") and (e["prev_rank"] - e["rank"]) >= 10
    ]
    if risers:
        lines = ["📈 Steam ウィッシュリスト 急上昇！\n"]
        for e in risers[:5]:
            diff = e["prev_rank"] - e["rank"]
            lines.append(f"↑{diff} {e['name']}　{e['prev_rank']}位→{e['rank']}位")
        lines.append("\n#Steam #ゲーム")
        tweets.append("\n".join(lines))

    return tweets


# ─────────────────────────────────────────────
# 投稿
# ─────────────────────────────────────────────
def post(client: tweepy.Client, text: str, dry_run: bool = False) -> None:
    print(f"\n--- ツイート ---\n{text}\n(文字数: {len(text)})")
    if dry_run:
        print("[DRY RUN] 実際には投稿しません")
        return
    resp = client.create_tweet(text=text)
    print(f"[OK] Tweet ID: {resp.data['id']}")


def main():
    dry_run = "--dry-run" in sys.argv

    data = load_rankings()
    client = get_client() if not dry_run else None

    # 1. 毎日トップ10
    top10_tweet = make_daily_top10(data)
    post(client, top10_tweet, dry_run=dry_run)

    # 2. 変動・新着
    mover_tweets = make_movers(data)
    for tweet in mover_tweets:
        post(client, tweet, dry_run=dry_run)

    print(f"\n[完了] {len(mover_tweets) + 1}件投稿")


if __name__ == "__main__":
    main()
