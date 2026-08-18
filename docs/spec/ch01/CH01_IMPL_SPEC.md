# CH01 実装仕様書（正本 / IMPLEMENTATION SPEC）

**Status**: v1.0-impl（正規化初版）
**Based on**: `source/CH01_DETAILED_SCRIPT_v0.17_SOURCE.md`（凍結済み原本・Draft v0.17）
**Target**: Godot 4.x / Orthographic Top-Down 2D（4方向Facing）/ 30分プロトタイプ

---

## 0. この文書について

- 本文書と同ディレクトリの JSON 台帳（`flags.json` / `scenes.json` / `dialogues.json` / `tuning.json`）が **CH01 実装の正本（SSOT）** である。原本（Google Doc / `source/`）は履歴であり、以後参照しない。
- 原本 v0.17 の積層構造（SECTION 7〜17 の監査・改訂履歴）から、**superseded な記述を除去した単一レイヤー**として抽出した。抽出優先順位: §17D（P0整合修正）> SECTION 15 > 14 > 13 > 12 > 2B > 2C > 1。
- 確定度タグは原本の規約を維持する: **CONFIRMED**（canon）/ **CANDIDATE**（設計）/ **ASSUMPTION**（canon未指定・確定しない）/ **UNDECIDED**（上位未決）/ **PROVISIONAL**（座標・尺の仮置き）。
- **更新規律**: 仕様変更は本文書と JSON 台帳を直接編集し、§9 Changelog に1行追記する。監査・レビューは別文書（PR コメント等）で行い、正本に積層させない。台詞の文芸 FINAL パスを GPT 等へ依頼する場合は `dialogues.json` の該当エントリのみ切り出して渡し、結果は PR で取り込む。

### 関連文書

| ファイル | 役割 |
|---|---|
| `flags.json` | フラグ台帳（型・初期値・書込点・読取点・閾値） |
| `scenes.json` | シーン台帳（S0〜S11・コントロールシーケンス・ゲート） |
| `dialogues.json` | 台詞台帳（★キーライン・分岐・afterState） |
| `tuning.json` | チューニング定数（Playtest 調整は数値変更のみ） |
| `CANON_SNAPSHOT.md` | canon 依存事実の抜き書き・禁止事項・未決レジスタ・外部文書依存 |
| `../../design/UIUX/SCREEN/SCREEN_CALLOUT_INPUT.md` | 呼びかけ入力 UI（Phase 1 で新設） |

---

## 1. 裁定記録（DECISION RECORD）

2026-08-18 合意済み。以後の変更は本表の改訂として行う。

| ID | 裁定 | 内容 |
|---|---|---|
| D1 | 実装ターゲット | **Godot 4.x**。Web プロトタイプ（`docs/rewrite-dev/`）は台詞・フロー参照として凍結し改修しない。HTML5 エクスポートで従来のブラウザ配布形態を維持可能 |
| D1a | 視点 | **Orthographic Top-Down（真上見下ろし）・4方向Facing**。Isometric は不採用（素材コスト・衝突判定・Y-sort の平易化、仕様の Facing 記述との一致） |
| D2 | S7 再構成 | **Feature Flag = OFF（未実装・データ定義のみ）**。S6→S8 直結が正パス。旧 Web の `ch01_070_reconstruction` は移植しない。`scenes.json` S7 / `flags.json` fragmentCount を予約として保持 |
| D3 | Phase2 タスク | シーン移行に統合。「誰も覚えてない」→S5 ミオ台詞側（証言NPCなし）、「忘れないでね」半欠落→S11 送信者反転に吸収 |
| D4 | 時刻モデル | **イベント駆動の擬似時計**（§3.2）。実時間クロック不採用 |
| D5 | mioTrust | **廃止 → mioBond（bool群）に分解**（`flags.json` 参照）。好感度の加減算・数値化はしない |
| D6 | S8 脱出条件 | **異なる動詞2回 or（1回以上＋タイムアウト）**。定数 `S8_PROBE_MIN_VERBS` / `S8_PROBE_TIMEOUT_SEC` |
| D7 | 呼びかけUI | **長押しチャージ版を Phase 1 で本実装**（仮UIを挟まない）。S9/S11 で同一コンポーネント厳守 |
| D8 | Area B 白層化variant | **再訪なし**（原本 QP-06 B案追認）。variant 台詞は FUTURE CANDIDATE として原本に残置 |
| D9 | セーブ | **チェックポイントのみ**（§3.7）。手動セーブなし |
| — | HTML5 ビルド | 暫定キープ。GC2026 提出要件確認後に最終裁定（Phase 3 前まで） |

