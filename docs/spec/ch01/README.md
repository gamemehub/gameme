# docs/spec/ch01 — CH01 実装仕様（正本セット）

CH01「RewriteMemory 第1章」の実装用 SSOT。**このディレクトリが正本**であり、Google Doc（旧正本）は `source/` に凍結済みの履歴。

## ファイル構成

| ファイル | 内容 |
|---|---|
| `CH01_IMPL_SPEC.md` | 正本仕様書（裁定記録・システム仕様・イベント・受け入れ条件） |
| `flags.json` | フラグ台帳 |
| `scenes.json` | シーン台帳（S0〜S11） |
| `dialogues.json` | 台詞台帳（★キーライン・SCRIPT DRAFT） |
| `tuning.json` | チューニング定数 |
| `CANON_SNAPSHOT.md` | canon 依存事実・禁止事項・未決レジスタ |
| `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md` | 原本凍結（編集禁止・監査履歴 SECTION 7〜17 含む） |

## 更新規律

1. 仕様変更は正本（本ディレクトリ）を**直接編集**し、`CH01_IMPL_SPEC.md` §9 Changelog に1行追記。監査・レビューを正本に積層させない（旧 Doc の轍を踏まない）。
2. フラグの書込オーナーは Dialogue/Event 完了時のみ（`flags.json` rules）。
3. canon の追加・変更は上位決裁。`CANON_SNAPSHOT.md` に実装側で canon を足さない。
4. 台詞の文芸 FINAL パスを GPT 等に依頼する場合、`dialogues.json` の該当エントリのみ切り出して渡し、結果は PR で取り込む（★keyLine の意図は変更不可）。
5. Playtest 調整は `tuning.json` の数値変更のみで行い、仕様改訂を伴わせない。

## 関連

- 実装: `/godot/`（Phase 1〜）
- 旧 Web プロトタイプ: `docs/rewrite-dev/` ほか（**凍結・参照のみ**。改修しない）
- UIUX: `docs/design/UIUX/`（`SCREEN_CALLOUT_INPUT.md` を Phase 1 で新設予定）
