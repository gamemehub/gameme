<!-- FROZEN SOURCE — 編集禁止
  原本: Google Doc "CH01_DETAILED_SCRIPT_v0.9.md" (実体 Draft v0.17)
  docId: 1FvgHXhKvMzXPPA-GNH5KWizQS7GAEz0Hpck6pKFMNpE
  取得日: 2026-08-18 / 最終更新: 2026-08-16
  本ファイルは履歴凍結。正本は ../CH01_IMPL_SPEC.md（このリポジトリ）。
-->

# CH01 DETAILED SCRIPT（SCRIPT DRAFT・現行canon準拠）

Status: Draft v0.17（Critical Route Desk Read-through＋S4以降Control-State Gate反映）（FULL PLAYER PLAYTHROUGH追加・Area/会話/調査/選択を実プレイ順に統合・未commit） Updated: 2026-08-16 Basis(SSOT): DECISION\_REGISTER → UNDECIDED\_REGISTER → chapters/CH01\_DETAIL.md(12シーン)。台詞ドラフトの母体=Docs/CHAPTER01\_SCENARIO\_MASTER.md。 Companion: CH01\_SCENARIO\_MASTER.md(Part) / CH01\_GPT\_SCENARIO\_INPUT\_PACKAGE.md(canon入力) / CH01\_PREPRODUCTION\_DESIGN.md(map)。

  

**これは SCRIPT DRAFT。** 台詞は「何を言う必要があるか / 何を言ってはいけないか / この会話で何が変わるか」を優先し、文芸FINALにしない。 **確定/仮定**: canon=CONFIRMED、設計=CANDIDATE、canon未指定=**ASSUMPTION(確定しない)**。spawn座標/facing/尺は **PROVISIONAL**。 **Canon Guard**: 金魚/水槽/水槽音/「記録されない小さな命」＝非採用（**復活禁止**）。時計塔=Landmark のみ／**内部Event追加禁止**（分類/制度/内部=UNDECIDED U-004）。ノア開示は場所非依存で最小。

  

**Flag 凡例（Implementation候補・DL-Y3未決／Story状態は明示）**: observation 観測度 / mioTrust 信頼 / fragmentCount 断片 / mioNameStability 名前安定 / anlogPressure アンログ圧 / playerChoseNotToLook 見ない選択 / mioVoluntarySpeech 自発発話 / relationAnchor 関係アンカー / whiteLayerProgress 白層化率。 Story状態: observer\_is\_tou / notification\_sender\_inverted / mio\_carried\_lost。 Control = LOCKED（操作不可・演出）/ UNLOCKED（探索可）。Camera = FOLLOW(屋外2x) / FIXED(屋内・演出)（MAP\_VISUAL\_MASTER\_CH01）。

  

## SECTION 1 — SCENE SCRIPT（S0–S11・全フィールド）

**Engagement分類（ACTIVE/REACTIVE/PASSIVE）**: S0=P→S1=A→S2=A→S3=R→S4=R→S5=A→S6=A→S7=A→S8=R→S9=A→S10=R→S11=R ＝ **PASSIVE最大連続=1 ✅ 後半PASSIVE連続なし ✅** ※ Gate条件は「PASSIVEが2シーン以上連続しないこと」。全動詞の一意性はGateではない。 **MIO BOND TRACE**: MIO-A/B/C経験の有無が後半に微小な痕跡として返る。**大分岐・好感度システムにしない。** 環境音・短い反応・配置差分として微弱に返る程度。CANDIDATE・Playtest検証。 **3原則（横断Gate・****CH01\_SCENARIO\_MASTER.md** **§3B参照）**: ①WORLD→SUSPICION→UI ②OBSERVATION≠CALLOUT ③CALLOUT SUCCESS≠CAPTURE CAUSE

### S0 — 冒頭フック：ミオに忘れられる

  - **PRIMARY VERB**: 見守る(Watch)
  - Scene ID / Beat: S0 / B0｜Location/Area/Zone: 導入（滲んだ白い場） **ASSUMPTION**｜Time: 17:17（滲み）｜World State: 滲みSave（不在の予告）
  - Entry Condition: New Game｜Entry Spawn: 中央 **PROVISIONAL**｜Player Facing: 正面｜Control: LOCKED（導入演出）
  - Characters Present: トウ・ミオ｜NPC Position: ミオ=正面近距離｜NPC Initial Action: トウを見て、少し笑ってから謝る
  - Player Goal: （提示前）｜Knowledge: なし→「何かが欠けている」予兆｜Emotion: 静かな好奇→喪失の予感
  - Required Action: 進行（Enter送り）｜Optional Action: なし
  - Dialogue: D-FORGET★（ミオ「ごめんなさい」「あなたは、誰ですか？」）｜Optional Dialogue: なし
  - Interaction: なし｜Optional Interaction: なし｜Choice: なし
  - Event Trigger: EVT-OPENING（滲みSave演出）｜Flag Read: —｜Flag Write: whiteLayerProgress=intro
  - Visual Change: 画面が白く滲む｜Sound/Silence: 環境音が引く・無音の後に一言｜Camera/Presentation: FIXED・VN寄り
  - UI: セーブUIが滲む｜World Change: 予告のみ（本編は平常へ）
  - Exit Condition: 導入終了｜Exit Route: S1（家の朝へ）｜Next Scene: S1｜Next Hook: 「誰がいない？」
  - WHY NOW: 章の核（**忘れられる恐怖＝受動的喪失**）を体験の最初に一度だけ提示。S11（構造的喪失＝呼ぶことは正しかったのに奪われた）とは異なる痛み——単純な予告→回収にしない。

### S1 — 朝：叔母との日常（トウの家）

  - **PRIMARY VERB**: 探索する(Explore)
  - Scene ID / Beat: S1 / B1｜Location/Area/Zone: トウの家 / A / A1自室・A2居間・A3母の部屋+玄関｜Time: 朝｜World State: 平常（塔=窓から遠景Partial）
  - Entry Condition: S0終了｜Entry Spawn: A1自室ベッド脇 **PROVISIONAL**｜Facing: 下｜Control: UNLOCKED（移動/調べ習得）
  - Characters Present: トウ・叔母（A2居間）・母=不在演出（A3）｜NPC Position: 叔母=台所/居間固定｜NPC Initial Action: 家事（皿/エプロン）
  - Player Goal: 家を出る｜Knowledge: 母の不在・名→安心の伏線・叔母の記憶の揺らぎ｜Emotion: 安心→微違和感｜Control: UNLOCKED
  - Required Action: A2で叔母に話す → 玄関へ移動｜Optional Action: A3母の部屋を調べる・自室の私物を調べる（配置候補）
  - Dialogue: D-AUNT-WAIT（叔母「誰かを待ちます、って顔」）／D-AUNT-NAME★（「名前を呼ばれると安心するって（母が）」→「…たぶんね」）｜Optional Dialogue: D-AUNT-FLOWER（花を替えた/替えてない→「覚えてることから先に怪しくなる」）
  - Interaction: INT-エプロン（母不在＋伏線）｜Optional Interaction: INT-母部屋/INT-花/INT-扉（母の不在の環境物語）
  - Choice: なし｜Event Trigger: なし
  - Flag Read: —｜Flag Write: mioTrust=base / (Opt調べで)observation+｜Visual Change: 母の部屋の光｜Sound/Silence: 生活音（床/扉/食器）／母の部屋だけ音がない｜Camera: FIXED（屋内）
  - UI: 操作ヘルプ（移動/調べ）｜World Change: なし
  - Exit Condition: 玄関を出る｜Exit Route: 玄関→坂道｜Next Scene: S2｜Next Hook: 坂道でミオと
  - WHY: 私的空間で操作を安全に教えつつ、母の「不在」を台詞に頼らず空間で提示（後の喪失の重みの基盤）。

### S2 — 帰り道：時計塔へ寄る理由（坂道）

  - **PRIMARY VERB**: 寄り添う(Accompany)
  - Scene ID / Beat: S2 / B2｜Location/Area/Zone: 坂道 / B / B1坂上・B2生活圏・B3坂下｜Time: 夕方前｜World State: 平常（塔=近づくFull）
  - Entry Condition: S1終了｜Entry Spawn: B1坂上（玄関側）｜Facing: 下（坂下=広場方向）｜Control: UNLOCKED（同行移動）
  - Characters Present: トウ・ミオ（同行）｜NPC Position: ミオ=トウに追随｜NPC Initial Action: 合流して並んで歩く
  - Player Goal: ミオと歩いて時計塔前へ｜Knowledge: ミオが17:17に寄る癖・「最初の日だけ思い出せない」｜Emotion: 親密｜Control: UNLOCKED
  - Required Action: B3坂下（広場口）へ歩く。B2主動線上でMIO-B「待つ」がNatural Eventとして自然発生（進行LOCKなし・先に進んでも回収可）｜Natural Dialogue: 店先を掃いている住人が歩行を止めず一言だけ声をかける（v0.14 Script Candidate）｜Optional Bond: MIO-A寄り道 ★MIO BOND｜Optional Action: B2生活圏調べ（ミオがコメント）
  - Dialogue: D-5MIN＋D-WAIT（MIO-B ★MIO BOND / Natural Route：ミオが主動線上で止まる→プレイヤーが少し待つ→「トウは待ってくれるんだ」）＋NPC-B2-AMBIENT-01（Natural Ambient / v0.14候補）｜Opt: D-DETOUR（MIO-A：猫への寄り道）＋Optional flavor NPC最大1名まで
  - Interaction: なし（Req）｜Optional Interaction: 生活圏の小物（flavor）
  - Choice: なし｜Event Trigger: なし｜Flag Read: —｜Flag Write: mioTrust+
  - Visual Change: 坂の湾曲で塔が中央上に現れる｜Sound/Silence: 夕方の生活音｜Camera: FOLLOW（屋外2x）
  - UI: —｜World Change: なし
  - Exit Condition: 広場口へ｜Exit Route: 坂下→時計塔前ベンチ｜Next Scene: S3｜Next Hook: なぜ時計塔？
  - WHY: 移動を「**一緒にいて楽しい**＋理由の言えない癖」に使い、Landmark(塔)へ自然に誘導。**謎に入る前に愛着を操作で成立させる（MIO-A/B ★MIO BOND）**。

### S3 — 時計塔前のベンチ（座りたがる理由）

  - **PRIMARY VERB**: 佇む(Linger)
  - Scene ID / Beat: S3 / B3｜Location/Area/Zone: 時計塔前ベンチ / C / C1入口・C2ベンチ｜Time: 夕方｜World State: 平常（塔=直近Full）
  - Entry Condition: S2終了｜Entry Spawn: C1入口｜Facing: 上（塔/ベンチ方向）｜Control: UNLOCKED
  - Characters Present: トウ・ミオ｜NPC Position: ミオ=ベンチ端（二番目に座りたがる）｜NPC Initial Action: ベンチへ向かい座る
  - Player Goal: ベンチに寄る・席の意味を感じる｜Knowledge: 「ここだけ静か／音がするのは名前の近く」（白層の局在）｜Emotion: 違和感の芽｜Control: UNLOCKED
  - Required Action: ベンチを調べる/隣に座る → MIO-C「ただ座る」Natural Beat（数秒UNLOCKのまま、何も起こさなくてよい時間を通過）｜Optional Action: 塔を見上げる（INT-時計塔）
  - Dialogue: D-BENCH1（「一番端は近すぎる」「二番目がいい」→トウ「何もないよ」）／D-QUIET（「少し静かになる」「音は名前の近く」）／D-NAME1★（トウ「ミオ」→「…止まった」「ちゃんと私だった」）
  - Optional Dialogue: 塔を見上げた時の一言（内部に触れない）
  - Interaction: INT-ベンチ（4席＋気配）｜Optional Interaction: INT-時計塔（見る・内部非開示）
  - Choice: なし｜Event Trigger: なし｜Flag Read: mioTrust｜Flag Write: mioNameStability=high（呼びかけ実演で一時安定）
  - Visual Change: ベンチ周りの微かな空白｜Sound/Silence: ベンチ付近だけ音が薄い｜Camera: FOLLOW→軽微FIXED（会話）
  - UI: —｜World Change: なし
  - Exit Condition: 17:17 が近づく｜Exit Route: そのままC2で滞在｜Next Scene: S4｜Next Hook: 17:17の通知
  - WHY: 呼びかけ(名→安心)を早期に実演＝後の攻略反転の伏線。Landmark(塔)を「意味の器」として提示。

### S4 — 17:17 の空白メッセージ

  - **PRIMARY VERB**: 確かめる(Verify)
  - Scene ID / Beat: S4 / B4｜Location/Area/Zone: 時計塔前ベンチ / C / C2｜Time: **17:17**｜World State: UI変質の始まり
  - Entry Condition: S3滞在中に17:17到達｜Entry Spawn: C2（継続）｜Facing: 端末｜Control: UNLOCKED→短時LOCKED（通知演出）
  - Characters Present: トウ・ミオ｜NPC Position: ミオ=隣｜NPC Initial Action: 端末を見て静かになる
  - Player Goal: 通知を確認する｜Knowledge: 送っていない通知・既読・本文空白／記録率→--%（欠損表示・ラベル判読不能）｜Emotion: 不安｜Control: 通知UI操作
  - Required Action: 通知を開く｜Optional Action: なし
  - Dialogue: D-BLANK★（ミオ「…来たんだ」「たぶん、それ、まだ見ちゃだめ」）｜Optional Dialogue: なし
  - Interaction: INT-通知（空白/既読）｜Optional Interaction: なし
  - Choice: なし｜Event Trigger: **EVT-1717**（§Event Script）｜Flag Read: time==17:17｜Flag Write: whiteLayerProgress+
  - Visual Change: 通知UIの本文が空白・記録率ラベルが欠損（--%・判読不能）｜Sound/Silence: 通知後に環境音が一段引く｜Camera: FIXED（端末寄り）
  - UI: スマホ通知オーバーレイ（Map保持）｜World Change: 記録率→--%(欠損)へ表示変質。**「白層化率」の名称はまだ出さない→S8で判読可能に**
  - Exit Condition: 通知を閉じる → C2を短時間UNLOCK（即S5へ自動遷移しない）。プレイヤーがベンチ/ミオ/周囲を見る・数歩動く余地を置き、5席目へ近づくことでS5開始｜Exit Route: C2継続｜Next Scene: S5｜Next Hook: 誰宛？
  - WHY: 「送っていない通知＝関係は在った」を入口の気味悪さで提示し、UIそのものを世界変化の器にする。

### S5 — 空いている席の違和感（5席目）

  - **PRIMARY VERB**: 調べる(Investigate)
  - Scene ID / Beat: S5 / B5｜Location/Area/Zone: 時計塔前ベンチ / C / C2（4席+5席目跡）｜Time: 17:17直後｜World State: 白層化↑
  - Entry Condition: S4終了｜Entry Spawn: C2｜Facing: ベンチ｜Control: UNLOCKED（近接調査）
  - Characters Present: トウ・ミオ｜NPC Position: ミオ=5席目の方を見る｜NPC Initial Action: 「五つ目」を指す
  - Player Goal: 席を確かめる｜Knowledge: 4席なのにミオは5つ目を見る（ミオだけ認識）｜Emotion: 疑念→恐怖→**否認**（「席は四つしかない」＝見なかったことにする合理化）｜Control: UNLOCKED
  - Required Action: ベンチ（5席目の跡/影）を調べる｜Optional Action: 影/跡の再調査（fragment+）＋**観測因果チェーン：調べた後に以前調べた物（刻印/色）が微変化→再調査で欠損ラベルがUI上で微増（--%→--%↑・名称はまだ判読不能）**
  - Dialogue: D-5TH★（ミオ「ほら、五つ目」→トウ「席は四つしかないよ」→「…そう、だよね」）｜Optional Dialogue: 再調査時の白層描写
  - Interaction: INT-空席（跡/影のみ）｜Optional Interaction: 跡の再調査（断片示唆）
  - Choice: なし（選択はS6）｜Event Trigger: \*\*EVT-EMPTYSEAT\*\*｜Flag Read: whiteLayerProgress｜Flag Write: fragmentCount+ / observation+（調べるほど）
  - Visual Change: 5席目に跡/影（プレイヤーには曖昧）｜Sound/Silence: 紙から文字を剥がす音（剥落音）｜Camera: FOLLOW→調査時ズーム
  - UI: 調査プロンプト｜World Change: なし（顕在化のみ）
  - Exit Condition: 調査完了 → 直後に選択UIを出さず短いUNLOCK。トウが立ち上がり、ミオが反応を待つ状態をプレイヤー自身が見る。その後S6選択UI｜Exit Route: C2継続｜Next Scene: S6｜Next Hook: どうする？
  - WHY: 「調べる」行為を恐怖と結び、後の「観測=加害」の伏線に。ロケは正本 CH01\_DETAIL §3（4席+5席目＝**bench**）に準拠。

  

**削除経緯**: 二次 14\_CHAPTER §2 の「教室(五つ目の席)」は旧案残存。設計ファイルでは **bench に統一**（2026-08-13）。上位canon側の学校記述残存は **STALE CANON CANDIDATE / GOVERNANCE FIX REQUIRED** として別途列挙。

### S6 — 最初の選択肢

  - **PRIMARY VERB**: 選ぶ(Choose)
  - Scene ID / Beat: S6 / B6｜Location/Area/Zone: 時計塔前ベンチ / C / C2｜Time: 夕方｜World State: 分岐点
  - Entry Condition: S5終了｜Entry Spawn: C2｜Facing: ミオ｜Control: 選択UI
  - Characters Present: トウ・ミオ｜NPC Position: 隣｜NPC Initial Action: トウの反応を待つ
  - Player Goal: 態度を選ぶ｜Knowledge: 選択が結果を変える｜Emotion: 緊張｜Control: 選択
  - Required Action: **Choice**（intent: observe / avoid / ask / wait）｜Optional Action: なし
  - Dialogue: 選択提示（各intentの短い前置き）｜Optional Dialogue: 各選択後の1リアクション
  - Interaction: なし｜Choice: CHOICE-S6（4 intent・§Dialogue Script）
  - Event Trigger: なし｜Flag Read: observation/mioTrust｜Flag Write: 選択に応じ observation± / mioTrust± / playerChoseNotToLook(avoid/wait時)
  - Visual Change: 選択に応じた微変化｜Sound/Silence: 選択中は環境音抑制｜Camera: FIXED（会話）
  - UI: 選択肢UI（intentタグ）｜World Change: 分岐フラグ
  - Exit Condition: 選択確定｜Exit Route: C2継続（→S7/S8）｜Next Scene: S7(Opt)/S8｜Next Hook: 結果を見る
  - WHY: 「観測/回避/問い/待つ」を最初に手に取らせ、後半の攻略反転（avoid/wait/呼びかけが正）へ接続。

### S7 — 再構成モード（⚠CD-13未決・Optional）

  - **PRIMARY VERB**: 組み直す(Reconstruct)
  - Scene ID / Beat: S7 / B7｜Location/Area/Zone: **場所非依存（再構成UI/心象） ASSUMPTION**｜Time: —｜World State: UNKNOWN
  - Entry Condition: S6で条件成立 **かつ 再構成モード採用時のみ**｜Entry Spawn: —｜Facing: —｜Control: 再構成UI（採用時）
  - Characters Present: トウ｜NPC Position: —｜NPC Initial Action: —
  - Player Goal: 断片で章の表の謎を解く｜Knowledge: 章の表の謎（一部）｜Emotion: 集中｜Control: 再構成操作
  - Required Action: （採用時）断片を組む｜Optional Action: —
  - Dialogue: UNKNOWN（未決）｜Interaction: 断片（fragmentCount参照）｜Choice: 再構成の組合せ
  - Event Trigger: EVT-RECONSTRUCT(未決)｜Flag Read: fragmentCount｜Flag Write: fragment解決フラグ(未決)
  - Visual/Sound/Camera: UNKNOWN｜UI: 再構成UI（未決）｜World Change: UNKNOWN
  - Exit Condition: 解決 or スキップ｜Exit Route: S8｜Next Scene: S8｜Next Hook: —
  - WHY / 注記: **CD-13 未決**。採用されない場合 S7 はスキップし S6→S8。設計は Optional として隔離、canon確定しない。

### S8 — アンログ逆流

  - **PRIMARY VERB**: 耐える(Endure)
  - Scene ID / Beat: S8 / B8｜Location/Area/Zone: 時計塔前 / C / C2 **ASSUMPTION**｜Time: 夕｜World State: 逆流・因果反転の顕在化
  - Entry Condition: S6(→S7)終了｜Entry Spawn: C2｜Facing: ミオ｜Control: OPENING短時LOCKED→PARTIAL UNLOCK（操作試行）→短時LOCK（気づき/UI）
  - Characters Present: トウ・ミオ・アンログ(声)｜NPC Position: ミオ=中心｜NPC Initial Action: 苦しむ/抗う
  - Player Goal: 抗う/見る（この後の反転へ）｜Knowledge: 記録外の力(アンログ)／**観測こそ加速因（因果反転）｜Emotion: 動揺・罪悪感→怒り**（状況/記憶局への抵抗）｜Control: 冒頭のみLOCKED／操作試行はPARTIAL UNLOCK
  - Required Action: 逆流を見る＋\*\*操作試行（移動/触れる/追跡する/記録する→全て率表示を跳ね上げる＝一方的に相手を確定しようとする操作＝観測→プレイヤーが「ぼくが見たから」と自分で到達）\*\*｜Optional Action: なし
  - **3原則②適用（OBSERVATION≠CALLOUT）**: 一方的に相手を確定しようとする操作（調べる/触れる/追跡する/記録する/問い詰める）＝**観測＝悪化させる行為**。名を呼ぶ→待つ→本人が「はい」と応える＝**呼びかけ＝成功動詞＝観測とは別系統**。呼びかけを悪化動詞のリストに入れない。
  - Dialogue: D-ANLOG★（声「来て」「待ってた」「トウ」「名前、呼んで」「見ないで」「でも、忘れないで」）／D-STOP（ミオ「やめて」「私の中から出さないで」）
  - Interaction: なし｜Choice: なし（選択はS9）｜Event Trigger: **EVT-ANLOG-BACKFLOW**
  - Flag Read: observation（高いほど逆流強）｜Flag Write: anlogPressure=high｜Visual Change: 欠損ラベル(--%→)がここで初めて「白層化率」として判読可能に＋急伸／色抜け｜Sound/Silence: 剥落音の重畳→呼びかけ前の無音準備｜Camera: FIXED（演出）
  - UI: 欠損ラベルが「白層化率」として判読可能に＋急変表示｜World Change: 因果反転（観測=白層化）
  - Exit Condition: 逆流ピーク｜Exit Route: C2継続｜Next Scene: S9｜Next Hook: 選ぶ
  - WHY: 「調べる＝悪化」を体感で確定させ、次の選択で攻略反転を成立させる土台。

### S9 — 逆流中の選択肢（呼びかけ）

  - **PRIMARY VERB**: 呼びかける(Call out)
  - Scene ID / Beat: S9 / B9｜Location/Area/Zone: 時計塔前 / C / C2 **ASSUMPTION**｜Time: 夕｜World State: 因果反転
  - Entry Condition: S8終了｜Entry Spawn: C2｜Facing: ミオ｜Control: 選択→呼びかけ入力
  - Characters Present: トウ・ミオ｜NPC Position: 正面近距離｜NPC Initial Action: 逆流に耐える
  - Player Goal: 本人へ向き合う｜Knowledge: 攻略反転（見ない/聞く/待つ/名を呼ぶ/手を取る が正）｜Emotion: 怒り→決意｜Control: 選択/呼びかけ
  - Required Action: \*\*Choice → 呼びかけ(名を呼ぶ)\*\*｜Optional Action: 見ない/聞く/待つ/手を取る（正の別解）
  - Dialogue: D-NOLOOK（「見ないの？」→「見ない方がいい」→「たぶん正しい」）／D-NAME2★（トウ「ミオ」→「…今の、ちゃんと私だった」）
  - Interaction: なし｜Choice: CHOICE-S9（見ない/聞く/待つ/名を呼ぶ/手を取る）｜Event Trigger: **EVT-CALLOUT**（名→「はい」）
  - Flag Read: anlogPressure/observation｜Flag Write: mioNameStability=restored / playerChoseNotToLook(該当時) / mioVoluntarySpeech / relationAnchor
  - Visual Change: 呼びかけ成功でミオの輪郭が戻る｜Sound/Silence: 呼びかけ後の無音→ミオの声だけ残す｜Camera: FIXED（顔）
  - UI: 呼びかけ入力（名→はい）｜World Change: 一時的に固定が解ける
  - Exit Condition: 呼びかけ成立｜Exit Route: 17:17 塔前へ（S10）｜Next Scene: S10｜Next Hook: 17:17 塔へ
  - WHY: canon固有の「名→はい」を攻略に据え、「観測でなく本人の応答」というテーマを操作化する。

### S10 — 一部理解の余韻（Transition Beat）

  - **PRIMARY VERB: 見届ける(Witness)**
  - Scene ID / Beat: S10 / B10｜Location/Area/Zone: 塔前 / C（塔は遠景Landmark） **ASSUMPTION**｜Time: 夕闇｜World State: 塔=Full/夕闇
  - Entry Condition: S9成立｜Entry Spawn: C2｜Facing: ミオ/ベンチ/塔｜Control: UNLOCKED（短い余韻。強制READなし）
  - Characters Present: トウ・ミオ・（ノア=場所非依存の声/示唆）｜NPC Position: ミオ=隣｜NPC Initial Action: 静かに待つ
  - Player Goal: いま起きたことを受け止める｜Knowledge: S8-S9の体験から白層/アンログ/観測の危険を一部理解。観測点の意味はS11で示唆｜Emotion: 安堵→薄い不安｜Control: 短い自由操作
  - Required Action: 数秒その場に留まり、ミオ/ベンチ/塔のいずれかを視界に入れる｜Optional Action: 塔を見上げる（内部に触れない）
  - Dialogue: D-5TH-TRUTH-SHORT（D-5TH-TRUTH既存3要素のうち「五つ目は、ほんとにあった」相当の核だけを短く返す。文芸FINALは別）／D-NOAHは必須から除外しCANDIDATE/ASSUMPTIONのまま保留。採用時も場所非依存・最小、塔内部/制度に踏み込まない
  - Interaction: INT-時計塔（遠景・内部非開示）｜Choice: なし｜Event Trigger: なし（Transition。独立Disclosure Eventを新設しない）
  - Flag Read: fragmentCount/mioNameStability｜Flag Write: worldKnowledge=partial は実装変数として未決扱い。S10縮退を理由にCanon化しない
  - Visual Change: 夕闇へ・塔のシルエット｜Sound/Silence: S9後の無音から環境音が完全には戻らない｜Camera: FOLLOW/軽微FIXED（余韻。強制VNにしない）
  - UI: 原則なし。必要なら既存Map保持UIのみ｜World Change: なし（理解はS8-S9の体験を受け止める形）
  - Exit Condition: 5〜15秒程度の余韻＋短いミオ反応後｜Exit Route: 決着へ（S11）｜Next Scene: S11｜Next Hook: 呼ぶことは正しかった。それでも何かが来る
  - WHY: S8-S9でプレイヤーが操作から理解した内容をREADで再説明しない。S9の成功とS11の構造的喪失を一本の感情線にしつつ、CH01で必要な一部理解は維持する。ノアは必須開示にしない（U-004厳守）。

