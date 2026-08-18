# CONTROL / GATE SPEC — CH01 操作状態とゲート

**Status**: v1.1 正規化ドラフト（実装準備・コード未着手）
**Source**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md` §17B / §17C / §17E
**注記**: 具体秒数・歩数・回数はすべて `TUNING.md` へ分離。本書は状態の定義と遷移条件（Story Requirement）のみを扱う。

---

## 1. Control State 定義

| State | 操作可能 | 操作不能 | Control復帰契機 |
|---|---|---|---|
| **LOCKED** | 台詞送りのみ（送りすら不可の演出区間もある） | 移動 / 調べる / 選択 / メニュー | 演出終了時、自動 |
| **UNLOCKED** | 移動 / Facing変更 / 調べる / NPC会話 / エリア遷移（Gate条件下） | — | （既に自由） |
| **CHOICE_CONTROL** | 選択肢の選択・決定 | 移動 / 調べる | 選択確定時 |
| **PARTIAL_UNLOCK_PROBE** | 定義済み試行動詞のみ（S8: 移動/触れる/追跡/記録）。**各操作は成功せず状態を悪化させる** | エリア離脱 / 通常の調べる / メニュー | 脱出条件充足時（§3） |
| **UI_LOCK** | UIオーバーレイ内の操作のみ（通知open/close、モノローグ送り） | 移動 / 調べる / エリア離脱 | UIクローズ時 |
| **CALLOUT_CONTROL** | 呼びかけ入力のみ（**入力方式UNDECIDED**） | 移動 / 選択 / 中断 | 呼びかけ成立時 |

**Requirement（実装制約・Canon）**:
- 完全受動演出（LOCKED / UI_LOCK）を3つ以上連続させない。各主要転換の間にPlayer Inputが存在すること。
- `CHOICE_CONTROL` は演出LOCKではなく **Player Decision State** として扱う（移動は止まるがプレイヤーの主体性は保持）。
- `PARTIAL_UNLOCK_PROBE` の「移動する」はエリア離脱ではなく**試行動詞**として処理する。

---

## 2. Scene別 Control 仕様

| Scene | Control遷移 | 操作可能 | 操作不能 | Control復帰 |
|---|---|---|---|---|
| S0 | LOCKED | 台詞送り | 移動・調べる | S1開始時 |
| S1 | UNLOCKED | 移動 / 調べる（A1私物・A2カップ等・A3母の部屋）/ 叔母会話 / 玄関 | — | — |
| S2 | UNLOCKED（同行） | 移動 / 寄り道 / NPC会話 / 調べる | — | — ※会話で歩行を止めない（Natural Ambient） |
| S3 | UNLOCKED → 軽微FIXED（会話中） | 移動 / ベンチ調べる・座る / 塔を見る | 会話中の移動 | 会話終了時 |
| S4 | UNLOCKED → **UI_LOCK**（通知）→ UNLOCKED | 通知open/close → 復帰後は移動・調べる | 通知表示中の移動 | 通知close時（**自動でS5へ遷移しない**） |
| S5 | UNLOCKED → 短時LOCK（調査中）→ UNLOCKED | 5席目調査 / 再調査 / 周囲を見る | 調査演出中 | 調査後（**即Choice UIを出さず余白**） |
| S6 | **CHOICE_CONTROL** | 4 intentの選択 | 移動・調べる | 選択確定時 |
| S7 | — | **UNDECIDED（Prototypeでは経由しない）** | — | — |
| S8 | LOCKED → **PARTIAL_UNLOCK_PROBE** → 短時LOCK | 試行動詞（移動/触れる/追跡/記録） | エリア離脱 / 通常Interact | REALIZATION到達後S9へ |
| S9 | **CHOICE_CONTROL** → **CALLOUT_CONTROL** | 5択の選択 → 呼びかけ入力 | 移動 / 中断 | 呼びかけ成立時 |
| S10 | UNLOCKED（余韻） | 移動 / ベンチ・塔を見る / その場に留まる | — | （既に自由。強制READ/VNなし） |
| S11 | CALLOUT_CONTROL → **LOCKED**（Capture）→ UNLOCKED（再解釈）→ UI_LOCK（通知） | 呼びかけ → （介入中は不可）→ 再調査・移動 → モノローグ送り | Capture演出中のすべて | Capture完了時に**必ず**返す |

---

## 3. S8 State Machine（候補）

```
[S8 ENTRY]
  ↓
OPENING_LOCK
  色抜け提示 / D-ANLOG★ / D-STOP
  Control: LOCKED
  ↓ （提示完了。尺は Tuning: S8_OPENING_LOCK_SEC）
PROBE_LOOP
  Control: PARTIAL_UNLOCK_PROBE
  試行動詞: 移動する / 触れる / 追跡する / 記録する
  各試行 → 白層化率が跳ぶ ＋ 固有フィードバック行 ＋ 色抜け進行
  ★ Story Requirement: 最低1回、プレイヤー自身の操作によって
     「観測操作 → 悪化」の因果を体験すること（UI説明で代替しない）
  脱出条件: [Tuning] 試行回数 or 経過時間（S8_PROBE_MIN_VERBS / S8_PROBE_TIMEOUT_SEC）
  ↓
REALIZATION
  Control: 短時LOCK
  トウ内語「…ぼくが、見たから。」（自分で到達・怒り）
  ↓
UI_REVEAL
  欠損ラベルが初めて「白層化率」として判読可能に ＋ 急伸
  ★ Requirement: この時点より前に名称を読めてはならない（3原則①）
  ↓
