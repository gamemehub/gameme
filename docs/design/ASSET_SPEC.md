# ASSET_SPEC：M03 Talk Window 顔アイコン（PortraitSmall / Face Icon）

> 位置づけ：**docs のみ・実装ではない**。M03 Talk Window で使う顔アイコンの素材仕様を確定する。
> 既存の Character Bible §13（命名規則）・§6（表情10キー）を踏襲し、新規則は作らない。
> 物語上の表情の使い分け（どの場面でどの表情か）は ChatGPT/Miya の領域。本書は技術仕様のみ。

---

## 1. GitHub上の現在のミオ画像（事実）

| 用途 | 実体 | サイズ/形式 | 備考 |
|---|---|---|---|
| 歩行マップNPC | `docs/rewrite-dev/assets/mio_sprite_front.png`（stage にも同名） | PNG RGBA / 251×360 | 探索スプライト |
| 会話立ち絵 | `index.html` の `MIO_SRC_NORMAL` / `MIO_SRC_ANXIOUS`（インラインSVG） | SVG data URI / 160×280 | 既存2値（normal/anxious） |
| **Talk Window 顔アイコン** | **未整備（0枚）** | — | 本仕様で新規定義 |

→ Talk Window 用の顔アイコン（`face` view）はリポジトリに存在しない。これが Issue #2 で用意する対象。

---

## 2. 添付ミオ画像を正式アセット化する切り出し方

添付キャラクターシートには「トークウィンドウ用アイコン」列がある。これを正式アセット化する。

- **元データ**：添付シートの顔アイコン列、または全身立ち絵（`full`）の顔部分。
- **切り出し**：正面顔を**正方形**でトリミング（顔の中心・目線の高さを揃える）。Bible §6 が「同一の顔の位置・サイズ・向き（正面）で目・眉・口・頬のみ差し替え」と定めているため、全表情で構図を固定すると差し替え時にズレない。
- **背景**：透過（RGBA）。Talk Window の黒背景に重ねる前提。
- **出力**：表情ごとに1ファイル（§4 命名規則）。

> 新規画像生成は行わず、まず添付シートからの切り出しを優先（前提：手元に切り出し可能な解像度があること。無ければ生成は別Issueで人間/ChatGPT判断）。

---

## 3. Face Icon のサイズ

- **表示サイズ**：64〜96px（COMPONENT の PortraitSmall に準拠。DialogBox 左）。
- **元画像**：正方形 **192×192px**（最大表示96pxの2倍＝Retina対応）。PNG RGBA。
- 縦横比は 1:1 固定（顔アイコンは正方形）。立ち絵（`full` 160×280 等）とは別物。

---

## 4. 命名規則（Bible §13 踏襲）

```
mio_face_<expression>[_<white>].png
```

- `<view>` は **face** 固定（Talk Window 顔アイコン）。
- `<expression>`：§5 の表情キー。
- `<white>`（任意）：`white00`|`white33`|`white66`|`white100`（省略 = white00）。白層化表現に使用。

例：`mio_face_normal.png` / `mio_face_anxious.png` / `mio_face_normal_white100.png`

---

## 5. 表情キー（Character Bible を正本に確定）

表情キーは **Character Bible §6 を正本**とする。Face Icon も Bible の表情キーに合わせ、新しい表記ゆれを作らない。

| キー（Bible §6 正本） | Face Icon ファイル |
|---|---|
| normal | `mio_face_normal.png` |
| smile | `mio_face_smile.png` |
| sad | `mio_face_sad.png` |
| anxious | `mio_face_anxious.png` |
| serious | `mio_face_serious.png` |
| surprise | `mio_face_surprise.png` |
| empty（虚ろ／白層化進行時） | `mio_face_empty.png` |

**確定事項**
1. **`surprise` を採用**（`surprised` は使わない。Character Bible が正本）。
2. 白層化は**単一キーにしない**。Bible 既存設計どおり、**通常表情キー `empty` ＋ 白層化サフィックス `_white100`** で表現する。
   - 例：白層化したミオ ＝ `mio_face_empty_white100.png`
   - 段階表現が要る場合は `_white33` / `_white66` / `_white100` を使い分け（省略時 = white00）。

---

## 6. 画像が無い場合のフォールバック（SCREEN_TALK_WINDOW §8 と整合）

1. 指定表情の画像が無い → **`normal` にフォールバック**。
2. `normal` も無い → **顔アイコンを非表示にしてテキストだけで進行**（会話は止めない）。
3. 名前が無い（独り言・通知）→ 名前行も顔アイコンも出さない。

→ アイコン未整備でも Talk Window は壊れない。実装（Issue #3）はこのフォールバック前提で進められる。

---

## 7. CH01 で最低限必要な顔アイコン数

- **技術的な最低ライン**：`normal`（基準）1枚あれば起動可能（他は normal フォールバック）。
- **CH01 テーマ（白層化）を考慮した推奨セット**：`normal` / `anxious` / `smile` / `sad` / `serious` / `surprise` / `empty`（白層化時は `empty_white100`）の **7枚**。
- **現実的な最小セット**：`normal` / `anxious` / `empty`（白層化は `empty_white100`）の **3枚**（基準・不安・白層化）。残りは normal フォールバックで成立。

> どの表情を優先するか（感情配分）は物語判断。ChatGPT/Miya が決める。本書は「3枚で起動でき、7枚で表現が揃う」という技術ラインを示すのみ。

---

## 8. GitHub に追加すべきファイルパス

| パス | 種別 | 内容 |
|---|---|---|
| `docs/design/ASSET_SPEC.md` | 新規 | 本仕様（顔アイコン）。Issue #2 で追加 |
| `docs/rewrite-dev/assets/characters/mio/face/mio_face_<expr>.png` | 新規（画像） | 顔アイコン本体。dev に配置 |
| `docs/characters/01_Mio_Character_Bible.md` | 追記（任意） | 「§ Talk Window 顔アイコン（face view）」節を追加し本書を参照。**surprise / empty / _white100 は Bible 既存設計のため修正不要**（本書が Bible に合わせる） |

※ 本番（`docs/rewrite/`）への配置は dev 検証後。

---

## 9. Issue 分割（画像生成 / 切り出し / 登録）

| Issue | 内容 | リスク | 担当 |
|---|---|---|---|
| **#2a（本書）** | `ASSET_SPEC.md` 追加（surprise / empty + _white100 で表記確定） | 低（docs） | Claude（docs） |
| #2b | 顔アイコン画像の用意（添付シート切り出し、不足分は生成） | 低〜中 | 人間 / ChatGPT |
| #2c | 画像を `docs/rewrite-dev/assets/characters/mio/face/` に登録（コミット） | 低 | 人間（画像コミット） |
| → #3 | M03A エンジンに PortraitSmall を接続し、dev で時計塔/ミオ会話に顔アイコン表示 | 中（コード） | Claude（実装案）/ dev検証 |

---

## 未確認事項

- 手元に切り出し可能な解像度の元画像があるか（無ければ #2b で生成）。
- CH01 で実際に使う表情の優先順位（物語判断・ChatGPT/Miya）。

> 表情キーの表記（`surprise` 採用・白層化は `empty` + `_white100`）は本書で**確定済み**。

---

## 次にワクワクするポイント

- 顔アイコンが3枚（normal/anxious/empty）揃うだけで、Talk Window でミオの「白層化した虚ろな無表情」と「不安」が出し分けられ、会話が一気に“感情のある探索”になります。
- 命名が Bible と揃っているので、将来 full（立ち絵・M04用）と face（顔アイコン・M03用）を同じ表情キーで管理でき、CH08 まで破綻しません。
