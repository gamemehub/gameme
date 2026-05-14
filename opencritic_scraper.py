"""
OpenCritic Scraper (RapidAPI経由)
==================================
OpenCriticから批評家スコアランキングを取得

環境変数:
    RAPIDAPI_KEY
"""

import json, os, sys, time
from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

RAPIDAPI_KEY  = os.environ.get("RAPIDAPI_KEY", "")
API_HOST      = "opencritic-api.p.rapidapi.com"
BASE_URL      = f"https://{API_HOST}"
OUTPUT_PATH   = Path("docs/data/opencritic.json")
JST           = timezone(timedelta(hours=9))

HEADERS = {
    "x-rapidapi-host": API_HOST,
    "x-rapidapi-key": RAPIDAPI_KEY,
}

MAJOR_COMPANIES = {
    "electronic arts", "activision", "ubisoft", "2k games", "take-two interactive",
    "bethesda softworks", "square enix", "bandai namco entertainment", "capcom",
    "konami", "sega", "sony interactive entertainment", "xbox game studios",
    "warner bros. games", "505 games", "paradox interactive", "devolver digital",
    "team17", "ncsoft", "nexon", "krafton", "valve",
}

def is_major(company: str) -> bool:
    return company.strip().lower() in MAJOR_COMPANIES


def fetch_recently_released(skip: int = 0, take: int = 25) -> list:
    """最近リリースされた批評家スコア付きゲーム取得"""
    try:
        resp = requests.get(
            f"{BASE_URL}/game/recently-released",
            headers=HEADERS,
            params={"skip": skip, "take": take},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[ERROR] recently-released: {e}", file=sys.stderr)
        return []


def fetch_top_games(skip: int = 0, take: int = 25) -> list:
    """スコア順トップゲーム取得"""
    try:
        resp = requests.get(
            f"{BASE_URL}/game",
            headers=HEADERS,
            params={"order": "score", "skip": skip, "take": take},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[ERROR] top games: {e}", file=sys.stderr)
        return []


def parse_game(rank: int, game: dict) -> dict:
    """ゲームデータをパース"""
    companies = game.get("Companies", []) or []
    publisher = ""
    for c in companies:
        if c.get("type") == "PUBLISHER":
            publisher = c.get("name", "")
            break
    if not publisher and companies:
        publisher = companies[0].get("name", "")

    # リリース日
    first_release = game.get("firstReleaseDate") or game.get("releaseDate") or ""
    if first_release:
        try:
            dt = datetime.fromisoformat(first_release.replace("Z", "+00:00"))
            release_date = dt.strftime("%Y-%m-%d")
            is_released = dt <= datetime.now(timezone.utc)
        except Exception:
            release_date = first_release[:10]
            is_released = True
    else:
        release_date = ""
        is_released = True

    # スコア
    top_critic_score = game.get("topCriticScore")
    median_score = game.get("medianScore")
    percent_recommended = game.get("percentRecommended")
    critic_reviews = game.get("numReviews", 0)

    # スコアラベル
    score_label = ""
    if top_critic_score is not None:
        s = int(top_critic_score)
        if s >= 90:   score_label = "Must Play"
        elif s >= 75: score_label = "Strong"
        elif s >= 60: score_label = "Fair"
        elif s >= 40: score_label = "Weak"
        else:         score_label = "Skip"

    return {
        "rank": rank,
        "opencritic_id": str(game.get("id", "")),
        "name": game.get("name", "不明"),
        "publisher": publisher,
        "is_major": is_major(publisher),
        "is_released": is_released,
        "release_date": release_date,
        "top_critic_score": top_critic_score,
        "median_score": median_score,
        "percent_recommended": percent_recommended,
        "critic_reviews": critic_reviews,
        "score_label": score_label,
        "url": f"https://opencritic.com/game/{game.get('id')}/{game.get('slug', '')}",
        "source": "opencritic",
    }


def main():
    if not RAPIDAPI_KEY:
        print("[ERROR] RAPIDAPI_KEY が未設定", file=sys.stderr)
        sys.exit(1)

    print("[INFO] OpenCritic 最近リリース取得中...")
    games_raw = []

    # 最近リリース分（25件×2ページ = 50件）
    for skip in [0, 25]:
        batch = fetch_recently_released(skip=skip, take=25)
        games_raw.extend(batch)
        if len(batch) < 25:
            break
        time.sleep(0.5)

    # スコア順トップも追加（重複除外）
    print("[INFO] OpenCritic トップスコア取得中...")
    existing_ids = {str(g.get("id")) for g in games_raw}
    top = fetch_top_games(skip=0, take=25)
    for g in top:
        if str(g.get("id")) not in existing_ids:
            games_raw.append(g)
            existing_ids.add(str(g.get("id")))

    # スコアでソート（スコアなしは末尾）
    def sort_key(g):
        s = g.get("topCriticScore")
        return -(s if s is not None else -1)

    games_raw.sort(key=sort_key)

    # パース
    entries = [parse_game(i + 1, g) for i, g in enumerate(games_raw)]
    print(f"[INFO] {len(entries)}件取得完了")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "updated_at": datetime.now(JST).isoformat(),
        "entries": entries,
    }
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[INFO] 保存完了: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