### S11 — ラスト（観測点=トウ / 送信者反転 / 連れ去り）

  - **PRIMARY VERB**: 手放す(Release)

  

**S0↔S11 意味論的反転**: S0＝受動的喪失（忘れられる）→ S11＝**構造的喪失**（呼びかけは成功し、ミオは一度自分に戻る。直後に記憶局が介入・連れ去り）。**3原則③適用**: 呼びかけが連れ去りの原因とは断定しない。設計解釈「制度が本人性の回復を検知→介入」は **CANDIDATE/DESIGN INTERPRETATION**（上位Canon根拠なし）。プレイヤーの痛み＝「呼ぶことは正しかった。それでも奪われた」。

  

  - Scene ID / Beat: S11 / B11｜Location/Area/Zone: 時計塔前ベンチ / C / C2（17:17） **ASSUMPTION：反復するベンチで閉じる**｜Time: **17:17→夜**｜World State: 喪失
  - Entry Condition: S10終了｜Entry Spawn: C2（ベンチ）｜Facing: ミオ｜Control: 呼びかけ入力→LOCKED（連れ去り）→UNLOCKED（C2再解釈）→短時LOCK（通知/終端）
  - Characters Present: トウ・ミオ・記憶局（出現）｜NPC Position: ミオ=ベンチ／記憶局=C入口から接近｜NPC Initial Action: ミオが応え、一度自分に戻る→直後に記憶局が現れる（**3原則③: 呼びかけが連れ去りの原因とは断定しない。機序=CANDIDATE**）
  - Player Goal: 名を呼び、応えを受け取る｜Knowledge: 観測点=トウ/初回観測日=未発生/次回=明日17:17｜Emotion: 喪失→執着｜Control: 呼びかけ後LOCKED
  - Required Action: \*\*呼びかけ（名→「はい」）\*\*｜Optional Action: なし
  - Dialogue: 呼びかけ「ミオ」→「はい」（成立）／D-END★（通知「次回観測予定：明日17:17」／送信者 **ミオ→トウ** 反転／トウ独白「送った覚えは、なかった。でも、既読だけは付いていた。」）
  - Interaction: INT-ベンチ（連れ去り後に**空席化**）｜Choice: なし｜Event Trigger: **EVT-CALLOUT-YES** **→** **EVT-CAPTURE****（連れ去り）→** **EVT-SENDER-INVERT****（送信者反転）**
  - Flag Read: mioNameStability/relationAnchor｜Flag Write: **observer\_is\_tou=true** **/** **mio\_carried\_lost=true** **/** **notification\_sender\_inverted=true**（Story状態）
  - Visual Change: 「はい」でミオが一度戻る（輪郭が鮮明に）→直後に記憶局が介入→連れ去り→ベンチが空席に→夜へ・塔の意味が変わる｜Sound/Silence: 「はい」で他音が引く→一瞬の安堵→連れ去りの静かな暴力→無音の余韻｜Camera: FIXED（顔→一瞬の回復→介入→空席→塔）
  - UI: carried.lost（灰スロット＝不可逆の喪失をUIに残す）／通知送信者が反転表示｜World Change: 連れ去り・空席化・送信者反転
  - Exit Condition: 連れ去り後にC2再解釈を1回以上行い、端末通知／モノローグ終了｜Exit Route: CH02接続｜Next Scene: (CH02)｜Next Hook: 「必ず取り戻す」→ CH02「未記録／記録されない街」
  - WHY: 呼びかけは**成功する**。ミオは一度、本当に「自分」に戻る。直後に記憶局が介入し連れ去る。**呼びかけが連れ去りの原因とは断定しない**（3原則③）。プレイヤーの痛み＝「**呼ぶことは正しかった。それでも制度に奪われた**」。CH02動機＝「あれは間違っていなかった。だから取り戻す」。S0「忘れられる恐怖」とは異なる——**正しい行為が報われない世界の構造的暴力**がCH02動機。**記憶局＝制度的暴力の初提示。時計塔内部は使わない。**

  

## SECTION 2 — DIALOGUE SCRIPT（実装粒度・SCRIPT DRAFT）

Text Draft は FINAL でない。★=canon確定キーライン（意図保持・書換慎重）。母体=Docs/CHAPTER01\_SCENARIO\_MASTER.md。

  

|  |  |  |  |  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*ID\*\* | \*\*Speaker→Target\*\* | \*\*Scene\*\* | \*\*Trigger\*\* | \*\*Req/Opt\*\* | \*\*Purpose（何を伝える/言ってはいけない）\*\* | \*\*Text Draft(要約)\*\* | \*\*Player Response\*\* | \*\*Branch\*\* | \*\*State Dep.\*\* | \*\*After State\*\* |
| D-FORGET★ | ミオ→トウ | S0 | 導入 | Req | 章の核=不在を予告／※誰が/なぜは言わない | 「ごめんなさい」「あなたは、誰ですか？」 | 送りのみ | — | — | whiteLayerProgress=intro |
| D-AUNT-WAIT | 叔母→トウ | S1 | A2会話 | Req | 「待つ」主題の導入／母の詳細は言わない | 「顔に書いてある。誰かを待ちます、って」 | 送り | — | — | — |
| D-AUNT-NAME★ | 叔母→トウ | S1 | A2会話 | Req | \*\*名→安心の伏線\*\*＋母の記憶の揺らぎ／母の状態は断定しない | 「名前を呼ばれると安心するって（母が）」→「…たぶんね」 | 送り | — | — | mioTrust=base |
| D-AUNT-FLOWER | 叔母→トウ | S1 | A3付近 | Opt | 叔母の白層化を身近に／母本人は出さない | 「花替えて」→「昨日替えた」→「そうだった？」 | 送り | — | Opt調べ | observation+ |
| D-5MIN | ミオ→トウ | S2 | 同行中 | Req | 反復行動と「最初の日」の空白／理由は説明させない | 「五分だけ」／内語「最初の日だけ思い出せない」 | 送り | — | — | mioTrust+ |
| D-BENCH1 | ミオ→トウ | S3 | ベンチ接近 | Req | 5席目の伏線／「何か」を明示しない | 「二番目がいい」→トウ「何もないよ」 | 送り | — | — | — |
| D-QUIET | ミオ→トウ | S3 | 着席 | Req | 白層の局在（名前の近くが静か） | 「少し静かになる」「音は名前の近く」 | 送り | — | — | — |
| D-NAME1★ | トウ→ミオ | S3 | 任意/進行 | Req | 呼びかけの実演（後の攻略の種） | トウ「ミオ」→「…止まった」「ちゃんと私だった」 | 名を呼ぶ | — | mioTrust | mioNameStability=high |
| D-BLANK★ | ミオ→トウ | S4 | 通知open | Req | 空白通知の気味悪さ／宛先は明かさない | 「…来たんだ」「まだ見ちゃだめ」 | 通知を開く | — | time==17:17 | whiteLayerProgress+ |
| D-5TH★ | ミオ→トウ | S5 | 席調査 | Req | 5席目パズル提示／誰の席かは言わない | 「五つ目」→トウ「席は四つ」→「…そうだよね」 | 調べる | — | — | fragmentCount+ |
| CHOICE-S6 | (システム) | S6 | 選択 | Req | observe/avoid/ask/wait を手に取らせる | 各intentの前置き | 4択 | intent分岐 | observation/mioTrust | 選択別フラグ |
| D-NOLOOK | ミオ/トウ | S6/S9 | avoid/wait | Opt→Req | 攻略反転=観測しない | 「見ないの？」→「見ない方がいい」→「たぶん正しい」 | 選択 | avoid/wait | — | playerChoseNotToLook |
| D-ANLOG★ | アンログ声 | S8 | 逆流 | Req | 残響の言語／正体・思想は明かさない | 「来て」「待ってた」「名前、呼んで」「見ないで」「でも忘れないで」 | 視聴 | — | observation高で強 | anlogPressure=high |
| D-STOP | ミオ→トウ | S8 | 逆流 | Req | 観測が壊す実感 | 「やめて」「私の中から出さないで」 | 視聴 | — | — | — |
| CHOICE-S9 | (システム) | S9 | 選択 | Req | 見ない/聞く/待つ/名を呼ぶ/手を取る＝正 | 5択 | 呼びかけ等 | 正解群 | anlogPressure | 正解フラグ群 |
| D-NAME2★ | トウ→ミオ | S9 | 呼びかけ | Req | 名→私に戻る（攻略成立） | トウ「ミオ」→「今の、ちゃんと私だった」 | 名を呼ぶ | — | mioNameStability | relationAnchor |
| D-5TH-TRUTH-SHORT | ミオ→トウ | S10 | 開示 | Req | S8-S9で体験した事実を短く受け止める／説明し直さない | 「……五つ目は、ほんとにあった。」相当の核のみ | 送り | — | fragmentCount | worldKnowledge=partial |
| D-NOAH | ノア(声) | S10 | 開示 | Opt(\*\*CANDIDATE/ASSUMPTION\*\*) | 必須から除外・採否保留。採用時のみ制度の断片を最小／塔内部・制度に踏み込まない(U-004)／※CH01\\\_DETAIL S10に無い設計追加 | 断片的な一言（場所非依存） | 送り | — | — | — |
| D-END★ | 通知/トウ独白 | S11 | ラスト | Req | 観測点=トウ/送信者反転／確定的意味は断定しない | 「次回観測予定：明日17:17」／送信者 ミオ→トウ／独白「送った覚えはない。でも既読だけは付いていた」 | 送り | — | relationAnchor | Story状態3種 |

  

**言ってはいけない（全Scene共通）**: 記憶局全貌/アンログ思想/白層科学/未来のトウ/母の保存詳細/ミオ=鍵・原型/時計塔の内部・分類・鐘/金魚（非採用）。

  

## SECTION 2A — BENCHMARK-STYLE SCENARIO × AREA / 場所 INDEX

  

## 目的: Benchmark Script の「場所を見ながら台詞・ト書きを追える」読み方を CH01 に適用する参照層。SECTION 1/2/2B の内容を置換せず、実装時に Scene → Area/Zone → 場所 → Script → Event/Flag を一続きで読むための索引とする。ロケ未確定は既存記載どおり ASSUMPTION / UNDECIDED を維持し、新規IDは作らない。

  

## 読み方: Scene/Beat｜Area/Zone｜場所・導線｜主Script（台詞/ト書き）｜Trigger/Event｜State/Flag｜Next

  

## S0 / B0｜Area: 導入（ASSUMPTION）｜場所: 滲んだ白い場・中央（spawn PROVISIONAL）｜Script: ⚙セーブデータが滲む・17:17 → \[ミオ\]「……ごめんなさい。」「あなたは、誰ですか？」★ → ◇画面が白く滲み環境音が引く｜Trigger/Event: EVT-OPENING｜State/Flag: whiteLayerProgress=intro｜Next: S1（家の朝）

  

## S1 / B1｜Area A｜場所: A1自室 → A2居間 → A3母の部屋+玄関｜Script: ⚙A1ベッド脇で起床 → A2叔母「誰かを待ちます、って顔」／「名前を呼ばれると安心するって（母が）」★ → A3母の部屋・花・扉を任意調査 → 玄関へ｜Trigger/Event: Req=叔母に話す→玄関、Eventなし｜State/Flag: mioTrust=base、Opt調べでobservation+｜Next: S2（坂道）

  

## S2 / B2｜Area B｜場所: B1坂上 → B2生活圏 → B3坂下（広場口）｜Script: \[ミオ\]合流・同行「帰ろ。……五分だけ、寄っていい？」→ 内語「最初の日だけ思い出せない」→ MIO-A寄り道 / MIO-B待つ（Optional Bond）→ ◇坂の湾曲で時計塔が正面に現れる｜Trigger/Event: Req=B3へ歩く、Eventなし｜State/Flag: mioTrust+｜Next: S3（時計塔前ベンチ）

  

## S3 / B3｜Area C｜場所: C1入口 → C2ベンチ（二番目の席）｜Script: \[ミオ\]「一番端は、近すぎる」「二番目がいい」→ MIO-Cただ座る（Optional Bond）→「ここに座ってると、少しだけ静かになる」→ \[トウ\]「ミオ。」★ → \[ミオ\]「…今の、止まった。ちゃんと、私だった。」★｜Trigger/Event: Req=INT-ベンチ（調べる/座る）、Opt=INT-時計塔｜State/Flag: mioNameStability=high｜Next: S4（17:17通知）

  

## S4 / B4｜Area C｜場所: C2ベンチ・端末UI｜Script: ⚙17:17端末通知 → \[トウ\]「送った覚えの、ない通知」→ 本文空白・既読 → \[ミオ\]「…来たんだ。」「たぶん、それ、まだ見ちゃだめ。」★ → 環境音が一段引く → UIラベル欠損(--%・名称未判読)｜Trigger/Event: EVT-1717 / INT-通知｜State/Flag: whiteLayerProgress+｜Next: S5（5席目）

  

## S5 / B5｜Area C｜場所: C2ベンチ・4席+5席目の跡/影｜Script: \[ミオ\]「……ほら、五つ目。」★ → \[トウ\]「席は、四つしかないよ。」★ → ◇否認 → ■5席目を調べる（1回目=跡/影、再調査=ミオだけ「空いている」）→ 剥落音｜Trigger/Event: EVT-EMPTYSEAT / INT-空席｜State/Flag: fragmentCount+, observation+｜Next: S6（最初の選択肢）

  

## S6 / B6｜Area C｜場所: C2ベンチ・ミオ隣｜Script: ▶どうする？ observe（見る）/ avoid（見ない）/ ask（聞く）/ wait（待つ）。各intentで短い反応を返す｜Trigger/Event: CHOICE-S6｜State/Flag: observation± / mioTrust± / avoid・wait時playerChoseNotToLook｜Next: S7（採用時）またはS8

  

## S7 / B7｜Area: 場所非依存（ASSUMPTION / CD-13 UNDECIDED）｜場所: 再構成UI/心象｜Script: ⚙採用時のみ → ◇断片が宙に浮かぶ → ▶断片を組む → ◇章の表の謎の一部が像を結ぶ。機構・台詞・報酬は未決｜Trigger/Event: EVT-RECONSTRUCT(未決)｜State/Flag: fragmentCount参照 / fragment解決フラグ未決｜Next: S8

  

## S8 / B8｜Area C（ASSUMPTION）｜場所: C2・ミオ正面/中心｜Script: ◇ミオの色が抜ける → \[アンログ/声\]「来て」「待ってた」「トウ」「名前、呼んで」「見ないで」「でも、忘れないで」★ → \[ミオ\]「やめて」「私の中から出さないで」→ ▶移動/触れる/追跡/記録＝一方的観測操作はすべて率上昇 → \[トウ\]「…ぼくが、見たから。」→ UIで初めて「白層化率」が判読可能｜Trigger/Event: EVT-ANLOG-BACKFLOW｜State/Flag: anlogPressure=high（observation高で強度↑）｜Next: S9

  

## S9 / B9｜Area C（ASSUMPTION）｜場所: C2・ミオ正面近距離｜Script: ▶見ない / 聞く / 待つ / 名を呼ぶ / 手を取る → Req到達「名を呼ぶ」→ \[トウ\]「ミオ。」★ → 無音 → \[ミオ\]「…今の、ちゃんと、私だった。」★。観測ではなく、相手の応答を待つ「呼びかけ」として成立｜Trigger/Event: EVT-CALLOUT / CHOICE-S9｜State/Flag: mioNameStability=restored / relationAnchor / mioVoluntarySpeech / 該当時playerChoseNotToLook｜Next: S10

  

## S10 / B10｜Area C（ASSUMPTION）｜場所: 塔前・C2周辺、時計塔は遠景Landmarkのみ｜Script: S9成功後に短いUNLOCK → \[ミオ\] D-5TH-TRUTH-SHORT「五つ目は、ほんとにあった」相当の核だけを返す → ◇夕闇、塔のシルエット。環境音は戻り切らない。D-NOAHは必須から外しCANDIDATE/ASSUMPTION保留｜Trigger/Event: なし（Transition） / Opt=INT-時計塔｜State/Flag: worldKnowledge=partialは実装未決｜Next: S11

  

## S11 / B11｜Area C（ASSUMPTION）｜場所: C2ベンチ → C入口から記憶局接近 → 連れ去り後の空席/端末｜Script: 17:17 \[トウ\]「ミオ。」★ → \[ミオ\]「はい。」★ → ◇一度「自分」に戻る → 直後に記憶局が静かに現れ「保護のため」→ 制御LOCK・ミオ連れ去り → ベンチ空席化・夜 → 通知「次回観測予定：明日17:17」→ 送信者 ミオ→トウ反転 → \[トウ\]「送った覚えは、なかった。でも、既読だけは付いていた。」★｜Trigger/Event: EVT-CALLOUT-YES → EVT-CAPTURE → EVT-SENDER-INVERT｜State/Flag: observer\_is\_tou=true / mio\_carried\_lost=true / notification\_sender\_inverted=true｜Next: CH02「必ず取り戻す」

  

## 実装接続ルール: このINDEXのArea/Zone・場所名称はSECTION 1/2B/3/4/5/6の既存表記を参照する。座標・spawn・facing・Collision/Trigger形状はMAP側で確定し、本INDEXでは新規推測しない。確定後は「場所」欄からMAP SCRIPT ANCHORS/Area仕様へ1:1で接続する。

  

## SECTION 2B — LINE-BY-LINE SCRIPT DRAFT（台本形式・Reference同等粒度）

公式スクリプト本（全台詞・分岐・ト書き）と同粒度で、CH01 を**一行ずつ**起こす。**すべて SCRIPT DRAFT（文芸FINALでない・書換可）**。母体=Docs/CHAPTER01\_SCENARIO\_MASTER.md／canon=CH01\_DETAIL。 **凡例**: \[話者\] 話者／◆=話す／◇=ト書き・演出・ナレーション／▶=選択肢／⚙=システム(UI/セーブ/場面制御)／↓=次へ／■=調べ物(1回目/2回目以降)／〔 〕=条件・状態タグ／★=canon確定キーライン(意図保持・書換慎重)。 **Canon Guard**: 金魚/水槽は登場させない。時計塔の内部/制度/鐘/組織/ノア恒常配置は台詞・ト書きに出さない（〔U-004〕）。S0/S7-S11 のロケは **(仮)=ASSUMPTION**。ノア開示は場所非依存・最小。台詞は下書き＝GPT/人間が書き直せる。

### S0 — 冒頭フック：忘れられる 〔導入(仮)〕

⚙ セーブデータが滲む。時刻表示は 17:17。

  

◇ 白い。どこかに、名前の抜けたにおいがする。

  

\[ミオ\] ◇ こちらを見て、少しだけ笑う。

  

\[ミオ\] ◆ ……ごめんなさい。 ★

  

\[ミオ\] ◆ あなたは、誰ですか？ ★

  

◇ 画面が白く滲み、環境音が引いていく。

  

⚙ → S1（家の朝へ）／whiteLayerProgress=intro

### S1 — 朝：叔母との日常 〔トウの家：A1自室→A2居間→A3母の部屋〕 Control: UNLOCKED / Camera: FIXED(屋内)

⚙ \[起床\] 画面が明るくなる。トウは自室のベッド脇で目を覚ます。

  

\[トウ\] ◆ ……いかなきゃ。（内語）

  

◇（自室）朝の光。家のどこかで、母の部屋だけが静かだ。

  

   ↓（居間 A2 へ）

  

\[叔母\] ◆ おはよう、トウ。

  

\[叔母\] ◆ ……顔に書いてある。「きょうも、だれかを待ちます」って。

  

\[トウ\] ◆ …そうかな。

  

\[叔母\] ◆ 会うまえは、みんな すこし待つものよ。

  

   ——（名→安心の伏線）——

  

\[叔母\] ◆ あの子は、名前を呼ばれると安心するって……お母さんが、よく言ってた。 ★

  

\[トウ\] ▶（聞き返す / 何も言わない）

  

   ├〔聞き返す〕→ \[叔母\] ◆ ……たぶん、ね。（記憶が、少しゆらぐ）

  

   └〔何も言わない〕→ \[叔母\] ◇ 少し困った顔で、笑う。

  

   ↓

  

\[叔母\] ◆ お母さんの花、替えておいてね。

  

\[トウ\] ◆ …昨日、替えたよ。

  

\[叔母\] ◆ そうだった？　…覚えてることから、先に あやしくなるのね。

  

【調べ物 / Interactable】

  

■ 母の部屋（A3・Opt重要）

  

   1回目: ◇ 花がある。毎日、だれかが替えている。／戸は、少しだけ開いている。／中は、音がしない。

  

   2回目以降: ◇ ……ここだけ、時間が止まっているみたいだ。

  

   結果: observation+ ／“不在”を体感

  

■ 叔母のエプロン（A2・Opt）: ◆〔母を匂わせる一言。断定しない〕

  

■ 自室の私物 / 朝の食卓（配置候補・flavor）: ◇ 使い慣れた席。いつもの食器。

  

⚙ 玄関を出る → S2 ／ mioTrust=base

### S2 — 帰り道：時計塔へ寄る理由 〔坂道 B1→B2→B3〕 Control: UNLOCKED(同行) / Camera: FOLLOW

\[ミオ\] ◇（合流）となりに並ぶ。

  

\[ミオ\] ◆ 帰ろ。……五分だけ、寄っていい？

  

\[トウ\] ▶（いいよ / どうして？）

  

   ├〔いいよ〕→ \[ミオ\] ◆ ありがとう。

  

   └〔どうして？〕→ \[ミオ\] ◇ 少し笑って、答えない。

  

   ↓（坂を下りながら）

  

\[トウ\] ◆ 三か月前から、ずっと「五分だけ」だ。（内語）

  

\[トウ\] ◆ …最初の日のことだけ、思い出せない。（内語）

  

   ——（MIO-A ★MIO BOND（Optional Bond Experience — 進行必須ではない愛着操作）：寄り道に付き合う）——

  

\[ミオ\] ◆ あ、……。

  

◇ ミオが立ち止まる。坂の端に、猫がいる。

  

\[ミオ\] ◆ …大丈夫かな。大丈夫。たぶん。

  

◇ 近づくと、猫が逃げる。ミオは一瞬 怖い顔をして、それから笑う。

  

\[ミオ\] ◆ …逃げちゃった。

  

   ——（MIO-B ★MIO BOND / NATURAL ROUTE：待つ。B2主動線上で自然発生・進行LOCKなし）——

  

◇ 少し先で、ミオが止まる。何かを見ている。

  

\[トウ\] ▶（先に行く / 待つ）

  

   ├〔先に行く〕→ \[ミオ\] ◆ あ、待って。

  

   └〔待つ〕→ ◇ しばらく、並んで立っている。

  

      \[ミオ\] ◆ ……トウは、待ってくれるんだ。

  

◇ 坂の途中、正面の空に 時計塔 が立ち上がる。

  

■ 生活圏（B2・Opt/flavor）

  

   住人（店先を掃いている人）: ◆ おはよう。今日は、落ち葉の方が早起きだ。

  

   掲示: ◇ いつもの町の、いつもの貼り紙。

  

⚙ 坂下（広場口）→ S3 ／ mioTrust+

### S3 — 時計塔前のベンチ 〔C1入口→C2ベンチ〕 Control: UNLOCKED / Camera: FOLLOW→FIXED(会話)

\[ミオ\] ◆ 一番端は、近すぎるの。

  

\[ミオ\] ◆ …二番目がいい。

  

\[トウ\] ◆ 何もないよ、そこ。

  

\[ミオ\] ◇ 二番目の席に座る。

  

   ——（MIO-C ★MIO BOND / NATURAL BEAT：ただ座る。17:17前に必ず通過・ControlはUNLOCKのまま）——

  

◇ しばらく、何も起きない。風が吹く。

  

\[ミオ\] ◆ ……風、気持ちいいね。

  

◇ ミオが空を見上げて、笑う。プロットと無関係の、ただの一瞬。

  

   ↓

  

\[ミオ\] ◆ ここに座ってると、少しだけ静かになる。

  

\[ミオ\] ◆ …音がするのは、私の名前の近くだけ。

  

   ——（呼びかけの実演）——

  

\[トウ\] ◆ ミオ。 ★

  

\[ミオ\] ◇ 一瞬、周りの音が止まる。

  

\[ミオ\] ◆ …今の、止まった。ちゃんと、私だった。 ★

  

■ 時計塔を見る（Opt・〔U-004：内部に触れない〕）

  

   1回目: ◇ 高い。夕方の光に、輪郭だけが濃い。

  

   2回目以降: ◇ ミオは、いつもここへ来る。

  

⚙ 17:17 が近づく → S4 ／ mioNameStability=high

### S4 — 17:17 の空白メッセージ 〔C2〕 Control: UNLOCKED→短時LOCK / Camera: FIXED(端末)

⚙ 時刻 17:17。端末が鳴る。

  

\[トウ\] ◆ …送った覚えの、ない通知。（内語）

  

⚙ 通知を開く。本文は空白。既読だけが付いている。

  

\[ミオ\] ◆ …来たんだ。 ★

  

\[ミオ\] ◆ たぶん、それ、まだ見ちゃだめ。 ★

  

◇ 通知のあと、環境音が一段、引く。

  

⚙ UI:「記録率」のラベルが欠損する（--%・判読不能）。名称はまだ見えない。

  

⚙ 通知を閉じる。Control: UNLOCKED。

◇ すぐには何も始まらない。環境音が一段薄いまま、プレイヤーはベンチの周囲を数歩動ける。

◇ ミオは五席目の方を見ている。近づく/ベンチ側へ戻ることで S5 が始まる。

⚙ → S5 ／ whiteLayerProgress+

  

**CAUSALITY ORDER**: 環境音の変質（WORLD CHANGE） → 「送った覚えはない」（PLAYER SUSPICION） → UIラベル欠損: 記録率→--%(名称は未判読＝**答えをまだ渡さない**)（UI CONFIRMATION）。UIの変質は最後に来る。

  

**Observation Causality**: ラベル欠損はワールド異変（B5の空席の跡/影など）をプレイヤーが体験した後にUIが追認する形で提示する。UIが先に白層化を告知しない。**「白層化率」という名称はS8の操作試行で初めて判読可能になる**＝世界異変→疑念→UI命名の順。

### S5 — 空いている席の違和感（5席目）〔C2：4席+5席目の跡〕 Control: UNLOCKED

\[ミオ\] ◆ ……ほら、五つ目。 ★

  

\[トウ\] ◆ 席は、四つしかないよ。 ★

  

\[ミオ\] ◆ ……そう、だよね。

  

◇（否認）トウは、見なかったことにしようとする。

  

■ 5席目を調べる（Req）

  

   1回目: ◇ 何かの跡がある。影のような、へこみのような。／紙から、文字だけを剥がすような音。

  

   2回目以降〔fragment再取得〕: ◇ ミオにだけ、そこは「空いている」。

  

   結果: fragmentCount+ ／ observation+

  

⚙ 調査終了。Control: UNLOCKED。

◇ トウが立ち上がる。ミオは何も言わず、トウの反応を待っている。

◇ 数秒または短い移動入力の後、S6の選択UIへ。

⚙ → S6

### S6 — 最初の選択肢 〔C2〕 Control: 選択

\[ミオ\] ◇ トウの反応を、待っている。

  