---

## 2. 全体構造

### 2.1 シーン構成

S0 → S1 → S2 → S3 → S4 → S5 → S6 → S8 → S9 → S10 → S11 → CH02
（S7 は D2 により恒久スキップ。採用裁定時に復帰）

- Engagement: S0=P → S1=A → S2=A → S3=R → S4=R → S5=A → S6=A → S8=R → S9=A → S10=R → S11=R（PASSIVE 最大連続=1 の Gate を維持）
- Area: **A** トウの家（A1自室/A2居間/A3母の部屋+玄関）/ **B** 坂道（B1坂上/B2生活圏/B3坂下）/ **C** 時計塔前（C1入口/C2ベンチ）
- S0/S8〜S11 のロケは ASSUMPTION（IMAGE-02 確定待ち）。灰箱は PROVISIONAL 座標で実装する。

### 2.2 3原則（横断 Gate・全実装判断に適用）

1. **WORLD → SUSPICION → UI**: 世界の異変が先、プレイヤーの疑念が次、UI の追認が最後。UI が先に答えを言わない。
2. **OBSERVATION ≠ CALLOUT**: 一方的に相手を確定しようとする操作（調べる/触れる/追跡する/記録する/問い詰める）＝観測＝悪化。名を呼び本人の応答を待つ＝呼びかけ＝別系統。呼びかけを悪化動詞に入れない。
3. **CALLOUT SUCCESS ≠ CAPTURE CAUSE**: S11 の連れ去りは呼びかけの成功と因果を断定しない。「制度が回復を検知→介入」は CANDIDATE/DESIGN INTERPRETATION。

### 2.3 MIO BOND TRACE

MIO-A（寄り道）/ MIO-B（待つ）の経験有無を `mioBond` bool で記録し、後半に**微小な痕跡**（台詞 variant 1行・配置差分 1点）としてのみ返す。大分岐・好感度システムにしない。MIO-C（ただ座る）は Natural Beat として Critical Route で必ず通過するためフラグ化しない。

### 2.4 C2 World State Matrix

C2（時計塔前ベンチ）は5状態で同一地点の意味を書き換える。**CH01 最重要の再解釈装置**。

| 要素 | 平常 | 17:17後 | 白層化↑(S5) | 逆流中(S8-9) | 連れ去り後(夜) |
|---|---|---|---|---|---|
| NPC通行 | 住人が通る | 減る | なし・孤立 | — | 完全無人 |
| 環境音 | 夕方の生活音 | −1段 | 静寂拡大 | 剥落音重畳 | 無音（風のみ） |
| 色/光 | 暖色の夕方 | 暖橙 | 端から色抜け | 歪み・明滅 | 夜・寒色 |
| Camera | FOLLOW | 微FIXED | 視野狭窄 | FIXED | WIDE（空虚） |
| Interactable | ベンチ/塔/生活痕 | +通知端末 | +5席目の跡 | 操作試行のみ | 空席/反転端末 |
| UI | 記録率 正常 | --%（欠損・名称未判読） | --%↑ | 「白層化率」初判読+急伸 | carried.lost 灰スロット |

状態は `whiteLayerStage` で駆動（`flags.json`）。各状態の調べ物 variant は `dialogues.json` / 原本 SECTION 2C の Active 採用分を Phase 1〜2 で配置。

