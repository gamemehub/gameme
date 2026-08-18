# NARRATIVE CLOCK — 17:17 仕様

**Status**: v1.1 正規化ドラフト（第一候補案・**未確定**）
**Source**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md` S3/S4/S11 / §17B
**目的**: 原本の「ゲーム内時刻==17:17」「17:17が近づく」を実装可能な形に定義する。原本には時刻の駆動方式が未定義であり、実装ブロッカーであった。

---

## 1. 方式の選定

| 案 | 内容 | 評価 |
|---|---|---|
| **A: 実時間クロック** | ゲーム内時計が実時間で進行し17:17に到達 | ✗ S3で待たされる／放置でソフトロック風になる。30分尺の管理が不能。Blind Playtestの再現性も落ちる |
| **B: 完全スクリプト駆動** | 会話送り完了で即17:17へ | △ 実装最少だが、§17Eの「Player入力なしで次が始まらない」「ただ座る余白」と衝突し、Core Event連打が復活する |
| **C: Narrative Clock（イベント駆動＋滞在条件）** | 表示時刻は演出変数。物語条件の充足＋短い滞在で発火 | ◎ **第一候補**。「17:17が近づく」という静かな待ちを保証しつつ、ソフトロックを構造的に排除 |

**第一候補: C案（Narrative Clock）**。ただし本書は候補整理であり、確定は Lock 前の人間裁定による。

---

## 2. 定義（C案）

### 2.1 時刻表示

時計表示は**演出変数**。シーンスクリプトで進める。実時間で進行させない。

| Scene | 表示時刻 | canon_status |
|---|---|---|
| S0 | 17:17（滲み） | CONFIRMED |
| S1 | 朝 | CONFIRMED |
| S2 | 夕方前 | CONFIRMED |
| S3 | 夕方 | CONFIRMED |
| S4〜S10 | **17:17** → 夕闇 | CONFIRMED |
| S11 | **17:17** → 夜 | CONFIRMED |

### 2.2 EVT-1717 発火条件（S4開始）

**Story Preconditions（Canon / Requirement）**
- S3 active
- D-NAME1 complete（名前の実演を通過している）
- MIO-C complete（「ただ座る」Natural Beatを通過している）
- プレイヤーがC2ゾーン内に滞在している

**Tuning（Canon化しない・PROVISIONAL）**
- `MIOC_LINGER_SEC` — MIO-C「ただ座る」の最短通過時間
- `S4_IDLE_TRIGGER_SEC` — 最終必須ビート完了後、発火までの滞在/アイドル時間

```
if (S3 active
    && D-NAME1.complete
    && MIO-C.complete
    && player.inZone(C2)
    && elapsedSinceLastRequiredBeat >= S4_IDLE_TRIGGER_SEC)
  → 表示時刻を 17:17 に更新
  → EVT-1717 発火（端末通知）
```

**設計意図**: 「17:17が近づく」という体験（少しの静かな待ち）を作りつつ、プレイヤーが動かなくても詰まらない。Story条件とTuning値を分離しているため、秒数の調整が仕様改訂を伴わない。

### 2.3 S11 の 17:17

S10余韻の終了を契機にシーンスクリプトで表示時刻を 17:17 に更新する（S4と同じ擬似時計。独立した時刻判定を持たない）。

### 2.4 17:17 前の Area C 離脱

`CONTROL_GATE_SPEC.md` G2 のソフトブロックで扱う。実時間到達を待たせる構造にしない。

---

## 3. 未確定事項

| 項目 | 状態 |
|---|---|
| C案の採用可否 | **DESIGN REVIEW REQUIRED**（第一候補として提示） |
| `S4_IDLE_TRIGGER_SEC` / `MIOC_LINGER_SEC` の値 | PROVISIONAL（`TUNING.md`） |
| 時刻表示UIの有無・見え方（端末UI内か常時HUDか） | UNDECIDED（UIUX側と要調整） |
| S3滞在中にプレイヤーが完全に静止し続けた場合の演出（環境音の変化等で待ちを可視化するか） | CANDIDATE |
| C2ゾーンの範囲定義 | **UNDETERMINED（IMAGE-02待ち）** |