▶ どうする？（intent）

  

   ・observe（見る） → \[トウ\] ◆ もっと調べたら、分かるかも。（内語）／ observation+ , mioTrust-

  

   ・avoid（見ない） → \[トウ\] ◆ …見ない方がいい気がした。（内語）／ playerChoseNotToLook , mioTrust+

  

   ・ask（聞く）     → \[トウ\] ◆ …大丈夫？　\[ミオ\] ◆ 大丈夫。たぶん。 ★ ／ mioTrust+

  

   ・wait（待つ）     → ◇ 何も言わず、となりにいる。／ playerChoseNotToLook , mioTrust+

  

⚙ → S7〔再構成採用時〕 / S8

### S7 — 再構成モード 〔場所非依存(仮)・Optional〕 〔CD-13 UNDECIDED〕

⚙〔再構成モード採用時のみ。未採用なら S6 → S8〕

  

◇（採用時）いくつかの断片が、宙に浮かぶ。

  

▶ 断片を組む（組合せ）

  

◇ 章の表の謎の一部が、像を結ぶ。

  

※ 機構・台詞・報酬は未決(UNDECIDED)。確定しない。

  

⚙ → S8

### S8 — アンログ逆流 〔時計塔前 C2(仮)〕 Control: LOCK(演出)

⚙ 部分UNLOCK（操作試行あり）。

  

◇ ミオの輪郭から、色が抜けはじめる。

  

\[アンログ/声\] ◆ 来て。 ★

  

\[アンログ/声\] ◆ 待ってた。

  

\[アンログ/声\] ◆ トウ。／名前、呼んで。 ★

  

\[アンログ/声\] ◆ 見ないで。／…でも、忘れないで。 ★

  

\[ミオ\] ◆ やめて。

  

\[ミオ\] ◆ …それ、私の中から出さないで。

  

   ——（操作試行：一方的観測操作は全て率を跳ね上げる。呼びかけは別）——

  

\[トウ\] ▶（移動する / 触れる / 追跡する / 記録する）

  

   ├〔移動する〕→ ⚙ 率が跳ぶ。ミオの色がさらに抜ける。

  

   ├〔触れる〕→ ⚙ 率が跳ぶ。届かない。

  

   ├〔追跡する〕→ ⚙ 率が跳ぶ。逃げるほど悪化する。

  

   └〔記録する〕→ ⚙ 率が跳ぶ。記録しようとするほど消える。

  

◇ \*\*こちらから固定しようとする操作はすべて\*\*——率だけが、上がる。

  

⚙ 欠損ラベル(--%→)がここで初めて「白層化率」として判読可能になる。

  

\[トウ\] ◆ …ぼくが、見たから。（内語／\*\*自分で到達\*\*・怒り）

  

⚙ → S9 ／ anlogPressure=high

  

**CAUSALITY ORDER**: 一方的観測操作のたびに世界の色が抜ける（WORLD CHANGE） → 「ぼくが見たから」（PLAYER SUSPICION＝自分で到達） → 欠損ラベルが「白層化率」として判読可能に＋急伸（UI CONFIRMATION）。UI表示は世界変化→プレイヤーの気づきの後に来る。 **観測 vs 呼びかけ**: 操作試行で失敗するのは「一方的に相手を固定しようとする操作（＝観測）」のみ。S9で「名を呼ぶ→待つ→本人が応える（＝呼びかけ）」が成功する理由は、相手自身の応答を待つ行為だから。この区別がRewriteMemoryのコアメカニクス。

### S9 — 逆流中の選択・呼びかけ 〔時計塔前 C2(仮)〕 Control: 選択→呼びかけ入力

▶ どうする？（正解群）

  

   ・見ない       → \[ミオ\] ◆ …今のは、たぶん正しい。／ playerChoseNotToLook

  

   ・聞く/待つ/手を取る → ◇ ミオの震えが、少し止まる。／ relationAnchor

  

   ・名を呼ぶ（Req到達）→ ⚙ 呼びかけ入力

  

\[トウ\] ◆ ミオ。 ★

  

⚙ 呼びかけのあと、他の音がすべて引く。

  

\[ミオ\] ◆ …今の、ちゃんと、私だった。 ★

  

⚙ mioNameStability=restored ／ relationAnchor ／ mioVoluntarySpeech

  

⚙ → S10

### S10 — 一部理解の余韻（Transition Beat）〔塔前 C(仮)・夕闇〕 Control: UNLOCKED(Transition)

### ⚙ S9の呼びかけ成立後、Controlを返す。5〜15秒程度、その場に留まれる。

### ◇ ミオはすぐには話さない。ベンチ、塔、トウのどれかを見る。

### \[ミオ\] ◆ ……五つ目は、ほんとにあった。〔D-5TH-TRUTH-SHORT〕

### ◇ それ以上は説明しない。夕闇。時計塔のシルエットだけが残る。

### ◇ S9後の無音から、環境音が完全には戻らない。

### ※ D-NOAHは必須から外す。CANDIDATE/ASSUMPTIONのまま採否保留。採用時も場所非依存・最小・U-004厳守。

### ⚙ worldKnowledge=partial は実装変数として未決。新規Canon化しない。

### ⚙ → S11

### S11 — ラスト（呼びかけ→連れ去り→送信者反転）〔時計塔前ベンチ C2(仮)・17:17→夜〕 Control: 呼びかけ→LOCK→モノローグ

⚙ 時刻 17:17。

  

\[トウ\] ◆ ミオ。 ★

  

\[ミオ\] ◆ はい。 ★

  

⚙ 呼びかけ成立。

  

◇ ミオの輪郭が、一瞬だけ鮮明に戻る。本当に「自分」に戻った顔。

  

◇ ——直後。記憶局が、静かに現れる。〔\*\*CANDIDATE/DESIGN INTERPRETATION\*\*: 制度が回復を検知したのか、別の契機か、は断定しない（3原則③）〕

  

\[記憶局\] ◆〔「保護のため」と、それだけ告げる。多くは語らない〕

  

⚙ 制御ロック（介入できない）。〔U-004：時計塔内部は使わない〕

  

◇ ミオが連れ去られていく。呼びかけは成功した。なのに、奪われた。ベンチが、空席になる。あたりは夜へ。

  

⚙ UI: carried.lost（灰スロット＝不可逆の喪失）。

  

⚙ observer\_is\_tou=true ／ mio\_carried\_lost=true

  

⚙ 端末に通知。「次回観測予定：明日 17:17」

  

⚙ 通知の送信者が、ミオ → トウ に反転する。

  

\[トウ\] ◆ 送った覚えは、なかった。でも、既読だけは付いていた。 ★

  

\[トウ\] ◆ …必ず、取り戻す。（内語）

  

⚙ notification\_sender\_inverted=true

  

■ ベンチ（連れ去り後）: ◇ だれもいない。二番目の席が、まだ少し、へこんでいる。

  

⚙ → CH02「未記録／記録されない街」

  

**注**: 上記は SCRIPT DRAFT。★キーラインは意図を保ち、それ以外は自由に書き直してよい。台詞本文の FINAL 化・条件分岐の網羅（state variant の全パターン）は GPT/人間レビュー後。**言ってはいけない（全Scene共通）** は SECTION 2 末尾に同じ。

  

## SECTION 2C — EXHAUSTIVE EXAMINABLES / STATE-VARIANTS / AMBIENT（悉皆台本・分類済・ロケ別）

公式スクリプト本と同様に、**ロケ別に調べ物を悉皆化**し、各に「1回目／2回目以降」＋**世界状態variant**を付す。RM の核である白層化＝進行で同じ場所の意味が書き換わるため、**状態variantが主要ボリューム**。全て SCRIPT DRAFT（書換可）。 凡例は SECTION 2B と同じ。状態タグ: 〔平常〕→〔17:17後〕→〔白層化↑〕→〔逆流後〕→〔連れ去り後(夜)〕。〔Cd〕=配置候補(canon非追加)／〔C〕=canon／〔U-004〕=時計塔・内部に触れない。**金魚/水槽は登場させない。**

  

**体験分類タグ**（各調べ物に付与。詳細は CH01\_30MIN\_EXPERIENCE\_AUDIT.md §6）:

  

  - 〔LIFE〕 生活・性格・人間関係。プロットと無関係の日常の質感（**増やす**）
  - 〔WORLD〕 世界設定・社会。説明に堕ちたものは削除候補
  - 〔FORESHADOW〕 後の展開の種。プレイヤーは気づかなくてよい
  - 〔OBS-RISK〕 調べると変化する。観測＝加害の体験装置（⑮因果チェーン接続）
  - 〔DEL候補〕 説明が目的で体験に寄与しない→GPT/人間レビューで最終判断

### C2 WORLD STATE CHANGE MATRIX（P3〜P5同一地理の意味書き換え）

P3〜P5がC2に留まる問題を、以下の要素変化で解く。**Mapは増やさない。**

  

|  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*要素\*\* | \*\*〔平常〕\*\* | \*\*〔17:17後〕\*\* | \*\*〔白層化↑〕\*\* | \*\*〔逆流中〕\*\* | \*\*〔連れ去り後(夜)〕\*\* |
| NPC通行 | 住人が通り過ぎる | 通行が減る | 通行なし・孤立 | — | 完全無人 |
| 環境音 | 夕方の生活音 | 音-1段 | 静寂が拡がる | 剥落音の重畳 | 無音（風だけ） |
| 色/光 | 暖色の夕方 | 暖橙 | 色抜け(端から白) | 歪み・明滅 | 夜・寒色 |
| Camera | FOLLOW(自由) | 微FIXED | 視野が狭まる | FIXED(緊迫) | WIDE(空虚) |
| ミオとの距離 | 隣(自由に近づける) | 隣(静かに) | 腕一本分 | 中心だが触れない | \*\*不在\*\* |
| Interactable | ベンチ/塔/生活痕 | \\+通知端末 | \\+5席目の跡/再調査 | 操作試行→全て失敗 | ベンチ(空席)/端末(反転) |
| UI | 記録率 | \\--%(欠損・名称未判読) | \\--%(微増) | \*\*「白層化率」として判読可能に\*\*＋急伸 | carried.lost灰スロット |
| ミオの台詞トーン | 日常（笑う/たぶん） | 少し静か | ヘッジが増える | 拒絶「出さないで」 | — |
| PLAYER FEELS (感情) | 穏やか | 戸惑い | 恐怖 | 動揺→決意 | 喪失→執着 |
| PLAYER DOES (行動) | 座る/見上げる | 通知を確認 | 空席を調べる | 耐える/呼ぶ | 立ち尽くす |
| PLAYER NOTICES (気づき) | 日常の景色 | ラベル変化 | 跡/影/剥落 | 残響の声 | 空席化/夜 |
| PLAYER SUSPECTS (疑い) | なし | 「送った覚えがない」 | 「ぼくが見たから？」 | 「観測が原因」 | 「ぼくのせいだ」 |

### Area A — トウの家（悉皆）

【叔母・任意会話（メインS1台詞の追加分）】

  

\[叔母\] ◆ いってらっしゃい。……ミオちゃんとは、まだ仲いいの？

  

\[トウ\] ▶（うん / …どうかな）

  

   ├〔うん〕→ \[叔母\] ◆ そう。……いいことね。名前を、ちゃんと呼んであげてね。

  

   └〔…どうかな〕→ \[叔母\] ◇ 少し困った顔で笑って、それ以上は聞かない。

  

\[トウ\] ◆ …ねえ、母さんは。

  

\[叔母\] ◆ ……お母さんの花、替えておいてね。（話を、そらす）

  

\[トウ\] ◆ 昨日、替えたよ。

  

\[叔母\] ◆ そうだった？　…最近、覚えてることから先に、あやしくなるの。

  

【調べ物】

  

■ 自室のベッド〔Cd/LIFE〕  1回目: ◇ もう、あたたかくない。／2回目以降: ◇ 二度寝したら、遅れる。

  

■ 机の私物〔Cd〕          1回目: ◇ 見慣れた物ばかり。ひとつずつ、名前が言える。／2回目以降: ◇ …名前が言える、うちは。

  

■ 窓（時計塔の遠景）〔C/U-004〕 1回目: ◇ 屋根の向こうに、時計塔。いつもの位置に、いつもの影。／2回目以降: ◇ ミオは、あの下に来る。

  

■ 居間の食卓／決まった席〔Cd〕 1回目: ◇ いつもの席。座る場所は、決まっている。／2回目以降: ◇ 決まっている、はずだ。

  

■ 使い慣れた食器〔Cd〕    1回目: ◇ 手になじむ。どれが誰の、も決まっている。／2回目以降: ◇ …一つ、多い気がした。気のせいだ。

  

■ 家具の修繕跡〔Cd〕      1回目: ◇ 直した跡がある。だれかが、ここで暮らしてきた。／2回目以降: ◇ 誰が直したかは、思い出せる。まだ。

  

■ 台所（叔母）〔C〕        1回目: ◇ 叔母が家事をしている。エプロンの柄に、見覚えがある。／2回目以降: \[叔母\] ◆ すぐ、ごはんにするからね。

  

■ 玄関〔C〕                1回目: ◇ 外へ。坂の下の方から、風。／2回目以降: ◇ 行こう。

  

■ 母の部屋の戸〔C/FORESHADOW〕        1回目: ◇ 少しだけ、開いている。／2回目以降: ◇ いつも、少しだけ。

  

■ 母の部屋の花〔C/FORESHADOW〕        1回目: ◇ 花がある。毎日、だれかが替えている。／2回目以降: ◇ …昨日も、見た。

  

■ 母の部屋（室内）〔C/FORESHADOW〕        1回目: ◇ 中は、音がしない。／2回目以降: ◇ ここだけ、時間が止まっている。（母本人・状態は断定しない＝CH02+）

  

■ 写真〔Cd/OBS-RISK〕      1回目: ◇ だれかと、だれか。顔の一つに、うまく焦点が合わない。／2回目以降: ◇ …誰、だっけ。

  

■ 壁の時計／カレンダー〔Cd/DEL候補〕 1回目: ◇ 針は、正しく動いている。17時が、少し気になる。／2回目以降: ◇ 17:17。まだ、先だ。

  

【環境音・ト書き】

  

◇ 床のきしみ。扉の開閉。食器の音。生活の音がする。

  

◇ 朝の光。ただ、母の部屋の方だけ、音がない。

### Area B — 坂道・生活圏（悉皆）

【ミオ同行・随伴コメント】

  

\[ミオ\] ◆ 帰ろ。……五分だけ、寄っていい？

  

\[ミオ\] ◆ この坂、下りると すぐ。

  

\[ミオ\] ◆ 三か月、毎日来てるのに。……最初の日だけ、思い出せないの。

  

\[トウ\] ▶（変だよ / そういうこともあるよ）

  

   ├〔変だよ〕→ \[ミオ\] ◆ ……だよね。でも、大丈夫。たぶん。 ★

  

   └〔そういうこともあるよ〕→ \[ミオ\] ◇ 少し笑って、答えない。

  

\[ミオ\] ◆ あそこ、見て。……ううん、なんでもない。

  

\[ミオ\] ◆ トウは、ちゃんと 覚えてる？　わたしのこと。

  

\[トウ\] ▶（覚えてる / どうして？）

  

   ├〔覚えてる〕→ \[ミオ\] ◆ ……よかった。

  

   └〔どうして？〕→ \[ミオ\] ◆ ……なんとなく。大丈夫。たぶん。 ★

  

\[ミオ\] ◆ 塔、見えてきた。

  

【住人NPC（flavor・状態variant）】

  

\[住人(掃除の人)\] ◆〔平常〕おかえり。／◆〔白層化↑〕……おかえり。（誰に、という顔で）

  

\[店主\]          ◆〔平常〕また明日な。／◆〔白層化↑〕…また、えっと……明日な。（名を言い淀む）

  

\[子ども\]        ◆〔平常〕ミオちゃんだ！／◆〔白層化↑〕……あの子、だれだっけ。

  

\[老人\]          ◆〔平常〕最近、日が暮れるのが早い。／◆〔白層化↑〕最近、思い出すのが、遅い。

  

\[近所の人\]      ◆〔平常〕また17時？　律儀だなあ。

  

【調べ物】

  

■ 掲示板〔Cd〕        1回目: ◇ いつもの町の、いつもの貼り紙。／2回目以降: ◇ 一枚、日付が抜けている。／〔白層化↑〕: ◇ 名前の欄が、白い。

  

■ 店先〔Cd〕          1回目: ◇ 見慣れた品。値札の字が、少しかすれている。／2回目以降: ◇ …何を買う予定だったか、忘れた。

  

■ 坂の手すり〔Cd/LIFE〕 1回目: ◇ 毎日つかむ。冷たさも、いつも通り。／2回目以降: ◇ いつも通り、のはず。

  

■ 自販機的なもの〔Cd〕 1回目: ◇ 灯りがついている。／2回目以降: ◇ おつりの音が、やけに響く。

  

■ 街灯〔Cd〕          1回目: ◇ まだ点いていない。夕方には点く。／〔白層化↑〕: ◇ 点いているのに、足元が暗い。

  

■ 側溝／落し物〔Cd/DEL候補〕  1回目: ◇ だれかの落し物。名前は、書いていない。／2回目以降: ◇ …拾い主も、もういない。

  

■ 貼り紙（迷い〇〇）〔Cd〕 1回目: ◇「さがしています」。写真の顔が、うまく見えない。／〔白層化↑〕: ◇ 写真だけ、白い。

  

■ 植木／花壇〔Cd〕    1回目: ◇ だれかが世話をしている。／2回目以降: ◇ 花は、母の部屋のと少し似ている。

  

■ 看板〔Cd/DEL候補〕  1回目: ◇ 町の名前。読める。／〔白層化↑〕: ◇ 町の名前が、思い出せない。

  

【ト書き】

  

◇ 坂の途中、正面の空に 時計塔 が立ち上がる。（内部には触れない・遠景のシルエット）

  

◇ 夕方前の生活音。人の気配は、まだ普通だ。

  

◇〔白層化↑で再訪時〕人の反応が、少しだけ遅い。名前を呼ぶ声が、減っている。

### Area C — 時計塔前広場・ベンチ（悉皆・状態variant＝主要ボリューム）

【ミオ・状況コメント（状態別）】

  

\[ミオ\] ◆〔平常〕一番端は、近すぎるの。二番目がいい。

  

\[ミオ\] ◆〔平常〕ここに座ってると、少しだけ静かになる。

  

\[ミオ\] ◆〔17:17後〕…来たんだ。たぶん、それ、まだ見ちゃだめ。 ★

  

\[ミオ\] ◆〔白層化↑〕ほら、五つ目。……あれ、四つ、だっけ。

  

\[ミオ\] ◆〔白層化↑〕大丈夫。たぶん。……たぶん、って、便利だね。 ★

  

\[ミオ\] ◆〔逆流中〕やめて。……それ、私の中から出さないで。

  

\[ミオ\] ◆〔逆流中〕見ないで。……でも、忘れないで。 ★

  

\[ミオ\] ◆〔呼びかけ後〕…今の、ちゃんと、私だった。 ★

  

\[ミオ\] ◆〔連れ去り直前〕……はい。 ★

  

【調べ物（状態variant）】

  

■ ベンチ全体〔C/OBS-RISK〕

  

   〔平常〕1回目: ◇ 四人がけの、古いベンチ。／2回目以降: ◇ ミオは、いつも二番目。

  

   〔白層化↑〕: ◇ 座面の一つ多い場所に、へこみがある気がする。

  

   〔連れ去り後(夜)〕: ◇ だれもいない。二番目の席が、まだ少し、へこんでいる。

  

■ 一番端の席〔C〕

  

   〔平常〕: ◇ 端。ミオは、ここには座らない。

  

   〔連れ去り後〕: ◇ ここなら、よかったのか。……分からない。

  

■ 二番目の席〔C/LIFE〕

  

   〔平常〕: ◇ ミオの場所。まだ、あたたかい。

  

   〔逆流後〕: ◇ あたたかさが、抜けていく。

  

   〔連れ去り後〕: ◇ もう、あたたかくない。

  

■ 5席目の跡〔Req/C/OBS-RISK〕

  

   〔平常〕1回目: ◇ 何かの跡。影のような、へこみのような。／2回目以降: ◇ ミオにだけ、そこは「空いている」。

  

   〔17:17後〕: ◇ 跡の輪郭が、はっきりする。

  

   〔白層化↑〕: ◇ 紙から、文字だけを剥がすような音。跡の中身が、白い。

  

   〔逆流後〕: ◇「だれか」が、待っていた場所だ。名前は、抜けている。

  

   〔連れ去り後〕: ◇ 五つ目の隣が、また一つ、空いた。

  

■ 時計塔を見上げる〔C/U-004・内部に触れない〕

  

   〔平常〕: ◇ 高い。夕方の光に、輪郭だけが濃い。

  

   〔17:17後〕: ◇ 針が、17:17。ここからは、それしか分からない。

  

   〔白層化↑〕: ◇ 見上げても、内側のことは何も見えない。ただ、立っている。

  

   〔連れ去り後(夜)〕: ◇ 夜。同じ塔なのに、意味が、変わってしまった。

  

■ 通知端末〔Req/C/OBS-RISK〕

  

   〔17:17後〕1回目: ◇ 送った覚えのない通知。本文は空白。既読だけが付いている。

  

   〔17:17後〕2回目以降: ◇ 何度開いても、空白。

  

   〔連れ去り後〕: ◇「次回観測予定：明日 17:17」。送信者が、ミオではなく——ぼくになっている。

  

■ 街灯（広場）〔Cd〕      〔平常〕: ◇ まだ点いていない。／〔連れ去り後〕: ◇ 点いた。だれも照らしていない。

  

■ 広場の敷石〔Cd〕        〔平常〕: ◇ すり減っている。毎日、だれかが通る。／〔白層化↑〕: ◇ 足音が、白く抜ける。

  

■ 落ち葉／生活痕〔Cd/LIFE〕 〔平常〕: ◇ だれかが座っていた気配。／〔連れ去り後〕: ◇ 気配だけが、残っている。

  

■ 掲示（広場）〔Cd/DEL候補〕 〔平常〕: ◇ 17:17 の待ち合わせ。よくある話だ。／〔白層化↑〕: ◇ 待ち合わせの、相手の名が白い。

  

■ 植込み／影〔Cd/DEL候補〕 〔平常〕: ◇ 夕日で、影が長い。／〔逆流後〕: ◇ 影の中に、声のかけらが混じる。

  

■ ベンチの下〔Cd〕        〔平常〕: ◇ だれかの忘れ物。名前は、書いていない。／2回目以降: ◇ …取りに来る人は、いるだろうか。

  

【記憶局・連れ去り（ト書き＋最小台詞）】

  

◇ 呼びかけが成立した——その直後。

  

◇ 記憶局が、静かに現れる。争う隙も、抵抗する言葉もない。

  

\[記憶局\] ◆ ……保護のため、です。

  

◇ それ以上は、何も言わない。

  

◇ ミオが連れ去られていく。ベンチが、空席になる。あたりは、夜へ。

  

【システム/UI（ト書き）】

  

⚙〔17:17〕UI:「記録率」のラベルが欠損し --%（名称未判読）。「白層化率」はS8の操作失敗後に初めて判読可能。

  

⚙〔17:17〕通知：本文は空白、既読だけが付く。

  

⚙〔連れ去り〕carried.lost：灰スロットが一つ増える（不可逆の喪失）。

  

⚙〔連れ去り後〕通知の送信者が、ミオ → トウ に反転する。

### （代替ロケ）学校・教室 — **削除（2026-08-13）**

学校/教室をCH01 Main Routeから除外したため、代替ロケセクションを削除。S5(5席目)は正本準拠で**C2ベンチに統一**。上位canon(CH01\_DETAIL.md:42/14\_CHAPTER\_BIBLE.md:27)に残る学校記述は **STALE CANON CANDIDATE / GOVERNANCE FIX REQUIRED**。

  

**注**: SECTION 2C は悉皆化のための DRAFT。状態variant・調べ物は設計候補（〔Cd〕）を多く含み、canonを増やすものではない（採否は GPT/人間レビュー）。金魚/水槽は非登場、時計塔内部は不使用。

  

## SECTION 3 — INTERACTION SCRIPT（Map配置と1:1追跡）

金魚/水槽=**非採用（行なし）**。属性が canon 未記載＝UNKNOWN（推測追加しない）。

  

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*ID\*\* | \*\*Object\*\* | \*\*Location(Area/Zone)\*\* | \*\*Visibility\*\* | \*\*Trigger\*\* | \*\*Before State\*\* | \*\*Response(要約)\*\* | \*\*After State\*\* | \*\*Req/Opt\*\* | \*\*Information\*\* | \*\*Emotion\*\* | \*\*Worldbuilding\*\* | \*\*Repeat\*\* |
| INT-母部屋 | 音のしない部屋 | 家/A3 | 玄関手前・奥 | 調べる | 平常 | 直接説明しない・不在の気配 | observation+ | Opt(重要) | 母の不在 | 寂寥 | 白層化の私的側 | 事件後に意味増 |
| INT-花 | 毎日替える花 | 家/A3 | 母の部屋 | 調べる | 平常 | 「昨日替えた？」の齟齬示唆 | — | Opt | 母の存在の痕跡 | 静かな不安 | 記憶の不安定 | 変化(候補) |
| INT-扉 | 少し開いた戸 | 家/A3 | 母の部屋 | 見る/調べる | 半開 | 中は音がない | — | Opt | 母の匂わせ | 寂寥 | 不在 | — |
| INT-エプロン | 叔母のエプロン | 家/A2 | 居間 | 会話/観察 | 家事中 | 名→安心の伏線 | mioTrust=base | Req(伏線) | 名前と安心 | 安心 | 家庭 | — |
| INT-ベンチ | 時計塔前ベンチ(4席+気配) | 時計塔前/C2 | 広場中央 | 調べる/座る | 平常 | ミオだけ「空いている」 | mioNameStability参照 | Req | 席の意味 | 違和感→疑念 | 白層の場 | 終盤=\*\*空席化\*\* |
| INT-空席 | 5席目の跡/影 | 時計塔前/C2 | ベンチ端 | 近接調査 | 気配のみ | 跡/影・ミオだけ認識 | fragmentCount+ | Req | 白層の証拠 | 疑念→恐怖 | 白層化 | 再調査で断片 |
| INT-通知 | スマホ通知(17:17空白) | 時計塔前/C2 | 端末UI | 17:17にopen | 未読 | 送っていない/既読/空白 | whiteLayerProgress+ | Req | 記録率→白層化率 | 不安 | 関係は在った | S11で送信者反転 |
| INT-時計塔 | 時計塔を見る | 坂道/B・塔前/C | 遠景Landmark | 見る | 遠景 | \*\*内部/組織は非開示\*\* | — | Opt | ミオが寄る理由 | — | Landmark(意味変化) | 時間帯で見え方変化 |

  

## SECTION 4 — EVENT SCRIPT（主要Event・詳細）

Input Lock/Camera/Sound/Flag/Resume まで定義。**時計塔内部Eventは作らない。**

### EVT-1717（17:17）

Trigger: ゲーム内時刻==17:17（S4）｜Precondition: S3滞在｜Location: 時計塔前/C2｜Player Position: ベンチ隣｜NPC Position: ミオ=隣｜Input Lock: 短時LOCK（通知表示中）｜Animation/Movement: 端末を取り出す｜Dialogue: D-BLANK★｜UI: 通知オーバーレイ・記録率ラベル→--%（名称未判読。「白層化率」はS8で初判読）｜Sound: 通知後に環境音-1段｜Camera: FIXED（端末）｜Flag Change: whiteLayerProgress+｜World State Change: UI変質｜Resume Control: 通知close｜Exit: S5。