---

## 3. システム仕様

### 3.1 フラグ

`flags.json` を正とする。設計原則:

- 書込オーナーは **Dialogue 完了時 or Event 完了時のみ**。シーン表の flagSummary は導出情報。
- impl 層はセーブ上 `impl.*` 名前空間に隔離（DL-Y3 未決のため Canon 化しない）。story 層（3種）は write-once。
- `whiteLayerProgress` は enum `whiteLayerStage` に改名（演算混在の解消）。`mioTrust` は廃止（D5）。`worldKnowledge` は実装しない。

### 3.2 擬似時計（17:17 トリガー）

時計表示は演出変数。シーンごとにスクリプトで進める（朝→夕方前→夕方→**17:17**→夜）。

```
EVT-1717 発火条件（S4開始）:
  D-NAME1 完了
  AND MIO-C Natural Beat 通過
  AND （最終必須ビートから S4_IDLE_TRIGGER_SEC 経過 かつ プレイヤーがC2ゾーン内）
発火時: 表示時刻を 17:17 に更新 → 端末通知
```

- 17:17 前の Area C 離脱はソフトブロック（§3.6）。実時間による発火は行わない。
- S11 冒頭の 17:17 も同様にシーンスクリプト駆動（S10 余韻終了→表示更新）。

### 3.3 コントロールステート正規シーケンス

原本 §17B（P0 整合修正後）を正とする。各シーンの `controlSequence` は `scenes.json` に定義。共通原則:

- S4 通知 close 後、**Player 入力なしで S5 が開始しない**（トリガーゾーン接近で開始）。
- S5 Inspect 後、即 Choice UI を出さず `S5_POST_INSPECT_BEAT_SEC` の UNLOCK 余白。
- S6/S9 の選択は演出 LOCK ではなく **CHOICE_CONTROL**（Player Decision State）として扱う。
- S8 は OPENING_LOCK → PARTIAL_UNLOCK_PROBE → 短時 LOCK（全面 LOCK 演出にしない）。
- S9 成功後 S10 で `S10_AFTERGLOW_*` の Control 返却。
- S11 連れ去り後、通知反転より前に必ず Control を返す（UNLOCK_REINTERPRET）。
- 3つ以上の完全受動演出を連続させない。

### 3.4 S8/S9 入力ループ状態機械

**S8（操作試行）**

```
OPENING_LOCK (S8_OPENING_LOCK_SEC)
  色抜け提示・D-ANLOG・D-STOP
→ PROBE_LOOP (PARTIAL_UNLOCK_PROBE)
  動詞: 移動する / 触れる / 追跡する / 記録する
  各試行 → 率ジャンプ（observation Tier で振幅決定）＋ 固有フィードバック行
  脱出: 異なる動詞 S8_PROBE_MIN_VERBS 回試行
     OR（1回以上試行 AND S8_PROBE_TIMEOUT_SEC 経過）
→ FAILURE_FEEDBACK（短時LOCK）
  内語「ぼくが見たから」 → uiRecordRateLabel = named_spike（「白層化率」初判読）
→ S9
```

**S9（呼びかけ）**

```
CHOICE_LOOP (CHOICE_CONTROL)
  選択肢: 見ない / 聞く / 待つ / 手を取る / 名を呼ぶ
  非呼びかけ選択 → 正のマイクロフィードバック（失敗ではない）→ 選択肢へ戻る
  非呼びかけ選択 S9_REPROMPT_AFTER_CHOICES 回連続 → D-ANLOG「名前、呼んで」再掲
  「名を呼ぶ」 → CALLOUT_INPUT → 成立 → S10
失敗状態・タイマー死: なし
```

### 3.5 呼びかけ入力 UI（SCREEN_CALLOUT_INPUT）

