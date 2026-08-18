# docs/spec/ch01 — CH01 実装準備仕様

CH01「RewriteMemory 第1章」を Godot 実装へ渡せる状態に近づけるための正規化セット。
**Status: 実装準備段階 / 実装未着手 / Lock前。** 実装可否は `REVIEW_REPORT.md` を参照。

## 正本（Markdown）

| ファイル | 役割 |
|---|---|
| `CH01_IMPL_SPEC.md` | **正本**。S0〜S11 の現行仕様のみ（Scene毎16フィールド） |
| `FLAG_REGISTRY.md` | フラグ台帳・型監査（whiteLayerProgress / mioTrust の案比較） |
| `EVENT_REGISTRY.md` | イベント定義（EVT 7件） |
| `CONTROL_GATE_SPEC.md` | Control State / Gate / S8・S9 State Machine |
| `NARRATIVE_CLOCK.md` | 17:17 仕様（イベント駆動案） |
| `TUNING.md` | 調整値一覧（Canonと分離） |
| `CANON_DEPENDENCIES.md` | 依存文書一覧（MISSING / PATH NOT VERIFIED 判定） |
| `CANON_SNAPSHOT.md` | canon事実・禁止事項・未決レジスタ |
| `AUDIT_HISTORY.md` | 監査・改訂履歴（正本から分離） |
| `REVIEW_REPORT.md` | 実装準備レビュー結果・ブロッカー・実装可否判定 |
| `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md` | 原本凍結（編集禁止） |

## 参考ドラフト（JSON）

`flags.json` / `scenes.json` / `dialogues.json` / `tuning.json` は**スキーマ形状の参考ドラフト**。
決定事項は上記 Markdown 各 Registry を正とする（JSON側の「確定」表記は候補へ格下げ済み・各ファイル `$status` 参照）。
`dialogues.json` は台詞テキストの回収先として有効。

## 前提（変更禁止）

- Runtime Target = Godot。既存Web版（`docs/rewrite-dev/` 等）は legacy / reference で実装先にしない
- S7 は UNDECIDED。Prototype は S6→S8 を前提とし、S7 を採用・実装しない
- CALLOUT 入力方式は UNDECIDED。S9/S11 同一操作のみ Requirement
- mioTrust 等のデータモデル変更は未確定（DESIGN REVIEW REQUIRED）
- 秒数・歩数・回数は Canon 化せず `TUNING.md` へ分離
- IMAGE-01 / IMAGE-02 / Area座標は別工程。推測で埋めない
- 金魚/水槽 復活禁止 / 時計塔内部 追加禁止
- OBSERVATION ≠ CALLOUT / CALLOUT SUCCESS ≠ CAPTURE CAUSE

## 更新規律

1. 仕様変更は正本と該当 Registry を直接編集し、`AUDIT_HISTORY.md` §4 に記録する。監査を正本に積層させない。
2. フラグ書込オーナーは Dialogue/Event 完了時のみ。
3. canon の追加・変更は上位決裁。実装側で canon を足さない。
4. 台詞の文芸FINALパスを外部へ依頼する場合は `dialogues.json` の該当エントリのみ切り出す（★keyLine の意図は変更不可）。
5. Playtest 調整は `TUNING.md` の数値変更のみで行う。