### EVT-EMPTYSEAT（空席）

Trigger: INT-空席調査（S5）｜Precondition: EVT-1717後｜Location: C2｜Player Pos: ベンチ前｜NPC Pos: ミオ=5席目側｜Input Lock: 調査中のみ｜Animation: しゃがみ調査｜Dialogue: D-5TH★｜UI: 調査プロンプト｜Sound: 剥落音｜Camera: 調査ズーム｜Flag Change: fragmentCount+,observation+｜World: 顕在化｜Resume: 調査後UNLOCK｜Exit: S6。

### EVT-ANLOG-BACKFLOW（アンログ逆流）

Trigger: S8開始｜Precondition: S6(→S7)完了｜Location: C2 **ASSUMPTION**｜Player Pos: ミオ正面｜NPC Pos: ミオ=中心｜Input Lock: LOCK（演出）｜Animation/Movement: ミオが抗う・色抜け波｜Dialogue: D-ANLOG★,D-STOP｜UI: 白層化率急変｜Sound: 剥落音重畳→無音準備｜Camera: FIXED｜Flag Change: anlogPressure=high（observation高で強度↑）｜World: \*\*因果反転（記録=白層化）\*\*｜Resume: S9で部分制御｜Exit: S9。

### EVT-CALLOUT（呼びかけ）＋ 名→「はい」

Trigger: S9で「名を呼ぶ」選択｜Precondition: 逆流ピーク｜Location: C2｜Player Pos: 正面近接｜NPC Pos: ミオ正面｜Input Lock: 呼びかけ入力のみ｜Animation: 手を伸ばす/名を呼ぶ｜Dialogue: トウ「ミオ」→ミオ「はい」（D-NAME2★）｜UI: 呼びかけ入力（名→はい）｜Sound: **呼びかけ後の無音**→ミオの声だけ｜Camera: FIXED（顔）｜Flag Change: mioNameStability=restored,mioVoluntarySpeech,relationAnchor,(該当時)playerChoseNotToLook｜World: 一時的に固定が解ける｜Resume: 成立後S10｜Exit: S10。

### EVT-CAPTURE（ミオ連れ去り）

Trigger: S11で「はい」成立直後（EVT-CALLOUT-YES）｜Precondition: relationAnchor成立｜Location: C2｜Player Pos: ベンチ｜NPC Pos: 記憶局=C入口→接近｜Input Lock: \*\*LOCK（介入不可）\*\*｜Animation/Movement: 記憶局がミオを連れ去る（静かな暴力・露骨描写は避ける）｜Dialogue: 最小（記憶局は多くを語らない）｜UI: carried.lost（灰スロット）｜Sound: 「はい」で他音消失→連れ去りの静けさ→無音余韻｜Camera: FIXED（ミオ→空席→塔）｜Flag Change: \*\*mio\_carried\_lost=true,observer\_is\_tou=true\*\*｜World: **ベンチ空席化・夜へ・塔の意味変化**｜Resume: 連れ去り完了後C2をUNLOCK（再解釈）｜Exit: 再解釈完了→EVT-SENDER-INVERT。 ※ **記憶局＝制度的「収容」。時計塔内部は使わない（U-004）。連れ去りの見せ方（明示/示唆）は演出調整範囲（canon=連れ去りの事実は確定）。**

### EVT-SENDER-INVERT（通知送信者反転）

Trigger: EVT-CAPTURE後かつ連れ去り後C2再解釈を1回以上完了｜Precondition: mio\_carried\_lost｜Location: C2/UI｜Player Pos: ベンチ（空席横）｜Input Lock: モノローグLOCK｜Animation: 端末に通知｜Dialogue: D-END★（独白）｜UI: 通知送信者が **ミオ→トウ** に反転表示／「次回観測予定：明日17:17」｜Sound: 無音の余韻｜Camera: FIXED（端末→トウ）｜Flag Change: \*\*notification\_sender\_inverted=true\*\*｜World: 送信者反転（観測点=トウの示唆）｜Resume: CH02接続｜Exit: CH02 Hook。

  

## SECTION 5 — SCENARIO × SCRIPT × MAP TRACEABILITY（Master Table）

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*Beat\*\* | \*\*Scene\*\* | \*\*Area/Zone\*\* | \*\*Player Goal\*\* | \*\*NPC\*\* | \*\*Dialogue ID\*\* | \*\*Interaction ID\*\* | \*\*Event ID\*\* | \*\*Required Action\*\* | \*\*Optional Action\*\* | \*\*Flag Change\*\* | \*\*World Change\*\* | \*\*Next Hook\*\* |
| B0 | S0 | 導入(ASSUMPTION) | (提示前) | ミオ | D-FORGET★ | — | EVT-OPENING | 送り | — | whiteLayerProgress=intro | 滲みSave | 誰がいない？ |
| B1 | S1 | 家/A1-A3 | 家を出る | 叔母 | D-AUNT-WAIT,D-AUNT-NAME★ | INT-エプロン | — | 叔母に話す→玄関 | INT-母部屋/花/扉 | mioTrust=base,(opt)observation+ | なし | 坂道でミオと |
| B2 | S2 | 坂道/B1-B3 | ミオと歩く | ミオ(同行) | D-5MIN | — | — | 坂下へ | 生活圏調べ | mioTrust+ | なし | なぜ時計塔？ |
| B3 | S3 | 塔前/C1-C2 | ベンチに寄る | ミオ | D-BENCH1,D-QUIET,D-NAME1★ | INT-ベンチ | — | ベンチ調べ/座る | INT-時計塔 | mioNameStability=high | なし | 17:17の通知 |
| B4 | S4 | 塔前/C2 | 通知確認 | ミオ | D-BLANK★ | INT-通知 | EVT-1717 | 通知open | — | whiteLayerProgress+ | UI変質 | 誰宛？ |
| B5 | S5 | 塔前/C2 | 席を確かめる | ミオ | D-5TH★ | INT-空席 | EVT-EMPTYSEAT | 5席目調査 | 再調査(断片) | fragmentCount+,observation+ | 白層化↑ | どうする？ |
| B6 | S6 | 塔前/C2 | 態度を選ぶ | ミオ | CHOICE-S6 | — | — | Choice(4 intent) | — | observation±,mioTrust±,(avoid/wait)playerChoseNotToLook | 分岐 | 結果を見る |
| B7 | S7 | 場所非依存(ASSUMPTION/CD-13未決) | 章の謎を解く | — | (未決) | 断片 | EVT-RECONSTRUCT(未決) | (採用時)再構成 | — | fragment解決(未決) | UNKNOWN | — |
| B8 | S8 | 塔前/C2(ASSUMPTION) | 抗う/見る | ミオ,アンログ | D-ANLOG★,D-STOP | — | EVT-ANLOG-BACKFLOW | 逆流を見る | — | anlogPressure=high | 因果反転 | 選ぶ |
| B9 | S9 | 塔前/C2(ASSUMPTION) | 本人へ向き合う | ミオ | D-NOLOOK,D-NAME2★,CHOICE-S9 | — | EVT-CALLOUT | 呼びかけ(名→はい) | 見ない/聞く/待つ/手を取る | mioNameStability=restored,relationAnchor,mioVoluntarySpeech | 固定が解ける | 17:17 塔へ |
| B10 | S10 | 塔前/C(ASSUMPTION) | 余韻を受け止める | ミオ | D-5TH-TRUTH-SHORT（D-NOAHはCANDIDATE保留） | INT-時計塔 | —（Transition） | 短いUNLOCKでその場を見る | 塔を見上げる | worldKnowledge=partial | 塔=夕闇/環境音戻り切らず | 決着へ |
| B11 | S11 | 塔前ベンチ/C2(ASSUMPTION) | 名を呼ぶ→受ける | ミオ,記憶局 | D-END★ | INT-ベンチ(空席化) | EVT-CALLOUT-YES→EVT-CAPTURE→EVT-SENDER-INVERT | 呼びかけ(名→はい) | — | observer\\\_is\\\_tou,mio\\\_carried\\\_lost,notification\\\_sender\\\_inverted | 連れ去り/空席化/夜/送信者反転 | CH02「必ず取り戻す」 |

  

## SECTION 6 — MAP SCRIPT ANCHORS（各Areaへ Script を反映：6つの WHERE）

### Area A — トウの家（S1）

  - WHERE SCENE STARTS: A1自室（起床・spawn PROVISIONAL）
  - WHERE PLAYER STOPS: A2居間（叔母の前）／A3母の部屋前
  - WHERE DIALOGUE FIRES: A2（叔母 D-AUNT-\*）
  - WHERE INTERACTABLE: A2エプロン(Req伏線)／A3母の部屋・花・扉(Opt重要)
  - WHERE EVENT LOCKS CONTROL: なし（自由探索）
  - WHERE NEXT HOOK VISIBLE: 玄関（坂道への出口）／窓から時計塔遠景

### Area B — 坂道（S2）

  - SCENE STARTS: B1坂上（玄関側）
  - PLAYER STOPS: B3坂下（広場口）
  - DIALOGUE FIRES: 同行中(B2)で D-5MIN／主動線でD-WAIT(MIO-B Natural)／NPC-B2-AMBIENT-01（店先を掃く住人・Natural Ambient・歩行LOCKなし）
  - INTERACTABLE: B2生活圏の小物（Opt flavor + WORLD/MIO/HOOK/MYSTERY役割タグ）／MIO-BはInteract強制ではなく主動線上のNatural Beat。Optional枝2〜3本＋小ループはIMAGE-02配置候補であり、新規Location IDは作らない
  - EVENT LOCKS: なし
  - NEXT HOOK VISIBLE: 坂の湾曲で塔が中央上に出現（B2）

### Area C — 時計塔前ベンチ（S3–S6, S8–S11）

  - SCENE STARTS: C1入口（S3）
  - PLAYER STOPS: C2ベンチ（滞在の中心）
  - DIALOGUE FIRES: C2（D-BENCH1/D-QUIET/D-NAME1/D-BLANK/D-5TH/D-ANLOG/D-NAME2/D-5TH-TRUTH-SHORT/D-END）
  - INTERACTABLE: C2ベンチ・5席目・通知端末／遠景で時計塔(Opt・内部非開示)
  - EVENT LOCKS CONTROL: C2で EVT-1717(短時)・EVT-ANLOG-BACKFLOW・EVT-CALLOUT・**EVT-CAPTURE(完全LOCK)**・EVT-SENDER-INVERT
  - NEXT HOOK VISIBLE: 17:17通知(S4)／逆流(S8)／連れ去り後の空席と夜の塔(S11)

### （代替）学校/教室 — **削除（2026-08-13）**

学校/教室を CH01 Main Route から除外。S5 は C2 ベンチで統一。

  

## SECTION 7 — SCRIPT GRANULARITY AUDIT（vs Benchmark）

基準=benchmark/mother3\_field/docs/SCENARIO\_MAP\_ANALYSIS.md の資料粒度。判定 PASS/PARTIAL/FAIL。FAIL＝実装前資料として Benchmark Reference より弱い（→画像生成へ進めない）。

  

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
| \*\*項目\*\* | \*\*RM Scenario Master\*\* | \*\*RM Detailed Script\*\* | \*\*総合\*\* | \*\*根拠\*\* |
| Overall Story | PASS | — | PASS | §1 Overview 完備 |
| Part Structure | PASS | — | PASS | 5 Part 全フィールド |
| Scene Sequence | PASS | PASS | PASS | S0-S11 全フィールドブロック |
| Player Goal | PASS | PASS | PASS | Part/Scene/Traceability 三層 |
| Character Action | PASS | PASS | PASS | NPC Position/Initial Action 定義 |
| Emotion (感情曲線) | PASS | PASS | PASS | 安心→違和感→罪悪感→\\\*\\\*否認(S5-S6)→怒り(S8-S9)\\\*\\\*→喪失→執着 を Beat/Scene に realize（CONFIRMED曲線と一致） |
| Dialogue | — | PASS | PASS | SECTION 2 サマリ表(19 ID) ＋ \*\*SECTION 2B 台本形式(全12シーン line-by-line・話者/◆◇▶⚙/↓/★)\*\* |
| Dialogue 台本粒度(line-by-line) | — | PASS | PASS | Reference(公式スクリプト本)同等：話者・行単位・分岐(▶/はい-いいえ枝)・条件タグ〔 〕・調べ物 1回目/2回目以降・ト書き◇・システム⚙ |
| Optional Dialogue | — | PASS | PASS | Opt行・調べ物 variant・分岐枝(S1/S2/S6/S9) |
| Interaction | — | PASS | PASS | SECTION 3 表(8 ID) ＋ \*\*SECTION 2C 悉皆調べ物(Area A約13/B約9/C約12)・1回目/2回目以降・世界状態variant\*\* |
| Optional Interaction | — | PASS | PASS | 母の部屋/花/扉/時計塔 ＋ 悉皆examinables(生活痕/掲示/席/端末 等) |
| State-variant dialogue/exam | — | PASS | PASS | Reference同等：同一対象が〔平常→17:17後→白層化↑→逆流後→連れ去り後〕で別台詞（白層化テーマの操作化） |
| Ambient NPC | — | PASS | PASS | 住人/店主/子ども/老人/近所の人（平常/白層化↑ variant） |
| Event Trigger | — | PASS | PASS | 6 Event 詳細(Lock/Camera/Sound/Flag) |
| State/Flag | PARTIAL | PASS | PASS | Story状態 vs 実装変数を分離(変数canon化はDL-Y3未決) |
| World Change | PASS | PASS | PASS | UI変質/因果反転/空席化/送信者反転 |
| Map Location | PARTIAL | PARTIAL | PARTIAL | S0/S7-S11 は ASSUMPTION（canon未指定）。§6 anchorsで補うが確定はHUMAN DECISION |
| Entry/Exit | — | PASS | PASS | Entry Condition/Spawn/Exit Route/Next Scene |
| Player Control | — | PASS | PASS | LOCKED/UNLOCKED を各Sceneに |
| Next Hook | PASS | PASS | PASS | 各Scene/Part終端 |

  

**FAIL: 0 / PARTIAL: 2（State/Flag=変数canon化未決, Map Location=ロケASSUMPTION）。** 2件の PARTIAL はいずれも **canon 側の未決（DL-Y3 / S7-S11ロケ UNKNOWN）** に起因し、資料の作り込み不足ではない。§Q/§R で HUMAN DECISION として隔離済み。→ **Benchmark 同等の実装前粒度に到達**（ロケ確定と変数canon化は人間決裁待ちで、画像生成の設計図には ASSUMPTION 明示で反映可）。

  

## Changelog

  - 2026-08-13 v0.1: 新規。Scene Script(S0-S11全フィールド)／Dialogue Script(19)／Interaction Script(8)／Event Script(6詳細)／Traceability Master／Map Script Anchors／粒度監査。台詞はSCRIPT DRAFT。ロケ未指定は ASSUMPTION、変数canon化はDL-Y3未決。金魚Forbidden・時計塔内部Event無し。実装/画像なし・未commit。
  - 2026-08-13 v0.2: doc-review反映。S5/S8/S9 感情に否認/怒りを realize（監査に Emotion 行追加=PASS）。D-NOAH を CANDIDATE/ASSUMPTION（CH01\_DETAIL S10 に無い設計追加・採否保留）に降格。S5ロケを CONFLICT(正本優先でbench解決)に精緻化。
  - 2026-08-13 v0.3: **Script Reference（公式スクリプト本）の粒度・ボリュームを反映**。SECTION 2B「LINE-BY-LINE SCRIPT DRAFT（台本形式）」を新設＝全12シーンを一行ずつ（話者・◆話す/◇ト書き/▶選択/⚙システム・↓flow・分岐枝・条件タグ〔 〕・調べ物 1回目/2回目以降・★キーライン）。内容は非コピー（RM canon由来のDRAFT）。金魚非登場・時計塔内部は台詞/ト書きに出さない・S0/S7-S11=(仮)。監査に line-by-line 行を追加。
  - 2026-08-13 v0.4: **悉皆化でボリュームを Reference 水準へ**。SECTION 2C「EXHAUSTIVE EXAMINABLES / STATE-VARIANTS / AMBIENT（ロケ別）」を新設＝Area A/B/C の調べ物を悉皆（各10〜13）＋「1回目/2回目以降」＋**世界状態variant〔平常→17:17後→白層化↑→逆流後→連れ去り後〕**、叔母/ミオの任意会話・分岐、住人の状態variant、記憶局連れ去りのト書き、システム/UI。全て DRAFT・多くは〔Cd〕配置候補（canon非追加）。金魚非登場・時計塔内部不使用を維持。監査に State-variant/Ambient 行を追加。
  - 2026-08-13 v0.5: **GPTレビュー反映・30分体験再編集**（6項目修正・情報量増なし）。(1)S0/S11 WHY書き分け（受動的喪失 vs 能動的加害）。(2)S2にミオ愛着操作（MIO-A寄り道/MIO-B待つ）、S3にMIO-C（ただ座る）を台本に追加。(3)S5に観測因果チェーン（調べた後に既調査物が微変化）。(4)S8に操作試行（移動/呼びかけ/触れる→全て白層化率が跳ぶ→「ぼくが見たから」自分で到達）。(5)SECTION 2C に体験分類タグ(LIFE/WORLD/FORESHADOW/OBS-RISK/DEL候補)と C2 World State Change Matrix を追加。(6)Companion: CH01\_30MIN\_EXPERIENCE\_AUDIT.md（Beat監査・Gate評価）。
  - 2026-08-13 v0.6: **学校/教室を CH01 Main Route から全除外**。S5 WHYから教室代替ロケ記述を削除（bench統一）。叔母台詞「学校、いってらっしゃい」→「いってらっしゃい」。「通学の生徒」→「近所の人」。SECTION 2C/6 の代替ロケ学校セクションを削除注記に置換。粒度監査のクラスメイト→近所の人。上位canon残存はSTALE CANON CANDIDATE。
  - 2026-08-13 v0.7: **30分Player Experience Final Design Pass**。全Scene に PRIMARY PLAYER VERB 追記（S3-S5「調べる」3連続→佇む/確かめる/探るに分散）。S4 に Observation Causality 順序注記（WORLD→SUSPICION→UI）。SECTION 2C World State Matrix に Player Feels/Does/Notices/Suspects 4列追加。MIO-A/B/C を Optional Bond Experience に再分類。S11 に S0↔S11意味論的反転注記。
  - 2026-08-13 v0.8: **GPT再レビュー反映（92→97目標）**。(1) S4「白層化率」名称を隠蔽→欠損表示(--%・判読不能)。S8で初めて名称判読可能。(2) S8の失敗動詞から「呼びかけ」を削除→一方的観測操作（調べる/触れる/追跡する/記録する）に統一。観測 vs 呼びかけの分離を明文化。(3) S11因果を変更: 呼びかけは成功→ミオは一度戻る→制度が回復を検知し介入・連れ去り（「助けたから傷つけた」→「助けたのに奪われた」＝構造的喪失）。(4) Engagement分類(ACTIVE/REACTIVE/PASSIVE)追加。(5) MIO BOND TRACEコンセプト追加。(6) C2 World State MatrixのUIラベル欄を更新。
  - 2026-08-13 v0.9: **Chairman修正GO・3原則明文化**。SECTION 1冒頭に3原則参照を追加。S0 WHY: 「能動的加害」→「構造的喪失」に修正。S8: 3原則②適用(OBSERVATION≠CALLOUT)を明記。S11: 機序「制度が回復を検知→介入」をCANDIDATE/DESIGN INTERPRETATIONに降格（3原則③）。S11 line-by-line: 「制度が検知する」→「直後に現れる（機序断定しない）」。MIO BOND TRACE: 「大分岐・好感度システムにしない」明記。Engagement Gate: 「全動詞一意」条件を撤廃→「PASSIVE最大連続≤1」のみ。

  
  

SECTION 8 — AUTHORED EXPERIENCE QUALITY PASS（vs Benchmark・実プレイ品質）

  

目的: SECTION 7 は「資料粒度」がBenchmark Reference同等かを監査した。本SECTIONは別に、プレイヤーがCritical / Natural Routeを通ったときの「会話・生活・寄り道・再解釈・感情テンポ」がBenchmarkの設計原則と同等水準かを監査する。Benchmark内容をコピーせず、Benchmark Bibleで抽出済みの原則だけを使う。

  

Benchmark側で確認済みの重要原則:

・NPC会話による世界理解。

・イベントを一本道に並べず、町を往復/再訪・再解釈させる。

・主動線だけでなく寄り道・任意行動が世界と人物の理解を増やす。

・Map / NPC / Interaction / Scriptを分離せず、歩行中の体験密度として成立させる。

  

現状判定（v0.9）:

Q-01 Documentation Granularity: PASS。SECTION 2B/2C/3/4/5/6でReference同等の追跡粒度。

Q-02 Critical Route Dialogue Density: PARTIAL。S0/S4-S11のPlot/Core台詞は強いが、S1-S3の人物愛着・生活会話の強い部分がOptional側へ寄っている。最短プレイでは「ミオを好きになる前に異常が始まる」危険がある。

Q-03 Mio Bond on Natural Route: PARTIAL。MIO-A/B/Cは質が高いがOptional。Completionistでは効くがCritical Route保証が弱い。

Q-04 Ambient NPC / World Understanding: PARTIAL。Area Bに住人variantは存在するが、主進行上は会話不要。Benchmark原則「NPC会話による世界理解」をNatural Routeで十分に体験できる保証がない。

Q-05 Optional Interaction Density: PASS。Area A/B/Cの調べ物・再調査・State Variantは十分。ただし候補〔Cd〕が多く、実採用数はIMAGE-02/Area制作時に絞る。

Q-06 Revisit / Reinterpretation: PARTIAL。C2は平常→17:17→白層化→逆流→連れ去り後で非常に強い再解釈を持つ。一方、Area Bの白層化variantは現行Scenarioでは物理再訪されず、Script上の体験にならない。存在するだけのvariantを品質点に数えない。

Q-07 Character Voice: PASS候補。叔母=生活語＋記憶の揺らぎ、ミオ=短文/ヘッジ/「大丈夫。たぶん」、トウ=内語中心で役割差がある。最終判断は通し音読で行う。

Q-08 Plot vs Life Balance: PARTIAL。S4以降は通知→五席目→Choice→逆流→呼びかけ→開示→CaptureとCoreイベントが連続する。S3までの「何も起きない時間」が短いプレイでは不足しうる。

Q-09 Silence / Physical Acting: PASS候補。S3のただ座る、S8/S9の無音、S11の空席等は強い。MIO-CがOptionalのためCritical Routeで欠落可能。

Q-10 Map × Script Coupling: PASS。A1-A3/B1-B3/C1-C2とDialogue/Event/Interactionが追跡可能。

  

総合: 「資料としてBenchmark同等」=達成。「実プレイScriptとしてBenchmark同等」=現時点 PARTIAL。主な不足は量そのものではなく、良い会話がOptionalに偏り、Critical/Natural Routeでの人物愛着と生活密度が保証されていないこと。

  

QUALITY PASS修正方針（新規Canonを増やさず、既存v0.9資産を再配置する）:

QP-01｜S2 MIO BONDをNatural Routeへ1つ昇格【CANDIDATE】

MIO-A猫 / MIO-B待つ のどちらか1つを「通れば自然に遭遇するが、進行を止めないNatural Event」にする。新規台詞は作らずSECTION 2B/2C既存台詞を使用。推奨=MIO-B「待つ」。理由: 本作コアの「待つ」を説明ではなく行動で先に経験できる。

  

QP-02｜S3 MIO-C「ただ座る」をNatural Beatへ昇格【CANDIDATE】

ベンチ到着後、17:17前に短い無目的時間（風/空を見る/一言）を必ず視界に入れる。完全LOCKムービーではなく、数秒の自由/待機を許す。プロット情報を追加しない。目的=ミオ喪失前の生活記憶をCritical Routeにも残す。

  

QP-03｜Area B NPCを1会話だけNatural Routeへ【CANDIDATE】

既存の掃除の人/店主/子ども/老人/近所の人から1名だけ、B1→B3主導線上で自然に声がかかる配置にする。追加説明はしない。「NPC会話による世界理解」を必須説明ではなく生活として体験させる。残りはOptional。

  

QP-04｜S4〜S6のCore連打に「操作を返す間」を確保【DESIGN】

S4通知close→即S5演出にせず、C2で短時間UNLOCK。プレイヤー自身がベンチ/ミオ/周囲を見てから5席目へ近づく。S5→S6も調査終了後に一拍置く。台詞追加より「歩く/見る/待つ」で密度を作る。

  

QP-05｜S8〜S11の説明密度を増やさない【LOCK方針】

不足感を世界設定台詞で埋めない。S8の操作失敗、S9呼びかけ、S11空席というPlayer Action/Visualで理解させる。S10は最小開示を維持し、説明増量でBenchmark感を作らない。

  

QP-06｜Area B白層化variantの扱いを整理【HUMAN DECISION】

A案: CH01でArea Bを物理再訪させる（Scenario/Map変更が大きい）。

B案: CH01では再訪しない。Area Bの白層化variantを「将来/別経路候補」として品質評価から除外し、C2の同一地点再解釈をRewriteMemory固有のBenchmark-equivalent機能とする。

推奨=B。30分Prototypeの構造を増やさず、C2の再解釈を深くする。

  

QP-07｜通し音読/最短プレイ監査をLock条件へ追加【REQUIRED】

Critical Routeだけで、S1日常→S2同行→S3静かな時間→S4異常開始が感情的に成立するかを音読・実測する。評価項目: (a)ミオへの愛着がS4前に成立、(b)説明台詞が連続しない、(c)30〜90秒ごとにPlayer Action/会話/観察の質が変わる、(d)S8-S11で情報過多にならない。

  

Benchmark同等Quality Gate:

1\. Critical RouteでもS4前に「叔母の日常」「ミオとの同行」「ミオと何も起きない時間」の3つを体験する。

2\. Natural Route上で少なくとも1回、町のNPC会話を経験する。

3\. Optionalを選んだ場合は人物/世界理解が増えるが、選ばなくても感情の核が欠落しない。

4\. C2の5状態が台詞だけでなくNPC/音/光/Camera/Interactable/UIで差分化される。

5\. S4-S11で説明台詞を追加して密度を水増ししない。

6\. Critical/Natural/Completionistの3経路を通し、感情曲線と尺を実測する。

7\. 上記を満たすまでは「実プレイScript Benchmark同等」とLOCKしない。

  

NEXT: QP-01〜QP-04をSECTION 2B/2Cの既存台詞の再配置だけで試作し、Scenario×Map整合を再確認する。QP-06は人間決裁までB案を推奨案として扱い、Canon/Scenarioを勝手に変更しない。

  

Changelog追記: 2026-08-14 Authored Experience Quality Pass追加。SECTION 7の「資料粒度PASS」と実プレイ品質を分離。新規台詞増量ではなく、既存MIO-A/B/C・Ambient NPC・C2状態差分のNatural Route再配置を改善軸とした。

  
  

SECTION 9 — QUALITY PASS IMPLEMENTATION RESULT（QP-01〜04反映後）

  

2026-08-14、SECTION 8のQP-01〜04をSECTION 1 / 2B / 6へ実反映した。新規世界設定・新規Canon・新規ロケは追加していない。既存台詞/演出資産のRoute分類と制御テンポのみ変更。

  

