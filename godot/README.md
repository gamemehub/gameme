# /godot — RewriteMemory CH01 実装（Phase 1〜）

Godot プロジェクト置き場。仕様の正本は `docs/spec/ch01/` を参照。

## 実装方針（裁定済み）

- **Godot 4.x** / **Orthographic Top-Down 2D**・4方向 Facing（Isometric 不採用）
- Phase 1: 灰箱（グレーボックス）で Area C 縦切り（S3→S11）
  - コントロールステートマシン（IMPL_SPEC §3.3〜3.4）
  - 擬似時計（§3.2）
  - 呼びかけ入力 UI 長押し版（§3.5・S9/S11 同一コンポーネント）
  - テレメトリ JSONL 出力（§3.8）
  - Exit Criteria: IMPL_SPEC §8.1（HTML5 エクスポートのスモークテスト含む）
- Phase 2: Area A/B 追加・30分通し・Blind Playtest（§8.2）
- Phase 3: IMAGE-02 実座標突合・アート差し替え・配布ビルド（§8.3）

## 決めごと（Phase 1 冒頭で確定させる）

- Godot マイナーバージョン固定
- 解像度・画面向き（横 16:9 / モバイル対応方針）
- 入力デバイス（キーボード＋タッチ）

旧 Web プロトタイプ（`docs/rewrite-dev/` 等）は参照のみ。コード移植はしない（台詞・フローは `docs/spec/ch01/dialogues.json` 経由で回収済み）。
