# RewriteMemory インフラ監査レポート（2026-07-02）

目的: Chapter 1 開発の自律運用開始前に、インフラの矛盾を検証・解消する（Go/No-Go 判断の前提調査）。
方法: リポジトリ実体（全リモートブランチ含む）・GitHub Actions 定義・オープンPRを読み取りで検証。ゲーム本体（HTML/JS）・CI（`.github/`）は一切変更していない。

---

## 1. メインファイルパスの確定【最重要・確定】

**正しいパスは以下の3系統。「`docs/index.html` が RewriteMemory 本体」という記述は誤り。**

| 環境 | パス | 公開URL（GitHub Pages, `docs/` 配下がURLパスに対応） | 実在 |
|---|---|---|---|
| 本番 | `docs/rewrite/index.html` | `https://gamemehub.github.io/gameme/rewrite/` | ✅（196KB, title=RewriteMemory） |
| stage | `docs/rewrite-stage/index.html` | `…/gameme/rewrite-stage/` | ✅（202KB） |
| dev（AI編集対象） | `docs/rewrite-dev/index.html` | `…/gameme/rewrite-dev/` | ✅（212KB, `tools/check_scenes.py` PASS: 143シーン・参照切れ0） |

- `docs/index.html` は **RewriteMemory ではない**。「GameMe Charts」（ゲームランキングチャートサイト、`docs/data/*.json` + ルートのスクレイパー群 + `daily_update.yml` が実体）の本体である。
- 本番URL `gamemehub.github.io/gameme/rewrite/` と整合するのは `docs/rewrite/index.html`。**HANDOFF.md 側の記述が正**。
- CI・ワークフローもこれを裏付ける:
  - `ci-dev.yml`（scene-integrity）は `docs/rewrite-dev/index.html` を検証
  - `promote-dev-to-stage.yml` は `docs/rewrite-dev/` → `docs/rewrite-stage/` へ rsync コピー
  - `auto-merge-dev.yml` は `docs/rewrite/`（本番）変更を自動マージ禁止としてガード

### 前提とされた「CLAUDE.md / HANDOFF.md の矛盾」の実態
- **`main` ブランチに CLAUDE.md は存在しない**（全30リモートブランチを走査）。CLAUDE.md が存在するのは未マージの2ブランチのみ:
  - `claude/autonomous-team-org-chdxa7`（PR #48・保留/HOLD）— 本体パスを `docs/rewrite-dev/index.html` と正しく記載
  - `claude/add-3questions-claude-md-i6gt0c`（PR #28・Draft）— パス記載なし（Unity前提の一般論）
- **HANDOFF.md はリポジトリ内のどのブランチにも存在しない**（リポジトリ外＝ローカル/会話由来の文書と推定）。
- リポジトリ内に「`docs/index.html` を RewriteMemory 本体とする」記述は発見できず。矛盾の発生源はリポジトリ外の文書か、`docs/index.html`（GameMe Charts）との混同と推定される。

---

## 2. FEED 混入の原因【特定】

**リポジトリのルートは FEED プロジェクトそのもの**であり、`main` にルート CLAUDE.md が無いため、セッション開始時に AI が最初に読む文書が FEED の README になる。これが誤コンテキストの原因。

- ルート `README.md` … 「# FEED — GC2026応募作品プロトタイプ」（FEED の説明のみ）
- ルート `index.html` … `FEED_game.html` と **バイト単位で同一**（FEED ゲーム本体のコピー）
- `feed/`・`docs/feed/` … FEED の公開ページ群
- さらに第3のプロジェクト「GameMe Charts」（`docs/index.html`, `docs/data/`, `igdb_scraper.py` ほかスクレイパー群, `daily_update.yml`, `twitter_poster.py`）も同居
- つまり **1リポジトリに3プロジェクト同居**（FEED / GameMe Charts / RewriteMemory）で、ルートの顔は FEED

**修正内容（本PR）**: ルートに最小限の `CLAUDE.md` を新規追加し、①3プロジェクト同居の事実、②現在の開発対象は RewriteMemory のみ、③正しい本体パス（上表）、④ブランチ構成、⑤自動化の発動条件を明記した。FEED / GameMe Charts のファイルには一切触れていない。

---

## 3. 実在するブランチ構成【確定】

