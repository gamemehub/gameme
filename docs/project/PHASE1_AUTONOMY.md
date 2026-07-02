# Phase1：AI自律開発基盤（Godot）実行計画

状態: v0.1 / 実行計画
更新: 2026-07-02
決定: エンジン=**Godot 確定(GO)**。7月成功条件=「Godot上でAIが24h自律開発できる体制」＋「1エリア提出品質の縦串」。
出典: DIRECTION_2026-07 / AUTONOMY_MACMINI / GPT(PM/アーキ/QA)判断 2026-07-02。

## 原則（CTO補足）
- **最小で効く基盤に絞る。** 基盤を真空で磨かない。**縦串(Phase2)を作りながら基盤を回して検証**する（ドッグフード）。
- スコープ管理が最大リスク。7月に「エンジン改善/システム追加/アート/演出/AI基盤」を同時多発させない。

## Godotプロジェクトの置き場所（確定）
- 本開発は `prototype/godot-1room/` を土台に、**`game/`（Godot本体プロジェクト）へ発展**させる（縦串はここ）。当面はプロトを継続使用し、Phase2着手時に `game/` へ整理。
- ※ 旧HTML版(`docs/rewrite-dev/index.html`)は参照・移植元。新規開発はGodot側。

## Phase1 タスクと担当
| # | タスク | 担当 | 状態 |
|---|---|---|---|
| 1 | **Godot ヘッドレス CI**（PRごとに `--headless --quit` でパース/インポート検証） | Claude(実装) | 本PRに同梱(要Chairman承認) |
| 2 | リポジトリ設定：**Allow auto-merge を ON** ＋ **`GH_PAT`** 設定 | **Chairman** | 未 |
| 3 | main ブランチ保護の必須チェックを **`godot-check`** に更新（HTMLの`scene-integrity`から） | **Chairman** | 未 |
| 4 | Mac mini：**セルフホストRunner** 登録＋`launchd`常駐 | Chairman(実機)＋Claude(手順) | 未 |
| 5 | Mac mini：**エージェント常駐ループ**（Ready課題→実装→PR）。Claude Code / Codex CLI＋`launchd` | Chairman(実機)＋Claude(スクリプト) | 未 |
| 6 | 予算上限・失敗アラート・停止条件の運用設定 | Chairman＋Claude | 未 |
| 7 | Issue/PR運用（1タスク=1PR、レビュー基準、承認レーン） | GPT(基準)＋Claude(PR) | 継続 |

## 安全弁（AUTONOMY_MACMINI準拠）
- 無人マージは **Godot dev/docs の安全変更のみ**。`game/`のゲーム核心・`.github/`・本番は人間承認。
- 体験に関わる実装（歩き心地・演出・UI）は**確認レーン**：Miyaの実機/URLチェックを残す（今回のプロトで有効性実証済み）。
- 停止条件：仕様矛盾/仕様判断要/大規模改修/本番影響 → 停止して報告。

## Go判定（Phase1完了条件）
- PR作成→`godot-check`(CI)→レビュー→（安全レーンは）自動マージ、が**無人で1周**回る。
- Mac miniが再起動しても`launchd`で基盤が自動復帰。
- 予算上限・停止条件が効く。
→ これが回ったら Phase2（1エリア縦串を提出品質へ）に、基盤を使いながら進む。

## Chairmanに必要なアクション（まとめ）
1. GitHub → Settings → General → **Allow auto-merge を ON**
2. GitHub → Settings → Secrets → **`GH_PAT`**（repo権限のPAT）を登録
3. GitHub → Settings → Branches → main の必須チェックを **`godot-check`** に
4. Mac mini：セルフホストRunner登録トークン取得（Settings → Actions → Runners → New self-hosted runner）→ Claude提供の手順でRunner＋Agent常駐を設定
5. Mac mini：Anthropic APIキー等をKeychainに安全保管、予算上限を設定
