# RewriteMemory 自律開発基盤（Mac mini / Phase1）

Mac mini 上で **Ready Issue → 実装 → PR → CI(godot-check) → 人間レビュー待ち** を無人で回すための足場。
設計は `docs/project/AUTONOMY_MACMINI.md` / `docs/project/PHASE1_AUTONOMY.md`。

> ⚠️ これは v0.1 の足場です。**Mac miniで実際に動かしながら、私（Claude）と一緒に詰めます。** まず小さく回して安全弁を確認してから常駐化してください。

## 構成
- `config.example.sh` … 設定サンプル。`config.sh` にコピーして実値を入れる（**Git管理しない・chmod 600**）
- `agent-runner.sh` … Ready Issue を1件取り、エージェントで実装→commit→push（auto-pr がPR化、godot-check が検証）
- `supervisor.sh` … 監視エージェント（ハートビート/コスト/CI失敗率/暴走検知→通知・PAUSE）
- `launchd/*.plist` … 常駐化テンプレート

## セットアップ（Mac mini）
1. 前提：`git`・`gh`（`gh auth login` 済み）・Godot 4.2・**エージェントCLI**（Claude Code か Codex）を導入。
2. 設定：
   ```
   cd ~/gameme/tools/autonomy
   cp config.example.sh config.sh && chmod 600 config.sh
   # config.sh を編集：REWRITE_AGENT_CMD（★）, ANTHROPIC_API_KEY, 予算, 通知Webhook 等
   ```
3. ラベル準備：GitHub に `ai-ready` / `ai-in-progress` ラベルを作成。実装させたい Issue に `ai-ready` を付ける。
4. 手動で1回テスト（常駐化の前に必ず）：
   ```
   bash agent-runner.sh      # Ready Issue を1件処理してPRまで行くか確認
   bash supervisor.sh        # 監視ロジックが回るか確認
   ```
5. 常駐化（launchd）：
   ```
   cp launchd/com.rewritememory.agent.plist ~/Library/LaunchAgents/
   cp launchd/com.rewritememory.supervisor.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.rewritememory.agent.plist
   launchctl load ~/Library/LaunchAgents/com.rewritememory.supervisor.plist
   ```
   （plist 内のパスを自分の環境に合わせて編集すること）

## 安全弁
- **PAUSE**：`touch ~/rewrite-autonomy/PAUSE` で全停止。削除で再開。
- **日次コスト上限**：`REWRITE_DAILY_USD_LIMIT` 超過で停止（コスト実測は agent 側で state に加算）。
- **暴走検知**：自動PRが短時間に増えすぎたら Supervisor が PAUSE。
- **レーン厳守**：エージェントは game/・docs のみ。本番/.github/セーブ核心は触らない。無人マージは安全レーンのみ、ゲーム核心は人間承認。

## ★ 未確定（config.sh で決める / 相談して確定）
- エージェント実行系：**Claude Code CLI**（`claude -p "$1" --allowedTools ...`）か **Codex**。
- 認証方式（APIキー直 or Keychain）と**予算額**。
- 通知先（Slack Webhook 等）。

## ドッグフード原則
Agent を空回しにしない。**必ず CH01 の1エリアを実際に作らせながら**基盤を育てる（`docs/project/PHASE1_AUTONOMY.md`）。