[S9 へ]
```

**Requirement（Canon）**:
- 最低1回の「観測操作→悪化」体験を必須とする。
- 「白層化率」名称の初判読は REALIZATION 後（UI が先に答えを言わない）。
- 呼びかけを試行動詞リストに含めない（3原則②）。

**Tuning / Candidate（Canon化しない）**: 試行必須回数、タイムアウト秒、OPENING_LOCK尺、率ジャンプ量、色抜け段階数。

---

## 4. S9 State Machine（候補）

```
[S9 ENTRY]
  ↓
CHOICE_LOOP
  Control: CHOICE_CONTROL
  選択肢: 見ない / 聞く / 待つ / 手を取る / 名を呼ぶ
  ★ Requirement: 「見ない/聞く/待つ/手を取る」は失敗ではない。
     正の反応（ミオの震えが少し止まる 等）を返し、選択へ戻れること。
     失敗ペナルティ・タイマー死・強制退場を設けない。
  [Candidate] 非呼びかけ選択が N 回続いた場合、
     D-ANLOG既存行「名前、呼んで」を再提示（新規台詞を作らない）
     → N は Tuning / 再提示の有無自体も CANDIDATE
  ↓ 「名を呼ぶ」選択
CALLOUT
  Control: CALLOUT_CONTROL
  ★ Requirement: S9 と S11 で同一操作であること（入力方式は UNDECIDED）
  ↓
RESPONSE
  呼びかけ後、他の音がすべて引く → 無音
  ミオ「…今の、ちゃんと、私だった。」★
  Flag: mioNameStability=restored / mioVoluntarySpeech / relationAnchor
  ↓
[S10 へ]
```

---

## 5. Gate 仕様

**原則**: LOCKED/演出中を除き、ハードロック（見えない壁・入力無効化）ではなく**作中の反応1行で戻す**ソフトブロックを第一候補とする。**新規Canon台詞は追加しない** — 下表の文言はすべて `Implementation Dialogue Candidate`（実装用の仮文言・canon非追加・差し替え可）。

| # | Gate | 状況 | 強制方法（候補） | 文言の扱い |
|---|---|---|---|---|
| G1 | S1 叔母会話前の玄関 | 叔母と話す前に玄関へ到達 | ソフト: 玄関Interactで内語1行を返し、その場に留める（移動自体は自由のまま） | **Implementation Dialogue Candidate**。既存資産の再利用が可能なら優先（例: A1内語「……いかなきゃ。」の再掲）。新規台詞を確定しない |
| G2 | S3 17:17前のArea C離脱 | C1入口方向へ戻ろうとする | ソフト: ミオが立ち止まる／短い引き留め反応。**進行はブロックするが操作は奪わない** | **Implementation Dialogue Candidate**。既存のミオ台詞（例「一番端は、近すぎるの。」系の再掲）で代替できないか実装時に検討 |
| G3 | S4→S5 | 通知close後 | **Player入力必須**: プレイヤー自身が5席目トリガーゾーンへ接近することでS5開始。自動遷移・自動吸着を禁止（§17E） | 台詞不要（ミオの視線＝5席目方向、で誘導） |
| G4 | S5→S6 | 5席目調査完了後 | **時間/入力の余白**: 即Choice UIを出さない。トウが立ち上がる／ミオが待つ、を見せてからChoice。余白長はTuning | 既存ト書きで成立（新規台詞不要） |
| G5 | S8→S9 | 操作試行中 | **Requirement充足**: 最低1回の観測操作→悪化体験。充足後にREALIZATION→UI_REVEAL→S9。回数/timeoutはTuning | 既存フィードバック行のみ |
| G6 | S9→S10 | 呼びかけ成立後 | **成立ベース**: CALLOUT成立で自動遷移。ただしS10で必ずControlを返す（余韻） | 台詞不要 |
| G7 | S11 Capture後→Sender Invert | 連れ去り完了後 | **必須Player Action**: 連れ去り後C2をUNLOCKし、ミオがいた位置（二番目の席/ベンチ）を1回以上プレイヤー自身が調べるまで EVT-SENDER-INVERT を発火しない。回数はTuning | 台詞不要。誘導文言も出さない（自発再訪の計測対象・15D H023） |

**未確定事項**:
- G1/G2 の文言をどの既存資産で賄うか、あるいは新規Implementation台詞を起こすかは **DESIGN REVIEW REQUIRED**（新規Canon台詞化は禁止）。
- G7 の必須再調査を、プレイヤーが長時間行わない場合の救済（Observer Rescue相当のゲーム内誘導）を設けるかは **UNDECIDED**。設ける場合も誘導文言はCanonにしない。

---

## 6. 受け入れ条件（§17E 準拠・Phase 1 検証項目）

1. S4通知close後、Player入力なしでS5が開始しない。
2. S5 Inspect後、即Choice UIへ連結せずUNLOCK余白がある。
3. S8で少なくとも1回はPlayer自身の通常操作が失敗し、UIだけで「観測が悪い」と教えない。
4. 「白層化率」名称は操作失敗より前に読めない。
5. S9成功後、S10でControlを返す（尺はTuning）。
6. S11連れ去り後、通知反転より前にControlを返す。
7. Critical Routeでも連れ去り後C2を最低1回Player自身が再調査する。
8. S4〜S11の各主要転換の間にPlayer Inputが存在し、3つ以上の完全受動演出が連続しない。
9. 後半の理解を新規Lore台詞で補わない（WORLD→SUSPICION→UI→PLAYER ACTION順守）。