- 方式: **長押しチャージ**（D7）。押し続けると名前が満ちる（`CALLOUT_CHARGE_SEC`）→ 離すと発声 → 全音が引く無音ビート（`CALLOUT_SILENCE_BEAT_SEC`）→ 応答（`CALLOUT_RESPONSE_DELAY_SEC` 後）。
- 状態: `IDLE → CHARGE → RELEASE → SILENCE → RESPONSE`。
- **S9 と S11 で完全に同一のコンポーネント・同一の操作**。S11 の意味反転は文脈のみで作る（不変条件）。
- 入力: キーボード（決定キー長押し）/ タッチ（ボタン長押し）両対応。
- 詳細は `docs/design/UIUX/SCREEN/SCREEN_CALLOUT_INPUT.md`（Phase 1 冒頭で既存 SCREEN 文書と同形式で新設）。

### 3.6 進行ゲート表

原則: **LOCKED/演出中以外はハードロックせず、作中1行のソフトブロック**で返す。ブロック台詞は Implementation 台詞（canon 非追加・SCRIPT DRAFT）。

| シーン | ゲート | 方式 | フィードバック例（DRAFT） |
|---|---|---|---|
| S1 | 叔母と話す前の玄関 | ソフト | 玄関調べ→トウ内語「…いってきます、くらい言おう」 |
| S2 | B3 到達前の B1 逆戻り | 許容 | ブロックなし（ミオが追随） |
| S3〜S4 | 17:17 前の Area C 離脱 | ソフト | ミオ「……もう少しだけ」 |
| S5〜S6 | Area C 離脱 | ソフト | 同上（ミオが5席目を見たまま） |
| S8〜S9 | エリア離脱 | 構造上不可 | PROBE の「移動する」は試行動詞として処理（離脱ではない） |
| S10 | エリア離脱 | ソフト | ミオが立ち止まる（台詞なし） |
| S11 再解釈中 | エリア離脱 | ソフト | 内語「……まだ、行けない」 |

### 3.7 セーブ（チェックポイント）

- シーン開始時に自動チェックポイント: **S1 / S2 / S3 / S6 / S8前 / S11前**。
- 手動セーブなし（D9）。中断時は直近チェックポイントから再開。
- S0 の「セーブ UI が滲む」はセーブ画面演出アセットで成立（実セーブ機構と独立）。
- チェックポイントは `impl.*` フラグ＋ story フラグ＋現在シーン ID を保存。

### 3.8 テレメトリ

- 形式: **JSONL**。1イベント1行。
- 必須フィールド: `event_name / h_id / timestamp_ms / area / player_position / control_state / interaction_or_choice / result / build_id / route_class`。
- イベント名は原本 15D の `HV_*` 系を Implementation Candidate として採用（H001〜H023 と動画タイムコードを結合可能にする）。
- 回収方式（ローカル保存 / POST）は Phase 1 のスキーマ凍結時に決定。
- EXPECTED（原本 15D 固定）と ACTUAL（Run ごと）を分離する。

---

## 4. シーン仕様

正: `scenes.json`（S0〜S11 全定義・controlSequence・ゲート・退出条件）。台詞は `dialogues.json`。ここでは実装上の要点のみ:

- **S0**: LOCKED 導入。Enter 送りのみ。滲みセーブ演出 → S1。
- **S1**: 初自由操作（移動/調べ習得）。叔母 Required 会話 → 玄関。A3 母の部屋は Optional（強制しない・母の状態を説明しない）。
- **S2**: 同行移動。Natural: P01 店先 → P02 住人 → P04 MIO-B「待つ」（移動で選ぶ）→ P07 塔 Reveal → P08 出口。Optional: P03→P06 Pocket / P05 猫ループ（CANDIDATE）。会話で歩行を止めない。
- **S3**: 二番目の席 → MIO-C「ただ座る」（UNLOCK 余白）→ D-QUIET → D-NAME1（名前の実演）。
- **S4**: 擬似時計発火 → 通知短時 LOCK → close 後 UNLOCK（自動で S5 に吸着しない）。UI は --%（名称未判読）。
- **S5**: 5席目接近 → 調査（1回目/再調査）→ 余白 → S6。
- **S6**: 4 intent 単発選択。
- **S8**: §3.4 ループ。「白層化率」初判読はここ。
- **S9**: §3.4 ループ → CALLOUT_INPUT → 成立。
- **S10**: 余韻 UNLOCK（5〜15秒）。D-5TH-TRUTH-SHORT のみ。説明追加禁止。D-NOAH 実装しない。
- **S11**: 呼びかけ（同一UI）→「はい」→ LOCK_CAPTURE（記憶局・最小台詞）→ UNLOCK_REINTERPRET（**必須再調査 ≥ S11_REQUIRED_REINSPECT_COUNT**）→ EVT-SENDER-INVERT → モノローグ → CH02。

