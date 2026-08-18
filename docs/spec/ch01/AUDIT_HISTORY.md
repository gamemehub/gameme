# AUDIT_HISTORY — CH01 監査・改訂履歴（正本から分離）

**目的**: `CH01_IMPL_SPEC.md`（正本）を単一レイヤーに保つため、監査・旧バージョン比較・レビュー履歴をここへ分離する。
**原本全文**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md`（SECTION 7〜17 に監査群が収録）
**規約**: 本ファイルは**履歴**であり、実装判断の根拠にしない。実装判断は正本と各Registryを参照する。

---

## 1. 原本の監査セクション対応表

| 原本SECTION | 内容 | 現在の扱い |
|---|---|---|
| SECTION 7 | Script Granularity Audit（vs Benchmark・資料粒度） | 履歴。判定 FAIL:0 / PARTIAL:2（State/Flag変数canon化=DL-Y3、Map Location=ロケASSUMPTION） |
| SECTION 8 | Authored Experience Quality Pass（QP-01〜07） | 履歴。QP-01〜04は SECTION 9 で反映済み |
| SECTION 9 | QP-01〜04 反映結果 | 履歴。MIO-B/MIO-C の Natural 化、Area B Ambient 1発話、S4/S5後UNLOCK |
| SECTION 10 | v0.10 S10 Consistency Audit | 履歴。S10 の READ-only → Transition Beat 縮退 |
| SECTION 11 | Exploration Information Layer v0.11 | 履歴。WORLD/MIO/HOOK/MYSTERY × Required/Natural/Optional |
| SECTION 12 | Benchmark Guide Pattern → AREA-B v0.12 | 履歴。B2-P01〜P08 の Draft |
| SECTION 13 | AREA-A/C Pass + Throughline Audit v0.13 | 履歴。23節Throughline / Mio Affection Gate / Next-Hook Gate |
| SECTION 14 | Benchmark Script Texture Pass v0.14 | 履歴。Stale/Superseded整理を含む |
| SECTION 15 | FULL PLAYER PLAYTHROUGH v0.15 | **実プレイ順の参照層**。15D（H001〜H023 Human Validation）は Playtest 時に EXPECTED 正本として使用 |
| SECTION 16 | Playthrough Benchmark Quality Review v0.16 | 履歴。スコア（資料97 / Script Design 93 / Runtime暫定87） |
| SECTION 17 | Critical Route Read-through + Control-State Audit v0.17 | **§17B/C/D/E は現行仕様**。正本・`CONTROL_GATE_SPEC.md` に反映済み |

## 2. Superseded / 廃止済み記述（正本に残さないもの）

| 旧記述 | 廃止根拠 | 現行 |
|---|---|---|
| S4 で「白層化率」へ変わる | §17D-1 | S4は --% / 名称未判読。S8の操作失敗後に初判読 |
| S8 = 全面 LOCKED（演出） | §17D-2 | 短時OPENING LOCK → PARTIAL UNLOCK 操作試行 → 短時LOCK |
| S11 連れ去り → 即モノローグ → 通知 | §17D-3 | 連れ去り後に必ずControlを返し、C2再解釈1回以上の後に通知反転 |
| S8 の失敗動詞に「呼びかけ」を含む | v0.8 / 3原則② | 一方的観測操作（調べる/触れる/追跡/記録）のみ |
| S11「助けたから傷つけた」 | v0.8 / 3原則③ | 呼びかけは成功→制度が奪う（構造的喪失）。因果は断定しない |
| S5 ロケ = 教室（五つ目の席） | 2026-08-13 | C2ベンチ（4席+5席目）に統一。上位canon残存は STALE CANON CANDIDATE |
| 学校/教室 Main Route | v0.6 | CH01から全除外。「通学の生徒」→「近所の人」 |
| 住人「おかえり。」固定 | v0.12 Canon Guard | Canon根拠なし。中立な生活挨拶へ置換候補 |
| Area-B 住人5名（店主/子ども/老人/近所の人等） | v0.14 | PROTOTYPE NON-ACTIVE。Natural 1名＋Optional最大1名 |
| Area-B 白層化 variant（再訪台詞） | v0.14 / QP-06 | FUTURE CANDIDATE。CH01では物理再訪しないため品質評価から除外 |
| Engagement Gate「全動詞一意」 | v0.9 | 撤廃。「PASSIVE最大連続≤1」のみ |
| S10 独立 Disclosure Event | v0.10 | 新設しない。Transition Beat |
| D-NOAH 必須開示 | v0.2 / v0.10 | 必須から除外。CANDIDATE/ASSUMPTION 保留 |

## 3. 原本 Changelog（v0.1〜v0.17 要約）

- v0.1（2026-08-13）新規。Scene/Dialogue/Interaction/Event/Traceability/Map Anchors/粒度監査
- v0.2 doc-review反映。否認/怒りをEmotionに realize。D-NOAH 降格
- v0.3 SECTION 2B（line-by-line 台本）新設
- v0.4 SECTION 2C（悉皆 examinables / state-variants / ambient）新設
- v0.5 30分体験再編集。MIO-A/B/C、観測因果チェーン、S8操作試行、C2 Matrix
- v0.6 学校/教室を全除外
- v0.7 PRIMARY PLAYER VERB 追記、Observation Causality 注記、Player Feels/Does/Notices/Suspects
- v0.8 S4「白層化率」隠蔽（--%）、S8失敗動詞から呼びかけ削除、S11因果変更、Engagement分類、MIO BOND TRACE
- v0.9 3原則明文化。S11機序を CANDIDATE へ降格。Engagement Gate 簡素化
- v0.10 S10 を Transition Beat へ縮退
- v0.11 Exploration Information Layer
- v0.12 AREA-B Dialogue/Inspect Pass
- v0.13 AREA-A/C Pass + Throughline Audit
- v0.14 Script Texture Pass（NPC人格・再会話・Stale整理）
- v0.15 FULL PLAYER PLAYTHROUGH（実プレイ順）
- v0.16 Playthrough Benchmark Quality Review
- v0.17 / v0.17a Critical Route Desk Read-through + Control-State Audit、Human Validation Layer（H001〜H023）

## 4. 正規化作業の履歴（本リポジトリ）

| 日付 | 作業 | 結果 |
|---|---|---|
| 2026-08-18 | Google Doc（実体v0.17）を `source/` に凍結 | 完了 |
| 2026-08-18 | 正規化セット初版作成 | 一部項目を過剰に「確定」扱いにしていたため v1.1 で格下げ |
| 2026-08-18 | **v1.1 実装準備正規化** | 正本の単一レイヤー化、FLAG/EVENT/CONTROL/CLOCK/TUNING/DEPENDENCIES 分離、mioTrust廃止・CALLOUT長押し・Narrative Clock を候補へ格下げ、S7 は UNDECIDED 維持 |
