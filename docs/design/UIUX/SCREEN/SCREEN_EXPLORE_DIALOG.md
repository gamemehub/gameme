# SCREEN_EXPLORE_DIALOG v0.2（ドラフト）

**対象画面: M03 探索会話モード（探索中のすべての会話を担当する会話専用モード）**

> 役割: M03 探索会話の画面仕様。`MODE_DEFINITION` の構造を、`COMPONENT_DEFINITIONS` / `DESIGN_TOKEN` の正本を使って画面に落とす。
> 状態: 本PRで更新（ドキュメントのみ・ドラフト v0.2）。
> 正本ルール: 数値は `DESIGN_TOKEN`、部品は `COMPONENT_DEFINITIONS` を参照する。生値・独自部品を本書で発明しない。
> 参考: レトロRPG（UNDERTALE 等）の会話UIの**構造**を参考にするが、色・世界観・素材・フォントは RewriteMemory 独自とする。

---

## 1. 対象モードと責務（確定）
- **M03 = 探索中のすべての会話を担当する会話専用モード**。M04 へ統合しない。
- **M04（VNオーバーレイ）= 記憶・白層化・特殊演出のみ**。通常会話は扱わない。
- フロー: M02 探索 → M03 会話 → M02 復帰（位置・向きを保持）。
- M03 から必要に応じて M04 を呼ぶことはあるが、責務は分離する（M03=会話／M04=演出）。
- CH01〜CH08 を通して同一ルールで拡張可能な構造とする。

---

## 2. 目的
探索の没入を切らずに会話を表示する。探索画面を主役にしたまま、画面下部に会話ボックスを出し、探索⇄会話を位置・向きを保って往復する。

---

## 3. M03 のサブモード（確定）
| サブ | 名称 | 使用率 | Portrait | 名前 | 背景 | 主用途 |
|---|---|---|---|---|---|---|
| M03A | 探索会話（通常） | 約90% | PortraitSmall | あり | 探索画面を保持 | NPC通常会話・オブジェクト調査・探索イベント |
| M03B | イベント会話（正面向き） | 約10% | PortraitFull（立ち絵） | あり | 維持＋キャラ正面 | 重要NPC・感情イベント・ボス会話・章ラスト |
| M03C | 独り言 | — | なし | なし | 保持 | プレイヤーの心の声・調査対象への反応 |
| M03D | システム通知 | — | なし | なし | 保持 | アイテム取得・セーブ通知・フラグ通知 |
| M03E | 選択肢 | — | （A/Bに付随） | — | 保持 | プレイヤー選択・分岐 |

---

## 4. 画面状態（共通）
| 状態 | 説明 |
|---|---|
| enter | 会話開始。探索入力ロック、DialogBox をフェードイン |
| typing | テキストを1文字ずつ表示（`--rm-text-speed`） |
| wait | メッセージ表示完了。`▼` を表示し次入力待ち |
| choosing | （M03E のみ）選択肢表示・カーソル移動 |
| next | 決定で次メッセージ／選択確定。最後なら exit |
| exit | 会話終了。フェードアウト → M02 復帰（位置・向き保持） |

---

## 5. レイアウト
- 共通: 画面下部に DialogBox（高さ `--rm-dialog-height`）。
- **M03A**: 探索画面を保持。DialogBox 左に PortraitSmall。背景はそのまま。
- **M03B**: 背景は維持しつつキャラクターを正面表示（PortraitFull）。下部に DialogBox。
- **M03C / M03D**: DialogBox のみ（Portrait・名前なし）。
- **M03E**: DialogBox 上に選択肢リスト（ChoiceList）。

---

## 6. 会話ボックス仕様（COMPONENT: DialogBox 参照）
- 部品: `DialogBox`。
- **色（確定値・TOKEN化が必要 → §15）**:
  - 背景: `#0B0D16`
  - 枠: `#EDEDED`
  - 文字: `#FFFFFF`
  - 名前色: `--rm-name-cyan`（既存トークン）
  - 選択中: 白い微発光
- テキスト: **3行以内**を推奨。超える場合は複数メッセージに分割。
- 行頭記号: `*`（半角アスタリスク＋スペース）を任意で付与可。地の文では省略可。
- 送りマーク: `▼` を wait 状態で右下に表示（点滅可）。
- テキスト表示: 1文字ずつ（`--rm-text-speed`）、句読点で小休止（`--rm-pause-short` / `--rm-pause-long`）。

---

## 7. Portrait の2分離（確定 / COMPONENT 連動 → §15）
| 種別 | 用途 | サイズ | 表示位置 |
|---|---|---|---|
| PortraitSmall | 探索会話（M03A） | 64〜96px 程度 | DialogBox 左側 |
| PortraitFull | イベント会話（M03B）・ボス・感情イベント | キャラクター立ち絵 | キャラ正面表示 |

- 表示条件: speaker が話者の場合のみ。地の文・独り言（M03C）・システム通知（M03D）は Portrait なし。
- 表情差分は感情に応じて切替（**素材制作は本書の対象外**。本書は表示ルールのみ）。