## 5. イベント仕様

| Event | Trigger | Precondition | Input Lock | 主要効果 | Flag書込（オーナー） | Exit |
|---|---|---|---|---|---|---|
| EVT-OPENING | New Game | — | LOCKED | 滲みSave演出・D-FORGET | whiteLayerStage=intro | S1 |
| EVT-1717 | §3.2 条件充足 | S3必須ビート完了 | 短時LOCK（S4_NOTIFICATION_LOCK_SEC） | 通知オーバーレイ・環境音−1段・記録率→--%（名称未判読） | whiteLayerStage=s4 | 通知close→UNLOCK |
| EVT-EMPTYSEAT | INT-空席 調査（S5） | EVT-1717後 | 調査中のみ | D-5TH・剥落音・調査ズーム | whiteLayerStage=s5 / fragmentCount+（再調査） / observation+ | 余白→S6 |
| EVT-ANLOG-BACKFLOW | S8開始 | S6完了 | §3.4 S8シーケンス | 色抜け・D-ANLOG/D-STOP・操作試行・白層化率初判読 | whiteLayerStage=s8 / anlogPressure=high | S9 |
| EVT-CALLOUT | S9「名を呼ぶ」成立 | 逆流ピーク | CALLOUT_INPUTのみ | 無音→D-NAME2・輪郭回復 | mioNameStability=restored / mioVoluntarySpeech / relationAnchor | S10 |
| EVT-CALLOUT-YES | S11 呼びかけ成立 | mioNameStability=restored | CALLOUT_INPUTのみ | 「ミオ。」→「はい。」・一瞬の完全回復 | — | EVT-CAPTURE |
| EVT-CAPTURE | EVT-CALLOUT-YES直後 | relationAnchor | **LOCK（介入不可）** | 記憶局接近・連れ去り（静かな暴力・露骨描写回避）・空席化・夜へ・carried.lost | whiteLayerStage=s11 / observer_is_tou / mio_carried_lost | UNLOCK_REINTERPRET |
| EVT-SENDER-INVERT | 再解釈 ≥ 必須回数 完了 | mio_carried_lost | モノローグLOCK | 通知「次回観測予定：明日17:17」・送信者 ミオ→トウ 反転・D-END | notification_sender_inverted | CH02 Hook |

※ EVT-CAPTURE は連れ去り直後に通知を**自動で被せない**。必須再調査の成立が EVT-SENDER-INVERT の発火条件（§17C 準拠）。

## 6. Map / Area アンカー（IMAGE-02 ハンドオフ）

- **Area A**: 起点=A1自室（spawn PROVISIONAL）/ 停止点=A2叔母前・A3母の部屋前 / 会話発火=A2 / Interactable=A2エプロン・カップ・修繕跡、A3戸・花・室内、窓（塔遠景）/ 出口=玄関。
- **Area B**: Pin順 = B1 ENTRY → P01 → P02 → P04 → [P03→P06 Optional Pocket] / [P05 Optional Loop] → P07 → P08 → C1。各 Pin に Role / Acquisition / Script ID / NEXT を付す。新規 Location ID は作らない。
- **Area C**: C1入口 → C2ベンチ（4席+5席目跡・二番目の席・通知端末・塔遠景）。EVT 群は全て C2。
- Lock 条件: P04 が最短ルートで経験可能 / P02 は歩行を止めない / P03/P06 は30〜60秒で完結 / P05 は小ループで自然復帰 / P07 後は C1 方向が迷わない / 設定説明3行以上の NPC 会話を置かない。
- 座標・Collision/Trigger 形状は IMAGE-02 で確定（Phase 1〜2 と並行、Phase 3 で突合）。灰箱は PROVISIONAL。

