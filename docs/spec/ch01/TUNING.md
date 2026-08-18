# TUNING — CH01 調整値一覧

**Status**: v1.1 正規化ドラフト（全値 PROVISIONAL）
**目的**: 原本本文に散在する秒数・歩数・回数を集約し、**Canon / Story Requirement と分離**する。

## 分離原則

| 区分 | 定義 | 変更時の扱い |
|---|---|---|
| **Story Requirement（Canon）** | 「Controlを返す」「最低1回体験する」「Player入力なしで次が始まらない」など、**満たすべき事実** | 仕様改訂（人間裁定） |
| **Tuning（本書）** | その事実を成立させる**具体値**（何秒・何歩・何回） | 本書の数値変更のみ。仕様改訂を伴わない |

**本書の値はすべて PROVISIONAL（設計仮置き）。Canon ではない。** Playtest 実測で調整する。

---

## 1. Narrative Clock

| Key | 暫定値 | 対応するStory Requirement | 出典 |
|---|---|---|---|
| `MIOC_LINGER_SEC` | 4 | S3「ただ座る」＝何も起きない時間をCritical Routeで通過する | 原本S3 / QP-02 |
| `S4_IDLE_TRIGGER_SEC` | 6 | 17:17が「近づく」感覚を作る（即発火しない） | 原本S3 Exit「17:17が近づく」 |

## 2. S4（17:17通知）

| Key | 暫定値 | Story Requirement | 出典 |
|---|---|---|---|
| `S4_NOTIFICATION_LOCK_SEC` | 3 | 通知表示中のみ短時LOCK | §17B |
| `POST_S4_FREE_STEPS_MIN` | 3 | 通知close後、Player自身が5席目へ近づく（自動吸着禁止） | §17B「3〜8歩程度」 |
| `POST_S4_FREE_STEPS_MAX` | 8 | 同上 | §17B |

※歩数は「トリガーゾーンまでの距離設計の目安」であり、実距離は IMAGE-02 の座標確定後に換算する。

## 3. S5（五席目）

| Key | 暫定値 | Story Requirement | 出典 |
|---|---|---|---|
| `S5_POST_INSPECT_BEAT_SEC` | 2.5 | 調査後、即Choice UIを出さず一拍置く | §17B / QP-04 |
| `S5_FRAGMENT_MAX_REINSPECT` | 1 | 再調査でfragment取得（上限） | 原本S5（上限は明記なし＝要判断） |

## 4. S8（アンログ逆流）

| Key | 暫定値 | Story Requirement | 出典 |
|---|---|---|---|
| `S8_OPENING_LOCK_SEC` | 4 | 異常を短く提示してから操作を返す | §17B |
| `S8_PROBE_MIN_VERBS` | 2 | **最低1回**の「観測→悪化」体験（Requirementは1回。2は学習確度を上げる暫定値） | §17E「2回目を必須にするかはPlaytestで決定」 |
| `S8_PROBE_TIMEOUT_SEC` | 20 | 動かないプレイヤーが詰まらない | 実装補完（原本に規定なし） |
| `S8_RATE_JUMP_LOW/MID/HIGH` | 未定 | observation Tierで逆流強度が変わる | 原本S8「observation高いほど逆流強」 |

## 5. S9（呼びかけ）

| Key | 暫定値 | Story Requirement | 出典 |
|---|---|---|---|
| `S9_REPROMPT_AFTER_CHOICES` | 2 | （**CANDIDATE**: 再提示の有無自体が未確定） | 実装補完 |
| `CALLOUT_*`（入力方式に依存する各値） | **定義不可** | S9/S11で同一操作 | 入力方式UNDECIDEDのため値を置かない |

## 6. S10 / S11

| Key | 暫定値 | Story Requirement | 出典 |
|---|---|---|---|
| `S10_AFTERGLOW_MIN_SEC` | 5 | S9成功後、Controlを返す（「助かった」と感じる時間） | 原本S10「5〜15秒程度」 |
| `S10_AFTERGLOW_MAX_SEC` | 15 | 同上 | 原本S10 |
| `S11_REINTERPRET_MIN_SEC` | 10 | 連れ去り後、通知反転より前にControlを返す | §17B「10〜20秒」 |
| `S11_REINTERPRET_MAX_SEC` | 20 | 同上 | §17B |
| `S11_REQUIRED_REINSPECT_COUNT` | 1 | Critical Routeでも連れ去り後C2を最低1回再調査 | §17C |

## 7. Bond / 移動

| Key | 暫定値 | Story Requirement | 出典 |
|---|---|---|---|
| `MIOB_STOP_WAIT_THRESHOLD_SEC` | 2.5 | 「待つ機会」を保証する（待つ成功はPlayer Choiceのまま・好感度正解化しない） | §17D-5 |
| `WALK_SPEED_INDOOR` / `WALK_SPEED_OUTDOOR` | 未定 | — | Phase 1で実測調整 |

---

## 8. 未確定・要判断

| 項目 | 状態 |
|---|---|
| S8 率ジャンプ量（Tier別） | 値未定（Phase 1） |
| `S5_FRAGMENT_MAX_REINSPECT` | 原本に上限規定なし → **要判断** |
| `S9_REPROMPT_AFTER_CHOICES` | 再提示の実施可否が **CANDIDATE** |
| CALLOUT 関連の全定数 | 入力方式 **UNDECIDED** のため定義できない |
| 歩数→実距離の換算 | **IMAGE-02待ち** |
| 移動速度 | Phase 1 灰箱で実測 |
