"""
Rank History Tracker
====================
毎日のランキングをdocs/data/history.jsonに蓄積する

history.jsonの構造:
{
  "app_id": [
    {"date": "2026-05-14", "rank": 3},
    {"date": "2026-05-15", "rank": 1},
    ...
  ],
  ...
}
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

JST = timezone(timedelta(hours=9))
RANKINGS_PATH = Path("docs/data/rankings.json")
HISTORY_PATH  = Path("docs/data/history.json")
MAX_DAYS = 30  # 保持する最大日数


def update_history():
    # 今日の日付
    today = datetime.now(JST).strftime("%Y-%m-%d")

    # 現在のランキング読み込み
    rankings = json.loads(RANKINGS_PATH.read_text(encoding="utf-8"))
    entries = rankings.get("entries", [])

    # 履歴読み込み（なければ空）
    if HISTORY_PATH.exists():
        history = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
    else:
        history = {}

    # 今日のランクを追記
    for entry in entries:
        app_id = entry["app_id"]
        if app_id not in history:
            history[app_id] = []

        # 同じ日付のデータがあれば上書き
        history[app_id] = [h for h in history[app_id] if h["date"] != today]
        history[app_id].append({"date": today, "rank": entry["rank"]})

        # 古いデータを削除（MAX_DAYS日分だけ保持）
        history[app_id] = sorted(history[app_id], key=lambda x: x["date"])[-MAX_DAYS:]

    # ランキング外になったアプリのデータは残す（履歴として価値あり）
    # ただし全アプリのうち上位100件のIDのみ保持
    active_ids = {e["app_id"] for e in entries}
    # 100位以内にいたことがある直近30日のデータは残す
    history = {k: v for k, v in history.items() if k in active_ids or any(
        h["date"] >= (datetime.now(JST) - timedelta(days=MAX_DAYS)).strftime("%Y-%m-%d")
        for h in v
    )}

    HISTORY_PATH.write_text(
        json.dumps(history, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8"
    )
    print(f"[INFO] 履歴更新完了: {len(history)}アプリ / {today}")


if __name__ == "__main__":
    update_history()
