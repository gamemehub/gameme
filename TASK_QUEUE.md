# TASK QUEUE

## Ready
- **HUMAN DECISION 裁定会（最優先）**: `docs/spec/ch01/REVIEW_REPORT.md` §3 の H1〜H9。特に H1(白層状態enum) / H2(mioTrustデータモデル) / H4(CALLOUT入力方式) / H5(Narrative Clock採否) の4件で高重大度ブロッカーが解消する。
- **依存文書の入手・凍結**: UNDECIDED_REGISTER → CH01_DETAIL.md → CHAPTER01_SCENARIO_MASTER.md → MAP_VISUAL_MASTER_CH01。`docs/spec/ch01/source/` へ凍結し `CANON_DEPENDENCIES.md` を更新。
- **IMAGE-02 の Area C 先行着手**: 全Areaを待たず C1/C2 の実座標（特に 5席目Trigger / C2ゾーン範囲）を確定すれば Phase 1 の GO 条件を満たせる。
- **STALE CANON 是正起票**: 上位canon（CH01_DETAIL.md:42 / 14_CHAPTER_BIBLE.md:27）の学校/教室記述。本仕様はC2ベンチで統一済み。
- `CH01_PHASE2_EMOTIONAL_HOOK_SPEC.md` の扱い決定: 現行仕様とシーン順序が不一致（`CANON_DEPENDENCIES.md` X2）。

## Blocked（GO条件未達）
- **Phase 1: Godot灰箱・Area C縦切り（S3→S11）** — **NO-GO**。`REVIEW_REPORT.md` §5 参照。GO条件: H1/H2/H4/H5 裁定 ＋ H6/H8 方針決定 ＋ Area C 実座標確定 ＋ 依存文書の部分入手。
- Phase 2: Area A/B 追加・30分通し・H001〜H023 Blind Playtest。
- Phase 3: IMAGE-02 全体突合・アート差し替え・配布ビルド。

## In Progress
（なし）

## Done
- Phase 0: 仕様正規化（`docs/spec/ch01/`）— 原本凍結、正本シングルレイヤー化、FLAG/EVENT/CONTROL/CLOCK/TUNING/DEPENDENCIES 分離、監査履歴分離、実装準備レビュー。

## Frozen / Superseded
- ~~Chapter01 Phase2 実装（CH01_PHASE2_EMOTIONAL_HOOK_SPEC.md）~~ → 現行仕様とシーン順序が不一致のため単独実施を保留。扱いは上記 Ready 項目で決定する。
- 旧Webプロトタイプ（`docs/rewrite-dev/` 等）: legacy / reference。実装先にしない。
