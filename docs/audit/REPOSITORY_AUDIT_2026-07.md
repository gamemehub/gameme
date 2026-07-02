# Repository Audit & Canonical-Repo Governance（2026-07）

状態: v0.9（ドラフト）/ **本監査の目的＝「AIが誤ったRepositoryで開発しても、自動検知・停止・修正できる運用基盤」を確立すること**。ファイル移動が目的ではない。
発生源: gameme に AI自律基盤を構築してしまった事故（PR #48）の是正。
制約: 本ドキュメント作成時点で、稼働セッションのGitHubスコープは **`gamemehub/gameme` のみ**。`gamemehub/RewriteMemory` は読み取り不可。したがって **①②③のRewriteMemory側は「dual-scopeセッションで確定」** とマークしている。⑤⑥⑦は本ファイル単独で確定可能。

> このファイルの最終的な正しい置き場所は **`gamemehub/RewriteMemory`**。ここ（gameme）は書き込み可能な唯一の場所のための**一時ステージング**であり、PR #48（保留・マージしない）に相乗りしている。dual-scopeセッションで RewriteMemory へ移植すること。

---

## 前提（Chairman 決定・確定事項）

| リポジトリ | 役割（確定） | AI開発を受け入れるか |
|---|---|---|
| **`gamemehub/RewriteMemory`** | **正典**：Godotプロジェクト本体 / AI自律開発基盤 / CI・Runner・Agent・Supervisor / Issue・PR・Labels / 開発用ドキュメント | ✅ **YES（唯一）** |
| **`gamemehub/gameme`** | 旧HTML版 / GitHub Pages / 公開デモ / 告知(LP) | ❌ NO |

---

## ① Repository Audit Report（比較表）

RewriteMemory 側は本セッションでは未取得（`ACCESS DENIED`）。dual-scopeセッションで実測して埋める。gameme 側は本セッションで確認済みの事実。

