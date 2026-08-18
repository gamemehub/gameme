# TASK QUEUE

## Ready
- Phase 1: Godot灰箱・Area C縦切り（S3→S11）。`docs/spec/ch01/CH01_IMPL_SPEC.md` §8.1 の Exit Criteria を満たす。ステートマシン/擬似時計/S8-S9ループ/呼びかけ長押しUI（SCREEN_CALLOUT_INPUT新設）/テレメトリJSONL/HTML5スモークテスト。冒頭で Godot バージョン・解像度・入力デバイスを確定。
- Phase 2: Area A/B 追加（S0〜S2・P01〜P08）・30分通し・3ルート実測・H001〜H023 Blind Playtest（灰箱のまま）。§8.2。
- Phase 3: IMAGE-02 実座標突合・アート差し替え・配布ビルド（HTML5はGC2026提出要件確認後に最終裁定）。§8.3。
- IMAGE-02: AREA-B拡張ルート・Script Pin実配置（Phase 1〜2と並行可。Pinは Step No / Area-Zone / Script ID / Req-Nat-Opt のみ・台詞全文を画像に入れない）。

## In Progress
- Phase 0: 仕様正規化セット構築（`docs/spec/ch01/`）— 正本移管・フラグ台帳・シーン/台詞/チューニング台帳・CANON_SNAPSHOT。本PRで完了予定。

## Done

## Frozen / Superseded
- ~~Chapter01 Phase2 実装（CH01_PHASE2_EMOTIONAL_HOOK_SPEC.md）~~ → **凍結（裁定D3）**: Godot移行・シーン順序変更（S5空席→S6選択→S8逆流）により旧導線前提のPhase2は単独実施しない。2モチーフは新仕様に統合済み（「誰も覚えてない」→S5ミオ台詞側 / 「忘れないでね」半欠落→S11送信者反転 D-END）。旧Webプロトタイプ（docs/rewrite-dev/ 等）は凍結・参照のみ。