反映結果:

・QP-01: MIO-B「待つ」をOptional Bond→Natural Routeへ昇格。プレイヤーに選択を強制せず、B2主動線上でミオが止まり「待つ」という行為を先に経験できる。

・QP-02: MIO-C「ただ座る」をOptional→Natural Beatへ昇格。17:17前に必ず通るが、ムービーLOCKにはせずUNLOCKの余白として保持。

・QP-03: Area B Natural Ambient NPCを1名だけ主動線へ置く。旧「おかえり。」固定案はv0.12以降のCanon GuardによりSUPERSEDED。v0.14では店先を掃く住人の短い生活会話をScript Candidateとして使用し、歩行LOCKなし。他NPCはOptional最大1名まで。

・QP-04: S4通知close後とS5調査後に短いUNLOCKを追加。Core Eventの自動連鎖を切り、プレイヤー自身が異変を見る/近づく/待つ時間を作った。

  

再監査（設計上。実機Playtest前）:

Q-02 Critical Route Dialogue Density: PARTIAL→PASS候補。S1叔母→S2ミオ同行/MIO-B→S3 MIO-Cが最短経路でも残る。

Q-03 Mio Bond on Natural Route: PARTIAL→PASS候補。MIO-BとMIO-CがNatural、MIO-AはOptionalとして追加報酬化。

Q-04 Ambient NPC / World Understanding: PARTIAL→PASS候補。Natural Routeで最低1回、町側から生活関係を確認するNPC発話を経験。

Q-08 Plot vs Life Balance: PARTIAL→PASS候補。S4→S5→S6の自動Core連打をUNLOCKで分節。

Q-09 Silence / Physical Acting: PASS候補→PASS候補（強化）。MIO-CがCritical/Natural Routeから欠落しなくなった。

  

残る未達:

・実機でCritical/Natural/Completionistの3経路を計測していないため、Benchmark同等を最終PASSにはしない。

・Q-06 Area B再訪は未決。推奨B案（再訪追加せずC2再解釈を深くする）を維持。

・Character Voiceは通し音読未実施。

・30〜90秒ごとの体験変化は実測未実施。

  

次のLock Gate: ①Critical Route通し音読、②30分尺のBeat秒数仮置き、③Critical/Natural/Completionistの想定所要時間比較、④説明台詞の連続箇所を削る。これを通過後に「実プレイScript Benchmark同等=PASS」を判定する。

  

Changelog追記: 2026-08-14 QP-01〜04実反映。MIO-B/MIO-C Natural化、Area B Natural Ambient 1発話、S4/S5後UNLOCKをSECTION 1/2B/6へ反映。実機Playtest前のため最終品質判定はPASS候補。

  

2026-08-14 v0.10相当更新: 上位入力Package/CH01\_DETAIL抽出を照合し、S10は12Scene IDとして保持しつつREAD-only開示Scene→Transition Beatへ縮退。CH01で「白層/アンログ/観測点を一部余韻を受け止める」機能はS8-S9の操作体験＋S11観測点示唆で維持。D-5TH-TRUTHは核のみ短縮、D-NOAHは必須から除外しCANDIDATE/ASSUMPTION保留。S10独立Disclosure Eventを使わず、5〜15秒UNLOCK＋夕闇/環境音でS9成功→S11構造的喪失を接続。Canon追加なし。

  

SECTION 10 — v0.10 S10 CONSISTENCY AUDIT

  

対象: SECTION 1 / 2 / 2A / 2B / 4 / 5 / 6 のS10参照。目的はTransition化後の旧READ表記を残さないこと。

・Scene ID S10/B10: KEEP。

・Role: CH01で必要な「一部理解」はKEEP。ただしS8-S9の操作体験を主、S10は余韻/短い再認識に変更。

・Control: UNLOCKED Transition。強制READ/VNを廃止。

・Dialogue: D-5TH-TRUTH-SHORTをReq。D-NOAHはCANDIDATE/ASSUMPTION・必須から除外。

・Event: EVT-DISCLOSUREはS10必須Eventとして使用しない。Transition自体はEvent追加なし。

・Map: Area C / C2周辺はASSUMPTIONを維持。時計塔内部は不使用。

・Flag: worldKnowledge=partialは実装変数未決。Story機能の「一部理解」と変数canon化を分離。

・S9→S10→S11: 呼びかけ成功→5〜15秒余韻→短い五席目再認識→S11呼びかけ/介入。CALLOUT SUCCESS≠CAPTURE CAUSEを維持。

・Benchmark quality: 旧READ-only問題は設計上解消。実機でS9後の安堵が感じられるかのみ未検証。

  

Consistency Verdict: SCRIPT DESIGN = PASS候補 / Canon Guard = PASS / Map Traceability = PASS候補 / Runtime Timing = NOT TESTED。

Remaining Lock Gate: Critical/Natural/Completionist 3パス実測と、IMAGE-02でS10 Transition位置・S11介入位置を実座標化する。

  
  

SECTION 11 — EXPLORATION INFORMATION LAYER v0.11（Map拡張×Script統合）

  

目的: IMAGE-01拡張方針をScriptへ安全に接続する。マップを広げる理由を歩行距離ではなく、探索による①世界理解、②ミオへの愛着、③次へ進みたくなる動機、④未解決の謎/引っ掛かりの形成とする。画像生成物に混入した具体設定・NPC台詞・書籍本文をそのままCanonへ逆輸入しない。既存Script/World/Story/Character Canonで根拠があるものを優先し、未確定はCANDIDATE/ASSUMPTIONとして隔離する。

  

情報役割タグ:

・WORLD = 世界の常識・生活・制度を、説明台詞ではなくNPC/掲示/本/生活物の異なる角度から理解する。

・MIO = ミオを人物評で説明せず、同行、待つ、ただ座る、町との関係、生活痕から好きになる。

・HOOK = 時計塔、17:17、通知、記憶局など、次の場所/Scene/CH02へ進みたくなる問いを残す。答えを先に言わない。

・MYSTERY = 記録・人数・名前・反応の食い違い等、CH01で完全解決しない違和感。Main Plot理解を阻害しない。

  

取得区分: Required = Main Scenario因果に必須。Natural = 主動線で自然に入るが長いLOCKをしない。Optional = 寄り道/再調査で人物・世界・謎の解像度が上がる。本筋理解の必須条件にしない。制作目安はRequired 40 / Natural 30 / Optional 30程度だがCanon値ではない。

  

AREA-A / S1: 大幅拡張しない。叔母の家事、食卓、決まった席、生活音で「普通」を記憶させる。母の部屋/花/写真等の既存FORESHADOW候補をMYSTERY/Optionalとして扱い、母の状態は断定しない。窓の時計塔遠景と玄関をHOOKとしてS2へ送る。

  

AREA-B / S2（主要拡張対象）: 正本B1坂上→B2生活圏→B3坂下はKEEP。体感幅を約1.5〜2倍へ拡張するが新規Location IDは作らない。Main RouteはD-5MIN→MIO-B「待つ」Natural→NPC-B2-AMBIENT-01 Natural→B3。Optional枝A=MIO+WORLD（既存MIO-A猫/生活圏小物）、枝B=WORLD+MYSTERY（既存掲示板/店先等のCd候補）、枝C=HOOK+MYSTERY（坂の湾曲/見晴らしから時計塔を視認）。小ループで主動線へ自然復帰し、寄り道を収集作業にしない。具体ルート形状はIMAGE-02で確定する。旧「おかえり。」固定案はSUPERSEDED。

  

AREA-C / S3-S11: C1→C2をKEEP。情報量を増やすより滞在余白を作る。MIO-C「ただ座る」/二番目の席/風/名前を呼ぶ実演をMIO/NaturalとしてS4前に保証。17:17通知→五席目→選択→逆流→呼びかけ→S10余韻→S11介入をHOOK/Coreとして維持。S8-S11で制度説明を追加しない。C2の平常→17:17後→白層化↑→逆流→連れ去り後をNPC数/音/光/Camera/Interactable/UIで差分化し、CH01の主要な再解釈体験とする。

  

NPC会話ルール: 各NPCにWORLD/MIO/HOOK/MYSTERYの主役割を原則1つ、必要なら副役割1つ。設定資料を朗読させない。同じ事実をNPC/本/掲示で重複説明しない。MIO役割は人物評より日常的な反応を優先。MYSTERYは答えを言わず、別情報とわずかに噛み合わない程度。Natural NPCは歩行を止めない1〜2行を基本とする。

  

Book / Notice / Inspectルール: Bookを世界設定の万能説明装置にしない。既存Canonに根拠がある短い断片のみ。Noticeは現在の町の表向きの常識。Inspectは生活/人物/空間の意味。Environmental clueは文字を読まなくても分かる差分を担当し、可能なら台詞より優先する。同じ情報を複数媒体で再説明しない。

  

Map×Script Lock条件追加: A)AREA-B拡張が単なる移動時間増加でない。B)Optional枝2〜3本すべてに情報報酬がある。C)Critical RouteでもS4前にMIO愛着と町の日常を体験。D)Optionalを無視してもMain Scenario因果を理解可能。E)CH01終了時に最低1つのMYSTERY/HOOKが未解決でCH02への興味になる。F)S8-S11説明台詞を増量しない。G)画像側仮設定をCanonへ逆輸入しない。H)IMAGE-02で各NPC/Book/Notice/InspectへRole+Acquisition+Area/Zone+State Variantを1:1配置する。

  

v0.11判定: Script Architecture=PASS候補 / Exploration Narrative=PASS候補 / Canon Guard=PASS / Map Geometry=IMAGE-02待ち / Runtime=NOT TESTED。

次工程: IMAGE-02でAREA-B拡張ルートと情報ポイントを実配置し、S0-S11 / B1-B3 / C1-C2との矛盾を再監査。その後Critical/Natural/Completionist 3パスをGodotで実測する。

  

Changelog追記 2026-08-15 v0.11: IMAGE-01拡張方針を既存Detailed Scriptへ統合。WORLD/MIO/HOOK/MYSTERY + Required/Natural/Optional のExploration Information Layerを追加。AREA-BはB1-B3を維持したままOptional枝2〜3＋小ループをIMAGE-02候補化。具体NPC台詞・本・掲示本文は画像から逆輸入せずCanon照合後に確定。S8-S11/S10 Transitionは増量しない。

  
  

SECTION 12 — BENCHMARK GUIDE PATTERN → AREA-B DIALOGUE / INSPECT PASS v0.12

  

参照：Google Drive「MOTHER3公式ガイド\_マップ&ガイド\_第1章\_テキスト化」A1:G31を再確認。Referenceは純粋な全台詞集ではなく、各節で「現在地/人物→話す・調べる・操作する→具体的な成果/情報→障害または状態変化→次の目的」を連結する進行ガイド構造を持つ。例として、地図NPCはNPC位置→会話→地図取得/使い方→次目的地、祈り場は場所→NPC誘導→プレイヤー名入力→意味づけ、火事区間はNPC証言→敵/環境変化→装備/救出→次の目的、再訪区間は火事後の地形/敵/取得物変化を同じ場所の再解釈として扱う。RewriteMemoryでは内容をコピーせず、この「会話/調査が必ずPlayer ActionまたはNext Goalへ接続する」構造を採用する。

  

12A. Benchmarkから採る会話設計原則

1\. NPCは世界設定を語るためだけに置かない。話すと「行く場所が分かる」「操作を覚える」「人物関係が分かる」「準備ができる」「異変の証拠が増える」のいずれかが起きる。

2\. 1会話の中に説明を詰め込まず、場所・NPC・物・次目的を空間的に連結する。

3\. Optionalは本筋の再説明ではなく、回復/準備/世界理解/人物理解/再訪発見など別の報酬を持つ。

4\. 同じ場所を状態変化後に使う場合、台詞だけでなく道・敵・物・取得物・利用可能性が変わる。RMではC2の音/光/NPC/Interactable/UI差分へ変換する。

5\. 本文は「何が起きるか」だけでなく「だから次に何をしたくなるか」まで書く。Dialogue Scriptでも各ブロックにNEXTを持たせる。

  

12B. AREA-B Critical/Natural Dialogue Pass

  

\[B2-P01 / WORLD / Natural\] 店先・生活物

発火：B1からB2へ入り、店先の視界範囲を通過。会話LOCKなし。

◇ 店先では、誰かが朝から使った箱や値札を片づけている。町は普通に動いている。

■ 任意Inspect 1回目：◇ 品物が並んでいる。値段が書いてある。

■ 2回目以降：◇ さっき見たものだ。まだ、ここにある。

PURPOSE：白峰市に商店/通貨/文字があるという確認済みWorld範囲を、百科事典説明でなく生活物として見せる。

NEXT：生活圏の人の動きへ視線を送る。

STATUS：CANDIDATE。固有店名/商品名/通貨名は作らない。

  

\[B2-P02 / WORLD(+MIO) / Natural Ambient\] すれ違う住人

発火：主動線上でNPCとすれ違う。自動LOCKなし。話しかけた場合のみ短会話。

\[住人\] ◆ おはよう。今日は、落ち葉の方が早起きだ。

◇ 住人は話しながら箒を動かし続ける。会話のために町の生活は止まらない。

\[ミオ\] ◇ 足元の落ち葉を見て、少しだけ笑う。

〔任意で話しかける〕

\[住人\] ◆ ほら、また一枚。きりがないね。

\[ミオ\] ◆ ……負けてるね。

〔再度話す〕

\[住人\] ◆ まだ負けてるよ。

PURPOSE：二人が特殊な存在として隔離されず、普通の町の日常の中を歩いていることを示す。

NEXT：NPCの先でミオが歩みを緩める→P04。

STATUS：SCRIPT CANDIDATE。旧「おかえり」はCanon根拠がないためv0.12では固定台詞から外し、より中立な生活挨拶へ置換候補。

  

\[B2-P04 / MIO / Natural\] 「待つ」

発火：NPCを抜けた先の踊り場。ミオが2〜3歩先で止まる。Control=UNLOCKED。

◇ ミオが立ち止まる。何かを見ている。

▶ プレイヤー行動：先へ進む / その場で待つ。

├〔先へ進む〕 \[ミオ\] ◆ あ、待って。

└〔待つ〕 ◇ 数秒、同じ方向を見たまま並んで立つ。

   \[ミオ\] ◆ ……トウは、待ってくれるんだ。

   \[トウ\] ◆ ……うん。

   \[ミオ\] ◇ 少しだけ笑って、歩き出す。

PURPOSE：ミオの人物説明ではなく、Player Action→Mio Responseで関係を作る。後半「待つ」の攻略意味を説明せず先に身体化する。

NEXT：ミオが再び歩き出した方向にOptional Pocketの掲示面が見える。

STATUS：既存MIO-BをBenchmark型に再構成。文芸FINALではない。

  

12C. AREA-B Optional WORLD→MYSTERY Chain

  

\[B2-P03 / WORLD / Optional\] 町の掲示面

発火：主動線から見える掲示面へ寄り道しInspect。

■ 1回目：◇ 町のお知らせが何枚か貼られている。買い物、施設、暮らしの案内。どれも読める。

■ 2回目以降：◇ 紙の端が風で揺れている。特別なことは書いていない。

PURPOSE：行政/商店/文字/書物が普通にある世界という確認済み範囲だけを伝える。具体条例・行事・時計塔時刻表は新造しない。

NEXT：掲示面の一段奥/横にP06の「小さなズレ」が見える。

  

\[B2-P06 / MYSTERY / Optional\] 表記の小さなズレ

発火：P03を見た後、同じOptional Pocketの別面をInspect。P03未閲覧でも調査可。

■ 1回目：◇ 一枚だけ、文字の並びと紙の剥がれ跡が、少し合っていない。

\[トウ\] ◆ ……貼り直したのかな。（内語）

■ 2回目以降：◇ 読めないわけじゃない。なのに、どこが変なのか説明できない。

PURPOSE：「白層化」「記憶局」「ノア」を言葉で出さず、普通のWORLDの直後に弱いMYSTERYを置く。

NEXT：答えは出ない。主動線へ戻るとミオのOptional Loop/P05または塔方向へ。

STATUS：DESIGN CANDIDATE。固有情報欠落を新Canon化しない。

  

12D. AREA-B Optional MIO Mini-Story

  

\[B2-P05 / MIO / Optional\] 短い寄り道

発火：小ループ入口付近でミオが何かに気づく。現行MIO-A猫はCANDIDATEのまま使用。

\[ミオ\] ◆ あ、……。

◇ ミオが主動線から少し外れた方を見る。

〔寄り道する〕

◇ 猫がいる。

\[ミオ\] ◆ ……大丈夫かな。

\[ミオ\] ◆ 大丈夫。たぶん。

◇ 近づくと猫が逃げる。

\[ミオ\] ◆ ……逃げちゃった。

\[トウ\] ▶（追わない / もう少し見る）

├〔追わない〕 ◇ ミオも追わない。少しだけ、その場にいる。

└〔もう少し見る〕 ◇ 猫は少し離れた場所からこちらを見ている。

\[ミオ\] ◆ 帰ろっか。

PURPOSE：プロット情報ゼロでも「一緒に寄り道した記憶」を作る。Referenceで本筋外のNPC/アイテムが世界・人物・準備の別報酬を持つ構造に対応。

NEXT：小ループがB2 COREへ戻り、P07の塔Revealへ接続。

STATUS：CANDIDATE。猫自体がCanon必須要素ではないためIMAGE-02/Playtestで採否可。

  

12E. AREA-B HOOK Dialogue / Landmark

  

\[B2-P07 / HOOK / Natural\] 時計塔Reveal

発火：Optional/Naturalルート合流後。建物/樹木の遮蔽が切れる。強制Camera Panなし。

◇ 坂の先で、時計塔の全体が見える。

\[ミオ\] ◆ 塔、見えてきた。

\[トウ\] ◆ ……あと五分？

\[ミオ\] ◆ うん。たぶん。

◇ ミオは塔を見たまま、少しだけ歩く速度を落とす。

PURPOSE：時計塔の設定を説明せず、ミオの反応で「この場所には個人的な意味がある」とだけ感じさせる。

NEXT：B3出口→C1→C2ベンチ。「なぜここへ毎日来るのか」をS3-S5へ持ち越す。

STATUS：既存Dialogue/Scenarioから再構成。塔内部/鐘/ノア/制度は非開示。

  

\[B2-P08 / ROUTE / Required\] B3出口

発火：B3境界へ到達。

◇ 生活圏の音が少し遠くなる。塔の前の開けた場所が見える。

\[ミオ\] ◆ ……こっち。

⚙ → AREA-C / C1。

PURPOSE：AREA-Bで説明を完結させず、WORLD→MIO→弱いMYSTERY→HOOKを抱えたままCへ送る。

NEXT：S3「二番目の席」。

  

12F. Benchmark-equivalent Information Economy Check

Critical/Natural Routeで得るもの：P01=町は普通に暮らしている(WORLD)／P02=二人はその生活圏に自然に存在する(WORLD+MIO)／P04=ミオとの関係を操作で経験(MIO)／P07=塔への個人的意味を感じる(HOOK)／P08=次の場所へ。

Optionalで増えるもの：P03=町の表向きの日常(WORLD)／P06=説明できない小さなズレ(MYSTERY)／P05=ミオとの無目的な共有時間(MIO)。

禁止：OptionalでMain Plotの必須答えを渡さない。P03とP06で同じ情報を繰り返さない。NPCに白層化/記憶局/ノアを説明させない。塔の内部設定を漏らさない。ミオを「優しい子」と人物評で説明しない。

  

12G. Referenceとの差分評価

Referenceは、NPC会話が地図取得、プレイヤー名入力、回復物取得、危険情報、装備準備、救出先決定など具体的なGameplay Outcomeへ頻繁に接続する。RewriteMemory CH01 AREA-Bは戦闘/装備/アイテム取得が少ないため、そのまま模倣すると不自然になる。代わりにGameplay Outcomeを「Route Choice / Companion Response / Inspect Discovery / Landmark Hook / State Reinterpretation」として設計する。この差はジャンル差による意図的変換であり、Referenceの文章量だけを真似てNPC説明を増やさない。

現状評価：AREA-B Dialogue/Inspect Structure = Benchmark-equivalent候補。Character Voice = 通し音読待ち。Map Geometry = IMAGE-02配置待ち。Runtime Density = NOT TESTED。

  

12H. IMAGE-02 Handoff

Pin順：B1 ENTRY → P01 → P02 → P04 → \[P03→P06 Optional Pocket\] / \[P05 Optional Loop\] → P07 → P08 → C1。

各Pinに「Role / Acquisition / Script ID / NEXT」を表示する。推奨Script ID候補：INT-B2-SHOPFRONT / NPC-B2-AMBIENT-01 / EVT-MIO-WAIT / INT-B2-NOTICE / INT-B2-MISMATCH / EVT-MIO-DETOUR / EVT-TOWER-REVEAL / EXIT-B2-C1。IDはImplementation CandidateでありCanon IDではない。

Lock条件：①P04を最短ルートで経験可能、②P02は歩行を止めない、③P03/P06は30〜60秒以内の寄り道で完結、④P05は小ループで自然復帰、⑤P07後は塔/C1方向が迷わない、⑥AREA-B全体を通して設定説明3行以上のNPC会話を置かない。

  

Changelog追記 2026-08-15 v0.12: Google DriveのMOTHER3公式ガイド\_マップ&ガイド\_第1章\_テキスト化 A1:G31を再読し、Referenceの「場所/NPC→Action→Outcome→Next Goal」構造を抽出。AREA-B P01〜P08へ実会話/Inspect Draftを追加。旧「おかえり」はCanon根拠不足のため固定から外す候補とし、中立的な生活挨拶へ変更。具体固有設定は追加せず、WORLD/MIO/MYSTERY/HOOKをGameplay Outcomeへ接続した。

  
  

SECTION 13 — AREA-A / AREA-C BENCHMARK GUIDE PASS + CH01 THROUGHLINE AUDIT v0.13

  

目的：SECTION 12でAREA-Bへ適用したReference構造「場所/NPC→Action→Outcome→Next Goal」を、既存AREA-A/C Scriptへも適用し、CH01全体の会話・調べ物が実際のPlayer Actionと次の目的に接続しているかを監査する。新規Canonは増やさず、既存SECTION 1/2B/2Cの台詞・Interactableを再編集/分類する。

  

13A. AREA-A — 朝の家：会話/Inspectを「外へ出る理由」へ接続

  

\[A1-P01 / LIFE / Required-Natural\] 起床・自室

発火：S1開始。Control=UNLOCKED。

◇ 朝の光。生活音がする。母の部屋の方向だけ静か。

\[トウ\] ◆ ……いかなきゃ。（内語）

■ ベッド 1回目：◇ もう、あたたかくない。

■ 自室の私物 1回目：◇ 見慣れた物ばかり。ひとつずつ、名前が言える。

PURPOSE：操作チュートリアルと「普通の生活」の基準を同時に作る。

OUTCOME：Playerが歩く/調べるを覚える。

NEXT：A2の生活音と叔母へ。

  

\[A2-P02 / WORLD+LIFE / Required\] 叔母との朝

発火：A2で叔母に話す。

\[叔母\] ◆ おはよう、トウ。

\[叔母\] ◆ ……顔に書いてある。「きょうも、だれかを待ちます」って。

\[トウ\] ◆ …そうかな。

\[叔母\] ◆ 会うまえは、みんな すこし待つものよ。

◇ 叔母は話しながら家事を続ける。会話のために生活が止まらない。

PURPOSE：ReferenceのNPC会話同様、人物紹介だけでなく「次に会う相手=ミオ」と「待つ」という行動を生活会話から準備する。

OUTCOME：家→ミオとの同行へ感情的な目的が生まれる。

NEXT：名→安心の伏線、任意A3調査、玄関。

  

\[A2-P03 / FORESHADOW / Required-short\] 名前と安心

\[叔母\] ◆ あの子は、名前を呼ばれると安心するって……お母さんが、よく言ってた。 ★

\[トウ\] ▶（聞き返す / 何も言わない）

├〔聞き返す〕 \[叔母\] ◆ ……たぶん、ね。

└〔何も言わない〕 ◇ 叔母は少し困った顔で笑う。

PURPOSE：後半のCalloutを攻略説明にせず、日常の会話として先に置く。

OUTCOME：「名を呼ぶ」という行為が後で再解釈される。

NEXT：A3の母の痕跡へ興味を残すが、必須調査にはしない。

  

\[A3-P04 / MYSTERY / Optional\] 母の部屋

■ 戸 1回目：◇ 少しだけ、開いている。

■ 花 1回目：◇ 花がある。毎日、だれかが替えている。

■ 室内 1回目：◇ 中は、音がしない。

■ 再調査：◇ ここだけ、時間が止まっているみたいだ。

PURPOSE：ReferenceでOptional NPC/物が本筋外の世界理解を増やす構造に対応。母の状態を答えず、「在るのに意味がつながらない」感覚を報酬にする。

OUTCOME：MYSTERY取得。observation+候補。

NEXT：答えは出ない→玄関へ戻る。

  

\[A3-P05 / HOOK / Natural\] 時計塔遠景と玄関

■ 窓：◇ 屋根の向こうに、時計塔。いつもの位置に、いつもの影。

■ 玄関：◇ 外へ。坂の下の方から、風。

PURPOSE：Referenceの「次の目的を地図/人物/場所で明示する」原則を、RMではランドマークと出口で実現する。

OUTCOME：プレイヤーが次に行く方向を視覚的に理解。

NEXT：AREA-B/B1でミオと合流。

  

AREA-A Quality Note：会話を増やす必要はない。叔母とのRequired会話は「待つ」「名前」の2機能で十分。母について質問→説明、世界制度の説明、時計塔説明を追加するとReference型ではなくLore Dumpになるため禁止。

  

13B. AREA-C — 同一場所を「Action→State Change→Next Goal」で再解釈

  

\[C1-P01 / MIO / Required-Natural\] ベンチへ行く

発火：AREA-BからC1へ入る。

\[ミオ\] ◆ ……こっち。

◇ ミオがC2のベンチへ先に向かう。

\[ミオ\] ◆ 一番端は、近すぎるの。

\[ミオ\] ◆ …二番目がいい。

PURPOSE：場所選択自体を人物情報にする。

OUTCOME：C2の「二番目」をプレイヤーが記憶する。

NEXT：座る/ただ待つ。

  

\[C2-P02 / MIO / Natural Required\] ただ座る

◇ しばらく、何も起きない。風が吹く。Control=UNLOCKED。

\[ミオ\] ◆ ……風、気持ちいいね。

◇ ミオが空を見る。プレイヤーはベンチ/塔/周囲を見てもよい。

PURPOSE：プロット報酬ゼロの共有時間を、後の喪失価値へ変換する。ReferenceのOptional生活/寄り道が人物を好きにさせる役割を、Critical Routeへ移植。

OUTCOME：ミオとの生活記憶。

NEXT：名前/静けさの短い実演。

  

\[C2-P03 / MIO+FORESHADOW / Required-short\] 呼びかけの実演

\[ミオ\] ◆ ここに座ってると、少しだけ静かになる。

\[トウ\] ◆ ミオ。 ★

◇ 一瞬、周囲の音が止まる。

\[ミオ\] ◆ …今の、止まった。ちゃんと、私だった。 ★

PURPOSE：後半の正解をUIチュートリアルで教えず、会話と音で経験させる。

