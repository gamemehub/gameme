# UIUX_MASTER.md
**RewriteMemory UI/UX ドキュメント索引（頂点）v1.0**

> 役割：UI/UX文書群の**入口・索引・統治ルール**。各文書の役割／読む順／正本関係／改訂運用をここで一元管理する。
> 状態：本PRで新規作成（ドキュメントのみ）。

---

## 1. 読む順（階層）
```
UIUX_MASTER（索引・本書）
  └ UIUX_BIBLE          … 思想・美学（上位）
     └ MODE_DEFINITION  … 画面モードの構造（中位）
        ├ DESIGN_TOKEN  … 色・サイズ・時間の数値（正本）
        ├ COMPONENT_DEFINITIONS … 共通UI部品（正本）
        └ SCREEN/*      … 各画面の具体仕様
```
迷ったら上位へ戻る：数値は DESIGN_TOKEN、部品は COMPONENT、構造は MODE_DEFINITION、思想は BIBLE。

---

## 2. 文書一覧と状態
| 文書 | 役割 | 正本範囲 | 状態 |
|---|---|---|---|
| `UIUX_MASTER.md` | 索引・統治 | 文書運用 | 本PRで作成 |
| `RewriteMemory_MODE_DEFINITION.md` | 画面モード M00–M13・遷移 | 構造 | **main既存（本PRで4節追記）** |
| `RewriteMemory_UIUX_BIBLE.md` | 美学・体験原則 | 思想 | ドラフト（別PR予定） |
| `DESIGN_TOKEN.md` | 色/サイズ/余白/時間の変数 | **数値の正本** | ドラフト（別PR予定） |
| `COMPONENT_DEFINITIONS.md` | 共通UI部品 | **部品の正本** | ドラフト（別PR予定） |
| `SCREEN/SCREEN_VN_OVERLAY.md` | M04画面仕様 | 画面 | ドラフト（別PR予定） |
| `SCREEN/SCREEN_EXPLORE.md` | M02画面仕様 | 画面 | 未作成（次PR） |
| `assets/mode_definition_v1.1.png` | モード一覧ボード図 | 図版 | 未コミット（別PR予定） |

※ 後回し（未作成）：SCREEN_TITLE / VN / EXPLORE_DIALOG / BATTLE / BATTLE_DIALOG / MENU / SAVELOAD / LOG / TALK。

---

## 3. 正本（Single Source of Truth）ルール
- **数値は `DESIGN_TOKEN` のみ**。他文書・コードは参照し、生値を直書きしない。
- **部品は `COMPONENT_DEFINITIONS` のみ**。各モードは部品を組み合わせるだけ。
- **構造は `MODE_DEFINITION`**。新規画面を自由に作らず既存モードに分類。
- 値・仕様の変更は**正本を1か所更新**して全体へ反映（重複記述を増やさない）。

---

## 4. 文書運用・改訂ルール
- 1 文書 = 1 責務。重複文書を作らない。
- 改訂は各文書末尾の「改訂履歴」に追記。バージョンは `vX.Y`。
- ドキュメント変更は**ドキュメントのみのPR**で行い、コード変更と混ぜない。
- main / develop へ直接 push 禁止、自動マージ禁止、人間レビュー前提。
- 図版は `assets/` に置き、文書から相対参照（参照先未コミットのリンク切れに注意）。

---

## 5. 推奨ディレクトリツリー
```
docs/design/UIUX/
├─ UIUX_MASTER.md
├─ RewriteMemory_UIUX_BIBLE.md
├─ RewriteMemory_MODE_DEFINITION.md
├─ DESIGN_TOKEN.md
├─ COMPONENT_DEFINITIONS.md
├─ SCREEN/
│   ├─ SCREEN_VN_OVERLAY.md
│   └─ SCREEN_EXPLORE.md（次PR）
└─ assets/
    └─ mode_definition_v1.1.png
```

---

## 6. 12月応募スコープ
- 必須は M04（VNオーバーレイ）と共通部品・トークン。これらで「探索→記憶が重なる→ミオ→探索へ戻る」を成立させる。
- BATTLE系・他SCREEN文書・フル相関図は後回し。文書を増やすより実体験を優先する。

---

## 7. 現在のTODO（文書側）
1. BIBLE / DESIGN_TOKEN / COMPONENT / SCREEN_VN_OVERLAY を別PRでコミット（ドラフトは用意済み）。
2. `assets/mode_definition_v1.1.png` を併せてコミット（リンク整合）。
3. SCREEN_EXPLORE.md を次PRで作成。
4. 実装は #217 所在確定後に M04 ミオ立ち絵統合へ。

---

## 8. 改訂履歴
- **v1.0**：初版。索引・階層・文書一覧と状態・正本ルール・運用ルール・ツリー・12月スコープ・TODOを定義。`MODE_DEFINITION v1.1`（main既存・本PRで4節追記）を構造の中位正本として位置づけ。
