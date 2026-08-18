# REVIEW_REPORT — CH01 実装準備レビュー結果

**日付**: 2026-08-18
**対象**: `CH01_DETAILED_SCRIPT`（実体 v0.17）
**作業種別**: 仕様の正規化と不足定義の整理のみ。**実装・Canon変更・Map座標確定・Godotコード変更なし**

---

## 1. 作成・変更したファイル

### 新規作成

| ファイル | 内容 |
|---|---|
| `FLAG_REGISTRY.md` | 13フラグの台帳・型監査。whiteLayerProgress の enum 2案比較、mioTrust の 2案比較 |
| `EVENT_REGISTRY.md` | EVT 7件を22項目で定義。座標系は全件 UNDETERMINED |
| `CONTROL_GATE_SPEC.md` | Control State 6種、Scene別仕様、S8/S9 State Machine、Gate G1〜G7 |
| `NARRATIVE_CLOCK.md` | 17:17 の3方式比較とC案（イベント駆動）の定義。Story条件とTuningを分離 |
| `TUNING.md` | 調整値18件を集約。Story Requirement と Tuning の分離原則 |
| `CANON_DEPENDENCIES.md` | 依存文書24件の一覧・MISSING判定・既知の不整合3件 |
| `AUDIT_HISTORY.md` | 監査履歴・superseded記述12件・原本Changelog を正本から分離 |
| `REVIEW_REPORT.md` | 本ファイル |

### 変更

| ファイル | 変更内容 |
|---|---|
| `CH01_IMPL_SPEC.md` | **全面改訂（v1.1）**。S0〜S11 を指定16フィールドで再構成。監査履歴を分離。前回「確定」扱いにしていた項目（mioTrust廃止 / CALLOUT長押し / Narrative Clock / S7 flag-off / セーブ方式）を**候補・未決へ格下げ** |
| `CANON_SNAPSHOT.md` | 未決レジスタに CALLOUT入力方式・データモデルを追加。CD-13 を「UNDECIDED維持」へ修正 |
| `README.md` | 前提条件（変更禁止事項）とファイル構成を更新 |
| `flags.json` / `scenes.json` / `tuning.json` / `dialogues.json` | `$status` を追加し **SUPERSEDED FOR DECISIONS**（スキーマ参考ドラフト）へ格下げ。削除はしていない |

**実施していないこと**: Godotコード変更 / Web版改修 / git commit・push / S7採用 / CALLOUT長押し確定 / mioTrust廃止確定 / Canon変更 / 新規世界設定追加 / Map座標推測 / IMAGE Lock / 既存資料の削除

---

## 2. 実装ブロッカー: **13件**

| # | 項目 | 種別 | 重大度 |
|---|---|---|---|
| B1 | 白層状態フラグの enum 設計（2案未選定） | DESIGN REVIEW | 高 |
| B2 | mioTrust データモデル（2案未選定）＋S3/S6デッドリード処置 | DESIGN REVIEW | 高 |
| B3 | CALLOUT 入力方式 | UNDECIDED | 高 |
| B4 | Narrative Clock（C案）の採用可否 | DESIGN REVIEW | 高 |
| B5 | S8 Probe 脱出条件値 / S9 再提示の有無 | Tuning + CANDIDATE | 中 |
| B6 | Gate G1/G2 の文言（既存流用 or Implementation Candidate 新規） | DESIGN REVIEW | 中 |
| B7 | S7 採否（CD-13） | UNDECIDED（上位） | 中（回避策あり） |
| B8 | フラグの Canon 化（DL-Y3） | UNDECIDED（上位） | 低（`impl.*` 隔離で待機可） |
| B9 | セーブ方式 | CANDIDATE | 中 |
| B10 | 座標・Collision・Trigger形状・C2ゾーン範囲 | IMAGE-02待ち | 高 |
| B11 | S0 / S8〜S11 のロケ確定 | ASSUMPTION | 中 |
| B12 | 上位canonの学校/教室記述（STALE CANON） | GOVERNANCE FIX | 中 |
| B13 | 依存文書の大半が MISSING / PATH NOT VERIFIED | 照合不能 | 高 |

**前回レビュー（PDF段階）からの解消状況**: 「フラグのデータモデル」「時刻システム」「入力ループ」は**定義の枠と候補を提示**したが、いずれも裁定待ちのため**ブロッカーとしては未解消**。書式・追跡性は改善した。

---

## 3. HUMAN DECISION が必要な項目: **9件**

| # | 決定事項 | 選択肢 | 備考 |
|---|---|---|---|
| H1 | 白層状態 enum 設計 | A: Scene-anchored `{none,intro,s4,s5,s8,s11}` / B: 意味状態 `{normal,foreshadow,ui_corrupted,localized,inverted,lost}` | 本Registryの整理では **B が優位**（Scene ID漏出なし・C2 Matrixと1:1・CH02拡張可）。ただし命名は要確定 |
| H2 | mioTrust の扱い | A: 数値信頼度として整備 / B: MIO BOND TRACE bool群 | 「好感度システムにしない」原則との整合は B が構造的に強い。A は増分・閾値・読取効果の全定義が新規に必要 |
| H3 | S3/S6 の mioTrust デッドリード | 削除 / 読取効果を新規定義 | H2 と連動 |
| H4 | CALLOUT 入力方式 | 長押し / 選択肢+固定ビート / その他 | **S9・S11 同一操作**のみ確定済み。UIUX 仕様（SCREEN_CALLOUT_INPUT）未作成 |
| H5 | Narrative Clock C案の採用 | C案 / 他案 | 実時間案・完全スクリプト案の欠点は `NARRATIVE_CLOCK.md` §1 に記載 |
| H6 | Gate G1/G2 の文言方針 | 既存台詞の再利用 / Implementation Dialogue Candidate を新規に起こす | **新規Canon台詞化は禁止** |
| H7 | S9 の呼びかけ再提示 | 実施する（N回後）/ 実施しない | 実施する場合も既存 D-ANLOG 行の再掲に限る |
| H8 | セーブ方式 | チェックポイントのみ / 手動+チェックポイント / その他 | S8〜S11 中のセーブ可否に影響 |
| H9 | S7 採否（CD-13） | 上位決裁 | Prototype は S6→S8 前提で待機可能 |