| 比較軸 | gamemehub/gameme（確認済み） | gamemehub/RewriteMemory（**要dual-scope確認**） | 備考 |
|---|---|---|---|
| ディレクトリ構成 | `docs/`（rewrite-dev/stage/rewrite、spec/design/characters/project/audit）、`prototype/godot-1room/`、`tools/autonomy/`、`.github/workflows/`、ルートに FEED_game.html 等 | ❓ Godotプロジェクト本体（project.godot、scenes/、scripts/…）想定 | gameme の rewrite-dev は **1DのDOM/CSS擬似歩行**（本物のtilemapエンジンではない） |
| ドキュメント | `docs/**` に spec/design/project 多数（今回追加分含む） | ❓ 開発ドキュメント群 | 重複疑い大 |
| CLAUDE.md | ルートに存在（gameme を「単一の真実」と自己宣言＝**誤誘導の元**） | ❓ 存在の有無・内容不明 | ②で重複判定 |
| AI運用基盤 | 今回 `docs/project/AI_OPS_ARCHITECTURE_v1.md` 等を新規構築 | ❓ **既存の同種基盤あり（本命）** | 重複の中心 |
| GitHub Actions | `auto-pr-claude.yml` / `ci-dev.yml`(scene-integrity) / `auto-merge-dev.yml` / `claude.yml` / `godot-check.yml`(今回追加) | ❓ Runner/Supervisor/CI群（本命） | 重複疑い |
| CI | scene-integrity（HTML用）＋ godot-check（今回追加） | ❓ Godot用CI（本命） | godot-check は RewriteMemory 向きの可能性 |
| Labels | auto-merge-dev 等 少数 | ❓ **191 labels（推定）**：policy/human-review/automerge系 | 桁違い、本命 |
| Issues | 少数 | ❓ **~130 issues（推定）** | 本命 |
| Pull Requests | PR #48（保留中）他 | ❓ **~184 closed PR（推定）** | 本命 |
| 自律Runner | `tools/autonomy/agent-runner.sh`（今回新規・未配線） | ❓ 稼働中Runner（本命） | 重複疑い |
| Pack Runner | なし | ❓ **存在（本命）** | gameme には無い |
| Supervisor | `tools/autonomy/supervisor.sh`（今回新規・未配線） | ❓ 稼働中Supervisor（本命） | 重複疑い |
| 開発フロー | dev→stage→本番（HTML）＋claude/**自動PR | ❓ Godot向けフロー（本命） | 別体系 |

> 推定値（191 labels / 130 issues / 184 closed PR）は、以前ユーザー提供のスクリーンショットに基づく**未検証の記憶**。dual-scopeセッションで必ず実測に置換すること。

---

## ② 重複調査（今回 gameme に作ったもの）

分類は RewriteMemory 側未確認のため**暫定**。`要確認` は dual-scope で判定。

| 今回の成果物（gameme） | RewriteMemoryにも存在 | 存在しない | 内容が異なる | 暫定判断 |
|---|---|---|---|---|
| `CLAUDE.md` | 要確認（存在濃厚） | | 要確認（内容は確実に異なる：gameme版はgameme前提） | **Merge**（RewriteMemory版を正に、有用ルールのみ移植） |
| `docs/project/AI_OPS_ARCHITECTURE_v1.md` | 要確認（同種基盤あり） | | 要確認 | **Merge/参照**（RewriteMemory既存を正、差分のみ提案） |
| `docs/project/DIRECTION_2026-07.md` | 要確認 | 恐らく無い（今回の意思決定資料） | | **Move**（内容はRewriteMemory向け） |
| `docs/design/UIUX/UIUX_BENCHMARK_2026-07.md` | 要確認 | 恐らく無い | | **Move** |
| `docs/project/PROTOTYPE_GODOT_1ROOM.md` | 要確認 | 要確認 | | **Move/Merge** |
| `docs/project/AUTONOMY_MACMINI.md` | 要確認 | 恐らく無い | | **Move** |
| `docs/project/PHASE1_AUTONOMY.md` | 要確認 | 恐らく無い | | **Move** |
| `docs/project/COST_OPERATIONS_2026-07.md` | 要確認 | 恐らく無い | | **Move** |
| `docs/project/AI_OPS_BACKLOG.md` | 要確認 | 要確認 | | **Merge** |
| `prototype/godot-1room/`（Godot実動プロト） | 要確認（本体があるなら不要/参考） | 要確認 | | **Merge/Delete**（本体に相当機能があるなら破棄、無ければ移植） |
| `.github/workflows/godot-check.yml`（GREEN実績） | 要確認（Godot CIあるはず） | 要確認 | | **Merge/Delete** |
| `tools/autonomy/`（Runner/Supervisor/DailyReport/launchd） | **要確認（本命に既存）** | | 要確認（設計思想が異なる可能性） | **Delete/参照**（既存が正。設計アイデアのみBacklog化） |

---

## ③ Migration Plan（Keep / Move / Merge / Delete）

> RewriteMemory の中身確認後に確定。以下は**方針の枠組み**。

- **Keep（gameme に残す）**：gameme本来の役割＝Pages/HTML版/デモ/LP に属するもの。旧 `docs/rewrite-dev|stage|rewrite` の HTML実装、FEED関連、公開用アセット。→ **AI基盤・Godot・運用ドキュメントはKeep対象外**。
- **Move（RewriteMemoryへ移設・gameme из削除）**：今回作った意思決定・設計ドキュメント（DIRECTION / UIUX_BENCHMARK / PROTOTYPE_GODOT / AUTONOMY_MACMINI / PHASE1 / COST）。RewriteMemory に同等が無いことを確認してから移設。
- **Merge（RewriteMemory既存に統合）**：CLAUDE.md の有用ルール、AI_OPS_ARCHITECTURE の差分アイデア、godot-check CI、Godotプロト、AI_OPS_BACKLOG。**既存を正とし、上書きせず差分をPRで提案**。
- **Delete（破棄）**：RewriteMemory に既存のより成熟した実体があるもの＝`tools/autonomy/`（Runner/Supervisor）、重複する自動化。gameme の godot-check も RewriteMemory 側CIがあれば削除。

**各判断は「RewriteMemory既存が正／gameme今回分は候補」を原則**とする。既存基盤を新規で上書きしない。

---

## ④ 最終構成図（役割が重複しない正式構成）

```
gamemehub/RewriteMemory  ← 正典（開発はすべてここ）
├── Godotプロジェクト本体（project.godot / scenes / scripts / assets）
├── AI自律開発基盤（Runner / Pack Runner / Agent / Supervisor）
├── CI（Godot向け・godot-check 等）
├── Issue / PR / Labels（policy / human-review / automerge …）
├── 開発ドキュメント（spec / design / project / ai-ops / audit）
└── ガバナンス（PROJECT_CONSTITUTION / DEVELOPMENT_WORKFLOW_MASTER / CLAUDE.md / .repo-identity.yml）

gamemehub/gameme  ← 公開面のみ（AI開発は受け入れない）
├── GitHub Pages
├── 旧HTML版（rewrite-dev/stage/rewrite の擬似実装）
├── 公開デモ
├── 告知ページ（LP）／FEED
└── .repo-identity.yml（role: public-demo-pages / accepts_ai_development: false）
```

**重複ゼロの原則**：Godot・AI基盤・CI/Runner/Supervisor・開発Issue/PR は **RewriteMemory のみ**。gameme は「見せる」だけで「作らない」。

---

## ⑤ Root Cause Analysis（根本原因分析）

### 事故の要約
AI自律開発基盤（CLAUDE.md / AI_OPS_ARCHITECTURE / Godotプロト / autonomy scaffold / godot-check CI）を、**正典でない `gamemehub/gameme`** に構築し、PR #48 まで進めた。

### なぜ誤ったRepositoryで作業したのか
1. **セッションのスコープ＝正典、と暗黙に等値した。** 環境が `gamemehub/gameme` にスコープ設定されて起動したため、「作業対象repo」を無検証で「正典repo」とみなした。**スコープされたrepo ≠ 正典repo** という区別が運用ルールに無かった。
2. **gameme が“それらしい中身”を持っていた。** `docs/rewrite-dev/index.html` に RewriteMemory の擬似実装、`docs/spec|design|characters` に仕様書群が存在したため、「ここが開発の家だ」という誤認が強化された（本物のGodot正典が別repoにある事実がマスクされた）。
3. **gameme の CLAUDE.md 自身が「gameme を単一の真実」と自己宣言していた。** 権威ある見た目の誤誘導シグナルが repo 内に存在し、それを疑う仕組みが無かった（自己参照的で、外部の正典を指していなかった）。

### なぜ途中で検知できなかったのか
1. **Repository Identity（自分は何repoで、役割は何か）を宣言・検証する仕組みが皆無。** 「今どこにいるか」と「この作業はどこへ行くべきか」を突き合わせる関門が一度も無かった。
2. **クロスrepo認識が無い。** RewriteMemory の存在を、作業前・PR作成時のどこでも参照しなかった。
3. **内容×役割の整合CIが無い。** AI基盤PRが「公開面repo」に入っても、CIは何も警告しなかった（scene-integrity はHTML参照切れしか見ない）。
4. **人間側の可視性が低かった。** Chairman は GitHub を直接見られず、早期に「repoが違う」と気づけなかった。

### AI運用ルールに不足していたもの
- (a) **機械可読な正典宣言**（どのrepoが何の正典か）。
- (b) **作業開始前の Repository Identity Check**（remote と宣言の一致確認）。
- (c) **内容×役割の CI ガード**（公開面repoにAI基盤/Godotが入ったら赤）。
- (d) **「スコープrepo は自動的に正典ではない」明文ルール**。
- (e) **Wrong Repository Detection と 停止（fail-closed）**。

### 再発防止策（⑥で具体設計）
上記 (a)〜(e) を、宣言ファイル＋Preflight＋CIガード＋CLAUDE.md先頭チェックの4点セットで実装する。

---

## ⑥ AI運用ルール改善（追加すべきルールと機構）

対象ドキュメント：`PROJECT_CONSTITUTION` / `DEVELOPMENT_WORKFLOW_MASTER` / `AI_OPS_ARCHITECTURE` / `CLAUDE.md`（いずれも**RewriteMemory側が正**）。

### 6-1. 機構1：`.repo-identity.yml`（機械可読な正典宣言）— 全repoルートに置く

RewriteMemory：
```yaml
# .repo-identity.yml
schema: repo-identity/v1
repo: gamemehub/RewriteMemory
role: canonical-development
accepts_ai_development: true
canonical_for: [godot-game, ai-ops, ci, runner, supervisor, dev-docs]
public_face_repo: gamemehub/gameme
```
gameme：
```yaml
schema: repo-identity/v1
repo: gamemehub/gameme
role: public-demo-pages
accepts_ai_development: false
canonical_dev_repo: gamemehub/RewriteMemory
redirect_ai_work_to: gamemehub/RewriteMemory
```

### 6-2. 機構2：Repository Identity Check（作業開始前・Preflight）
すべての Runner/Agent/対話セッションが**最初に必ず**実行：
1. `git remote get-url origin` を取得。
2. ルートの `.repo-identity.yml` を読む。
3. **一致検証**：remote の `owner/repo` が `repo:` フィールドと一致するか（誤clone・誤push先の検知）。
4. **役割検証（Canonical Repository Validation）**：これからの作業種別（AI開発/Godot/CI/Runner）に対し `accepts_ai_development==true` かつ `canonical_for` に含まれるか。
5. **不一致なら Wrong Repository Detection 発火 → 即停止（fail-closed）**：`redirect_ai_work_to` を提示し、`exit 1`。人間に通知。作業を1コミットも行わない。

参考スクリプト（Runner 冒頭に組み込む想定）：
```bash
# preflight_repo_identity.sh — 失敗したら非ゼロで即停止
set -euo pipefail
ORIGIN="$(git remote get-url origin)"
ID_FILE=".repo-identity.yml"
[ -f "$ID_FILE" ] || { echo "::error:: .repo-identity.yml が無い。正典未宣言のrepoでのAI作業は禁止。"; exit 1; }
DECL_REPO="$(grep -E '^repo:' "$ID_FILE" | awk '{print $2}')"
ACCEPTS="$(grep -E '^accepts_ai_development:' "$ID_FILE" | awk '{print $2}')"
case "$ORIGIN" in *"$DECL_REPO"*) : ;; *)
  echo "::error:: Wrong Repository: origin=$ORIGIN だが宣言は $DECL_REPO。誤clone/誤push先。停止。"; exit 1;; esac
if [ "${TASK_CLASS:-ai-dev}" = "ai-dev" ] && [ "$ACCEPTS" != "true" ]; then
  REDIR="$(grep -E '^redirect_ai_work_to:' "$ID_FILE" | awk '{print $2}')"
  echo "::error:: このrepo($DECL_REPO)はAI開発を受け入れない(role非正典)。正典=$REDIR へ。停止。"; exit 1
fi
echo "[preflight] OK: $DECL_REPO は本作業の正典。"
```

### 6-3. 機構3：CI ガード `repo-identity-guard.yml`（内容×役割の整合／PR毎）
- 全PRで起動。`.repo-identity.yml` を読む。
- `accepts_ai_development==false` の repo で、PRの変更が **AI基盤/Godot系パス**（`tools/autonomy/**`, `docs/**/AI_OPS_*`, `prototype/godot*/**`, `project.godot`, Runner/Supervisor系 `.github/workflows/**`）に触れていたら → **赤（fail）**、メッセージ「AI開発は正典 `gamemehub/RewriteMemory` へ。本repoの役割は public-demo-pages」。
- **これが今回の事故を止めた関門**：AI基盤PRが gameme に入った瞬間にCIが赤くなる。
- ブランチ保護で必須チェック化 → **人間が気づかなくても機械が止める**。

### 6-4. 機構4：CLAUDE.md 先頭の「Repository Identity Check」節（対話セッション用）
CLAUDE.md の最上部に、作業前チェックリストを明文化：
```
## 0. 作業開始前チェック（Repository Identity Check）— 最優先・スキップ禁止
1. `git remote get-url origin` と `.repo-identity.yml` を照合。
2. role が canonical-development か。AI開発を受け入れるか。
3. 違うなら STOP。redirect 先の正典repoを人間に提示して指示を仰ぐ。
4. **スコープされたrepo ≠ 正典repo。** 環境が開いたrepoを正典と決めつけない。
```

### 6-5. 明文ルール（Constitution/Workflow に追記）
- **R1 Canonical Repository確認**：AI作業は必ず `.repo-identity.yml` の `canonical_for` に該当する repo でのみ行う。
- **R2 Repository Identity Check**：全Runner/対話は Preflight を最初に実行（fail-closed）。
- **R3 Wrong Repository Detection**：remote と宣言の不一致、役割不適合を検知したら停止・通知。
- **R4 Canonical Repository Validation**：作業種別ごとに正典repoを検証（Godot/AI基盤/CI は RewriteMemory のみ）。
- **R5 Repository Audit手順**：新規repo追加・役割変更時は本監査テンプレで棚卸し（本ファイルを雛形化）。
- **R6 Repository切替手順**：誤repo検知時＝①作業停止 ②成果を patch/branch で退避 ③正典repoで再開 ④誤repo側は revert/close。
- **R7 Migration手順**：Keep/Move/Merge/Delete で分類→既存を正として差分PR→誤repo側を掃除。

---

## ⑦ 作業計画（実施手順）

| Step | 内容 | 前提/場所 | 状態 |
|---|---|---|---|
| **Step0** | dual-scope セッション作成（RewriteMemory＋gameme 両方をスコープ） | Chairman 環境設定 | ⬜ 未 |
| **Step1** | Repository Audit（①を実測で完成：RewriteMemory の構成・Runner・Labels・Issue/PR・CI） | dual-scope | ⬜ |
| **Step2** | 重複調査（②を確定） | dual-scope | ⬜ |
| **Step3** | Migration Plan（③を Keep/Move/Merge/Delete で確定） | dual-scope | ⬜ |
| **Step4** | Root Cause Analysis 確認（⑤：本ファイルで下書き済み→確定） | 本ファイル | 🟩 下書き済 |
| **Step5** | Repository統合：Move/Merge対象を RewriteMemory へPR、gameme側を掃除、PR #48 を適切にclose | dual-scope | ⬜ |
| **Step6** | AI運用ルール更新：⑥の機構を RewriteMemory の Constitution/Workflow/AI_OPS/CLAUDE.md＋`.repo-identity.yml`＋`repo-identity-guard.yml` として実装。gameme にも `.repo-identity.yml`(role: public-demo-pages) を追加 | dual-scope | ⬜ |
| **Step7** | 開発再開（以後 AI開発は RewriteMemory のみ。Preflight＋CIガードが常時ガード） | RewriteMemory | ⬜ |

### 今すぐ（本セッション・gameme のみで）できる先行タスク
- ✅ PR #48 を保留（HOLD・Draft維持・引き継ぎコメント）— 完了
- ✅ 本監査ドキュメント作成（⑤⑥⑦設計＋①②④枠）— 本ファイル
- ⬜（任意・要指示）gameme に `.repo-identity.yml`(role: public-demo-pages, accepts_ai_development:false) を先行追加し、**再発防止の第一歩を gameme 側から打つ**

---

## まとめ（この監査の到達点）
- **本丸の設計は完了**：`.repo-identity.yml`＋Preflight＋`repo-identity-guard.yml` CI＋CLAUDE.md先頭チェックの4点セットで、「誤repoでのAI開発を機械が検知・停止・誘導」できる。今回の事故は 6-3 のCIガードだけでも赤くなって止まっていた。
- **残りは dual-scope 待ち**：①②③の RewriteMemory 実測と Step5〜7 の実装。
- **原則**：スコープされたrepo ≠ 正典repo。正典は宣言ファイルで機械可読にし、毎回検証する。
