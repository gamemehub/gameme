# CLAUDE.md — このリポジトリの構成と現在の開発対象

セッション開始時にまずこのファイルを読むこと。
ルートの `README.md` は **FEED（別プロジェクト）** の説明であり、現在の開発対象ではない。

## このリポジトリには3つのプロジェクトが同居している

| プロジェクト | 実体 | 状態 |
|---|---|---|
| **RewriteMemory** | `docs/rewrite*/`（下表参照）+ `docs/spec/` `docs/design/` `docs/characters/` | ✅ **現在の開発対象** |
| FEED | ルートの `FEED_game.html` / `index.html` / `README.md`、`feed/`、`docs/feed/` | ❌ スコープ外・触らない |
| GameMe Charts | `docs/index.html`、`docs/data/`、ルートのスクレイパー群（`*_scraper.py` 等）、`daily_update.yml` | ❌ スコープ外・触らない |

**注意**: `docs/index.html` は GameMe Charts の本体であり、RewriteMemory とは無関係。

## RewriteMemory 本体ファイル（唯一の正）

| 環境 | パス | 公開URL | 編集 |
|---|---|---|---|
| dev | `docs/rewrite-dev/index.html` | https://gamemehub.github.io/gameme/rewrite-dev/ | ✅ **AIが編集するのはここだけ** |
| stage | `docs/rewrite-stage/index.html` | https://gamemehub.github.io/gameme/rewrite-stage/ | ❌ `promote-dev-to-stage` 手動実行で反映 |
| 本番 | `docs/rewrite/index.html` | https://gamemehub.github.io/gameme/rewrite/ | ❌ 人間承認PRのみ |

変更後は必ず実行し PASS を確認する:

```
python3 tools/check_scenes.py docs/rewrite-dev/index.html
```

## ブランチ構成（実測・2026-07-02）

- 長寿命ブランチは **`main` のみ**。**`dev` / `develop` は存在しない**（全PRのベースは `main`）。
- ワークフロー名の「dev」（`ci-dev.yml` / `auto-merge-dev.yml`）はブランチではなく **ディレクトリ `docs/rewrite-dev/`** を指す。
- AI作業ブランチは `claude/**`（`auto-pr-claude.yml` の自動PRトリガー条件）。人間は `docs/*` / `feat/*`。

## 自動化パイプライン（発動条件の要約）

1. `claude/**` へ push → `auto-pr-claude.yml` が自動でPR作成。変更が `docs/rewrite/`・`.github/` を含まなければ `auto-merge-dev` ラベル付与。
2. base=main + `auto-merge-dev` ラベル → `auto-merge-dev.yml` が発火。`docs/rewrite/` か `.github/` を含むPRは guard で拒否。通過するとネイティブ auto-merge を有効化。
3. main 宛て全PRで `ci-dev.yml`（scene-integrity）が `check_scenes.py` を実行。これがグリーンでマージされる。
4. dev→stage 反映は `promote-dev-to-stage.yml`（手動 workflow_dispatch のみ）。

**人間レビューを必須にしたい docs 変更PRは Draft のまま維持すること**（Draft は auto-merge を有効化できない）。

## 詳細・経緯

- インフラ監査の全記録: `docs/audit/INFRA_AUDIT_2026-07-02.md`
- より包括的な運用ルール（レーン定義・役割分担・正典リポジトリ方針）は PR #48（保留/HOLD）で検討中。本ファイルと矛盾する決定が人間承認された場合はそちらを正とする。