OUTCOME：mioNameStability=high候補。

NEXT：17:17までその場所に留まる理由が生まれる。

  

\[C2-P04 / MYSTERY / Required\] 17:17通知

⚙ 時刻17:17。端末が鳴る。

\[トウ\] ◆ …送った覚えの、ない通知。（内語）

⚙ 本文は空白。既読だけが付いている。

\[ミオ\] ◆ …来たんだ。 ★

\[ミオ\] ◆ たぶん、それ、まだ見ちゃだめ。 ★

◇ 環境音が一段引く。

PURPOSE：Referenceの「NPC/出来事が次の調査対象を明確にする」構造。通知自体が次Actionを作る。

OUTCOME：Player Suspicion。UIは--%欠損で答えを伏せる。

NEXT：通知close後Controlを返す→プレイヤー自身がベンチへ戻る。

  

\[C2-P05 / MYSTERY+OBS-RISK / Required\] 五席目

\[ミオ\] ◆ ……ほら、五つ目。 ★

\[トウ\] ◆ 席は、四つしかないよ。 ★

\[ミオ\] ◆ ……そう、だよね。

■ 5席目を調べる：◇ 何かの跡。影のような、へこみのような。

◇ 剥落音。

PURPOSE：Dialogue→Inspectへ直結。会話だけで謎を進めない。

OUTCOME：fragmentCount+/observation+候補。プレイヤー自身が調べたため後の因果反転が自分事になる。

NEXT：一拍UNLOCK→S6態度選択。

  

\[C2-P06 / CORE / Required\] 最初の態度選択

▶ observe / avoid / ask / wait。

PURPOSE：謎の正解当てではなく、自分がどう関与するかを入力させる。

OUTCOME：observation/mioTrust/playerChoseNotToLook等の実装候補。

NEXT：S8で選択の意味を再解釈。

  

\[C2-P07 / CORE / Required\] 観測操作が悪化させる

◇ ミオの色が抜ける。

▶ 移動する / 触れる / 追跡する / 記録する。

⚙ 一方的に対象を確定しようとする操作のたび率が上がる。

\[トウ\] ◆ …ぼくが、見たから。

⚙ ここで初めて欠損ラベルが「白層化率」として判読可能。

PURPOSE：Referenceの危険地帯/戦闘/道具のように、テキストではなくGameplay Outcomeでルールを学ばせる。

OUTCOME：観測=悪化をPlayerが操作で理解。

NEXT：別の動詞を探す。

  

\[C2-P08 / CORE+MIO / Required\] 呼びかけ

▶ 見ない / 聞く / 待つ / 名を呼ぶ / 手を取る。

\[トウ\] ◆ ミオ。 ★

◇ 他の音が引く。

\[ミオ\] ◆ …今の、ちゃんと、私だった。 ★

PURPOSE：A2/P03とC2/P03で経験した「名」を、攻略として自分でつなげる。

OUTCOME：呼びかけ成功。mioNameStability=restored / relationAnchor候補。

NEXT：成功をすぐ否定せずS10余韻へ。

  

\[C2-P09 / MIO+HOOK / Natural\] S10余韻

⚙ 5〜15秒Control=UNLOCKED。

\[ミオ\] ◆ ……五つ目は、ほんとにあった。

◇ 夕闇。環境音は完全には戻らない。

PURPOSE：Referenceの「救出後に戻って報告/状況が変わる」ような結果確認の役割。ただし説明READではなく空間を見せる。

OUTCOME：プレイヤーは「成功した」と感じる。

NEXT：何かが来る気配→S11。

  

\[C2-P10 / CORE / Required\] 呼びかけ成功→制度介入

\[トウ\] ◆ ミオ。 ★

\[ミオ\] ◆ はい。 ★

◇ 一度、輪郭が鮮明に戻る。

◇ 直後に記憶局が現れる。原因機序は断定しない。

\[記憶局\] ◆ ……保護のため、です。

⚙ Control=LOCKED。ミオが連れ去られる。

PURPOSE：成功を偽物にせず、その後に別レイヤーの障害を置く。

OUTCOME：mio\_carried\_lost=true / observer\_is\_tou=true候補。

NEXT：同じベンチを再度見る。

  

\[C2-P11 / REINTERPRET / Required-Natural\] 連れ去り後の同一地点

■ 二番目の席：◇ もう、あたたかくない。

■ ベンチ全体：◇ だれもいない。二番目の席が、まだ少し、へこんでいる。

■ 時計塔：◇ 夜。同じ塔なのに、意味が、変わってしまった。

PURPOSE：Referenceの再訪/状態変化をRM固有の「同じ場所の意味が変わる」に変換。新マップを増やさずC2を再解釈させる。

OUTCOME：喪失をPlayerの実記憶と空間差分で成立。

NEXT：端末通知。

  

\[C2-P12 / HOOK+MYSTERY / Required\] 送信者反転

⚙ 「次回観測予定：明日17:17」。送信者がミオ→トウへ反転。

\[トウ\] ◆ 送った覚えは、なかった。でも、既読だけは付いていた。 ★

\[トウ\] ◆ …必ず、取り戻す。

PURPOSE：CH01の答えを全部出さず、CH02の行動目的を明確にする。

OUTCOME：notification\_sender\_inverted=true候補。HOOK保持。

NEXT：CH02。

  

13C. CH01 Throughline — Benchmark Style 23節との接続監査

01 S0 Hook：Mystery only。PASS。

02 A1操作習得：Action=walk/inspect、Outcome=生活基準。PASS。

03 A2叔母：Action=talk、Outcome=待つ/名前、Next=ミオ。PASS。

04 A3母Optional：Action=inspect、Outcome=MYSTERY、Next=戻る。PASS。

05 A3窓/玄関：Action=look/exit、Outcome=塔/方向。PASS。

06 B1-B2同行：Action=walk、Outcome=MIO関係。PASS。

07 P01/P02生活圏：Action=walk/talk、Outcome=WORLD。PASS候補。

08 P03/P06寄り道：Action=inspect、Outcome=WORLD→MYSTERY。PASS候補。

09 P05 MIO寄り道：Action=detour、Outcome=Bond。PASS候補。

10 P07/P08塔Reveal：Action=walk、Outcome=HOOK、Next=C。PASS。

11 C1/C2着席：Action=sit/linger、Outcome=MIO記憶。PASS。

12 名前実演：Action=call、Outcome=一時安定。PASS。

13 17:17：Action=open notification、Outcome=Suspicion。PASS。

14 五席目：Action=inspect、Outcome=異常証拠。PASS。

15 四択：Action=choose、Outcome=態度Flag。PASS。

16 S7再構成：UNDECIDED。品質点から除外。

17 S8逆流：Action=try conventional verbs、Outcome=悪化。PASS。

18 S9別動詞探索：Action=choose/call、Outcome=回復。PASS。

19 呼びかけ成功：Action=call/wait for response、Outcome=本物の成功。PASS。

20 S10余韻：Action=look/linger、Outcome=結果確認。PASS。

21 S11介入：Action=call→LOCK、Outcome=制度的喪失。PASS。

22 C2再解釈：Action=look/inspect、Outcome=同じ場所の意味変化。PASS候補（実装でControl時間要確認）。

23 通知反転：Action=read、Outcome=CH02目的。PASS。

  

13D. 会話量・説明臭さ監査

Critical Routeの長い説明会話：0件を目標。叔母、ミオ、記憶局はいずれも短文中心。

3行以上連続してWorld Loreを説明するNPC：禁止。現Draftでは該当なし。

同じ情報の重複：

・「待つ」＝叔母は概念、P04は操作、S9は攻略。役割が異なるためKEEP。

・「名前」＝叔母は生活伏線、S3は実演、S9/S11は攻略/決着。役割が異なるためKEEP。

・「時計塔」＝Aは遠景、Bは接近Hook、Cは意味の器。段階差があるためKEEP。

・「最初の日を思い出せない」＋母の記憶揺らぎ＋掲示のズレ：MYSTERYが3本並ぶため、Natural Routeで全部強く見せると過密。P06はOptionalかつ弱いVisual表現を維持。

削減候補：旧SECTION 2CのArea-B住人「店主/子ども/老人/近所の人」全員をPrototypeへ同時採用しない。P02 1名＋必要ならOptional 1名まで。旧掲示/自販機/側溝/迷い貼り紙/看板等も全採用しない。P03/P06＋生活物1〜2点で十分。

  

13E. Mio Affection Gate before S4

Critical RouteでS4前に保証する体験：

A) トウが誰かを待っていることを叔母から知る。

B) AREA-Bでミオと並んで歩く。

C) P04で「待つ」機会を持つ。

D) C2でミオが二番目を選ぶ。

E) 数秒ただ座り「風、気持ちいいね」を共有する。

F) 名を呼ぶとミオが「ちゃんと私だった」と返す。

判定：設計上 PASS候補。Optional猫を見なくても愛着の最低線は成立する構造になった。最終判定は音読/実機。

  

13F. Next-Hook Gate

AREA-A終端：「外へ/ミオへ」=明確。

AREA-B終端：「なぜ塔へ？」=明確。

S3終端：「17:17に何が起きる？」=明確。

S4終端：「空白通知は何？」=明確。

S5終端：「どう向き合う？」=明確。

S8終端：「別のやり方は？」=明確。

S9終端：「助かったのか？」=明確。

S11終端：「取り戻す/明日17:17」=CH02へ明確。

判定：PASS。

  

13G. Benchmark Quality Verdict v0.13

Documentation Granularity：PASS（既達成）。

Map→Dialogue/Inspect→Outcome→Next Goal Coupling：PASS候補。

AREA-A Life/Character Density：PASS候補。

AREA-B World/Mio/Mystery/Hook Density：PASS候補。

AREA-C State Reinterpretation：PASS候補、かつRewriteMemory固有の強み。

Mio Affection before Anomaly：PASS候補。

Lore Dump Control：PASS。

Optional Reward Diversity：PASS候補。

Character Voice：NOT TESTED（通し音読待ち）。

Runtime Pacing：NOT TESTED。

IMAGE-02 Coordinates/Geometry：PENDING。

総合：Script DesignはReferenceの構造原則と同等水準へ到達候補。ただし「実プレイ同等」は音読/実機/IMAGE-02座標化前なのでLOCKしない。

  

13H. 次工程（順序固定）

1\) IMAGE-02へA1-P05 / B2-P01〜P08 / C2-P01〜P12のうちMap Pinが必要なものだけ配置。台詞全文を画像へ書かずScript IDを付す。

2\) Critical Route通し音読。S0→S11を実際に読み、S4前の愛着と後半説明密度を確認。

3\) Beat秒数仮置き：AREA-A / B / C、会話LOCK、UNLOCK、Optionalを計測表へ。

4\) Critical / Natural / Completionistの想定30分を比較。

5\) その後にDialogue文芸FINAL Pass。先に台詞を磨き込みすぎない。

  

Changelog追記 2026-08-15 v0.13: AREA-B v0.12に続きAREA-A/CへBenchmark Guide Patternを適用。既存会話/InteractableをAction→Outcome→Next Goalへ再接続。CH01 23節Throughline、会話量/Lore Dump、Mio Affection、Next Hookを監査。新規Canonなし。Script Design=Benchmark-equivalent候補、Runtime/Character Voice/IMAGE-02は未検証のため最終LOCK保留。

  
  

SECTION 14 — BENCHMARK SCRIPT TEXTURE PASS v0.14（実ページ比較反映）

  

参照範囲：Driveフォルダ「1SBtteehy30WrwyqZOTgYE8jKSfuBdUM-」内の索引および実ページ（代表: IMG\_6447 / 6448 / 6451 / 6475）。ここで採るのは固有台詞や設定ではなく、スクリプトの質感・密度・状態差分の設計原則のみ。MOTHER3固有表現はコピーしない。

  

14A. 実ページから追加で確認できた強み

・短いNPCでも「情報提供係」ではなく、その人自身の口調・癖・生活行動がある。

・1回目の会話だけでなく、再度話した時の短い差分がある。プレイヤーが「もう一度押してみる」こと自体に小さな報酬がある。

・本筋に不要なNPC/物でも、世界の温度、可笑しさ、人間関係を増やす。Optionalの報酬がLoreだけに偏らない。

・事件後/状況変化後は、同じ人物・同じ物への反応が変わる。再訪の価値を台詞だけでなく文脈差分で作る。

・NPC発話、調べ物、ト書きが混在し、長文説明より多数の短い観察で世界像を組ませる。

・危機前に普通の会話/少し変な人/生活物を十分経験させることで、危機後の変化が効く。

  

14B. RewriteMemoryへの変換方針

1\. CH01のNPC数はReferenceと同数へ増やさない。30分PrototypeではNatural 1名＋Optional最大1名程度でよい。

2\. その代わり採用NPCには「初回 / 任意会話 / 再会話」の最低2段階を与え、短い人格を出す。

3\. NPCの役割はWORLDだけにしない。生活の可笑しさ・ミオの反応を通してLIFE/MIOを副報酬にする。

4\. 調べ物も「謎の伏線」ばかりにしない。AREA-A/Bでは平常の生活物を優先し、S4前のMYSTERY過密を避ける。

5\. State Variantは物理的に再訪する対象だけをPrototype品質に数える。AREA-B白層化variantは将来候補、C2 State Variantを現行本命とする。

6\. 台詞の面白さを世界設定の奇抜さで作らない。言葉遣い、行動、間、再会話で人物を立てる。

  

14C. AREA-A Life Texture追加候補（Canon追加なし）

\[A2-LIFE-01 / Optional\] 食卓のカップ

■ 1回目：◇ 食卓の端に、叔母がいつも使うカップ。今日も同じ場所にある。

■ 2回目：◇ さっきより、湯気が少ない。

PURPOSE：不穏さゼロの生活記憶。後半の喪失に直接説明でつなげない。

STATUS：CANDIDATE。既存食卓/食器資産の使い方候補。

  

\[A2-LIFE-02 / Optional\] 家具の修繕跡

■ 1回目：◇ 直した跡がある。まだ使えるから、捨てない。

■ 2回目：◇ きれいじゃない。でも、ここではこれでいい。

PURPOSE：この家の価値観を物から感じる。世界謎ではなく「帰る場所」の質感。

STATUS：CANDIDATE。既存家具修繕跡資産の短文化。

  

AREA-A採用優先順位：LIFE 2〜3点 \> MYSTERY 1〜2点。写真/時計/食器の「数が違う」「名前が抜ける」系を全採用しない。危機前から全てが不穏だと、正常状態の記憶が弱くなる。

  

14D. AREA-B NPC Voice Pass

\[NPC-B2-AMBIENT-01 / Natural / LIFE+WORLD\]

初回すれ違い：

\[住人\] ◆ おはよう。今日は、落ち葉の方が早起きだ。

◇ 箒は止まらない。

\[ミオ\] ◇ 足元の落ち葉を見て、少し笑う。

任意で話しかける：

\[住人\] ◆ ほら、また一枚。きりがないね。

\[ミオ\] ◆ ……負けてるね。

再会話：

\[住人\] ◆ まだ負けてるよ。

PURPOSE：町が機能しているというWORLDを説明せず、生活行動と軽い可笑しさで記憶させる。ミオも説明役ではなく、その場への反応で人柄を出す。

STATUS：SCRIPT CANDIDATE / 非Canon。Playtestで台詞が作為的ならさらに短縮可。

  

Optional NPCを追加する場合の条件：P03/P06/P05と情報役割が重複しないこと。追加するなら「塔/白層化/記憶局を語る人」ではなく、町の普通さや小さな個性を担当する。Prototypeでは0〜1名。

  

14E. Inspect Repeat Reward Pass

\[B2-P01 店先\]

1回目：◇ 箱が積まれている。値札の向きだけ、きれいに揃っている。

2回目：◇ 一つ売れたらしい。空いた場所だけ四角い。

目的：WORLDではなく「今この瞬間も町が動いている」感覚。実装負荷が高ければ2回目は同文で可。

  

\[B2-P03 掲示\]

1回目：◇ 町のお知らせが何枚か貼られている。特別なことは書いていない。

2回目：◇ 読み返しても、やっぱり普通のお知らせだ。

目的：P06の異常との差を作るため、P03自身は正常であることを守る。

  

\[B2-P06 小さなズレ\]

1回目：◇ 一枚だけ、文字と剥がれ跡の位置が少し合わない。

2回目：◇ 読める。意味も分かる。なのに、そこだけ目が戻ってしまう。

目的：答えではなく引っ掛かり。Lore説明なし。

  

\[C2 二番目の席\]

平常：◇ ミオの場所。まだ、あたたかい。

17:17後：◇ まだ、あたたかい。なのに、さっきより遠い。

逆流後：◇ あたたかさが、抜けていく。

連れ去り後：◇ もう、あたたかくない。

目的：Referenceの状況変化後台詞を、RewriteMemoryでは同一Interactableの意味変化へ変換する。

  

14F. Humor / Warmth Gate（S4前）

S4前に最低1回、プロットにも謎にも直接寄与しない「少し笑える/かわいい/人間らしい」瞬間をCritical/Natural Routeへ含める。候補はNPC-B2-AMBIENT-01の落ち葉、MIO-Bの待つ時の間、C2の風。ただしギャグイベントにはしない。

理由：Benchmark実ページでは危機前の日常会話の幅が広く、危機だけを予告する会話列になっていない。RMでもS0の不穏後にA/BがずっとFORESHADOWだけだと、ミオと世界を失う痛みが薄くなる。

判定：v0.14でPASS候補。

  

14G. Repeat / Optional Quality Gate

・各Areaに最低1つ、「2回目に反応が変わる」調べ物または会話を用意する。

・ただし2回目差分を全オブジェクトに強制しない。Prototype採用対象だけ。

・再会話の報酬は情報量でなく人格/空気でもよい。

・Optional NPCは本筋情報を再説明しない。

・Optional会話を見なくてもMIO愛着とMain Plot理解は成立する。

・一度も物理再訪しないAreaのState Variantを品質達成数に含めない。

  

14H. Stale/Superseded整理

・旧「掃除の人『おかえり。』」固定案：SUPERSEDED。Canon根拠がないため現行Prototype Scriptから除外。Natural NPCという機能だけKEEP。

・旧Area-B住人5名（店主/子ども/老人/近所の人等）：REFERENCE-SCALE DRAFT / PROTOTYPE NON-ACTIVE。現行採用数として数えない。必要ならOptional最大1名を後から選ぶ。

・旧Area-B白層化再訪台詞：FUTURE CANDIDATE。CH01現行Routeでは再訪しないためRuntime Quality評価から除外。

・旧大量Interactable候補：候補台帳として保持するが、IMAGE-02には役割が重複しない採用対象だけを置く。

・最新優先順：SECTION 14 \> SECTION 13 \> SECTION 12 \> 旧SECTION 2CのPrototype配置候補。Canonキーライン/SECTION 1の確定機能は別途維持。

  

14I. Benchmark Script Quality Audit v0.14

NPC Voice Distinctness：PARTIAL→PASS候補。Natural NPCに固有の生活行動/口調/再会話を付与。

Ordinary-Life Range before Crisis：PASS候補。AREA-A LIFE優先＋AREA-B軽い生活会話を追加。

Repeat-talk / Repeat-inspect Reward：PASS候補。A/B/Cに代表差分を配置。

Optional Personality Reward：PASS候補。MIO-A/P05 + NPC再会話。

State-aware Reinterpretation：PASS候補。C2が主役。Area B未再訪variantは評価除外。

Lore Dump Control：PASS維持。

Canon Guard：PASS。新しい制度/組織/歴史は追加していない。

Character Voice Final：NOT TESTED。文芸FINAL/通し音読前。

Runtime Density：NOT TESTED。

  

総合：v0.13は構造上Benchmark-equivalent候補だった。v0.14は実ページで確認した「短い人格会話・再会話・普通の生活・状態後の意味変化」を加え、Script TextureまでBenchmark-equivalent候補へ前進。ただし実プレイ同等の最終判定はIMAGE-02座標化＋Critical/Natural/Completionist実測後。

  

14J. 次工程

1\. IMAGE-02へ現行Active Pinのみ配置：AREA-A LIFE 2〜3/MYSTERY 1、AREA-B P01/P02/P04/P07/P08＋Optional P03/P06/P05、AREA-C主要C2 Pin。

2\. 画像に台詞全文を書かずScript ID＋Role＋Acquisitionを付ける。

3\. Critical Route通し音読で、叔母・Natural NPC・ミオの声が混同しないか確認。

4\. Natural Routeで「普通→少し可笑しい→ミオ→小さなズレ→塔」の順が体験として成立するか確認。

5\. その後にDialogue文芸FINAL Pass。Referenceの台詞を模倣せず、RewriteMemory固有の声へ磨く。

  

Changelog追記 2026-08-15 v0.14: Driveベンチマークフォルダの索引＋実ページを確認し、単なるGuide構造比較からScript Texture比較へ拡張。Natural NPCを人格/生活行動/再会話付きへ更新、AREA-A LIFE比率を強化、代表Interactableのrepeat responseを定義。旧「おかえり」固定、Area-B大量NPC/未使用白層化variantをSUPERSEDED/FUTUREへ整理。新規Canonなし。

  
  

SECTION 15 — CH01 FULL PLAYER PLAYTHROUGH v0.15（実プレイ順・Benchmark Style）

  

目的：SECTION 1/2B/2C/12〜14を「設計項目別」ではなく、初見プレイヤーが実際にCH01を遊ぶ順番へ一本化する。Area/Zone、誰に話すか、何を調べるか、どの選択肢を選べるか、操作がいつ返るか、次にどこへ行くかを連続して読むためのプレイスルー層。既存仕様を置換せず参照層として追加する。台詞はSCRIPT DRAFT。★キーラインは意図保持。CANDIDATE/ASSUMPTIONはCanon化しない。

  

ROUTE凡例：

\[REQ\] Main Scenario成立に必要。

\[NAT\] 主動線で自然に経験する。長時間LOCKしない。

\[OPT\] 寄り道・再会話・再調査。見なくてもMain Plot成立。

\[STATE\] 同じ場所/物の状態差分。

PLAYER ACTION = 実際にプレイヤーが行う操作。

NEXT = 次に自然に向かう場所/行動。

  

\========================================

00\. PROLOGUE / S0 — 滲んだ白い場〔Area未確定 / ASSUMPTION〕

\========================================

\[REQ\] New Game。

⚙ セーブデータが滲む。時刻表示 17:17。Control=LOCKED。

◇ 白い。どこかに、名前の抜けたにおいがする。

◇ 正面にミオ。

\[ミオ\] ◆ ……ごめんなさい。 ★

\[ミオ\] ◆ あなたは、誰ですか？ ★

◇ 画面が白く滲む。環境音が消える。

PLAYER ACTION：Enter/決定で台詞を送る。

OUTCOME：whiteLayerProgress=intro。理由は説明しない。

NEXT：AREA-A / A1 自室。

  

\========================================

01\. AREA-A — トウの家 / A1 自室〔S1〕

\========================================

\[REQ\] 起床。

⚙ トウはA1自室・ベッド脇。Control=UNLOCKED。ここで初めて自由操作。

◇ 朝の光。床・扉・食器の生活音。母の部屋方向だけ静か。

\[トウ\] ◆ ……いかなきゃ。（内語）

  

PLAYER ACTION：部屋を歩く。出口へ向かえば進行できる。

  

\[OPT\] ■ ベッドを調べる。

1回目：◇ もう、あたたかくない。

2回目：◇ 二度寝したら、遅れる。

  

\[OPT\] ■ 自室の私物を調べる。

1回目：◇ 見慣れた物ばかり。ひとつずつ、名前が言える。

※v0.14方針により危機前MYSTERY過密を避け、2回目の不穏差分はPrototype採用時に再審査。

  

PLAYER ACTION：A1出口からA2居間へ。

NEXT：A2で叔母が家事をしている。

  

\========================================

02\. AREA-A — A2 居間・台所 / 叔母〔S1〕

\========================================

\[REQ\] PLAYER ACTION：叔母に話しかける。

◇ 叔母は皿などを片づけながら話す。生活動作は止まらない。

\[叔母\] ◆ おはよう、トウ。

\[叔母\] ◆ ……顔に書いてある。「きょうも、だれかを待ちます」って。

\[トウ\] ◆ …そうかな。

\[叔母\] ◆ 会うまえは、みんな すこし待つものよ。

\[叔母\] ◆ あの子は、名前を呼ばれると安心するって……お母さんが、よく言ってた。 ★

  

CHOICE：

▶ 聞き返す

▶ 何も言わない

  

〔聞き返す〕

\[叔母\] ◆ ……たぶん、ね。

◇ 一瞬だけ家事の手が止まる。

  

〔何も言わない〕

◇ 叔母は少し困った顔で笑い、それ以上は説明しない。

  

OUTCOME：プレイヤーは「待つ」「名前を呼ぶ」を日常語として先に知る。攻略説明にはしない。

  

\[OPT\] ■ 食卓のカップ。

1回目：◇ 食卓の端に、叔母がいつも使うカップ。今日も同じ場所にある。

2回目：◇ さっきより、湯気が少ない。

  

\[OPT\] ■ 家具の修繕跡。

1回目：◇ 直した跡がある。まだ使えるから、捨てない。

2回目：◇ きれいじゃない。でも、ここではこれでいい。

  

\[OPT\] PLAYER ACTION：叔母へ再度話しかける場合は、長いLore会話を追加しない。短い生活反応のみ。

  

NEXT：玄関へ向かう途中にA3母の部屋がある。調べず外へ出てもよい。

  

\========================================

03\. AREA-A — A3 母の部屋前〔Optional Exploration〕

\========================================

\[OPT\] PLAYER ACTION：少し開いた戸を調べる。

1回目：◇ 少しだけ、開いている。

2回目：◇ いつも、少しだけ。

  

\[OPT\] PLAYER ACTION：花を調べる。

1回目：◇ 花がある。毎日、だれかが替えている。

2回目：◇ ……昨日も、見た。

  

\[OPT\] PLAYER ACTION：室内を調べる。

1回目：◇ 中は、音がしない。

2回目：◇ ここだけ、時間が止まっているみたいだ。

  

OUTCOME：母の状態を説明しない。「不在」の感覚だけを持ち帰る。observation+はImplementation Candidate。

NEXT：A3玄関へ戻る。

  

\========================================

04\. AREA-A — A3 窓・玄関 → AREA-B

\========================================

\[NAT/OPT\] ■ 窓を見る。

◇ 屋根の向こうに時計塔。いつもの位置に、いつもの影。

  

\[REQ\] PLAYER ACTION：玄関を調べる / 出口へ歩く。

◇ 外へ。坂の下の方から風。

⚙ AREA TRANSITION：AREA-A → AREA-B / B1。

NEXT：ミオと合流。

  

\========================================

05\. AREA-B — B1 坂上 / ミオ合流〔S2〕

\========================================

\[REQ\] ◇ ミオが隣に並ぶ。Control=UNLOCKED。

\[ミオ\] ◆ 帰ろ。……五分だけ、寄っていい？

  

CHOICE：

▶ いいよ

▶ どうして？

  

〔いいよ〕

\[ミオ\] ◆ ありがとう。

  

〔どうして？〕

◇ ミオは少し笑う。答えない。

  

\[トウ\] ◆ 三か月前から、ずっと「五分だけ」だ。（内語）

\[トウ\] ◆ ……最初の日のことだけ、思い出せない。（内語）

  

