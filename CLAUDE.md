# CLAUDE.md

このリポジトリで作業する際のガイダンス。

## RewriteMemory のジャンル定義（重要・誤認防止）

**RewriteMemory はビジュアルノベル（VN）ではない。ゲーム体験を中心に置いた探索型RPGであり、プレイヤーがキャラクターを操作して進めていくゲームである。**

- 基本はプレイヤー操作による探索（M02 探索モード）。ゲームループは `Map(M02) → 会話/イベント → Map` で、常に Map（探索）が主軸。
- VN 的な画面（M04 VN Overlay）は「重要イベント専用」の演出オーバーレイにすぎない。探索画面の上に一時的に重なるものであり、ゲームの本体ではない。
- 通常会話も M03 Talk Window（顔アイコン式）で探索画面を保持したまま行う。
- 詳細: `docs/design/UIUX/RewriteMemory_MODE_DEFINITION.md` / `docs/design/UIUX/RewriteMemory_UIUX_BIBLE.md`

**タスク作成・仕様記述・レビューの際、RewriteMemory を「VN」「ノベルゲーム」として扱わないこと。** 「探索型RPG（重要イベント時のみ VN オーバーレイ演出あり）」と記述する。

## リポジトリの位置づけ

`.repo-identity.yml` を参照。GameMe は独立プロダクトであり、RewriteMemory のゲーム本体・エンジン（Godot 等）はこのリポジトリでは開発しない。

## タスク運用

タスクは `TASK_QUEUE.md` で管理する（Ready / In Progress / Done）。
