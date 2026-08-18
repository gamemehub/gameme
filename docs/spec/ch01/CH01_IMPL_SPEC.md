# CH01_IMPL_SPEC — CH01 実装用シングルレイヤー仕様（正本）

**Status**: v1.1 正規化ドラフト — **実装未着手 / Lock前**
**Source**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md`（凍結原本）
**Runtime Target**: Godot（既存Web版は legacy / reference。実装先にしない）

## 0. この文書について

- 原本の積層構造（監査・改訂履歴）から **現行仕様のみ** を抜き出した実装用シングルレイヤー。superseded な旧仕様は本書に残さない。
- 監査履歴・旧バージョン比較・レビュー履歴は `AUDIT_HISTORY.md` に分離。原本全文は `source/` に凍結。
- 確定度タグ: **CONFIRMED**（canon）/ **CANDIDATE**（設計案）/ **ASSUMPTION**（canon未指定・確定しない）/ **UNDECIDED**（上位未決）/ **PROVISIONAL**（仮置き値）/ **DESIGN REVIEW REQUIRED**（実装前に人間裁定が必要）
- **本書は実装開始の許可を与えるものではない**。ブロッカーは §7 を参照。

### 関連文書

| ファイル | 役割 |
|---|---|
| `FLAG_REGISTRY.md` | フラグ台帳・型監査（whiteLayerProgress / mioTrust の案比較を含む） |
| `EVENT_REGISTRY.md` | イベント定義（7イベント） |
| `CONTROL_GATE_SPEC.md` | Control State / Gate / S8・S9 State Machine |
| `NARRATIVE_CLOCK.md` | 17:17 仕様（イベント駆動案） |
| `TUNING.md` | 調整値一覧（Canonと分離） |
| `CANON_DEPENDENCIES.md` | 依存文書一覧・MISSING判定 |
| `CANON_SNAPSHOT.md` | canon事実・禁止事項の抜き書き |
| `AUDIT_HISTORY.md` | 監査・改訂履歴（正本から分離） |

## 1. 横断制約（Canon・全実装判断に適用）

1. **WORLD → SUSPICION → UI**: 世界の異変が先、疑念が次、UIの追認が最後。UIが先に答えを言わない。
2. **OBSERVATION ≠ CALLOUT**: 一方的に相手を確定しようとする操作（調べる/触れる/追跡する/記録する/問い詰める）＝観測＝悪化。名を呼び本人の応答を待つ＝呼びかけ＝別系統。**呼びかけを悪化動詞リストに入れない**。
3. **CALLOUT SUCCESS ≠ CAPTURE CAUSE**: S11の連れ去りと呼びかけ成功の因果を断定しない。
4. **Canon Guard**: 金魚/水槽/水槽音/「記録されない小さな命」＝**非採用・復活禁止**。時計塔=Landmarkのみ、**内部Event追加禁止**（U-004）。ノア開示は場所非依存で最小（D-NOAHは必須から除外・保留）。
5. **言ってはいけない（全Scene共通）**: 記憶局全貌 / アンログ思想 / 白層科学 / 未来のトウ / 母の保存詳細 / ミオ=鍵・原型 / 時計塔の内部・分類・鐘 / 金魚。
6. **MIO BOND TRACE**: MIO-A/B/C の経験有無は微小な痕跡（環境音・短い反応・配置差分）としてのみ返す。**大分岐・好感度システムにしない**。
7. **Engagement Gate**: PASSIVEが2シーン以上連続しないこと（S0=P / S1=A / S2=A / S3=R / S4=R / S5=A / S6=A / S8=R / S9=A / S10=R / S11=R）。

## 2. 前提（今回の作業前提として確認済み）

| 項目 | 状態 |
|---|---|
| Runtime Target | Godot（CONFIRMED as project decision） |
| 既存Web版 | legacy / reference。実装先にしない |
| S7 再構成 | **UNDECIDED**。Prototypeは S6→S8 を前提とし、採用・実装しない |
| CALLOUT 入力方式 | **UNDECIDED**。S9/S11で「同一操作を使う」ことのみ Requirement |
| mioTrust 等のデータモデル | **DESIGN REVIEW REQUIRED**（`FLAG_REGISTRY.md`で候補比較） |
| 秒数・歩数・回数 | Canon化せず `TUNING.md` へ分離 |
| Map座標 / IMAGE-01・02 | 別工程。推測で埋めない |

---

## 3. SCENE SPEC（S0〜S11・現行仕様のみ）

各Sceneの記載順: Area/Zone → World State → Entry Condition → Required Action → Optional Action → Dialogue ID → Interaction ID → Event ID → Control State → Gate → Flag Read → Flag Write → World Change → Exit Condition → Next Scene

> Flag名は `FLAG_REGISTRY.md` を正とする。白層状態フラグは enum 案が未決のため、本書では値を確定表記せず状態名で記す。

### S0 — 冒頭フック：ミオに忘れられる

| 項目 | 内容 |
|---|---|
| Area / Zone | 導入（滲んだ白い場）/ — — **ASSUMPTION** |
| World State | 滲みSave（不在の予告） |
| Entry Condition | New Game |
| Required Action | 台詞送り（Enter） |
| Optional Action | なし |
| Dialogue ID | D-FORGET★ |
| Interaction ID | なし |
| Event ID | EVT-OPENING |
| Control State | LOCKED（導入演出） |
| Gate | なし |
| Flag Read | — |
| Flag Write | 白層状態=導入の滲み |
| World Change | 画面が白く滲む。予告のみ（本編は平常へ） |
| Exit Condition | 導入演出終了 |
| Next Scene | S1 |
| WHY | 章の核（忘れられる恐怖＝受動的喪失）を最初に一度だけ提示。S11の構造的喪失とは異なる痛み |

### S1 — 朝：叔母との日常（トウの家）

| 項目 | 内容 |
|---|---|
| Area / Zone | A / A1自室・A2居間台所・A3母の部屋+玄関 — CONFIRMED |
| World State | 平常（塔=窓から遠景Partial） |
| Entry Condition | S0終了。Entry spawn=A1ベッド脇（**PROVISIONAL**）/ Facing=下 |
| Required Action | A2で叔母に話す（D-AUNT-WAIT / D-AUNT-NAME）→ 玄関から外へ |
| Optional Action | A1ベッド・私物 / A2カップ・修繕跡・叔母再会話 / A3戸・花・室内 / 窓（塔遠景） |
| Dialogue ID | D-AUNT-WAIT / D-AUNT-NAME★ / D-AUNT-FLOWER(Opt) |
| Interaction ID | INT-エプロン / INT-母部屋(Opt) / INT-花(Opt) / INT-扉(Opt) / 窓(Opt) |
| Event ID | なし |
| Control State | UNLOCKED（移動/調べ習得・初自由操作）/ Camera=FIXED（屋内） |
| Gate | **G1**: 叔母会話前の玄関 → ソフトブロック（`CONTROL_GATE_SPEC.md` §5） |
| Flag Read | — |
| Flag Write | observation+（A3 Opt調べ）/ ミオ関係フラグ=**DESIGN REVIEW REQUIRED**（`FLAG_REGISTRY.md` §3） |
| World Change | なし（母の部屋だけ音がない） |
| Exit Condition | 玄関を出る |
| Next Scene | S2 |
| WHY | 私的空間で操作を教えつつ、母の不在を空間で提示。「待つ」「名前」を日常語として先置き |

### S2 — 帰り道：時計塔へ寄る理由（坂道）

| 項目 | 内容 |
|---|---|
| Area / Zone | B / B1坂上・B2生活圏・B3坂下（広場口）— CONFIRMED |
| World State | 平常（塔=近づくFull） |
| Entry Condition | S1終了。Entry spawn=B1坂上（**PROVISIONAL**）/ Facing=下 |
| Required Action | B3坂下（広場口）へ歩く |
| Natural（主動線・LOCKなし） | P01店先（視界通過）/ P02 掃除の住人（すれ違い1行）/ **P04 MIO-B「待つ」**（移動で成立）/ P07 時計塔Reveal（強制Camera Panなし） |
| Optional Action | P03掲示 → P06表記のズレ（Optional Pocket）/ P05 MIO-A猫の寄り道（**CANDIDATE**）/ 生活物Inspect / 住人への任意会話・再会話 |
| Dialogue ID | D-5MIN / D-WAIT(MIO-B) / NPC-B2-AMBIENT-01 / 塔Reveal会話 / D-DETOUR(MIO-A・Opt) |
| Interaction ID | INT-B2-SHOPFRONT / INT-B2-NOTICE / INT-B2-MISMATCH（**すべてImplementation Candidate ID**・Canon IDではない） |
| Event ID | なし |
| Control State | UNLOCKED（同行移動）/ Camera=FOLLOW（屋外2x）/ **会話で歩行を止めない** |
| Gate | なし（B3到達で自然遷移） |
| Flag Read | — |
| Flag Write | ミオ関係フラグ（MIO-A/B痕跡）=**DESIGN REVIEW REQUIRED** |
| World Change | なし |
| Exit Condition | B3出口（P08）到達 |
| Next Scene | S3 |
| WHY | 移動を「一緒にいて楽しい＋理由の言えない癖」に使い、塔へ自然誘導。謎の前に愛着を操作で成立させる |

### S3 — 時計塔前のベンチ（座りたがる理由）

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C1入口・C2ベンチ — CONFIRMED |
| World State | 平常（塔=直近Full） |
| Entry Condition | S2終了。Entry spawn=C1入口（**PROVISIONAL**）/ Facing=上 |
| Required Action | ベンチを調べる/隣に座る → **MIO-C「ただ座る」Natural Beat通過** → D-QUIET → D-NAME1（名前の実演） |
| Optional Action | 塔を見上げる（内部非開示・U-004） |
| Dialogue ID | D-BENCH1 / MIO-C（ただ座る）/ D-QUIET / D-NAME1★ |
| Interaction ID | INT-ベンチ / INT-時計塔(Opt) |
| Event ID | なし |
| Control State | UNLOCKED（MIO-C中もUNLOCK維持・ムービーLOCKにしない）→ 軽微FIXED（会話） |
| Gate | **G2**: 17:17前のArea C離脱 → ソフトブロック |
| Flag Read | ミオ関係フラグ（**読取効果が未定義＝DESIGN REVIEW REQUIRED**） |
| Flag Write | mioNameStability=high（**D-NAME1完了時**。S4遷移時ではない） |
| World Change | なし（ベンチ付近だけ音が薄い） |
| Exit Condition | Narrative Clock条件充足（`NARRATIVE_CLOCK.md` §2.2） |
| Next Scene | S4 |
| WHY | 呼びかけ（名→安心）を早期に実演＝後の攻略反転の伏線。塔を「意味の器」として提示 |

### S4 — 17:17 の空白メッセージ

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2 — CONFIRMED |
| World State | UI変質の始まり |
| Entry Condition | S3滞在中に Narrative Clock 条件充足（D-NAME1完了 ∧ MIO-C完了 ∧ C2滞在 ∧ アイドル[Tuning]） |
| Required Action | 通知を開く → 閉じる |
| Optional Action | 二番目の席の再調査（State variant） |
| Dialogue ID | D-BLANK★ |
| Interaction ID | INT-通知 |
| Event ID | EVT-1717 |
| Control State | UNLOCKED → **UI_LOCK**（通知表示中）→ **UNLOCKED**（自動でS5へ遷移しない） |
| Gate | **G3**: S4→S5 は Player入力必須（自動吸着禁止） |
| Flag Read | Narrative Clock条件 |
| Flag Write | 白層状態=17:17後 |
| World Change | 記録率ラベルが欠損（--%）。**「白層化率」の名称はまだ出さない**（S8で初判読） |
| Exit Condition | 通知を閉じ、プレイヤー自身が5席目へ接近 |
| Next Scene | S5 |
| Causality | 環境音の変質(WORLD) → 「送った覚えはない」(SUSPICION) → UIラベル欠損(UI) |

### S5 — 空いている席の違和感（5席目）

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2（4席+5席目の跡）— CONFIRMED（教室/学校案は削除済み・上位canon残存は STALE CANON CANDIDATE） |
| World State | 白層化↑ |
| Entry Condition | S4終了後、5席目付近へ接近 |
| Required Action | 5席目の跡/影を調べる（1回目） |
| Optional Action | 再調査（fragment示唆）／観測因果チェーン（既調査物の微変化・欠損ラベル微増） |
| Dialogue ID | D-5TH★ |
| Interaction ID | INT-空席 |
| Event ID | EVT-EMPTYSEAT |
| Control State | UNLOCKED → 調査中のみ短時LOCK → UNLOCKED（**即Choice UIを出さない**） |
| Gate | **G4**: S5→S6 は調査後に一拍の余白（尺はTuning） |
| Flag Read | 白層状態 |
| Flag Write | 白層状態=白層化↑ / fragmentCount+（再調査）/ observation+ |
| World Change | なし（顕在化のみ） |
| Exit Condition | 調査完了＋余白経過 |
| Next Scene | S6 |
| WHY | 「調べる」行為を恐怖と結び、後の「観測=加害」の伏線に |

### S6 — 最初の選択肢

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2 — CONFIRMED |
| World State | 分岐点 |
| Entry Condition | S5終了 |
| Required Action | CHOICE-S6（intent: observe / avoid / ask / wait） |
| Optional Action | なし |
| Dialogue ID | CHOICE-S6（各intentの短い前置き＋1リアクション） |
| Interaction ID | なし |
| Event ID | なし |
| Control State | **CHOICE_CONTROL**（Player Decision State。演出LOCKではない） |
| Gate | 選択確定で進行 |
| Flag Read | observation / ミオ関係フラグ（**読取効果が未定義＝DESIGN REVIEW REQUIRED**） |
| Flag Write | observation±（observe）/ playerChoseNotToLook（avoid・wait）/ ミオ関係フラグ=**DESIGN REVIEW REQUIRED** |
| World Change | 分岐フラグ |
| Exit Condition | 選択確定 |
| Next Scene | **S8**（S7は UNDECIDED のため Prototype では経由しない） |
| WHY | 「観測/回避/問い/待つ」を最初に手に取らせ、後半の攻略反転へ接続 |

### S7 — 再構成モード（**UNDECIDED / CD-13**）

| 項目 | 内容 |
|---|---|
| 状態 | **UNDECIDED。Prototypeでは採用・実装しない。S6→S8 を前提とする** |
| Area / Zone | 場所非依存（再構成UI/心象）— **ASSUMPTION** |
| Entry Condition | 再構成モード採用時のみ（採用条件も未決） |
| 定義済みの唯一の事実 | 未採用の場合 S7 をスキップし S6→S8 |
| その他全項目 | **UNKNOWN（未決）**。機構・台詞・報酬・Event・Flag効果を本書で定義しない |
| Next Scene | S8 |

### S8 — アンログ逆流

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2 — **ASSUMPTION** |
| World State | 逆流・因果反転の顕在化 |
| Entry Condition | S6終了（S7は経由しない） |
| Required Action | 逆流を見る＋**操作試行**（移動する/触れる/追跡する/記録する）。★**最低1回、観測操作→悪化の因果をプレイヤー自身が体験すること**（Requirement） |
| Optional Action | なし |
| Dialogue ID | D-ANLOG★ / D-STOP / 操作試行フィードバック行 |
| Interaction ID | なし（試行動詞はInteractではなくProbe操作） |
| Event ID | EVT-ANLOG-BACKFLOW |
| Control State | OPENING_LOCK → **PARTIAL_UNLOCK_PROBE** → 短時LOCK（`CONTROL_GATE_SPEC.md` §3） |
| Gate | **G5**: Requirement充足で REALIZATION → UI_REVEAL → S9（回数・timeoutはTuning） |
| Flag Read | observation（高いほど逆流強） |
| Flag Write | 白層状態=逆流中 / anlogPressure=high |
| World Change | 因果反転（観測=白層化）。**欠損ラベルがここで初めて「白層化率」として判読可能に**＋急伸 |
| Exit Condition | REALIZATION到達 |
| Next Scene | S9 |
| 原則 | 3原則②適用。呼びかけを悪化動詞に入れない |

### S9 — 逆流中の選択肢（呼びかけ）

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2 — **ASSUMPTION** |
| World State | 因果反転 |
| Entry Condition | S8終了 |
| Required Action | CHOICE-S9 → **呼びかけ（名を呼ぶ）** |
| Optional Action | 見ない / 聞く / 待つ / 手を取る（**正の別解**。失敗扱いにせず、反応後に選択へ戻れる） |
| Dialogue ID | D-NOLOOK / CHOICE-S9 / D-NAME2★ |
| Interaction ID | なし |
| Event ID | EVT-CALLOUT（名→応答） |
| Control State | **CHOICE_CONTROL** → **CALLOUT_CONTROL**（入力方式 **UNDECIDED**。S9/S11同一操作がRequirement） |
| Gate | **G6**: 呼びかけ成立で S10へ。S10で必ずControlを返す |
| Flag Read | anlogPressure / observation |
| Flag Write | mioNameStability=restored / mioVoluntarySpeech / relationAnchor /（該当時）playerChoseNotToLook |
| World Change | 一時的に固定が解ける（輪郭が戻る） |
| Exit Condition | 呼びかけ成立 |
| Next Scene | S10 |
| WHY | canon固有の「名→はい」を攻略に据え、「観測でなく本人の応答」というテーマを操作化する |

### S10 — 一部理解の余韻（Transition Beat）

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2周辺（塔は遠景Landmark）— **ASSUMPTION** |
| World State | 塔=Full/夕闇 |
| Entry Condition | S9成立 |
| Required Action | 数秒その場に留まり、ミオ/ベンチ/塔のいずれかを視界に入れる（強制READなし） |
| Optional Action | 塔を見上げる（内部に触れない）/ 二番目の席のState variant |
| Dialogue ID | D-5TH-TRUTH-SHORT（核のみ短く）/ **D-NOAH は必須から除外・CANDIDATE保留（実装しない）** |
| Interaction ID | INT-時計塔（遠景・内部非開示） |
| Event ID | なし（Transition。独立Disclosure Eventを新設しない） |
| Control State | **UNLOCKED**（余韻。強制VNにしない。尺はTuning） |
| Gate | 余韻経過＋短いミオ反応で S11へ |
| Flag Read | fragmentCount / mioNameStability |
| Flag Write | なし（`worldKnowledge` は**実装しない**・`FLAG_REGISTRY.md` §13） |
| World Change | 夕闇へ・塔のシルエット。S9後の無音から環境音が完全には戻らない |
| Exit Condition | 余韻終了 |
| Next Scene | S11 |
| WHY | S8-S9で操作から理解した内容をREADで再説明しない。説明増量禁止 |

### S11 — ラスト（観測点=トウ / 送信者反転 / 連れ去り）

| 項目 | 内容 |
|---|---|
| Area / Zone | C / C2（17:17）— **ASSUMPTION**（反復するベンチで閉じる） |
| World State | 喪失 |
| Entry Condition | S10終了 |
| Required Action | ①呼びかけ（名→「はい」）②**連れ去り後、ミオがいた位置（二番目の席/ベンチ）をプレイヤー自身が1回以上調べる** |
| Optional Action | ベンチ全体 / 時計塔 / 端末の再解釈 |
| Dialogue ID | 呼びかけ「ミオ」→「はい」★ / 記憶局=最小台詞 / D-END★ |
| Interaction ID | INT-ベンチ（空席化）/ INT-通知端末（反転） |
| Event ID | EVT-CALLOUT-YES → EVT-CAPTURE → EVT-SENDER-INVERT |
| Control State | CALLOUT_CONTROL → **LOCKED**（連れ去り・介入不可）→ **UNLOCKED**（C2再解釈）→ UI_LOCK（通知/終端） |
| Gate | **G7**: 必須再調査 完了まで EVT-SENDER-INVERT を発火しない（連れ去り直後に自動で被せない） |
| Flag Read | mioNameStability / relationAnchor |
| Flag Write | 白層状態=連れ去り後 / observer_is_tou / mio_carried_lost / notification_sender_inverted |
| World Change | 連れ去り・空席化・夜へ・塔の意味が変わる・送信者反転・carried.lost（灰スロット） |
| Exit Condition | 再解釈1回以上 → 通知反転 → モノローグ終了 |
| Next Scene | CH02「未記録／記録されない街」 |
| 原則 | 3原則③。介入機序（制度が回復を検知）は **CANDIDATE / DESIGN INTERPRETATION**。時計塔内部は使わない |
| S0↔S11 | 受動的喪失 ↔ 構造的喪失（呼ぶことは正しかった。それでも奪われた） |

---

## 4. Map / Area アンカー

| Area | Scene starts | Player stops | Dialogue fires | Interactable | Event locks | Next hook visible |
|---|---|---|---|---|---|---|
| A（家） | A1自室 | A2叔母前 / A3母の部屋前 | A2（D-AUNT-*） | A2エプロン(Req伏線) / A3母の部屋・花・扉(Opt) / 窓 | なし（自由探索） | 玄関 / 窓の塔遠景 |
| B（坂道） | B1坂上 | B3坂下（広場口） | B2（D-5MIN / MIO-B / Ambient NPC） | B2生活圏小物（Opt flavor） | なし | 坂の湾曲で塔が出現（B2） |
| C（塔前） | C1入口 | C2ベンチ | C2（D-BENCH1〜D-END） | C2ベンチ・5席目・通知端末 / 遠景で塔(Opt) | C2で EVT-1717 / ANLOG-BACKFLOW / CALLOUT / CAPTURE / SENDER-INVERT | 17:17通知 / 逆流 / 連れ去り後の空席と夜の塔 |

**座標・spawn・facing・Collision/Trigger形状は本書で確定しない（IMAGE-02待ち）。** 記載の spawn は原本の PROVISIONAL を転記したもの。

## 5. 未定義・要判断（実装ブロッカー）

| # | 項目 | 種別 | 状態 |
|---|---|---|---|
| B1 | 白層状態フラグの enum 設計（Scene-anchored / 意味状態の2案） | DESIGN REVIEW REQUIRED | `FLAG_REGISTRY.md` §1 |
| B2 | mioTrust のデータモデル（数値信頼度 / BOND TRACE bool群の2案）＋S3/S6デッドリードの処置 | DESIGN REVIEW REQUIRED | `FLAG_REGISTRY.md` §3 |
| B3 | CALLOUT 入力方式（S9/S11同一操作のみ確定） | UNDECIDED | UIUX仕様が未作成 |
| B4 | Narrative Clock（C案）の採用可否 | DESIGN REVIEW REQUIRED | `NARRATIVE_CLOCK.md` |
| B5 | S8 Probe の脱出条件値 / S9 再提示の有無 | Tuning + CANDIDATE | `TUNING.md` |
| B6 | Gate G1/G2 の文言（既存資産流用 or Implementation Dialogue Candidate 新規） | DESIGN REVIEW REQUIRED | 新規Canon台詞化は禁止 |
| B7 | S7 採否（CD-13） | UNDECIDED（上位） | Prototypeは S6→S8 |
| B8 | フラグの Canon 化（DL-Y3） | UNDECIDED（上位） | `impl.*` 隔離で待機 |
| B9 | セーブ方式（チェックポイント案） | CANDIDATE | 未確定 |
| B10 | 座標・Collision・Trigger形状・C2ゾーン範囲 | IMAGE-02待ち | 全Event |
| B11 | S0 / S8〜S11 のロケ確定 | ASSUMPTION | IMAGE-02 + 上位canon |
| B12 | 上位canonの学校/教室記述（STALE CANON） | GOVERNANCE FIX REQUIRED | `CANON_DEPENDENCIES.md` X1 |
| B13 | 依存文書の大半が MISSING / PATH NOT VERIFIED | 照合不能 | `CANON_DEPENDENCIES.md` |

## 6. 実装可否

**現時点で Godot 実装開始は不可**（`REVIEW_REPORT.md` 参照）。B1〜B4・B6 の裁定と、最低限 B10 の一部（Area C の座標）が揃うまで、Phase 1 灰箱の着手判断を行わない。

## 7. Changelog

- **v1.1（本ドラフト）**: 原本v0.17から現行仕様のみを抽出したシングルレイヤー版を作成。Scene毎に必須16フィールドを整備。監査履歴を `AUDIT_HISTORY.md` へ分離。mioTrust廃止・CALLOUT長押し・Narrative Clock を**確定扱いから候補（DESIGN REVIEW REQUIRED / UNDECIDED）へ格下げ**。Tuning値を `TUNING.md` へ分離。