PLAYER ACTION：ミオと坂を下りB2生活圏へ。

NEXT：町の日常を通過する。

  

\========================================

06\. AREA-B — B2 / P01 店先〔Natural World Texture〕

\========================================

\[NAT\] ◇ 店先に箱や値札。誰かが片づけている。町は普通に動いている。

  

\[OPT\] ■ 店先を調べる。

1回目：◇ 箱が積まれている。値札の向きだけ、きれいに揃っている。

2回目：◇ 一つ売れたらしい。空いた場所だけ四角い。

  

PLAYER ACTION：そのまま主動線を歩ける。

NEXT：掃除をしている住人の前を通る。

  

\========================================

07\. AREA-B — B2 / P02 掃除をしている住人〔Natural NPC〕

\========================================

\[NAT\] 主動線上ですれ違う。会話LOCKなし。

\[住人\] ◆ おはよう。今日は、落ち葉の方が早起きだ。

◇ 箒は止まらない。

\[ミオ\] ◇ 足元の落ち葉を見て、少し笑う。

  

\[OPT\] PLAYER ACTION：住人に自分から話しかける。

\[住人\] ◆ ほら、また一枚。きりがないね。

\[ミオ\] ◆ ……負けてるね。

  

\[OPT\] PLAYER ACTION：もう一度話す。

\[住人\] ◆ まだ負けてるよ。

  

OUTCOME：町の制度説明ではなく、「二人がこの町の日常にいる」ことを経験。

NEXT：NPCを抜けた先でミオが歩みを緩める。

  

\========================================

08\. AREA-B — B2 / P04 「待つ」〔Natural Mio Bond〕

\========================================

\[NAT\] ◇ ミオが2〜3歩先で止まる。何かを見ている。Control=UNLOCKED。

  

PLAYER ACTIONはUI選択ではなく移動で成立：

▶ 先へ進む

▶ その場で待つ

  

〔先へ進む〕

\[ミオ\] ◆ あ、待って。

◇ ミオが追いつき、進行は止まらない。

  

〔待つ〕

◇ 数秒、同じ方向を見たまま並んで立つ。

\[ミオ\] ◆ ……トウは、待ってくれるんだ。

\[トウ\] ◆ ……うん。

◇ ミオは少しだけ笑って歩き出す。

  

OUTCOME：「待つ」を説明ではなく操作で経験。

NEXT：主動線へ。ここからOptional Pocket / Optional Loopへ寄れる。

  

\========================================

09\. AREA-B — B2 / P03→P06 Optional Pocket〔WORLD→MYSTERY〕

\========================================

\[OPT\] PLAYER ACTION：主動線から見える掲示へ寄る。

■ P03 掲示 1回目：◇ 町のお知らせが何枚か貼られている。特別なことは書いていない。

■ P03 2回目：◇ 読み返しても、やっぱり普通のお知らせだ。

  

\[OPT\] PLAYER ACTION：隣/一段奥のP06を調べる。

■ P06 1回目：◇ 一枚だけ、文字と剥がれ跡の位置が少し合わない。

\[トウ\] ◆ ……貼り直したのかな。（内語）

■ P06 2回目：◇ 読める。意味も分かる。なのに、そこだけ目が戻ってしまう。

  

OUTCOME：WORLDの正常を見てから弱いMYSTERYを得る。白層化/記憶局/ノアの説明なし。

NEXT：小道からB2主動線へ自然復帰。

  

\========================================

10\. AREA-B — B2 / P05 Optional Mio Loop〔CANDIDATE〕

\========================================

\[OPT\] ミオが主動線の外を見る。

\[ミオ\] ◆ あ、……。

◇ 猫がいる。〔猫自体はCANDIDATE・IMAGE-02/Playtestで採否〕

\[ミオ\] ◆ ……大丈夫かな。

\[ミオ\] ◆ 大丈夫。たぶん。

◇ 近づくと猫が逃げる。

\[ミオ\] ◆ ……逃げちゃった。

  

CHOICE：

▶ 追わない

▶ もう少し見る

  

〔追わない〕

◇ ミオも追わない。少しだけその場にいる。

  

〔もう少し見る〕

◇ 猫は少し離れた場所からこちらを見ている。

  

\[ミオ\] ◆ 帰ろっか。

OUTCOME：Plot情報ゼロ。「一緒に寄り道した」という人物報酬。

NEXT：小ループから主動線へ復帰。

  

\========================================

11\. AREA-B — B2 / P07 時計塔Reveal → B3 / P08出口

\========================================

\[NAT\] ◇ 建物/樹木の遮蔽が切れ、坂の先で時計塔の全体が見える。強制Camera Panなし。

\[ミオ\] ◆ 塔、見えてきた。

\[トウ\] ◆ ……あと五分？

\[ミオ\] ◆ うん。たぶん。

◇ ミオは塔を見たまま、少し歩く速度を落とす。

  

\[REQ\] PLAYER ACTION：B3坂下まで歩く。

◇ 生活圏の音が少し遠くなる。塔前の開けた場所が見える。

\[ミオ\] ◆ ……こっち。

⚙ AREA TRANSITION：AREA-B → AREA-C / C1。

NEXT：C2ベンチ。

  

\========================================

12\. AREA-C — C1入口 → C2 ベンチ〔S3〕

\========================================

\[REQ\] ◇ ミオが先にC2ベンチへ向かう。

\[ミオ\] ◆ 一番端は、近すぎるの。

\[ミオ\] ◆ ……二番目がいい。

\[トウ\] ◆ 何もないよ、そこ。

◇ ミオは二番目の席に座る。

  

PLAYER ACTION：ベンチを調べる / 隣に座る。

  

\[NAT\] 「ただ座る」。Control=UNLOCKED。

◇ しばらく何も起きない。風が吹く。

\[ミオ\] ◆ ……風、気持ちいいね。

◇ ミオが空を見る。プレイヤーは塔や周囲を見てもよい。

  

\[OPT\] ■ 時計塔を見る。

1回目：◇ 高い。夕方の光に、輪郭だけが濃い。

2回目：◇ ミオは、いつもここへ来る。

  

NEXT：静けさ/名前の会話。

  

\========================================

13\. AREA-C — C2 / 名前の実演〔S3〕

\========================================

\[REQ\]

\[ミオ\] ◆ ここに座ってると、少しだけ静かになる。

\[トウ\] ◆ ミオ。 ★

◇ 一瞬、周囲の音が止まる。

\[ミオ\] ◆ ……今の、止まった。ちゃんと、私だった。 ★

  

OUTCOME：mioNameStability=high候補。「名前を呼ぶ→相手が自分として戻る」を説明なしで経験。

NEXT：17:17までC2に滞在。

  

\========================================

14\. AREA-C — C2 / 17:17空白通知〔S4〕

\========================================

\[REQ\] ⚙ 時刻17:17。端末が鳴る。短時LOCK。

\[トウ\] ◆ ……送った覚えの、ない通知。（内語）

  

PLAYER ACTION：通知を開く。

⚙ 本文は空白。既読だけが付いている。

\[ミオ\] ◆ ……来たんだ。 ★

\[ミオ\] ◆ たぶん、それ、まだ見ちゃだめ。 ★

◇ 環境音が一段引く。

⚙ UIラベルは --% / 名称未判読。

  

PLAYER ACTION：通知を閉じる。

⚙ Control=UNLOCKED。

◇ すぐ次のイベントへ飛ばない。数歩歩ける。ミオは5席目方向を見ている。

  

\[STATE\] ■ 二番目の席を調べる場合：◇ まだ、あたたかい。なのに、さっきより遠い。

NEXT：プレイヤー自身がベンチ/5席目へ近づく。

  

\========================================

15\. AREA-C — C2 / 五席目〔S5〕

\========================================

\[REQ\] 5席目付近へ近づく。

\[ミオ\] ◆ ……ほら、五つ目。 ★

\[トウ\] ◆ 席は、四つしかないよ。 ★

\[ミオ\] ◆ ……そう、だよね。

◇ トウは見なかったことにしようとする。

  

PLAYER ACTION：5席目の跡を調べる。

■ 1回目：◇ 何かの跡。影のような、へこみのような。

◇ 紙から文字だけを剥がすような音。

■ 再調査：◇ ミオにだけ、そこは「空いている」。

  

OUTCOME：fragmentCount+ / observation+候補。

⚙ 調査後Control=UNLOCKED。即Choiceを出さず一拍置く。

◇ ミオは何も言わずトウの反応を待つ。

NEXT：S6 Choice。

  

\========================================

16\. AREA-C — C2 / 最初の態度選択〔S6〕

\========================================

\[REQ\] ⚙ Choice UI。

▶ 見る / observe

▶ 見ない / avoid

▶ 聞く / ask

▶ 待つ / wait

  

〔見る〕

\[トウ\] ◆ もっと調べたら、分かるかも。（内語）

⚙ observation+ / mioTrust-候補。

  

〔見ない〕

\[トウ\] ◆ ……見ない方がいい気がした。（内語）

⚙ playerChoseNotToLook / mioTrust+候補。

  

〔聞く〕

\[トウ\] ◆ ……大丈夫？

\[ミオ\] ◆ 大丈夫。たぶん。 ★

⚙ mioTrust+候補。

  

〔待つ〕

◇ 何も言わず、隣にいる。

⚙ playerChoseNotToLook / mioTrust+候補。

  

NEXT：S7採用時のみ再構成。未採用ならS8。

  

\========================================

17\. S7 — 再構成モード〔Area非依存 / CD-13 UNDECIDED〕

\========================================

\[OPT/UNDECIDED\] 採用時のみ。

◇ 断片が宙に浮かぶ。

PLAYER ACTION：断片を組む。

※機構/台詞/報酬は未決。ここをv0.15で創作確定しない。

NEXT：AREA-C / C2 S8。

  

\========================================

18\. AREA-C — C2 / アンログ逆流〔S8〕

\========================================

\[REQ\] ◇ ミオの輪郭から色が抜け始める。部分UNLOCK。

\[アンログ/声\] ◆ 来て。 ★

\[アンログ/声\] ◆ 待ってた。

\[アンログ/声\] ◆ トウ。／名前、呼んで。 ★

\[アンログ/声\] ◆ 見ないで。／……でも、忘れないで。 ★

\[ミオ\] ◆ やめて。

\[ミオ\] ◆ ……それ、私の中から出さないで。

  

PLAYER ACTION：状況を何とかしようと操作する。

▶ 移動する

▶ 触れる

▶ 追跡する

▶ 記録する

  

各操作結果：

〔移動〕⚙ 率が跳ぶ。ミオの色がさらに抜ける。

〔触れる〕⚙ 率が跳ぶ。届かない。

〔追跡〕⚙ 率が跳ぶ。逃げるほど悪化。

〔記録〕⚙ 率が跳ぶ。記録しようとするほど消える。

  

◇ 一方的に相手を固定しようとする操作は全部悪化させる。

\[トウ\] ◆ ……ぼくが、見たから。（内語）

⚙ ここで初めて欠損ラベルが「白層化率」として判読可能になる。

OUTCOME：Player自身が観測=悪化へ到達。

NEXT：別の動詞を選ぶS9。

  

\========================================

19\. AREA-C — C2 / 呼びかけ〔S9〕

\========================================

\[REQ\] Choice UI。

▶ 見ない

▶ 聞く

▶ 待つ

▶ 名を呼ぶ

▶ 手を取る

  

〔見ない〕

\[ミオ\] ◆ ……今のは、たぶん正しい。

  

〔聞く / 待つ / 手を取る〕

◇ ミオの震えが少し止まる。relationAnchor候補。

  

〔名を呼ぶ〕

PLAYER ACTION：ミオの名を呼ぶ。

\[トウ\] ◆ ミオ。 ★

◇ 他の音がすべて引く。

\[ミオ\] ◆ ……今の、ちゃんと、私だった。 ★

⚙ mioNameStability=restored / relationAnchor / mioVoluntarySpeech候補。

  

OUTCOME：呼びかけは観測と別。相手自身の応答を待つことで成功する。

NEXT：S10余韻。

  

\========================================

20\. AREA-C — C2 / S10 成功後の余韻

\========================================

\[NAT/REQ\] ⚙ Control=UNLOCKED。5〜15秒程度。

◇ ミオはすぐ話さない。ベンチ、塔、トウのどれかを見る。

\[ミオ\] ◆ ……五つ目は、ほんとにあった。

◇ 夕闇。環境音は完全には戻らない。

  

PLAYER ACTION：その場にいる / 数歩歩く / ベンチを見る / 時計塔を見る。

\[STATE\] ■ 二番目の席：◇ あたたかさが、抜けていく。

※D-NOAHは必須から除外。制度説明を足さない。

NEXT：S11。

  

\========================================

21\. AREA-C — C2 / 呼びかけ成功→記憶局介入〔S11〕

\========================================

\[REQ\]

\[トウ\] ◆ ミオ。 ★

\[ミオ\] ◆ はい。 ★

◇ ミオの輪郭が一瞬だけ鮮明に戻る。本当に「自分」に戻った顔。

◇ ——直後。記憶局が静かに現れる。原因機序は断定しない。

\[記憶局\] ◆ ……保護のため、です。

⚙ Control=LOCKED。プレイヤーは介入できない。

◇ ミオが連れ去られる。

◇ ベンチが空席になる。夜へ。

⚙ carried.lost灰スロット。

⚙ observer\_is\_tou=true / mio\_carried\_lost=true。

  

OUTCOME：呼びかけは成功した。それでも制度に奪われた。

NEXT：同じC2を連れ去り後の状態で見る。

  

\========================================

22\. AREA-C — C2 / 連れ去り後の同一地点〔State Reinterpretation〕

\========================================

\[REQ/NAT\] Control=UNLOCKED。Critical Routeでも必ず短く返す。

  

PLAYER ACTION：二番目の席を見る/調べる。

■ ◇ もう、あたたかくない。

  

PLAYER ACTION：ベンチ全体を見る。

■ ◇ だれもいない。二番目の席が、まだ少し、へこんでいる。

  

PLAYER ACTION：時計塔を見る。

■ ◇ 夜。同じ塔なのに、意味が、変わってしまった。

  

OUTCOME：新しい場所へ移動せず、プレイヤー自身の数分前の記憶と現在のC2を衝突させる。

NEXT：端末通知。

  

\========================================

23\. AREA-C — C2 / 送信者反転 → CH01 END

\========================================

\[REQ\] ⚙ 端末に通知。

「次回観測予定：明日 17:17」

⚙ 送信者が ミオ → トウ に反転。

\[トウ\] ◆ 送った覚えは、なかった。でも、既読だけは付いていた。 ★

\[トウ\] ◆ ……必ず、取り戻す。（内語）

⚙ notification\_sender\_inverted=true。

NEXT：CH02「未記録／記録されない街」。

  

\========================================

15A. 3 ROUTE VIEW — 実際のプレイヤー差

\========================================

CRITICAL ROUTE：S0 → A1起床 → A2叔母 → A3玄関 → B1ミオ → P01/P02通過 → P04待つ機会 → P07塔Reveal → C1/C2 → ただ座る → 名前実演 → 17:17 → 五席目 → S6 → S8 → S9 → S10 → S11 → C2再解釈 → 通知反転。

  

NATURAL ROUTE：Critical + Aの生活物1〜2点 + P02住人任意会話 + P03/P06またはP05のどちらか + 時計塔Inspect + C2のState差分1〜2点。

  

COMPLETIONIST ROUTE：Natural + A3母の部屋全調査/再調査 + AREA-B P03/P06/P05すべて + NPC再会話 + 店先再調査 + C2ベンチ/二番目/五席目/時計塔/端末の各State差分。ただし旧大量NPC/大量Interactable候補はActive Routeに含めない。

  

15B. PLAYTHROUGH QUALITY CHECK

・Area/Zoneがプレイ順に常時追える：PASS。

・誰に話すか：叔母 / ミオ / Natural住人 / 記憶局を実プレイ順に明示：PASS。

・何を調べるか：A生活物/A3母の痕跡/B店先・掲示/Cベンチ・五席目・塔・端末：PASS。

・選択肢：A2 / B1 / B2待つ / P05 / S6 / S8操作試行 / S9を明示：PASS。

・Required/Natural/Optionalの区別：PASS。

・State差分：C2を平常→17:17後→逆流後→連れ去り後で通し体験化：PASS候補。

・Benchmark型「Action→Outcome→Next Goal」：PASS候補。

・実時間30分：NOT TESTED。

・IMAGE-02実座標：PENDING。

・Character Voice通し音読：NOT TESTED。

  

15C. 次のLock Gate

1\. このSECTION 15を基準にIMAGE-02へScript Pinを置く。PinにはStep No / Area-Zone / Script ID / Req-Nat-Optのみ。台詞全文は画像へ入れない。

2\. SECTION 15 Critical Routeを頭から実際に音読し、会話送り時間を計測する。

3\. AREA-A/B/Cの歩行時間をIMAGE-02 Geometryから仮置きし、Critical/Natural/Completionistの総尺を算出する。

4\. S4前に「町とミオを失いたくない」と感じる時間が十分か確認する。

5\. S4以降でイベントが自動連鎖しすぎないか、UNLOCK区間を実座標で検証する。

6\. 上記通過後にv0.15をPLAYTHROUGH LOCK候補とし、Dialogue文芸FINALへ進む。

  

Changelog追記 2026-08-16 v0.15: Benchmarkの「実際のプレイを場所順に追う」読み方へ合わせ、SECTION 15 FULL PLAYER PLAYTHROUGHを追加。S0→AREA-A(A1/A2/A3)→AREA-B(B1/B2/B3)→AREA-C(C1/C2)→CH01 ENDを、Player Action / 誰に話す / 調べ物 / 選択 / State / Outcome / Nextの順で一本化。既存SECTION 1/2B/2C/12〜14のActive要素のみ再構成し、新規Canonなし。Critical/Natural/Completionist 3経路を定義。実時間・IMAGE-02座標・音読は未検証のためLOCK保留。

  

15D. HUMAN VALIDATION LAYER — BLIND FIRST PLAY / EXPECTED v0.17a

  

目的：SECTION 15の00〜22をHuman PlaytestのEXPECTED正本として1:1検証する。別Playtest Scriptは作らない。既存のPlayer Action / Outcome / NextをSOURCEとし、以下のExpected Notice / Spontaneous Action / Do Not Tell / Telemetry / VerdictはTEST DESIGNとして追加する。ここで追加するTelemetry名・判定閾値はImplementation CandidateでありCanonではない。

  

15D-0. BLIND TEST RULE

・テスターには「CH01を普通に初見で遊んでください」のみ伝える。目的地、正解選択、調べる物、待つ行為、五席目、再調査を先に教えない。

・進行不能時だけObserver Rescueを行い、その時点で該当H-IDをPARTIAL/FAIL候補として記録する。救済内容も記録する。

・プレイ中に「どう思った？」と割り込まない。推論/感情質問はCH01 END後にまとめて行う。

・Actualは動画＋Telemetryを正とし、Observerメモは補助。発言だけで行動を上書きしない。

・REQ = Main Scenario成立に必要、NAT = 主動線で自然発生を期待、OPT = 自発訪問率を測る、STATE = 同一地点の再解釈を測る。

・PASSは「クリアした」だけではなく、設計したNotice→Action→Outcome→Next Motivationが誘導なしで成立したかで判定する。

  

共通記録：H-ID / Source Step / Area-Place / Expected Notice / Expected Action / Expected Outcome / Next Motivation / Req-Nat-Opt-State / Do Not Tell Tester / Telemetry Event / Actual / Verdict(PASS・PARTIAL・FAIL・N/A)。

  

H001 — Source 00. PROLOGUE / S0 — 滲んだ白い場〔Area未確定 / ASSUMPTION〕

Area/Place：導入。

Expected Notice：白い場と正面のミオ、「あなたは、誰ですか？」、環境音消失。

Expected Action：Enter/決定で台詞を送る。

Expected Outcome：理由を説明されないまま「何かが欠ける」予兆を受け取る。

Next Motivation：平常のAREA-Aへ進み、今の場面の意味を保留したまま本編を始める。

Class：REQ。

Do Not Tell：冒頭が未来/予告である、白層化である等を説明しない。

Telemetry：HV\_H001\_ENTER / D\_FORGET\_ADVANCE / HV\_H001\_EXIT。

Actual：PENDING｜Verdict：PENDING。

  

H002 — Source 01. AREA-A — トウの家 / A1 自室〔S1〕

Area/Place：AREA-A / A1自室。

Expected Notice：初自由操作、朝の生活音、母の部屋方向だけ静か。

Expected Action：自室を歩きA2出口へ向かう。ベッド/私物Inspectは任意。

Expected Outcome：操作を学びながら「普通の家」と局所的な静けさを体感する。

Next Motivation：生活音の先、A2へ。

Class：REQ + OPT。

Do Not Tell：母の部屋方向の静けさを指摘しない。Inspectを促さない。

Telemetry：HV\_H002\_CONTROL\_UNLOCK / A1\_EXIT / A1\_INSPECT\_\*。

Actual：PENDING｜Verdict：PENDING。

  

H003 — Source 02. AREA-A — A2 居間・台所 / 叔母〔S1〕

Area/Place：AREA-A / A2居間・台所。

Expected Notice：叔母が家事を続けている日常。

Expected Action：自分から叔母に話しかける。再会話/家具Inspectは任意。

Expected Outcome：「待つ」「名前」が生活会話の中で先に置かれ、後半の意味を説明なしで仕込む。

Next Motivation：玄関へ向かい、途中のA3を通る。

Class：REQ + OPT。

Do Not Tell：「待つ」「名前」が攻略伏線だと説明しない。

Telemetry：HV\_H003\_AUNT\_TALK / A2\_RECHAT / A2\_INSPECT\_\*。

Actual：PENDING｜Verdict：PENDING。

  

H004 — Source 03. AREA-A — A3 母の部屋前〔Optional Exploration〕

Area/Place：AREA-A / A3母の部屋前。

Expected Notice：少し開いた戸、花、音のない室内。

Expected Action：興味が生じた場合のみ自発Inspect。スキップしても進行可。

Expected Outcome：母の状態の答えではなく「不在」の感覚だけを持ち帰る。

Next Motivation：玄関へ戻る。

Class：OPT。

Do Not Tell：「母の部屋を調べて」と言わない。母の状態を補足説明しない。

Telemetry：HV\_H004\_ENTER\_OPTIONAL / A3\_DOOR / A3\_FLOWER / A3\_ROOM / A3\_SKIP。

Actual：PENDING｜Verdict：PENDING。※未訪問はFAILではなくOptional発見率として集計。

  

H005 — Source 04. AREA-A — A3 窓・玄関 → AREA-B

Area/Place：AREA-A / A3窓・玄関。

Expected Notice：窓から時計塔遠景、玄関の先の坂と風。

Expected Action：玄関を調べる/出口へ歩く。窓を見るのはNAT/OPT。

Expected Outcome：説明台詞ではなくランドマークと出口で次方向を理解する。

Next Motivation：AREA-B/B1でミオと合流。

Class：REQ + NAT/OPT。

Do Not Tell：時計塔を見るよう指示しない。

Telemetry：HV\_H005\_WINDOW / AREA\_A\_EXIT / AREA\_B\_ENTER。

Actual：PENDING｜Verdict：PENDING。

  

H006 — Source 05. AREA-B — B1 坂上 / ミオ合流〔S2〕

Area/Place：AREA-B / B1坂上。

Expected Notice：ミオが自然に隣へ並び「五分だけ、寄っていい？」と頼む。

Expected Action：ミオと歩いてB2へ進む。

Expected Outcome：目的地移動を「同行」に変え、プロット前に二人で歩く時間を作る。

Next Motivation：ミオと町の日常を通過する。

Class：REQ。

Do Not Tell：ミオへの愛着を感じるべきだと伝えない。

Telemetry：HV\_H006\_MIO\_JOIN / B1\_TO\_B2 / COMPANION\_DISTANCE\_TRACE。

Actual：PENDING｜Verdict：PENDING。

  

H007 — Source 06. AREA-B — B2 / P01 店先〔Natural World Texture〕

Area/Place：AREA-B / B2 P01店先。

Expected Notice：生活物が置かれ、町が普通に動いていること。

Expected Action：主動線をそのまま歩く。店先Inspectは任意。

Expected Outcome：事件説明より先に「普通の生活圏」を記憶する。

Next Motivation：掃除をしている住人の前へ。

Class：NAT + OPT。

Do Not Tell：店先を調べるよう促さない。

Telemetry：HV\_H007\_P01\_VISIBLE / P01\_INSPECT / P01\_PASS。

Actual：PENDING｜Verdict：PENDING。

  

H008 — Source 07. AREA-B — B2 / P02 掃除をしている住人〔Natural NPC〕

Area/Place：AREA-B / B2 P02。

Expected Notice：住人は挨拶しながら箒を止めず、ミオも小さく反応する。

Expected Action：歩き続けても成立。自発会話/再会話が起きたかは別記録。

Expected Outcome：「二人がこの町の日常にいる」を制度説明なしで経験する。

Next Motivation：NPCを抜け、歩みを緩めるミオへ注意が移る。

Class：NAT + OPT。

Do Not Tell：住人に話しかける必要があると言わない。

Telemetry：HV\_H008\_NPC\_VISIBLE / NPC\_B2\_AMBIENT\_01 / NPC\_B2\_TALK / NPC\_B2\_RETALK。

Actual：PENDING｜Verdict：PENDING。

  

H009 — Source 08. AREA-B — B2 / P04 「待つ」〔Natural Mio Bond〕

Area/Place：AREA-B / B2 P04。

Expected Notice：ミオが2〜3歩先で止まる。Control=UNLOCKED。

Expected Action：UI選択ではなく、先へ進む/その場で待つを移動で選ぶ。

Expected Outcome：「待つ」を説明ではなく身体的な操作として経験する。

Next Motivation：ミオが再び歩く方向/Optional Pocket・Loopへ。

Class：NAT。

Do Not Tell：「待ってください」「ここで止まって」と絶対に指示しない。

Telemetry：HV\_H009\_MIO\_STOP / PLAYER\_STOP\_DURATION / PLAYER\_DISTANCE\_AFTER\_STOP / EVT\_MIO\_WAIT\_RESULT。

Actual：PENDING｜Verdict：PENDING。

  

H010 — Source 09. AREA-B — B2 / P03→P06 Optional Pocket〔WORLD→MYSTERY〕

Area/Place：AREA-B / B2 Optional Pocket。

Expected Notice：主動線から掲示面/小さなズレへ寄れること。

Expected Action：興味があれば自発的に寄り、P03/P06をInspectして主動線へ戻る。

Expected Outcome：正常なWORLDの後に弱いMYSTERYを得る。白層化/記憶局/ノアの答えは得ない。

Next Motivation：未解決のまま主動線/Mio Loop/塔方向へ戻る。

Class：OPT。

Do Not Tell：Optional Pocketの存在・謎の意味を説明しない。

Telemetry：HV\_H010\_BRANCH\_ENTER / P03\_INSPECT / P06\_INSPECT / OPTIONAL\_POCKET\_EXIT。

Actual：PENDING｜Verdict：PENDING。※未訪問はOptional発見率として集計。

  

H011 — Source 10. AREA-B — B2 / P05 Optional Mio Loop〔CANDIDATE〕

Area/Place：AREA-B / B2 P05小ループ。

Expected Notice：ミオが主動線外の何かに気づく。猫はCANDIDATE。

