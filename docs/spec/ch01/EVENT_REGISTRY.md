# EVENT_REGISTRY — CH01 主要イベント定義

**Status**: v1.1 正規化ドラフト（実装準備・コード未着手）
**Source**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md` SECTION 4 / §17B / §17C
**共通注記**:
- **座標・Collision shape・Trigger形状は全イベントで UNDETERMINED（IMAGE-02待ち）**。本Registryで推測しない。
- 時計塔内部を使うイベントは作らない（U-004）。金魚/水槽は登場させない。
- Flag名は `FLAG_REGISTRY.md` を正とする。whiteLayer系はenum案未決のため本文では「白層状態」と記述し、値は確定表記しない。
- `Save allowed?` は D9候補（チェックポイント方式・**未確定**）を前提とした暫定判断。

---

## EVT-OPENING

| 項目 | 内容 |
|---|---|
| Event ID | EVT-OPENING |
| Scene | S0 |
| Area | 導入（滲んだ白い場）— **ASSUMPTION**（canon未指定） |
| Trigger | New Game |
| Preconditions | なし |
| Player State Before | 中央（spawn PROVISIONAL）/ Facing 正面 |
| NPC State Before | ミオ=正面近距離。トウを見て少し笑ってから謝る |
| Control Before | LOCKED |
| Control During | LOCKED（Enter送りのみ） |
| Dialogue | D-FORGET★ |
| Interaction | なし |
| UI | セーブUIが滲む |
| Sound | 環境音が引く → 無音の後に一言 |
| Camera | FIXED（VN寄り） |
| World Mutation | 画面が白く滲む。予告のみ（本編は平常へ） |
| Flag Read | — |
| Flag Write | 白層状態=導入の滲み（値はenum案未決） |
| Resume Control | 導入終了時にS1へ（S1開始でUNLOCKED） |
| Exit Condition | 導入演出終了 |
| Next | S1 |
| Save allowed? | No（導入演出中） |
| Replay allowed? | No（New Game時のみ） |
| canon_status | 台詞・機能=CONFIRMED / ロケ=ASSUMPTION / spawn=PROVISIONAL |

---

## EVT-1717

| 項目 | 内容 |
|---|---|
| Event ID | EVT-1717 |
| Scene | S4 |
| Area | C / C2（時計塔前ベンチ）— CONFIRMED |
| Trigger | Narrative Clock 条件充足（`NARRATIVE_CLOCK.md` §2）。**実時間時計ではない** |
| Preconditions | S3滞在中 / D-NAME1完了 / MIO-C完了 |
| Player State Before | C2ベンチ付近・UNLOCKED |
| NPC State Before | ミオ=隣。端末を見て静かになる |
| Control Before | UNLOCKED |
| Control During | UI_LOCK（通知オーバーレイ操作のみ。Map保持） |
| Dialogue | D-BLANK★ |
| Interaction | INT-通知 |
| UI | スマホ通知オーバーレイ。本文空白・既読のみ。記録率ラベルが欠損（--%・**名称判読不能**） |
| Sound | 通知後に環境音-1段 |
| Camera | FIXED（端末寄り） |
| World Mutation | UI変質の始まり。「白層化率」の名称はまだ出さない（S8で初判読） |
| Flag Read | Narrative Clock条件（D-NAME1完了 / MIO-C完了） |
| Flag Write | 白層状態=17:17後 |
| Resume Control | 通知closeで **UNLOCKED**（自動でS5へ遷移しない） |
| Exit Condition | 通知を閉じる |
| Next | S5（プレイヤー自身が5席目へ接近して開始） |
| Save allowed? | 通知close後のUNLOCK区間で可 |
| Replay allowed? | No（1章1回） |
| canon_status | CONFIRMED（§17D-1: 旧「17:17で白層化率へ変わる」表記は廃止済み） |
| Causality | 環境音の変質(WORLD) → 「送った覚えはない」(SUSPICION) → UIラベル欠損(UI)。**UIが先に告知しない** |

---

## EVT-EMPTYSEAT

| 項目 | 内容 |
|---|---|
| Event ID | EVT-EMPTYSEAT |
| Scene | S5 |
| Area | C / C2（4席+5席目の跡）— CONFIRMED（教室/学校案は削除済み・STALE CANON） |
| Trigger | INT-空席の調査（プレイヤー自身の接近＋調べる） |
| Preconditions | EVT-1717完了 |
| Player State Before | ベンチ前・UNLOCKED |
| NPC State Before | ミオ=5席目側を見る。「五つ目」を指す |
| Control Before | UNLOCKED |
| Control During | 調査中のみ短時LOCK |
| Dialogue | D-5TH★ |
| Interaction | INT-空席（1回目=跡/影 / 再調査=「ミオにだけ、そこは空いている」） |
| UI | 調査プロンプト。再調査時に欠損ラベルが微増（--%↑・名称は依然判読不能） |
| Sound | 剥落音（紙から文字を剥がす音） |
| Camera | 調査時ズーム |
| World Mutation | 顕在化のみ（世界は変化しない） |
| Flag Read | 白層状態 |
| Flag Write | 白層状態=白層化↑ / fragmentCount+（再調査）/ observation+ |
| Resume Control | 調査後 UNLOCKED（**即Choice UIを出さない**・一拍の余白） |
| Exit Condition | 調査完了＋余白経過 |
| Next | S6 |
| Save allowed? | 調査後のUNLOCK区間で可 |
| Replay allowed? | 再調査は可（fragment取得は上限あり・回数はTuning） |
| canon_status | CONFIRMED |

---

## EVT-ANLOG-BACKFLOW

| 項目 | 内容 |
|---|---|
| Event ID | EVT-ANLOG-BACKFLOW |
| Scene | S8 |
| Area | C / C2 — **ASSUMPTION** |
| Trigger | S8開始（S6完了後。S7はUNDECIDEDのためPrototypeでは経由しない） |
| Preconditions | S6完了 |
| Player State Before | ミオ正面 |
| NPC State Before | ミオ=中心。苦しむ/抗う。輪郭から色が抜けはじめる |
| Control Before | UNLOCKED（S6選択直後） |
| Control During | OPENING_LOCK → PARTIAL_UNLOCK_PROBE（操作試行）→ 短時LOCK（気づき/UI）※詳細 `CONTROL_GATE_SPEC.md` §3 |
| Dialogue | D-ANLOG★ / D-STOP / S8操作試行フィードバック行 |
| Interaction | 操作試行（移動する/触れる/追跡する/記録する）＝**すべて悪化**。呼びかけは含めない（3原則②） |
| UI | 欠損ラベルが**ここで初めて**「白層化率」として判読可能に＋急伸 |
| Sound | 剥落音の重畳 → 呼びかけ前の無音準備 |
| Camera | FIXED（演出） |
| World Mutation | 因果反転（観測=白層化）の顕在化。色抜け進行 |
| Flag Read | observation（Tierで逆流強度を決定） |
| Flag Write | 白層状態=逆流中 / anlogPressure=high |
| Resume Control | S9でPARTIAL→CHOICE_CONTROLへ |
| Exit Condition | REALIZATION到達（Requirement: 最低1回の観測操作→悪化の体験。回数・timeoutはTuning） |
| Next | S9 |
| Save allowed? | **No**（演出・逆流の連続性を切らない） |
| Replay allowed? | No |
| canon_status | CONFIRMED（§17D-2: 旧「全面LOCKED」表記は廃止済み） |
| Causality | 操作のたび色が抜ける(WORLD) → 「ぼくが見たから」(SUSPICION・自分で到達) → 白層化率 初判読+急伸(UI) |

---

## EVT-CALLOUT

| 項目 | 内容 |
|---|---|
| Event ID | EVT-CALLOUT |
| Scene | S9 |
| Area | C / C2 — **ASSUMPTION** |
| Trigger | CHOICE-S9で「名を呼ぶ」を選択 |
| Preconditions | 逆流ピーク（anlogPressure=high） |
| Player State Before | 正面近接 |
| NPC State Before | ミオ正面・逆流に耐える |
| Control Before | CHOICE_CONTROL |
| Control During | **CALLOUT_CONTROL**（呼びかけ入力のみ受付。具体的入力方式は**UNDECIDED**） |
| Dialogue | トウ「ミオ」→ ミオ「…今の、ちゃんと、私だった」（D-NAME2★） |
| Interaction | なし |
| UI | 呼びかけ入力UI（**方式未決**。S9/S11で同一操作であることのみRequirement） |
| Sound | 呼びかけ後に他音がすべて引く → 無音 → ミオの声だけ残す |
| Camera | FIXED（顔） |
| World Mutation | 一時的に固定が解ける（輪郭が戻る） |
| Flag Read | anlogPressure / observation |
| Flag Write | mioNameStability=restored / mioVoluntarySpeech / relationAnchor /（該当時）playerChoseNotToLook |
| Resume Control | 成立後 S10 で UNLOCKED |
| Exit Condition | 呼びかけ成立（応答受領） |
| Next | S10 |
| Save allowed? | No（S10のUNLOCK区間で可） |
| Replay allowed? | No |
| canon_status | 機能・台詞=CONFIRMED / 入力方式=**UNDECIDED** |
| 原則 | 3原則②: 呼びかけは観測と別系統。成功する理由は「相手自身の応答を待つ行為」だから |

---

## EVT-CAPTURE

| 項目 | 内容 |
|---|---|
| Event ID | EVT-CAPTURE |
| Scene | S11 |
| Area | C / C2 — **ASSUMPTION** |
| Trigger | S11の呼びかけ成立直後（EVT-CALLOUT-YES: トウ「ミオ」→ ミオ「はい」★） |
| Preconditions | relationAnchor成立 / mioNameStability=restored |
| Player State Before | ベンチ（C2） |
| NPC State Before | ミオ=応え、一度「自分」に戻る（輪郭が鮮明に）/ 記憶局=C入口から接近 |
| Control Before | CALLOUT_CONTROL |
| Control During | **LOCKED（介入不可）** |
| Dialogue | 記憶局=最小（「……保護のため、です。」のみ。多くを語らない） |
| Interaction | なし（連れ去り後にINT-ベンチが空席化） |
| UI | carried.lost（灰スロット＝不可逆の喪失） |
| Sound | 「はい」で他音消失 → 連れ去りの静けさ → 無音の余韻 |
| Camera | FIXED（顔 → 一瞬の回復 → 介入 → 空席 → 塔） |
| World Mutation | 連れ去り / ベンチ空席化 / 夜へ / 塔の意味が変わる |
| Flag Read | mioNameStability / relationAnchor |
| Flag Write | 白層状態=連れ去り後 / observer_is_tou=true / mio_carried_lost=true |
| Resume Control | 連れ去り完了後 **必ずC2をUNLOCK**（再解釈のため。§17C） |
| Exit Condition | 連れ去り演出完了 |
| Next | UNLOCK_REINTERPRET区間 → EVT-SENDER-INVERT |
| Save allowed? | No（直後のUNLOCK_REINTERPRET区間で可） |
| Replay allowed? | No |
| canon_status | 連れ去りの事実=CONFIRMED / 見せ方(明示/示唆)=演出調整範囲 / 介入機序=**CANDIDATE・DESIGN INTERPRETATION** |
| 原則 | 3原則③: 呼びかけが連れ去りの原因とは断定しない。「制度が回復を検知→介入」は上位canon根拠なし。露骨な暴力描写は避ける。時計塔内部は使わない（U-004） |

---

## EVT-SENDER-INVERT

| 項目 | 内容 |
|---|---|
| Event ID | EVT-SENDER-INVERT |
| Scene | S11 |
| Area | C / C2・UI — **ASSUMPTION** |
| Trigger | EVT-CAPTURE後 **かつ** 連れ去り後C2の再解釈を1回以上完了（§17C・**回数はTuning**） |
| Preconditions | mio_carried_lost=true |
| Player State Before | ベンチ（空席横）・UNLOCKED（再解釈中） |
| NPC State Before | 不在（完全無人） |
| Control Before | UNLOCK_REINTERPRET |
| Control During | UI_LOCK（モノローグ） |
| Dialogue | D-END★（通知「次回観測予定：明日17:17」/ 独白「送った覚えは、なかった。でも、既読だけは付いていた。」） |
| Interaction | INT-通知端末（送信者反転表示） |
| UI | 通知の送信者が ミオ→トウ に反転表示 |
| Sound | 無音の余韻 |
| Camera | FIXED（端末 → トウ） |
| World Mutation | 送信者反転（観測点=トウの示唆） |
| Flag Read | mio_carried_lost |
| Flag Write | notification_sender_inverted=true |
| Resume Control | CH02接続 |
| Exit Condition | モノローグ終了 |
| Next | CH02「未記録／記録されない街」 |
| Save allowed? | Yes（章末チェックポイント） |
| Replay allowed? | No |
| canon_status | CONFIRMED（§17D-3: 旧「連れ去り→即モノローグ→通知」は廃止済み。**連れ去り直後に自動で被せない**） |

---

## 付記: EVT-RECONSTRUCT（S7）

**UNDECIDED（CD-13）。Prototypeでは実装しない。** S6→S8を前提とする。機構・台詞・報酬・トリガー・Flag効果はすべて未決であり、本Registryで定義しない。採否裁定が出た時点で本Registryに追加する。

## 付記: EVT-DISCLOSURE（S10）

**S10の必須Eventとして使用しない**（v0.10でTransition Beatへ縮退済み）。S10は独立Disclosure Eventを新設せず、UNLOCK余韻＋D-5TH-TRUTH-SHORTで成立させる。
