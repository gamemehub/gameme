# CANON_DEPENDENCIES — 本仕様が依存する文書

**Status**: v1.1 ドラフト
**目的**: CH01実装仕様が参照している上位文書・関連文書を一覧化し、参照可否を明示する。
**規約**: 存在確認できないものは**新設せず** `MISSING / PATH NOT VERIFIED` と記載する。パスは原本v0.17の記載を転記したものであり、実在確認したものだけ `VERIFIED` とする。

---

## 1. SSOT チェーン（上位canon）

| 文書 | 役割 | 記載パス（原本v0.17より） | 状態 | 依存箇所 |
|---|---|---|---|---|
| DECISION_REGISTER | SSOT最上位・決定台帳 | （パス記載なし） | **MISSING / PATH NOT VERIFIED** | 全般。確定/仮定の判定根拠 |
| UNDECIDED_REGISTER | 未決台帳（U-004 / CD-13 / DL-Y3 の原本） | （パス記載なし） | **MISSING / PATH NOT VERIFIED** | S7採否・フラグCanon化・時計塔内部 |
| CH01_DETAIL.md | CH01 canon（12シーン） | `chapters/CH01_DETAIL.md` | **MISSING / PATH NOT VERIFIED** | シーン構成・S5ロケ（§3 4席+5席目=bench）・S10縮退判断 |
| CHAPTER01_SCENARIO_MASTER.md | 台詞ドラフト母体・3原則（§3B） | `Docs/CHAPTER01_SCENARIO_MASTER.md` | **MISSING / PATH NOT VERIFIED** | ★キーライン・3原則の原本 |
| 14_CHAPTER_BIBLE.md | 上位canon（学校記述の残存元） | `14_CHAPTER_BIBLE.md:27` | **MISSING / PATH NOT VERIFIED** | STALE CANON CANDIDATE の対象 |

## 2. Companion 文書（CH01設計）

| 文書 | 役割 | 記載パス | 状態 | 依存箇所 |
|---|---|---|---|---|
| CH01_SCENARIO_MASTER.md | Part構成 | （同ディレクトリ想定） | **MISSING / PATH NOT VERIFIED** | Part/Scene/Traceability 三層 |
| CH01_GPT_SCENARIO_INPUT_PACKAGE.md | canon入力パッケージ | — | **MISSING / PATH NOT VERIFIED** | canon照合 |
| CH01_PREPRODUCTION_DESIGN.md | map設計 | — | **MISSING / PATH NOT VERIFIED** | Area/Zone構成 |
| MAP_VISUAL_MASTER_CH01 | Camera定義（FOLLOW屋外2x / FIXED屋内） | — | **MISSING / PATH NOT VERIFIED** | 全SceneのCamera欄 |
| CH01_30MIN_EXPERIENCE_AUDIT.md | Beat監査・体験分類タグ（§6） | — | **MISSING / PATH NOT VERIFIED** | SECTION 2C の LIFE/WORLD/FORESHADOW/OBS-RISK タグ |

## 3. Map / 画像工程

| 項目 | 役割 | 状態 | 依存箇所 |
|---|---|---|---|
| IMAGE-01 | Map拡張方針 | **別工程・未Lock** | AREA-B拡張の根拠（v0.11） |
| IMAGE-02 | 実座標・Pin配置 | **別工程・未着手 / PENDING** | 全spawn・facing・Collision・Trigger形状・C2ゾーン範囲・歩数→距離換算 |

**注記**: 座標・Collision・Trigger形状は本仕様で推測しない（`EVENT_REGISTRY.md` 全イベントで UNDETERMINED）。

## 4. UIUX SCREEN 仕様（このリポジトリ内）

| 文書 | 状態 | 依存箇所 |
|---|---|---|
| `docs/design/UIUX/UIUX_MASTER.md` | **VERIFIED**（実在） | UI全般 |
| `docs/design/UIUX/RewriteMemory_UIUX_BIBLE.md` | **VERIFIED** | UI全般 |
| `docs/design/UIUX/RewriteMemory_MODE_DEFINITION.md` | **VERIFIED** | モード定義（探索/VN/Phone等） |
| `docs/design/UIUX/COMPONENT_DEFINITIONS.md` | **VERIFIED** | コンポーネント |
| `docs/design/UIUX/DESIGN_TOKEN.md` | **VERIFIED** | トークン |
| `docs/design/UIUX/SCREEN/SCREEN_TALK_WINDOW.md` | **VERIFIED** | 会話UI（M03A/M03B） |
| `docs/design/UIUX/SCREEN/SCREEN_VN_OVERLAY.md` | **VERIFIED** | VNオーバーレイ |
| `docs/design/ASSET_SPEC.md` | **VERIFIED** | 顔アイコン等アセット |
| SCREEN_CALLOUT_INPUT（呼びかけ入力UI） | **NOT CREATED**（入力方式UNDECIDEDのため未着手） | S9/S11 CALLOUT_CONTROL |
| SCREEN_NOTIFICATION / 記録率ラベル表示 | **PATH NOT VERIFIED**（既存UIUX内の該当箇所を要特定） | EVT-1717 / UI_REVEAL / carried.lost |

## 5. このリポジトリ内の関連資産

| 文書 | 状態 | 扱い |
|---|---|---|
| `docs/characters/01_Mio_Character_Bible.md` | **VERIFIED** | ミオのCharacter Voice照合用 |
| `docs/spec/CH01_PHASE2_EMOTIONAL_HOOK_SPEC.md` | **VERIFIED** | 旧Web版前提の仕様。**シーン順序が現行仕様と不一致**（詳細は §6） |
| `docs/rewrite-dev/index.html` ほか | **VERIFIED** | legacy / reference。実装先にしない |
| `docs/spec/ch01/source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md` | **VERIFIED** | 原本凍結 |

## 6. 既知の不整合（要人間裁定）

| # | 内容 | 影響 |
|---|---|---|
| X1 | 上位canon（`CH01_DETAIL.md:42` / `14_CHAPTER_BIBLE.md:27`）に学校/教室記述が残存。本仕様はC2ベンチで統一（2026-08-13） | **STALE CANON CANDIDATE / GOVERNANCE FIX REQUIRED**。上位側の修正が必要 |
| X2 | `CH01_PHASE2_EMOTIONAL_HOOK_SPEC.md` の導線は `anlog_flood → missing_chair → choice → reconstruction`。現行仕様は `S5(五席目) → S6(選択) → S8(逆流)` で**順序が逆**、かつ reconstruction は UNDECIDED | Phase2タスクを現行構造のまま実施すると手戻り。**要裁定** |
| X3 | 既存Web実装の `legacy_ch01_030_missing_chair` は「椅子」＋証言NPC（清掃員/通行人/店員）。現行canonはベンチ5席目・証言NPCなし | legacy/reference扱いのため実装影響なし。参照時に注意 |

## 7. 入手優先度

1. **UNDECIDED_REGISTER**（CD-13 / DL-Y3 / U-004 の正確な文面）— 未決3件の判断根拠
2. **CH01_DETAIL.md** — シーン構成のcanon照合
3. **CHAPTER01_SCENARIO_MASTER.md** — ★キーライン・3原則の原本照合
4. **MAP_VISUAL_MASTER_CH01** — Camera仕様
5. DECISION_REGISTER — 決定履歴

入手できたものから `docs/spec/ch01/source/` へ凍結追加し、本ファイルの状態を更新する。