## 7. 未決事項と予約（実装はすべて吸収済み・ブロッカーなし）

| 項目 | 状態 | 実装上の扱い |
|---|---|---|
| CD-13（S7 再構成の採否） | UNDECIDED（上位決裁） | flag-off + データ予約（D2） |
| DL-Y3（フラグ Canon 化） | UNDECIDED | `impl.*` 名前空間隔離 |
| U-004（時計塔の分類/制度/内部） | UNDECIDED | 内部 Event・台詞・ト書きに一切出さない（Canon Guard） |
| D-NOAH 採否 | CANDIDATE 保留 | 実装しない・`dialogues.json` に予約 |
| S0/S8〜S11 ロケ正式確定 | ASSUMPTION | IMAGE-02 で確定・灰箱は PROVISIONAL |
| STALE CANON（上位 canon の学校/教室記述） | GOVERNANCE FIX 待ち | 本仕様はベンチ5席目で統一（正） |
| GC2026 提出要件 | 確認待ち | HTML5 ビルド暫定キープ |

## 8. 受け入れ条件

### 8.1 Phase 1 Exit Criteria（灰箱・Area C 縦切り）

原本 §17E を正とする。全項目 PASS で Phase 1 完了:

1. S4 通知 close 後、Player 入力なしで S5 が開始しない。
2. S5 Inspect 後、即 Choice UI へ連結せず UNLOCK 余白がある。
3. S8 で少なくとも1回は Player 自身の通常操作が失敗し、UI だけで「観測が悪い」と教えない。
4. 「白層化率」名称は操作失敗より前に読めない。
5. S9 成功後、S10 で 5〜15秒 Control を返す。
6. S11 連れ去り後、通知反転より前に Control を返す。
7. Critical Route でも連れ去り後 C2 を最低1回 Player 自身が再調査する。
8. S4〜S11 の各主要転換の間に Player Input が存在し、3つ以上の完全受動演出が連続しない。
9. 後半の理解を新規 Lore 台詞で補わない（WORLD→SUSPICION→UI→PLAYER ACTION 順守）。
10. テレメトリ JSONL スキーマ凍結。
11. HTML5 エクスポートのスモークテスト1回（音声解禁・テレメトリ出力先・ホスティングヘッダ確認）。

### 8.2 Phase 2 Exit Criteria

- Critical / Natural / Completionist 3ルートの実測尺（30分目標）。
- H001〜H023 Blind Playtest（原本 15D を EXPECTED 正本として使用・灰箱のまま実施）。
- Human Gates HG-01〜HG-09 の判定記録。

### 8.3 Phase 3 Exit Criteria

- IMAGE-02 実座標との整合再監査。
- アート・音差し替え後の §17E 再確認。
- 配布ビルド（HTML5 or ネイティブ・提出要件裁定後）。

## 9. Changelog

- **2026-08-18 v1.0-impl**: 原本 v0.17 から正規化初版を抽出。裁定 D1〜D9/D1a 反映（Godot・Orthographic・S7 flag-off・mioTrust→mioBond・擬似時計・S8/S9 ループ定義・呼びかけ長押しUI・Area B 再訪なし・チェックポイントセーブ）。superseded 記述（旧 S4 UI ラベル・S8 全面 LOCK・S11 即時通知・旧「おかえり」・Area B 住人5名・教室ロケ）を除去。whiteLayerProgress→whiteLayerStage 改名。書込タイミング競合2件を裁定（D-AUNT-NAME は D5 で消滅・D-NAME1 完了時書込）。