**上位canon側の宿題（実装側で決められない）**: STALE CANON（学校/教室記述）の修正、DL-Y3、U-004 の維持確認。

---

## 4. IMAGE-02 待ちの項目: **8件**

| # | 項目 | 影響範囲 |
|---|---|---|
| I1 | 全 spawn 座標（A1/B1/C1/C2 等） | S0〜S11 の Entry |
| I2 | Facing 初期値の実座標対応 | 各Scene Entry |
| I3 | Collision shape | 全Area |
| I4 | Trigger ゾーン形状・配置（特に 5席目・C2境界） | EVT-EMPTYSEAT / G3 |
| I5 | C2 ゾーン範囲（Narrative Clock の滞在判定） | EVT-1717 |
| I6 | 「3〜8歩」→ 実距離の換算 | S4→S5 のトリガー距離設計 |
| I7 | AREA-B の Optional Pocket / 小ループのルート形状 | P03/P06/P05 |
| I8 | S0 / S8〜S11 のロケ実体化（ASSUMPTION解消） | 上記すべて |

---

## 5. Godot 実装開始可否

### 判定: **開始不可（NO-GO）**

厳しめの判定基準で評価した結果、以下の理由により Phase 1（灰箱）の着手も推奨しない。

**理由**

1. **データモデルが未確定（B1/B2）** — フラグの型・書込・読取効果が確定していないため、セーブ構造とステート管理の骨格が決まらない。着手すると後で全面手直しになる。
2. **主要インタラクションが未定義（B3）** — CALLOUT は S9/S11 の中核操作。入力方式が決まらないと `CALLOUT_CONTROL` の実装形が決まらず、UIUX 仕様も書けない。
3. **進行の駆動方式が未確定（B4）** — Narrative Clock は第一候補を示したのみ。S3→S4 の遷移条件が確定しないと Area C の縦切りが組めない。
4. **空間定義が全面的に未確定（B10/I1〜I8）** — 灰箱は PROVISIONAL 座標で進められるという見方もあるが、C2 ゾーン範囲は Narrative Clock の滞在判定に直結し、5席目 Trigger は G3（Player入力必須）の成立条件そのもの。仮座標で組んだ場合、§17E の受け入れ条件のうち複数が「仮の値で通ったこと」にしかならず、検証として成立しない。
5. **canon 照合手段がない（B13）** — 依存文書の大半が MISSING / PATH NOT VERIFIED。実装中に canon 疑義が出た場合、確認先がない。

**部分着手が可能な範囲（参考）**: Godot プロジェクトの初期設定（バージョン固定・解像度・入力マップの定義）と、フラグ非依存の描画/移動プロトタイプは技術検証として先行可能。ただしこれは**仕様実装ではない**ため、本判定を変えない。

### GO 条件（次にこれが揃えば着手判断可）

- H1・H2・H4・H5 の裁定完了（B1〜B4 の解消）
- H6・H8 の方針決定
- IMAGE-02 のうち **Area C（C1/C2）だけでも実座標が確定**（I4/I5 が最優先）
- `UNDECIDED_REGISTER` / `CH01_DETAIL.md` の入手（B13 の部分解消）

---

## 6. 次の推奨作業

**優先度順**

1. **HUMAN DECISION 9件の裁定会**（H1〜H9）。所要は短く、H1・H2・H4・H5 の4件だけでもブロッカーの高重大度が解消する。本レポート §3 の表がそのまま議題になる。
2. **依存文書の入手・凍結**（B13）。優先順は `UNDECIDED_REGISTER` → `CH01_DETAIL.md` → `CHAPTER01_SCENARIO_MASTER.md` → `MAP_VISUAL_MASTER_CH01`。`source/` へ凍結し `CANON_DEPENDENCIES.md` を更新。
3. **IMAGE-02 の Area C 先行着手**（I4/I5）。全Areaを待たず、C1/C2 だけ先に実座標化すれば Phase 1 の GO 条件を満たせる。
4. **STALE CANON の是正依頼**（B12）。上位canon（`CH01_DETAIL.md:42` / `14_CHAPTER_BIBLE.md:27`）の学校/教室記述について、ガバナンス側へ修正を起票。
5. **SCREEN_CALLOUT_INPUT の仕様化**（H4裁定後）。既存 `docs/design/UIUX/SCREEN/` と同形式で作成。
6. **`CH01_PHASE2_EMOTIONAL_HOOK_SPEC.md` の扱いを決定**（`CANON_DEPENDENCIES.md` X2）。現行仕様とシーン順序が不一致のため、旧導線前提のまま着手すると手戻りになる。

**推奨しない作業**: 現時点での Godot 実装着手、Map 座標の仮確定、台詞の文芸FINALパス（構造が固まる前に磨くと手戻りになる。原本 §13H でも「先に台詞を磨き込みすぎない」と規定）。