Expected Action：追う/寄るか、そのまま進むかを自発選択。

Expected Outcome：Plot情報ではなく「一緒に寄り道した」記憶を作る。

Next Motivation：小ループから自然に主動線へ復帰。

Class：OPT / CANDIDATE。

Do Not Tell：寄り道すると好感度が上がる等の説明をしない。

Telemetry：HV\_H011\_MIO\_LOOP\_OFFER / MIO\_LOOP\_ENTER / MIO\_LOOP\_SKIP / MIO\_LOOP\_EXIT。

Actual：PENDING｜Verdict：PENDING。※未実装ならN/A。

  

H012 — Source 11. AREA-B — B2 / P07 時計塔Reveal → B3 / P08出口

Area/Place：AREA-B / B2→B3。

Expected Notice：遮蔽が切れて時計塔全体が自然に見える。強制Camera Panなし。

Expected Action：塔方向を認識し、B3坂下まで歩く。

Expected Outcome：塔を「説明された目的地」ではなく、ミオが五分寄る個人的なLandmarkとして受け取る。

Next Motivation：開けた塔前AREA-Cへ。

Class：NAT + REQ。

Do Not Tell：「時計塔を見て」と視線誘導の答えを口頭で与えない。

Telemetry：HV\_H012\_TOWER\_REVEAL\_VISIBLE / PLAYER\_FACING\_TOWER / P08\_EXIT / AREA\_C\_ENTER。

Actual：PENDING｜Verdict：PENDING。

  

H013 — Source 12. AREA-C — C1入口 → C2 ベンチ〔S3〕

Area/Place：AREA-C / C1→C2。

Expected Notice：ミオが先にベンチへ向かい、二番目の席を選ぶ。

Expected Action：ベンチを調べる/隣に座る。その後UNLOCKの「ただ座る」時間を通過する。

Expected Outcome：二番目の席と、何も起こらない共有時間をミオの記憶として持つ。

Next Motivation：静けさ/名前の会話へ。

Class：REQ + NAT。

Do Not Tell：二番目の席が後で重要になると伝えない。すぐ操作を急かさない。

Telemetry：HV\_H013\_BENCH\_REACH / SECOND\_SEAT\_INTERACT / SIT\_START / LINGER\_DURATION / PLAYER\_MOVE\_DURING\_LINGER。

Actual：PENDING｜Verdict：PENDING。

  

H014 — Source 13. AREA-C — C2 / 名前の実演〔S3〕

Area/Place：AREA-C / C2。

Expected Notice：トウが「ミオ」と呼ぶと周囲の音が一瞬止まり、ミオが「ちゃんと私だった」と返す。

Expected Action：会話を送り、現象を受け取る。

Expected Outcome：「名前を呼ぶ→相手が自分として戻る」を攻略説明なしで一度経験する。

Next Motivation：17:17までその場にいる。

Class：REQ。

Do Not Tell：後のS9の正解動詞が「名を呼ぶ」だと教えない。

Telemetry：HV\_H014\_NAME\_CALLOUT / NAME\_STABILITY\_BEAT\_COMPLETE。

Actual：PENDING｜Verdict：PENDING。

  

H015 — Source 14. AREA-C — C2 / 17:17空白通知〔S4〕

Area/Place：AREA-C / C2。

Expected Notice：17:17に端末が鳴り、送った覚えのない空白通知、ミオの反応、音の後退。

Expected Action：通知を開き、閉じる。Control復帰後に数歩動ける。

Expected Outcome：WORLD→SUSPICION→UIの順で異常に接触し、すぐ自動連鎖しない。

Next Motivation：ミオの視線とベンチ/五席目へ自分で近づく。

Class：REQ + STATE。

Do Not Tell：空白通知の意味、--%の名称、次に五席目を見ることを説明しない。

Telemetry：HV\_H015\_1717 / NOTIFICATION\_OPEN / NOTIFICATION\_CLOSE / POST\_S4\_FREE\_MOVE\_TIME / SECOND\_SEAT\_REINSPECT。

Actual：PENDING｜Verdict：PENDING。

  

H016 — Source 15. AREA-C — C2 / 五席目〔S5〕

Area/Place：AREA-C / C2ベンチ。

Expected Notice：ミオには「五つ目」が見え、トウには四席しかない矛盾。

Expected Action：自分で5席目付近へ近づき、跡を調べる/再調査する。

Expected Outcome：説明を受けるのでなく、同じ物の認識差をPlayer Actionで発見する。

Next Motivation：ミオが反応を待つため、自分の態度を選ぶ。

Class：REQ + STATE。

Do Not Tell：五席目の位置を口頭で指示しない。現象名を与えない。

Telemetry：HV\_H016\_FIFTH\_SEAT\_ZONE / FIFTH\_SEAT\_INSPECT\_1 / FIFTH\_SEAT\_REINSPECT / TIME\_TO\_FIRST\_INSPECT。

Actual：PENDING｜Verdict：PENDING。

  

H017 — Source 16. AREA-C — C2 / 最初の態度選択〔S6〕

Area/Place：AREA-C / C2。

Expected Notice：Choice UI「見る / 見ない / 聞く / …」が態度として提示される。

Expected Action：初回選択を自分で決める。

Expected Outcome：初回四択をObservation Profileとして記録し、選択に対するミオ/世界の反応を経験する。

Next Motivation：選択後の結果から次の対処へ。

Class：REQ。

Do Not Tell：推奨選択・善悪・True条件を示さない。

Telemetry：HV\_H017\_CHOICE\_SHOWN / FIRST\_ATTITUDE\_CHOICE / CHOICE\_LATENCY / CHOICE\_RESULT。

Actual：PENDING｜Verdict：PENDING。

  

H018 — Source 17. S7 — 再構成モード〔Area非依存 / CD-13 UNDECIDED〕

Area/Place：Area非依存。

Expected Notice：採用時のみ断片が提示される。

Expected Action：採用時のみ断片を組む。

Expected Outcome：CD-13未決のためHuman Gateを現時点で固定しない。

Next Motivation：AREA-C/C2 S8。

Class：OPT / UNDECIDED。

Do Not Tell：未決仕様をテスト中に補完説明しない。

Telemetry：HV\_H018\_FEATURE\_PRESENT / RECONSTRUCT\_START / RECONSTRUCT\_END。

Actual：PENDING｜Verdict：未実装時N/A。

  

H019 — Source 18. AREA-C — C2 / アンログ逆流〔S8〕

Area/Place：AREA-C / C2。

Expected Notice：ミオの輪郭から色が抜け、声/状態が逆流する。部分UNLOCK。

Expected Action：移動/触れる/追跡/記録など「何とかしよう」と自分で操作する。

Expected Outcome：操作結果から「観測するほど悪化している」ことへPlayer自身が到達する。

Next Motivation：同じやり方を続けず、別の動詞を探す。

Class：REQ。

Do Not Tell：「観測=悪化」「白層化率」という答えを失敗より先に表示/説明しない。

Telemetry：HV\_H019\_REVERSE\_START / FIRST\_RESPONSE\_ACTION / RESPONSE\_SEQUENCE / STATE\_WORSEN\_DELTA / TIME\_TO\_CHANGE\_STRATEGY。

Actual：PENDING｜Verdict：PENDING。

  

H020 — Source 19. AREA-C — C2 / 呼びかけ〔S9〕

Area/Place：AREA-C / C2。

Expected Notice：S8の失敗後、見ない/聞く/待つ/手を取る/名を呼ぶ等、観測以外の態度が取れる。

Expected Action：別動詞を試し、「名を呼ぶ」に到達した場合はトウがミオを呼ぶ。

Expected Outcome：呼びかけは観測と別で、相手自身の応答を待つことで安定が戻ることを経験する。

Next Motivation：成功したのかを確かめる余韻へ。

Class：REQ。

Do Not Tell：S3の名前実演を正解ヒントとして口頭で回収しない。「名を呼ぶ」を選ばせない。

Telemetry：HV\_H020\_CHOICE\_SHOWN / FIRST\_RECOVERY\_CHOICE / RECOVERY\_SEQUENCE / NAME\_CALLOUT / MIO\_STABILITY\_RESTORED。

Actual：PENDING｜Verdict：PENDING。

  

H021 — Source 20. AREA-C — C2 / S10 成功後の余韻

Area/Place：AREA-C / C2。

Expected Notice：Controlが5〜15秒程度戻り、ミオはすぐ話さず、同じベンチ/塔が残る。

Expected Action：その場にいる/数歩歩く/ベンチを見る/時計塔を見る。自発的な余韻行動を記録する。

Expected Outcome：「助かった」と感じるためのPlayer-owned timeを確保し、次の介入との差を作る。

Next Motivation：ミオの状態を確かめながらS11へ。

Class：NAT/REQ + STATE。

Do Not Tell：次に連れ去りが起こると予告しない。早送りを促さない。

Telemetry：HV\_H021\_CONTROL\_UNLOCK / S10\_DWELL / BENCH\_LOOK / TOWER\_LOOK / PLAYER\_MOVE\_COUNT。

Actual：PENDING｜Verdict：PENDING。

  

H022 — Source 21. AREA-C — C2 / 呼びかけ成功→記憶局介入〔S11〕

Area/Place：AREA-C / C2。

Expected Notice：トウ「ミオ」→ミオ「はい」で一度鮮明に戻った直後、記憶局介入が起こる。

Expected Action：演出中の許可された入力のみ。介入原因をPlayerの呼びかけ失敗として誤読しないかを終了後質問で確認する。

Expected Outcome：「呼びかけは成功した。それでも制度に奪われた」という二段構造を受け取る。

Next Motivation：ミオがいなくなった同じC2を自分の目で見直す。

Class：REQ。

Do Not Tell：「呼びかけたから捕まった」と説明しない。逆に正解解説もプレイ中はしない。

Telemetry：HV\_H022\_CALLOUT\_SUCCESS / MIO\_REPLY\_HAI / INTERVENTION\_START / MIO\_CARRIED\_LOST / CONTROL\_RETURN。

Actual：PENDING｜Verdict：PENDING。

  

H023 — Source 22. AREA-C — C2 / 連れ去り後の同一地点〔State Reinterpretation〕

Area/Place：AREA-C / C2・連れ去り後。

Expected Notice：ミオが消え、同じ二番目の席/ベンチ/時計塔だけが残る。

Expected Action：Critical Routeでも最低1回は再調査できる。Human Gateでは、誘導前に二番目の席/ベンチ/塔を自発的に見直したかを別記録する。

Expected Outcome：新しい場所へ移動せず、数分前のPlayer自身の記憶と現在のC2を衝突させる。

Next Motivation：端末通知→notification\_sender\_inverted→CH02「未記録／記録されない街」へ。

Class：REQ/NAT + STATE。

Do Not Tell：「ベンチを調べてください」と言わない。まず自発再訪時間を与える。進行救済を出した場合はObserver Rescueとして記録する。

Telemetry：HV\_H023\_CONTROL\_UNLOCK / FIRST\_POST\_LOSS\_ACTION / SECOND\_SEAT\_POST\_LOSS / BENCH\_POST\_LOSS / TOWER\_POST\_LOSS / TIME\_TO\_REINSPECT / NOTIFICATION\_SENDER\_INVERTED / CH01\_END。

Actual：PENDING｜Verdict：PENDING。

  

15D-1. HUMAN GATES（CH01横断）

HG-01 WORLD NOTICE：P01/P02の生活層を少なくとも視覚/聴覚で経験したか。Optional会話数だけで判定しない。

HG-02 MIO BOND：S4前に「同行」「P04待つ機会」「二番目の席」「ただ座る」「名前実演」がCritical Route上で欠落なく成立したか。

HG-03 LANDMARK：強制Camera Pan/口頭誘導なしでP07時計塔Revealが次方向として機能したか。

HG-04 OPTIONAL CURIOSITY：P03→P06 / P05 / A3等へ何件自発寄り道したか。0件でもMain Plot FAILにはしないが、世界への好奇心指標として記録する。

HG-05 S8 INFERENCE：UI/Observerが名称や答えを出す前に、Playerが行動変更によって「今のやり方が悪化させる」と判断できたか。

HG-06 CALLOUT TRANSFER：S3「名前実演」の経験が、S9で別動詞へ切り替える認知的手掛かりとして働いたか。プレイ中には質問しない。

HG-07 FALSE CAUSALITY：S11後に「呼びかけに失敗したから奪われた」「呼びかけたせいで奪われた」と誤読していないか。End後質問で確認。

HG-08 LOSS REINTERPRETATION：S11後、通知反転より前にC2を自分で再解釈する時間が成立し、可能なら誘導なしで再調査欲求が生じたか。

HG-09 NEXT HOOK：CH01 END時点で「次に何を知りたい/したいか」を自由回答させ、CH02継続意欲を記録する。

  

15D-2. END-OF-CHAPTER DEBRIEF（Blind Play後のみ）

質問は正解を含めず、順番を固定する。

Q1「いちばん気になったもの/場所/人は？」

Q2「ミオについて、S4より前にどんな印象を持った？」

Q3「17:17以降、何が起きていると思った？」

Q4「S8で、あなたはなぜ行動を変えた/変えなかった？」

Q5「名前を呼ぶ行為は、何をしたと思う？」

Q6「ミオが連れていかれた原因を、今どう理解している？」

Q7「連れ去り後、最初に何を見た/見たかった？」

Q8「この先を遊ぶなら、次に何を確かめたい？」

※Observerは回答をCanon正解へ訂正せず、まず原文で記録する。

  

15D-3. VERDICT RULE

PASS：誘導なしでExpected Action/Outcome/Next Motivationが成立、またはOPTでは設計意図どおり任意性が保たれる。

PARTIAL：進行は成立するがNotice不足、誤読、長い迷い、Observer Rescue、UI依存などで意図の一部が崩れる。

FAIL：進行不能、必須因果の誤読、S4前Bond欠落、S8の意味がUI説明でしか分からない、S11が呼びかけ失敗/原因として読まれる、S11後C2再解釈時間が成立しない等。

N/A：未実装のUNDECIDED/CANDIDATE等で今回のBuildに存在しない。

  

15D-4. IMPLEMENTATION HANDOFF

Godot側はH001〜H023を動画タイムコードと結合できるよう、最低限 event\_name / H-ID / timestamp\_ms / area / player\_position / control\_state / interaction\_or\_choice / result を記録する。座標・具体Event IDは現行実装に合わせて確定し、この文書から架空IDをCanonへ昇格させない。Human Run出力は EXPECTED（本節固定）と ACTUAL（Runごと）を分離する。

  

Changelog追記 2026-08-16 v0.17a: SECTION 15の00〜22を1:1でH001〜H023へ対応させるHuman Validation Layerを追加。Blind First Playで「クリア可否」ではなくNotice→Action→Outcome→Next Motivationの自然成立を検証し、Do Not Tell / Telemetry / Actual / Verdict / 横断Human Gate / End Debriefを定義。既存Canon・台詞・Main Routeは変更せず、Telemetry名はImplementation Candidate。

  
  

SECTION 16 — FULL PLAYER PLAYTHROUGH BENCHMARK QUALITY REVIEW v0.16

  

目的：SECTION 15 FULL PLAYER PLAYTHROUGHを、Drive上のMOTHER3第1章Benchmark（場所→NPC/物→Player Action→Outcome→Next Goal、日常NPC、再会話、Optional、状態変化後の再解釈）と比較し、設計台本としての完成度と実プレイ品質の証明度を分離して評価する。

  

16A. SCORE

・Documentation / 資料完成度：97/100

・FULL PLAYER PLAYTHROUGH Script Design：93/100

・Benchmark-equivalent Runtime Quality（暫定）：87/100

  

※87点は品質不足そのものではなく、IMAGE-02実座標、通し音読、歩行・会話時間、Critical/Natural/Completionist実測が未実施であることによる検証保留を含む。

  

16B. CATEGORY REVIEW

・Area→Action→Outcome→Next Goal：97 / ほぼBenchmark同等。

・プレイ順の追跡性：98 / Benchmark同等以上。S0→AREA-A→B→C→ENDを一続きで読める。

・Required / Natural / Optional分類：96 / 強い。

・NPC・会話の生活感：90 / 改善済みだがBenchmark側の「何でもない人・物」の層がまだ厚い。

・調べ物の面白さ：92 / Repeat responseとState差分が効いている。

・寄り道の意味：92 / WORLD・MIO・MYSTERY・HOOKの報酬分離が成立。

・Mio Affection before S4：94 / Critical Routeでも「同行」「待つ」「ただ座る」「名を呼ぶ」を保証。

・世界理解の自然さ：90 / Lore Dumpは抑制できている。生活NPC/生活物をあと少量強化余地。

・Mystery / Hook：96 / 17:17、五席目、送信者反転の問いが次行動へつながる。

・同一地点の再解釈：98 / C2の平常→17:17→白層化→逆流→連れ去り後はRewriteMemory固有の強み。

・Player Actionとの一体化：95 / 「待つ」「調べる」「観測失敗」「呼びかけ」を操作で成立。

・NPC Voice / 人格幅：86 / Natural NPCは改善したが、Benchmarkほど生活人格の幅はまだない。

・Ordinary-Life Range：89 / Prototypeとしては十分。ただし危機前の日常層はBenchmarkが上。

・Character Voice：88暫定 / 文芸FINAL・通し音読未実施。

・Runtime Pacing：80暫定 / 30分実測前。S4以降のC2イベント密度が最大リスク。

・Map Geometry / Script Coupling：82暫定 / IMAGE-02実座標前。

  

16C. STRONGEST POINT

C2のState Reinterpretationを最重要強みとする。同じベンチ・二番目の席・時計塔・端末が、数分前のPlayer Memoryとの比較で意味を変えるため、新Mapを増やさず再訪/状態変化のBenchmark原則をRewriteMemory固有の「意味の書き換え」へ変換できている。ここは模倣ではなく独自価値として評価する。

  

16D. MAIN GAP VS BENCHMARK

最大差は「何でもない人・物の層」。Benchmarkは本筋に直接必要のない住人、動物、家、看板、道標、生活物の短い反応が多く、事件前に世界が先に存在している感覚を作る。現v0.15は機能接続が綺麗な分、A/Bで「攻略用に配置された世界」に見えるリスクが残る。

  

PrototypeでNPCを大量追加しない。AREA-BにOptional人物/生活体験を最大1件だけ追加候補とし、条件は以下：

・白層化/記憶局/時計塔を説明しない。

・その人物自身の生活行動・口調・再会話を持つ。

・MIOまたはLIFEの副報酬を持つ。

・Main Plotの必須情報を持たない。

  

16E. HIGHEST RUNTIME RISK

S4以降：17:17→五席目→Choice→逆流→操作失敗→呼びかけ→成功→S10余韻→記憶局→連れ去り→C2再解釈→通知反転、が同一C2に集中する。Script上はUNLOCKを挟んでいるため設計上は成立候補だが、実座標で「イベント自動連鎖感」が出ないか未検証。

  

判定条件：

・S4通知close後、Playerが自分で5席目へ近づいた感覚がある。

・S5後の一拍がUI待ちではなく空間を見る時間になる。

・S9成功後、S10で「助かった」と感じる時間がある。

・S11後、通知反転の前にC2を自分の目で再解釈できる。

  

16F. LOCK GATE — 93→96〜98候補へ上げる順序

1\. IMAGE-02へSECTION 15 Active Pinを実座標化。

2\. Critical Routeを頭から通し音読し、会話送り秒数を計測。

3\. AREA-A/B/C歩行秒数＋UNLOCK/LOCK秒数を仮置き。

4\. Critical / Natural / Completionistの総尺を比較。

5\. S4前の愛着時間と、S4以降のCore Event密度を実測。

6\. 問題箇所だけ削る/間を広げる。新Lore・新説明台詞で埋めない。

7\. 上記通過後にDialogue文芸FINAL Pass。

  

16G. VERDICT

現段階では「Script Architectureが弱い」状態ではない。資料粒度とプレイスルー設計はBenchmark-equivalent候補まで到達。最終差は文章量ではなくRuntime証明。IMAGE-02と3ルート実測でC2再解釈が機能し、S4以降の密度が破綻しなければ、FULL PLAYER PLAYTHROUGHは96〜98/100級へ到達可能。

  

Status：PLAYTHROUGH LOCK保留。次工程はIMAGE-02実配置→Timing/Voice実測。新規Canon追加なし。

  
  
  

17\. CRITICAL ROUTE READ-THROUGH + CONTROL STATE AUDIT v0.17

  

目的：SECTION 15 FULL PLAYER PLAYTHROUGHをCritical Routeで頭から通し、①台詞を音読したときの人物声の分離、②S4前にミオへの愛着が最低限成立するか、③S4以降が受動イベント列になっていないか、④LOCK/UNLOCKの矛盾、をDesk Auditする。これは実機・実音声の代替ではなく、Script Design Gate。Runtime/演技尺はGodot Playtestで確定する。

  

17A. Critical Route Desk Read-through 判定

  

・叔母：PASS。生活用語と短い気遣いを中心にし、制度説明役になっていない。家庭の安心と微かな記憶揺らぎが同じ声に共存する。

・Ambient住人：PASS。P02は生活行動＋短い一言のみで、世界設定の説明NPCになっていない。

・ミオ：PASS候補。短文、間、言い切らなさ、「たぶん」、視線や停止への反応で声が分離する。Criticalでも合流→同行→待つ機会→塔Reveal→ベンチでただ座る→名前実演を経験できる。

・トウ：PASS候補。説明より観察・反応が中心。後半で自己解説を増やさない。

・Lore Dump：PASS。S4以前に制度説明を追加しない。S8の名称判読もPlayer Action失敗の後に置く。

・S4前のMIO BOND：DESIGN PASS候補。P04そのものはCriticalで必ず通るが、「待つ」という良い結果はPlayer-dependent。したがってGateは「待つ成功を強制」ではなく「待つ機会を必ず与える」。最低愛着は同行・塔・ベンチ・名前実演の積み重ねで成立させる。

・S9とS11の二度の呼びかけ：KEEP。S9=Mechanic Success、S11=Success後のStructural Loss。S10の自由操作を挟むことで同じ入力の意味を分離する。

・実音読時間／演技間：RUNTIME PENDING。文字数だけで増減せず、Godot上で会話送り・間・歩行込みで測る。

  

17B. S4以降 Control-State 正規シーケンス

  

S4 / 17:17：UNLOCKED探索 → 通知発生時だけ短時LOCK → Playerが通知を閉じる → UNLOCKED。自動で五席目へ吸着・自動遷移しない。3〜8歩程度、自分で近づく。

  

S5 / 五席目：UNLOCKED\_APPROACH → Inspect時のみ短時LOCK → 情報提示後UNLOCKED\_REACT。ここで直ちにS6 Choiceを開かず、一拍の移動／停止余白を置く。

  

S6 / 最初の態度選択：CHOICE\_CONTROL。通常移動は止めるが、これは演出LOCKではなくPlayer Decision Stateとして扱う。

  

S7 / 再構成：採否未決。Criticalではスキップ可能。採用してもS4-S6で返した操作主体性を壊さない。

  

S8 / アンログ逆流：OPENING\_LOCK（視覚/音の異常を短く提示） → PARTIAL\_UNLOCK\_PROBE（Playerが実際に移動/触れる/追跡/記録の通常操作を試す） → FAILURE\_FEEDBACK → 短時LOCKで気づき/UI更新 → S9。UI名称「白層化率」はこの失敗後に初判読。

  

S9 / 呼びかけ：CHOICE\_CONTROL → CALLOUT\_INPUT（名を呼ぶ） → 応答「はい」 → Success。OBSERVATIONとCALLOUTを入力上も分離する。

  

S10 / 成功余韻：UNLOCK\_AFTERGLOW 5〜15秒。Playerがベンチ/ミオ/塔へ自分で視線を戻せる。説明会話を足さない。

  

S11 / 記憶局介入：CALLOUT/会話 → LOCK\_CAPTURE（介入・連れ去り） → UNLOCK\_REINTERPRET 10〜20秒 → Criticalでも最低1回、同じ場所を自分で再調査 → END\_NOTIFICATIONの短時LOCK → CH02。

  

17C. S11 連れ去り後の必須Player Action

  

Critical Route必須：二番目の席またはベンチの「ミオがいた位置」をPlayer自身が1回調べる。自動モノローグだけで終えない。

Natural：上記＋ベンチ全体または時計塔のどちらかを追加で見る。

Completionist：二番目の席＋ベンチ全体＋時計塔＋必要なら端末再確認。

  

通知「送信者反転」は、連れ去り直後に自動で被せない。Critical必須の再調査が1回成立してから発火可能にする。これにより「奪われた」映像を見るだけでなく、「同じ場所を自分で見直したら意味が変わっていた」をPlayer Actionとして成立させる。

  

17D. P0整合修正

  

1\. S4 UI：旧記述「17:17で白層化率へ変わる」を廃止。S4は --% / 名称未判読。S8の操作失敗後に「白層化率」を初判読。

2\. S8：旧LOCKED表記を、短時OPENING LOCK→PARTIAL UNLOCK操作試行→気づきの短時LOCKへ統一。

3\. S11：旧「連れ去り→モノローグ→通知」を廃止。連れ去り後にControlを必ず返し、同一C2の再解釈を1回以上要求してから通知反転。

4\. S10：5〜15秒の自由操作をKEEP。新しい世界設定説明を追加しない。

5\. P04：Criticalで「待つ機会」は保証するが、待つ成功はPlayer Choiceのまま。好感度正解化しない。

  

17E. Quality Gate

  

PASS条件：

・S4通知close後、Player入力なしでS5が開始しない。

・S5 Inspect後、即座にChoice UIへ連結せず短いUNLOCK余白がある。

・S8で少なくとも1回はPlayer自身の通常操作が失敗し、UIだけで「観測が悪い」と教えない。2回目の試行を必須にするかはPlaytestで決定。

・S8の「白層化率」名称は操作失敗より前に読めない。

・S9成功後、S10で5〜15秒Controlを返す。

・S11連れ去り後、通知反転より前にControlを返す。

・Critical Routeでも連れ去り後C2を最低1回Player自身が再調査する。

・S4〜S11の各主要転換の間にPlayer Inputが存在し、3つ以上の完全受動演出が連続しない。

・後半の理解を新規Lore台詞で補わない。WORLD→SUSPICION→UI→PLAYER ACTIONの順を守る。

  

17F. Gate判定

  

Critical Route Character Voice：DESIGN PASS候補 / PERFORMANCE PENDING。

Pre-S4 Mio Affection：DESIGN PASS候補 / PLAYTEST PENDING。

S4+ Player Input Continuity：P0 PATCH後 DESIGN PASS候補。

LOCK/UNLOCK Consistency：P0矛盾を本v0.17で整理。Runtime StateMachine検証はPENDING。

FULL PLAYER PLAYTHROUGH：SCRIPT LOCK CANDIDATE。FINAL LOCKはGodot灰箱でCritical/Natural/Completionist実測後。

  

Changelog 2026-08-16 v0.17：Critical RouteをDesk Read-throughし、人物声/Lore密度/Mio愛着を監査。S4の--%→S8初判読へUI矛盾を修正。S8を短時LOCK→PARTIAL UNLOCK操作試行→短時LOCKへ定義。S11は連れ去り後にCriticalでもControlを必ず返し、同一C2再調査後に送信者反転を発火する構造へ修正。後半を受動イベント列ではなくPlayer Input Chainとして固定候補化。

  
