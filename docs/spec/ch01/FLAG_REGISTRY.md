# FLAG_REGISTRY — CH01 フラグ台帳・監査

**Status**: v1.1 正規化ドラフト（実装準備・コード未着手）
**Source**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md`
**規約**:
- `layer`: `impl`（実装変数・DL-Y3未決のためCanon化しない・セーブ上 `impl.*` 名前空間に隔離）/ `story`（Story状態・canon明示）
- `write timing`: フラグ書込のオーナーは **Dialogue完了時 または Event完了時のみ**。Scene退出時書込は禁止（旧仕様の書込タイミング揺れの再発防止）
- `persistence`: `checkpoint`（チェックポイントに保存）/ `permanent`（story・write-once）/ `derived`（保存しない導出値）
- `canon_status`: CONFIRMED / CANDIDATE / ASSUMPTION / UNDECIDED / **DESIGN REVIEW REQUIRED**（実装前に人間裁定が必要）

---

## 1. whiteLayerProgress ⚠ 型混在あり — 解消案2案を比較

**原本の問題**: `whiteLayerProgress=intro`（文字列代入・S0）と `whiteLayerProgress+`（インクリメント・S4/S5）が混在し、型が定義不能。実際の進行はすべてシーンスクリプト駆動であり、演算としてのカウンタは存在しない。→ **enum化で解消する**。enumの設計に2案。

### A案: Scene-anchored enum

`{none, intro, s4, s5, s8, s11}` — 書込点のScene IDをそのまま値にする。

### B案: 意味状態 enum（Semantic State）

`{normal, foreshadow, ui_corrupted, localized, inverted, lost}` — C2 World State Matrix の状態タグ〔平常→17:17後→白層化↑→逆流中→連れ去り後〕に対応する意味名。

| 対応 | B案の値 | 意味 | 書込点（オーナー） |
|---|---|---|---|
| 導入の滲み | `foreshadow` | 予告のみ・本編は平常 | EVT-OPENING |
| 17:17後 | `ui_corrupted` | UI変質の始まり（--%） | EVT-1717 |
| 白層化↑ | `localized` | 白層の局在が顕在化（5席目） | EVT-EMPTYSEAT |
| 逆流中 | `inverted` | 因果反転（観測=白層化） | EVT-ANLOG-BACKFLOW |
| 連れ去り後 | `lost` | 喪失・夜 | EVT-CAPTURE |

### 比較

| 観点 | A案（Scene-anchored） | B案（意味状態） |
|---|---|---|
| 実装の単純さ | ◎ 書込点と1:1 | ○ マッピング表が1枚要る |
| シーン並び替え耐性 | × S番号変更で値が嘘になる | ◎ 影響なし |
| CH02以降での再利用 | × CH01のScene IDが漏出 | ◎ 「街の白層化状態」としてそのまま拡張可 |
| C2 State Matrixとの対応 | △ 間接 | ◎ Matrixの状態タグと1:1 |
| デバッグ時の可読性 | ○ | ◎ 値だけで世界状態が読める |

**推奨**: **B案（意味状態enum）** を第一候補とする。ただし値の命名はCanonでないため、**CANDIDATE — DESIGN REVIEW REQUIRED**（Lock前に命名確定）。

| 項目 | 内容 |
|---|---|
| name | `whiteLayerState`（B案採用時の改名候補。A案なら `whiteLayerStage`） |
| layer | impl |
| type | enum（上記2案） |
| initial | `normal` / `none` |
| writer | EVT-OPENING / EVT-1717 / EVT-EMPTYSEAT / EVT-ANLOG-BACKFLOW / EVT-CAPTURE |
| reader | C2 World State Matrix（NPC/環境音/色光/Camera/Interactable variant選択）、`uiRecordRateLabel` 導出 |
| effect | 同一地点C2の状態差分の駆動源 |
| write timing | 各Event完了時 |
| persistence | checkpoint |
| canon_status | 進行事実=CONFIRMED / enum設計=**DESIGN REVIEW REQUIRED** |
| unresolved | enum案の選定（推奨B）・改名の可否 |

### 付随: uiRecordRateLabel（表示導出値）

| 項目 | 内容 |
|---|---|
| name | `uiRecordRateLabel` |
| layer | impl / type: derived-enum / persistence: **derived（保存しない）** |
| values | `normal` → `corrupted`(--%・名称未判読) → `corrupted_up`(--%↑) → `named_spike`(「白層化率」初判読+急伸) → `carried_lost`(灰スロット) |
| derivation | whiteLayer状態 + S5再調査有無 + S8操作試行有無 から導出 |
| effect | §17D P0整合（S4で名称未判読・S8の操作失敗後に初判読）を型で保証 |
| canon_status | 表示順序=CONFIRMED（3原則①）/ 値名=CANDIDATE |
| unresolved | なし（whiteLayer enum確定に追従） |

---

## 2. observation

| 項目 | 内容 |
|---|---|
| name | `observation` |
| layer | impl / type: int / initial: 0 / range: 0〜99 |
| writer | INT-母部屋(A3 Opt調べ) +1 / INT-空席 初回 +1・再調査 +1 / CHOICE-S6 observe +2 ※増分値は**PROVISIONAL（Tuning扱い）** |
| reader | S8 逆流強度Tier |
| effect | Tier: low(0-2) / mid(3-5) / high(6+) → S8の色抜け段階・率ジャンプ振幅・D-ANLOG残響レイヤ数。**閾値はPROVISIONAL** |
| write timing | 各Interaction/Choice完了時 |
| persistence | checkpoint |
| canon_status | 「observation高いほど逆流強」=CONFIRMED（v0.17 S8）/ 増分・閾値=CANDIDATE(Tuning) |
| unresolved | 増分表・閾値の実測調整（Phase 1 Playtest） |

---

## 3. mioTrust ⚠ 廃止を確定しない — 2案比較（DESIGN REVIEW REQUIRED）

**原本の問題**: `mioTrust=base` / `mioTrust±` の増分量が全箇所未定義。S3/S6 の `Flag Read: mioTrust` は読取効果が未定義（デッドリード疑い）。書込タイミングも揺れ（D-AUNT-NAME時 vs 玄関退出時）。一方、原本の MIO BOND TRACE 原則は「大分岐・好感度システムにしない。環境音・短い反応・配置差分として微弱に返る程度」。

### A案: 数値信頼度（mioTrust を int として整備）

- `base=1` 起点、MIO-A/B/C・選択肢で ±1、閾値で後半の微小variantを切替
- 長所: 原本のフラグ名・表記をそのまま維持。将来の段階的variantに拡張余地
- 短所: 増分・閾値・読取効果の**全定義を新規に起こす必要**があり、その定義自体がCanonにない。「好感度システムにしない」原則と運用上衝突しやすい（数値がある限り攻略値化する）

### B案: MIO BOND TRACE bool群（mioBond）

- `mioBond.detour`（MIO-A寄り道）/ `mioBond.waited`（MIO-B待つ）の bool 記録。各bool→後半の痕跡1点（台詞variant 1行・配置差分1点）に1:1対応
- MIO-C（ただ座る）はNatural BeatとしてCritical Routeで必ず通過するためフラグ化しない
- 長所: MIO BOND TRACE原則を型で強制（数値化・閾値化が構造的に不可能）。デッドリード問題が消える。定義量最小
- 短所: 原本のフラグ名から変わる。3段階以上の濃淡表現は不可

### 比較と扱い

| 観点 | A案 int | B案 bool群 |
|---|---|---|
| 原本原則（好感度化しない）との整合 | △ 運用規律頼み | ◎ 構造保証 |
| 未定義箇所の追加定義量 | 多（増分・閾値・全読取効果） | 少（痕跡2点のみ） |
| 原本表記との連続性 | ◎ | △ 改名 |
| CH02拡張 | ○ | ○（bool追加で対応） |

**状態: DESIGN REVIEW REQUIRED — 本Registryでは決定しない。** 裁定までの実装影響: S9/S10の痕跡variant（微小）のみで、Main Route進行には無関係。どちらの案でも S3/S6 のデッドリードは「削除」または「読取効果の新規定義」の裁定が必要。

| 項目 | 内容 |
|---|---|
| name | `mioTrust`（A案）/ `mioBond.*`（B案） |
| layer | impl / persistence: checkpoint |
| writer | A案: D-AUNT-NAME完了時=base、MIO-A/B・CHOICE-S6で± / B案: MIO-A完了時 detour=true、MIO-B待機成立時 waited=true |
| reader | S9待つ選択のvariant・S10配置差分（両案共通の痕跡先） |
| write timing | Dialogue/Event完了時（玄関退出時書込は両案とも廃止） |
| canon_status | MIO BOND TRACE原則=CONFIRMED / データモデル=**DESIGN REVIEW REQUIRED** |
| unresolved | 案の選定・S3/S6デッドリードの処置 |

---

## 4. mioNameStability

| 項目 | 内容 |
|---|---|
| name | `mioNameStability` |
| layer | impl / type: enum `{unstable, high, restored}` / initial: `unstable` |
| writer | D-NAME1完了時→`high`（**書込タイミング裁定: S4遷移時ではなく台詞完了時**）/ EVT-CALLOUT→`restored` |
| reader | S3 ベンチ付近の環境音減衰演出 / S11 EVT-CALLOUT-YES前提条件 |
| effect | 呼びかけによる一時安定→回復の状態表現 |
| write timing | Dialogue/Event完了時 |
| persistence | checkpoint |
| canon_status | 状態遷移=CONFIRMED / enum値名=CANDIDATE |
| unresolved | なし |

## 5. anlogPressure

| 項目 | 内容 |
|---|---|
| name | `anlogPressure` |
| layer | impl / type: enum `{none, high}` / initial: `none` |
| writer | EVT-ANLOG-BACKFLOW→`high` |
| reader | S9 CHOICE_LOOP中の背景演出強度（observation Tierと併用） |
| effect | 逆流状態の有無。強度の段階は observation 側で持つ（二重管理しない） |
| write timing | Event完了時 / persistence: checkpoint |
| canon_status | CONFIRMED（原本S8 Flag Write準拠） |
| unresolved | なし |

## 6. fragmentCount

| 項目 | 内容 |
|---|---|
| name | `fragmentCount` |
| layer | impl / type: int / initial: 0 / range: 0〜9 |
| writer | INT-空席 再調査 +1（S5） |
| reader | S7再構成（**CD-13 UNDECIDED・S7未実装のため現行読者なし=休眠**）/ `uiRecordRateLabel.corrupted_up` 導出 |
| effect | 断片蓄積。Prototypeでは表示導出のみに寄与 |
| write timing | Interaction完了時 / persistence: checkpoint |
| canon_status | 書込=CONFIRMED / 読取=UNDECIDED（CD-13連動） |
| unresolved | S7採否（上位決裁）。**書込は実装する**（採否どちらでも無害） |

## 7. playerChoseNotToLook

| 項目 | 内容 |
|---|---|
| name | `playerChoseNotToLook` |
| layer | impl / type: bool / initial: false |
| writer | CHOICE-S6 avoid/wait / CHOICE-S9 見ない |
| reader | CH01内読者なし（CH02持ち越し・記録のみ） |
| write timing | Choice確定時 / persistence: checkpoint |
| canon_status | CONFIRMED（Story状態候補として原本明示） |
| unresolved | CH02での用途未定義（CH02仕様側の宿題） |

## 8. mioVoluntarySpeech

| 項目 | 内容 |
|---|---|
| name | `mioVoluntarySpeech` / layer: impl / type: bool / initial: false |
| writer | EVT-CALLOUT（ミオが自発的に応答した事実） |
| reader | CH01内読者なし（CH02持ち越し） |
| write timing | Event完了時 / persistence: checkpoint |
| canon_status | CONFIRMED / unresolved: CH02用途未定義 |

## 9. relationAnchor

| 項目 | 内容 |
|---|---|
| name | `relationAnchor` / layer: impl / type: bool / initial: false |
| writer | CHOICE-S9 聞く/待つ/手を取る（マイクロフィードバック時）/ EVT-CALLOUT |
| reader | S11 EVT-CAPTURE前提条件（原本SECTION 4準拠） |
| write timing | Choice/Event完了時 / persistence: checkpoint |
| canon_status | CONFIRMED |
| unresolved | S9で「名を呼ぶ」に一直線で到達した場合もEVT-CALLOUTで立つため、前提条件として実質常時成立。**前提条件として意味を持たせるか、記録専用に格下げするかは実装時に確認**（挙動には影響なし） |

## 10〜12. Story状態（canon明示・write-once）

| name | writer | reader | persistence | canon_status |
|---|---|---|---|---|
| `observer_is_tou` | EVT-CAPTURE | CH02 | permanent | CONFIRMED |
| `mio_carried_lost` | EVT-CAPTURE | EVT-SENDER-INVERT前提条件 / CH02 | permanent | CONFIRMED |
| `notification_sender_inverted` | EVT-SENDER-INVERT | CH02 | permanent | CONFIRMED |

共通: layer=story / type=bool / initial=false / write timing=Event完了時 / **一度trueにしたら変更禁止** / unresolved: なし。

## 13. worldKnowledge

| 項目 | 内容 |
|---|---|
| name | `worldKnowledge` |
| 状態 | **実装しない** |
| 根拠 | 原本v0.17自身が「worldKnowledge=partial は実装変数として未決扱い。S10縮退を理由にCanon化しない」と明記（SECTION 1 S10 / SECTION 10） |
| 代替 | S10の「一部理解」はS8-S9の操作体験＋S11観測点示唆で成立させる（フラグ不要） |
| canon_status | UNDECIDED（実装対象外として凍結） |
| unresolved | なし（上位でCanon化されない限り着手しない） |

---

## 14. 監査サマリ

| フラグ | 型監査 | 状態 |
|---|---|---|
| whiteLayerProgress | ⚠ 型混在 → enum化2案提示 | DESIGN REVIEW REQUIRED（推奨B案） |
| observation | int・閾値定義済（PROVISIONAL） | 実装可 |
| mioTrust | ⚠ 増分未定義・デッドリード → 2案提示 | DESIGN REVIEW REQUIRED |
| mioNameStability | enum化・書込タイミング裁定済 | 実装可 |
| anlogPressure | enum化 | 実装可 |
| fragmentCount | int・休眠読者 | 実装可（書込のみ） |
| playerChoseNotToLook / mioVoluntarySpeech / relationAnchor | bool | 実装可（CH02用途は未定義） |
| story 3種 | bool write-once | 実装可 |
| worldKnowledge | — | 実装しない |
