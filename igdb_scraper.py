"""
IGDB Upcoming Games Scraper
============================
IGDBから未発売ゲームのhypes（注目度）ランキングを取得

環境変数:
    IGDB_CLIENT_ID
    IGDB_CLIENT_SECRET
"""

import json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
import requests

TWITCH_TOKEN_URL = "https://id.twitch.tv/oauth2/token"
IGDB_API_URL     = "https://api.igdb.com/v4/games"
OUTPUT_PATH      = Path("docs/data/igdb_upcoming.json")

MAJOR_COMPANIES = {
    "electronic arts", "ea sports", "activision", "blizzard entertainment",
    "ubisoft", "2k games", "take-two interactive", "bethesda softworks",
    "square enix", "bandai namco entertainment", "capcom", "konami", "sega",
    "sony interactive entertainment", "microsoft studios", "xbox game studios",
    "warner bros. games", "505 games", "paradox interactive", "devolver digital",
    "team17", "ncsoft", "nexon", "krafton", "valve",
}

def is_major(company: str) -> bool:
    return company.strip().lower() in MAJOR_COMPANIES


def get_token(client_id: str, client_secret: str) -> str:
    resp = requests.post(TWITCH_TOKEN_URL, params={
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }, timeout=10)
    resp.raise_for_status()
    return resp.json()["access_token"]


def fetch_upcoming(client_id: str, token: str, limit: int = 100) -> list:
    now_ts = int(datetime.now(timezone.utc).timestamp())

    # IGDBのApicalypseクエリ
    query = f"""
    fields name, hypes, first_release_date,
           involved_companies.company.name, involved_companies.publisher,
           platforms.abbreviation, summary, url;
    where first_release_date > {now_ts}
      & hypes != null
      & hypes > 0
      & platforms = (6);
    sort hypes desc;
    limit {limit};
    """
    # platform 6 = PC (Windows)

    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {token}",
        "Content-Type": "text/plain",
    }

    resp = requests.post(IGDB_API_URL, headers=headers, data=query.strip(), timeout=15)
    resp.raise_for_status()
    return resp.json()


def parse_games(raw: list) -> list:
    results = []
    for rank, game in enumerate(raw, start=1):
        # パブリッシャー取得
        publisher = ""
        for ic in game.get("involved_companies", []):
            if ic.get("publisher"):
                publisher = ic.get("company", {}).get("name", "")
                break
        if not publisher:
            for ic in game.get("involved_companies", []):
                publisher = ic.get("company", {}).get("name", "")
                break

        # リリース日
        ts = game.get("first_release_date")
        release_date = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d") if ts else ""

        # プラットフォーム
        platforms = [p.get("abbreviation", "") for p in game.get("platforms", [])]

        results.append({
            "rank": rank,
            "igdb_id": str(game.get("id", "")),
            "name": game.get("name", "不明"),
            "hypes": game.get("hypes", 0),
            "publisher": publisher,
            "is_major": is_major(publisher),
            "is_released": False,
            "release_date": release_date,
            "platforms": ", ".join(platforms),
            "summary": game.get("summary", "")[:200],
            "url": game.get("url", ""),
            "source": "igdb",
        })

    return results


def main():
    client_id     = os.environ.get("IGDB_CLIENT_ID")
    client_secret = os.environ.get("IGDB_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("[ERROR] IGDB_CLIENT_ID / IGDB_CLIENT_SECRET が未設定", file=sys.stderr)
        sys.exit(1)

    print("[INFO] Twitchトークン取得中...")
    token = get_token(client_id, client_secret)

    print("[INFO] IGDBから未発売ゲーム取得中...")
    raw = fetch_upcoming(client_id, token)

    games = parse_games(raw)
    print(f"[INFO] {len(games)}件取得完了")

    from datetime import timedelta
    JST = timezone(timedelta(hours=9))
    output = {
        "updated_at": datetime.now(JST).isoformat(),
        "entries": games,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[INFO] 保存完了: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