---

## 8. 選択肢（M03E / COMPONENT: ChoiceList 参照）
- DialogBox 上に選択肢を縦並び表示。
- カーソル移動: ↑↓ / W・S / タップ。決定: Enter / Z / タップ。
- 選択中の項目は白い微発光で示す。

---

## 9. システム通知（M03D）
- 名前なし・Portrait なし・DialogBox のみ。
- アイテム取得・セーブ通知・フラグ通知に使用。会話と同じ送り操作で閉じる。

---

## 10. 推奨 CSS（TOKEN 参照のみ・生値直書き禁止）
```css
.rm-explore-dialog {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  min-height: var(--rm-dialog-min-height);
  background: var(--rm-dialog-m03-bg);      /* #0B0D16 を TOKEN に追加 */
  border: 1px solid var(--rm-dialog-m03-border); /* #EDEDED */
  border-radius: var(--rm-dialog-radius);
  padding: var(--rm-dialog-padding-y) var(--rm-dialog-padding-x);
  color: var(--rm-dialog-m03-text);         /* #FFFFFF */
  line-height: var(--rm-dialog-line-height);
}
.rm-explore-dialog .rm-name { color: var(--rm-name-cyan); }
.rm-explore-dialog .rm-choice.selected { /* 白い微発光 */ }
.rm-explore-dialog .rm-next-mark { /* ▼ : wait 時のみ表示・点滅 */ }
```
> `--rm-dialog-m03-bg/border/text` は `DESIGN_TOKEN` に追加してから参照する（§15）。

---

## 11. 入力
- 決定（次へ／選択確定）: Enter / Z / タップ。
- キャンセル / 会話スキップ: Esc / X / 右クリック。
- 選択肢カーソル移動: ↑↓ / W・S / タップ。
- typing 中の決定: 全文を即時表示（早送り）。
- 会話中は探索入力（移動・調べる）をロックする。

---

## 12. 遷移
- M02 → M03: 近接対象に決定入力（ExploreActionButton 発火）。
- M03 → M03: 次メッセージ／選択分岐。
- M03 → M02: 会話終了 → 探索復帰（`playerX` / `dir` を保持）。
- M03 → M04: 記憶・白層化など演出が必要なときのみ（`SCREEN_VN_OVERLAY`）。M04 で通常会話は扱わない。

---

## 13. 受け入れ条件
- 探索中の決定で DialogBox がフェードインし、探索入力がロックされる。
- M03A で PortraitSmall（左）、M03B で PortraitFull（正面）が表示される。
- M03C / M03D は Portrait・名前なしで DialogBox のみ。
- M03E で選択肢が出て、カーソル移動・決定ができる。
- 終了で探索画面に戻り、プレイヤーの位置・向きが保持される。
- 色・サイズはすべて `DESIGN_TOKEN` 変数経由（生値直書きが無い）。

---

## 14. 禁止事項
- 戦闘UI・コマンドUI・HPゲージの表示（M03 の対象外）。
- 既存作品（UNDERTALE 等）の画像・素材・フォントの流用。
- M04 で通常会話を扱う／M03 が記憶演出を抱える（責務違反）。
- 4行以上の長文を1メッセージに詰める。
- 物語・セリフ内容の追加（本書は UI 仕様に限定）。
- 新規数値・新規部品の発明（`DESIGN_TOKEN` / `COMPONENT_DEFINITIONS` を更新してから参照する）。

---

## 15. 連動更新が必要な正本（本SCREENを有効化する前提・各1文書1PR）
- **MODE_DEFINITION**: M03 を「会話専用・5サブモード（A〜E）」に更新。**M03B で立ち絵（PortraitFull）を許可**（現行「M03＝立ち絵なし」を改訂）。M03/M04 の責務分離を明記。
- **DESIGN_TOKEN**: M03 会話ボックス色を追加 — `--rm-dialog-m03-bg #0B0D16` / `--rm-dialog-m03-border #EDEDED` / `--rm-dialog-m03-text #FFFFFF`、選択中の微発光。
- **COMPONENT_DEFINITIONS**: `Portrait` を `PortraitSmall`（64〜96px・DialogBox左）/ `PortraitFull`（立ち絵）に分離。M03D システム通知の扱いを追記。M03E は既存 `ChoiceList` を流用。

---

## 16. 未確認事項
- トウの内心独白（M03C）の表示トーン（行頭 `*` の有無など）。
- PortraitFull（立ち絵）と M04 で使う立ち絵の素材共用可否。

---

## 17. 改訂履歴
- v0.1: 初版ドラフト。M03 探索会話の状態・レイアウト・会話ボックス・顔グラ・2形態の使い分け・入力・遷移を定義。
- v0.2: M03 確定方針を反映。会話専用モード化（M04非統合）、5サブモード（M03A〜E）、Portrait2種（Small/Full）、会話ボックス色確定（#0B0D16 / #EDEDED / #FFFFFF）、M03/M04 責務分離、連動更新リスト（§15）を追加。v0.1 の未確認3点を確定済みに反映。