- **`dev` も `develop` も存在しない。** 長寿命ブランチは `main` のみ（リモート全30ブランチを実測）。
- その他は全てトピックブランチ: `claude/**`（AI作業・自動PRトリガー）、`docs/*`、`feat/*`、`feature/*`（旧）、`sync/*`（旧）、`gamemehub-patch-1`。
- 全PRのベースは `main`。ワークフロー名の「dev」（`ci-dev.yml` / `auto-merge-dev.yml`）は **ブランチではなくディレクトリ `docs/rewrite-dev/` を指す**。過去にも PR #28 が「base=develop 指定だが develop 不在のため main に変更」と記録しており、既知の混乱ポイント。

---

## 4. auto-merge パイプラインの発動条件【現状報告のみ・無変更】

実体は4ワークフローの連鎖:

1. **`auto-pr-claude.yml`** — トリガー: `claude/**` への push。main と差分があれば open PR が無い場合に**自動でPRを作成**し、変更ファイルに `docs/rewrite/`・`.github/` が**含まれない場合のみ** `auto-merge-dev` ラベルを付与。
2. **`auto-merge-dev.yml`** — トリガー: PR の labeled/opened/synchronize/reopened、かつ `base == main` **かつ** ラベル `auto-merge-dev` 付き。guard ステップで変更ファイルに `^docs/rewrite/` または `^\.github/` があれば **exit 1（自動マージ拒否）**。通過すれば `gh pr merge --auto --merge --delete-branch`（GitHub ネイティブ auto-merge を有効化）。
3. **`ci-dev.yml`（scene-integrity）** — トリガー: main 宛て全PR。`python3 tools/check_scenes.py docs/rewrite-dev/index.html` が PASS で成功。auto-merge の「CIグリーン」判定対象。
4. **`promote-dev-to-stage.yml`** — `workflow_dispatch`（手動）のみ。dev→stage の rsync コピー。本番には触れない。

補足（ワークフロー内コメントに明記されている前提・リポジトリからは検証不能）:
- 完全無人化には `secrets.GH_PAT` の設定が必要（既定の GITHUB_TOKEN では作成PR/ラベルが後続ワークフローを起動しない）。
- main のブランチ保護で必須チェック `scene-integrity` が有効であることが「CIグリーンまでマージ保留」の担保。**未設定の場合、auto-merge 有効化後に CI を待たずマージされ得る**。

⚠️ **運用上の注意（本監査で顕在化）**: docs のみを変更する `claude/**` ブランチの push は、上記 1→2 により**自動マージ経路に乗る**（`docs/rewrite/`・`.github/` を含まないため）。「自動マージ禁止・人間レビュー前提」の作業は、**PR を Draft のまま維持する**こと（Draft は auto-merge を有効化できないため物理的に止まる）。本PRもこの方法で自動マージを回避している。

---

## 5. 未確認事項・残課題（Go/No-Go 判断向け）

1. **GitHub Pages の公開設定**（ソース: main の `/docs` か）はリポジトリ設定のため読み取り不能。公開URLの構造（`/gameme/rewrite/` 等）から `docs/` 配下対応はほぼ確実だが、設定画面での確認を推奨。
2. **main のブランチ保護**（必須チェック `scene-integrity` の有無）と **`secrets.GH_PAT` の設定有無**は確認不能。未設定なら「CIグリーン前にマージ」「自動化チェーン不発」のリスクが残る。**Go 判断前に要確認**。
3. **HANDOFF.md の所在**: リポジトリ内に存在しない。正本をリポジトリに入れるか、リポジトリ外文書と割り切るかの判断が必要。
4. **PR #48（保留/HOLD）との関係**: #48 はより包括的な CLAUDE.md と監査文書（正典リポジトリ = `gamemehub/RewriteMemory`、gameme は公開面のみとする方針案）を含む。本PRの CLAUDE.md は現状の事実記述に留めており、#48 の方針判断（Chairman 決定）とは独立。#48 をマージする際は CLAUDE.md が競合するため統合が必要。
5. **正典リポジトリ問題**: #48 の監査ドラフトは「開発の正典は `gamemehub/RewriteMemory`（本セッションからはアクセス不可）」と主張。gameme での Chapter 1 自律運用開始とどう整合させるかは未決。
6. PR #28 / #36 / #35 / #42 が open のまま滞留。クローズ/マージの判断が必要。
7. 作業ブランチ名: 指示は `chore/infra-audit-20260703` だったが、本セッションに割り当てられたブランチが `claude/rewrite-memory-infra-audit-ndd86m` であり、別ブランチへの push が禁止されているためこちらを使用。なお `chore/**` は `auto-pr-claude.yml` のトリガー対象外である点も命名規約検討時の材料になる。
