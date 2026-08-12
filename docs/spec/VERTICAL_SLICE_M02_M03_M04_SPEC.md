# 縦スライス実装仕様書 — M02 探索 → M03A 会話 → M04 VN Overlay → Map 復帰

> 対象実装ファイル: `docs/rewrite-dev/index.html`
> 検証スクリプト: `tools/check_vertical_slice.py`
> ステータス: **仕様（この文書）＋検証スクリプトのみ。ゲーム本体の実装は別PR。**
> 目的: ベンチマーク（MOTHER3 の見下ろし探索設計 ＋ RewriteMemory UIUX_BIBLE §5 の UNDERTALE型/Ib型）を元に、**Claude Code 単体で確実に実装完了まで到達できる**最小の縦スライス1本を、固定ID・固定DOM・固定関数名まで確定する。

---

## 0. ベンチマーク（実装の判断基準）

### 0-1. 参照素材

| 出典 | 内容 | 本スライスへの寄与 |
| --- | --- | --- |
| MOTHER3 攻略本ワールドマップ（提供写真 IMG_6428〜6430） | 見下ろし型の歩けるワールド。`START`地点、散在する調べポイント（ナッツ/ヤスリ/ドラゴのキバ 等のアイテム）、建物（SHOP/BED/家）、章構成（第1章） | **M02 探索のレベルデザイン言語**：開始地点＋世界に散らばる微発光インタラクト＋建物＝イベント |
| `docs/design/UIUX/RewriteMemory_UIUX_BIBLE.md` §5 ベンチマーク | 5.1 UNDERTALE型＝M03探索会話（立ち絵なし・下部会話窓・探索画面を保つ）／5.2 Ib型＝M04 VNオーバーレイ（探索画面維持・立ち絵・暗幕・記憶/白層化） | **M03A と M04 の体験原型** |
| `docs/design/UIUX/SCREEN/SCREEN_TALK_WINDOW.md` | M03 Talk Window の画面正本 | M03A の DOM/挙動の正本 |
| `docs/design/UIUX/SCREEN/SCREEN_VN_OVERLAY.md` | M04 VN Overlay の画面正本（探索の上に重ねる） | M04 overlay の DOM/レイヤー順の正本 |
| `docs/design/UIUX/DESIGN_TOKEN.md` | 色・サイズ・発光・時間の数値正本 | 生値直書き禁止。トークン参照 |

### 0-2. ベンチマーク対応表（MOTHER3 要素 → 本スライスのモード）

| MOTHER3 の要素 | 本スライスでの表現 | 担当モード | 既存/新規 |
| --- | --- | --- | --- |
| `START` 地点 | walk シーンの `startX` | M02 | 既存 |
| 歩けるワールド | `WK` 横移動ワールド（`worldWidth` 幅・カメラ追従） | M02 | 既存 |
| 散在するアイテム（ナッツ等）＝調べる | `type:"obj"` ＋ `talk`（近接で ✦ 微発光 → 調べ会話） | M02→M03A | 既存 |
| フィールド上の NPC ＝話す | `type:"npc"` ＋ `talk`（近接で … 微発光 → 会話） | M02→M03A | 既存 |
| 建物/イベント（記憶が動く重要地点） | `type:"obj"` ＋ `vn`（暗幕＋立ち絵を Map の上に重ねる） | M02→M04 | **新規（本仕様の核）** |
| 会話/イベント後にフィールドへ戻る | `WK.resume()` で同じ位置へ復帰 | →M02 | 既存(M03A)/新規(M04) |
| `BED`（宿・セーブ）/`SHOP` | **本スライスでは扱わない（非目標）** | — | — |

> ⚠️ 既存 walk エンジンは**横移動（←→）の1レーン**である。MOTHER3 の2D見下ろし移動そのものは**再現しない**（非目標）。採用するのは MOTHER3 の**レベルデザイン言語**（開始地点＋散在する発光インタラクト＋建物＝イベント）だけ。

---

## 1. スコープ

### 1-1. このスライスで実現すること（1本の遊びの筋）

```
起動 → walk シーン slice_ch01_walk（M02 探索）
  ├ ✦ ベンチを調べる         → M03A（独り言・名前なし。探索画面保持）→ 探索へ復帰
  ├ … ミオに話す             → M03A（顔アイコン＋名前。探索画面保持）→ 探索へ復帰
  └ ✦ 時計塔を見上げる       → M04 VN Overlay（暗幕＋立ち絵＋白層化。Map を残す）→ 同じ位置で探索へ復帰
```

- **M02**：既存 `WK` walk エンジンを使い、`slice_ch01_walk` を1シーン追加する。
- **M03A**：既存 M03A エンジン（`WK.doAction()` → `M03A.start()`）を**そのまま**使う。
- **M04**：**Map の上に重ねる VN Overlay エンジン `VNO` を新規実装**する（現状の `vn` 全画面遷移＝`showVN`は使わない）。

### 1-2. 非目標（このスライスでやらないこと）

- 2D 見下ろし移動、上下移動、複数マップ間の遷移。
- BED（宿/セーブ）・SHOP・バトル（M05/M06）・タイトル（M00）。
- 既存シーン（`ch01_*` 等 143 シーン）のテキスト改変・リネーム・削除。
- 顔アイコン素材（PortraitSmall）の新規制作。素材が無い場合はテキストのみで進行（§5-7）。
- `localStorage` 永続化。

---

## 2. 既存エンジンの再利用（調査で確定した事実）

`docs/rewrite-dev/index.html` に既に存在し、**本スライスがそのまま使う**もの：

| 機構 | 実体（関数/変数） | 挙動 |
| --- | --- | --- |
| walk 描画・移動 | `showWalk(s)` / `wkTick()` / `wkRender()` / `WK` | `startX`・`worldWidth`・`objects[]` を読み、←→移動＋カメラ追従＋近接発光（`Math.abs(playerX-obj.x)<8`） |
| 近接アクション | `WK.doAction()` | `WK.nearTarget` に対して `talk` があれば M03A、無ければ `gotoScene`（全画面遷移） |
| 探索の停止/復帰 | `WK.pause()` / `WK.resume()` | 移動・近接判定を止める/再開する（背景・スプライトは残る） |
| M03A 会話 | `M03A.start(lines, onDone)` / `M03A.render()` / `M03A.next()` / `M03A.end()` | 下部会話窓 `#m03a-dialog`。`line.name`（任意）・`line.portrait`（任意・PortraitSmall）・`line.text`。終了時 `onDone()` |
| フラグ | `setCh01Flag(name)` / `hasCh01Flag(name)` / `CH01_STATE.flags` | シーン/オブジェクト/選択の `setFlag` で立つ。章内・セッション内のみ（非永続） |
| シーン整合チェック | `tools/check_scenes.py` | 参照切れ・id重複・0件を検出 |

**確定した現状の制約 / 差分**

- 現状 `runScene()` の `s.type==='vn'` は `showVN()` → `show('S-scene')` で**別画面へ全画面遷移**する。これは Ib型（探索画面維持）に反する。
- よって本スライスの M04 は、`vn` シーンへ遷移するのではなく、**walk 画面 `#S-walk` の内側に重なる overlay** として新規実装する。これが唯一の新規エンジンである。

---

## 3. データ契約（実装が必ず従うスキーマ）

### 3-1. walk シーン（本スライスで追加する1件）

固定 id：**`slice_ch01_walk`**（`type:"walk"`）。必須フィールド：

| フィールド | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `id` | string | ● | `"slice_ch01_walk"` 固定 |
| `type` | string | ● | `"walk"` 固定 |
| `location` | string | ● | HUD 左に表示する地名 |
| `time` | string | ● | HUD 時刻（例 `"17:17"`） |
| `bg` | string | ● | CSS background（既存アセット再利用可） |
| `startX` | number | ● | 開始 X（%）。MOTHER3 の `START` に相当 |
| `worldWidth` | number | ● | ワールド幅（%）。`> 100` |
| `objects` | array | ● | 下記オブジェクト（**3件以上**） |

### 3-2. walk オブジェクト schema（`objects[]` の各要素）

| フィールド | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `type` | `"obj"` \| `"npc"` | ● | `obj`＝頭上 `✦`（調べる）/ `npc`＝頭上 `…`（話す） |
| `name` | string | ● | 表示名 |
| `x` | number | ● | ワールド上の位置（%） |
| `action` | string | – | 近接ラベル（例 `"調べる"`／`"話す"`） |
| `icon` | string | – | `obj` のアイコン絵文字（`sprite` 無い時） |
| `sprite` | string | – | 画像パス（`assets/…`） |
| `setFlag` | string | – | 近接アクション実行時に立てるフラグ |
| `eerie` | bool | – | 微発光の明滅演出 |
| `talk` | array | – | **M03A** 会話行の配列（§3-3）。あれば最優先で M03A |
| `vn` | array | – | **M04** VN ビートの配列（§3-4）。`talk` が無く `vn` があれば M04 overlay |
| `scene` | string | – | 全画面遷移先 id（既存挙動。`talk`/`vn` の両方が無い時のフォールバック） |
| `sceneIfFlag` | `{flag,scene}` | – | フラグ有りで `scene` を差し替え（既存挙動） |

**`WK.doAction()` のディスパッチ優先順位（実装が従う確定仕様）**

1. `t.setFlag` があれば `setCh01Flag(t.setFlag)`。
2. `t.talk` があれば → `WK.pause()` → `M03A.start(t.talk, onDone)`。`onDone` は「遷移先(`scene`/`sceneIfFlag`)があれば進む、無ければ `WK.resume()`」。**（既存挙動を維持）**
3. `t.talk` が無く `t.vn` があれば → `WK.pause()` → `VNO.start(t.vn, onDone)`。`onDone` は「遷移先があれば進む、無ければ `WK.resume()`」。**（本仕様で新規追加）**
4. いずれも無ければ → `WK.teardown()` → `WK.gotoScene(t)`（既存の全画面遷移）。

### 3-3. M03A 会話行 schema（`talk[]` の各要素）

| フィールド | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `text` | string | ● | 本文 |
| `name` | string | – | 話者名。無ければ名前行を出さない（M03C 独り言 / M03D 通知） |
| `portrait` | string | – | PortraitSmall（顔アイコン）画像パス。無ければ非表示でテキストのみ進行 |

### 3-4. M04 VN ビート schema（`vn[]` の各要素）※本仕様で新規定義

| フィールド | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `text` | string | ● | 本文（会話窓に表示） |
| `name` | string | – | 名前プレート。無ければ非表示 |
| `portrait` | string | – | 立ち絵（バストアップ）画像パス。無ければ立ち絵なしでテキスト進行（§5-7） |
| `effect` | `"white"` | – | 記憶/白層化演出をこのビートで発火（`--rm-white-layer-*` トークン） |

---

## 4. M04 VN Overlay — DOM 契約（`#S-walk` の内側に追加）

`SCREEN_VN_OVERLAY.md` §3 レイヤー順（探索→暗幕→粒子/白層→立ち絵→名前→会話窓→ヒント）に従い、**walk 画面の子として**以下を追加する。id は固定。

```html
<!-- #S-walk の内側、.walk-controls より前に配置 -->
<div class="walk-vn" id="walk-vn">
  <div class="walk-vn-dim"></div>
  <div class="walk-vn-white" id="walk-vn-white" aria-hidden="true"></div>
  <img class="walk-vn-portrait" id="walk-vn-portrait" alt="" aria-hidden="true">
  <div class="walk-vn-dialog">
    <div class="walk-vn-name" id="walk-vn-name"></div>
    <div class="walk-vn-text" id="walk-vn-text"></div>
    <div class="walk-vn-hint">クリック / Space で進む</div>
  </div>
</div>
```

**必須 DOM id（検証スクリプトが存在を確認する）**：`walk-vn` / `walk-vn-portrait` / `walk-vn-name` / `walk-vn-text` / `walk-vn-white`。

**CSS 要件（DESIGN_TOKEN を参照。生値直書き禁止）**

| 要素 | 要件 | 参照トークン |
| --- | --- | --- |
| `.walk-vn` | `position:absolute; inset:0;` 初期 `display:none`。`.show` で表示。`z-index` は `--rm-m04-z-index`(60) 相当だが walk-controls より上 | `--rm-m04-z-index` |
| `.walk-vn-dim` | 暗幕。**背景 Map を完全に消さない**半透明 | `--rm-m04-dim` |
| `.walk-vn-white` | 白層化。既定は透明、`effect:"white"` で `opacity` を上げる | `--rm-white-layer-opacity` / `--rm-white-layer-glow` |
| `.walk-vn-portrait` | 立ち絵。右下寄せ。画面いっぱいにしない | `--rm-portrait-*` |
| `.walk-vn-dialog` | 下部会話窓（`--rm-m04-safe-margin` 余白） | `--rm-window-*` / `--rm-dialog-*` |
| `.walk-vn-name` | 名前プレート | `--rm-name-cyan` |

---

## 5. M04 VN Overlay — エンジン契約（新規 `VNO`）

`M03A` と対になる最小エンジン。**関数名・シグネチャは固定**（検証スクリプトが存在を確認する）。

```
var VNO = { beats:null, idx:0, onDone:null, active:false };

VNO.start(beats, onDone)   // beats が空なら即 onDone()。active=true。#walk-vn に .show。keydown 登録。VNO.render()
VNO.render()               // 現在ビートの name/portrait/text/effect を DOM へ反映。最終ビートでヒントを「▸ とじる」相当に
VNO.next()                 // idx を進める。末尾で VNO.end()
VNO.end()                  // active=false。.show 解除。keydown 解除。onDone を1回だけ呼ぶ
```

### 5-1. 挙動要件

1. **開始**：`VNO.start()` の前に呼び出し側（`WK.doAction()`）が `WK.pause()` 済みであること。overlay 表示中は探索の移動・近接判定を止める。
2. **背景保持（Ib型の核）**：`#S-walk` の walk-world / walk-player / objects は**消さず**、`.walk-vn-dim` で沈めて残す。全画面 `show('S-scene')` へ切り替えない。
3. **送り**：`#walk-vn` クリック、または Space/Enter で `VNO.next()`。`effect:"white"` のビートで `#walk-vn-white` を発光。
4. **立ち絵なし耐性**：`portrait` が無いビートは `#walk-vn-portrait` を非表示にしてテキストだけで進行（会話を止めない）。
5. **終了→Map 復帰**：末尾で `VNO.end()` → `onDone()`。`onDone` は「遷移先があれば `runScene`、無ければ **`WK.resume()`**」。復帰後、プレイヤーは**同じ位置**にいる（`WK.playerX` を変更しない）。
6. Esc で途中終了を許可してよい（任意。許可する場合も末尾同様 `VNO.end()` 経由で `onDone()` を1回だけ呼ぶ）。

### 5-2. `WK.doAction()` への追加（§3-2 の優先順位3を実装）

```
// 既存の talk 分岐の直後に追加（scene 全画面遷移より前）
if (t.vn && t.vn.length) {
  WK.pause();
  VNO.start(t.vn, function () {
    if (!WK.gotoScene(t)) WK.resume();
  });
  return;
}
```

---

## 6. 縦スライスのシーン定義（実装が投入する具体データ）

`SCENES` 配列に **`slice_ch01_walk` を1件追加**する（既存データは改変しない、additive）。内容は以下を満たすこと（テキストは調整可、**構造は必須**）。

```jsonc
{
  "id": "slice_ch01_walk",
  "type": "walk",
  "location": "テリの広場",
  "time": "17:17",
  "bg": "#0a0a12 url(assets/white_square_bg.png) center/cover no-repeat",
  "startX": 12,
  "worldWidth": 170,
  "objects": [
    {
      "type": "obj", "name": "ベンチ", "icon": "🪑", "x": 42,
      "action": "調べる", "setFlag": "slice_bench_checked",
      "talk": [                                   // ← M03A（独り言・名前なし＝M03C）
        { "text": "古いベンチ。ペンキが半分だけ剥げている。" },
        { "text": "（ここに、誰かが座っていた気がする。\n——誰だっけ。）" }
      ]
    },
    {
      "type": "npc", "name": "ミオ", "x": 88,
      "sprite": "assets/mio_sprite_front.png",
      "action": "話す", "setFlag": "slice_mio_talked",
      "talk": [                                   // ← M03A（顔アイコン＋名前）
        { "name": "ミオ", "portrait": "assets/mio_sprite_front.png",
          "text": "「あ、トウ。……ここ、静かだね」" },
        { "name": "ミオ", "portrait": "assets/mio_sprite_front.png",
          "text": "「時計の音だけが、聞こえる」" },
        { "text": "ミオは時計塔の方を、ちらりと見た。" }   // 名前なし＝ト書き
      ]
    },
    {
      "type": "obj", "name": "時計塔", "icon": "🕰", "x": 150,
      "action": "見上げる", "setFlag": "slice_tower_seen", "eerie": true,
      "vn": [                                     // ← M04 VN Overlay（暗幕＋立ち絵＋白層化）
        { "text": "時計塔を見上げた。\n毎日 17:17 に鐘が鳴る。" },
        { "name": "ミオ", "portrait": "assets/mio_sprite_front.png",
          "text": "「……もう、思い出せないの」" },
        { "effect": "white", "text": "白い光が、視界に薄く重なった。" },
        { "text": "（——今、誰かの声がした気がした。）" }
      ]
    }
  ]
}
```

**このシーンを最初に表示する**：起動導線（`si` の初期化 or タイトル→開始）から `slice_ch01_walk` に入れること。最小実装では `var si=0` の初期シーンを本 walk にするか、既存の開始点から `next`/遷移で到達させる（**参照切れを作らない**）。

---

## 7. 実装手順（Claude Code 向け・この順で行う）

1. **CSS**：`docs/rewrite-dev/index.html` の `<style>` に `.walk-vn*` を追加（§4。DESIGN_TOKEN 参照。生値直書き禁止）。必要なら `:root` に DESIGN_TOKEN の該当変数を用意。
2. **DOM**：`#S-walk` の内側（`.walk-controls` の前）に §4 の overlay マークアップを追加。
3. **エンジン**：`M03A` の定義の近くに `VNO` を追加（§5）。
4. **ディスパッチ**：`WK.doAction()` に §5-2 の `vn` 分岐を追加（`talk` 分岐の直後・`scene` 遷移の前）。
5. **データ**：`SCENES` に §6 の `slice_ch01_walk` を追加（additive のみ）。起動時に本 walk へ入る導線を用意。
6. **検証**：
   - `python3 tools/check_scenes.py docs/rewrite-dev/index.html` → **PASS**（参照切れ0・id重複0）。
   - `python3 tools/check_vertical_slice.py docs/rewrite-dev/index.html` → **PASS**（§8 の全項目）。
   - 実機（ブラウザ）で 起動→ベンチ調べ(M03A)→ミオ会話(M03A)→時計塔(M04 overlay で Map が残る)→同じ位置で復帰 を目視確認。

**変更ファイルは `docs/rewrite-dev/index.html` の1つのみ**（additive）。既存 143 シーン・既存エンジンの挙動を壊さない。

---

## 8. 完了条件（受け入れ基準）＝ `tools/check_vertical_slice.py` が PASS

実装 PR は、以下を自動判定する `tools/check_vertical_slice.py` が **PASS（exit 0）** になるまで完了としない。スクリプトが検査する項目：

| # | 判定項目 | 合格条件 |
| --- | --- | --- |
| C1 | SCENES が解析可能 | `SCENES=[…]` が JSON として解析でき、シーン数 > 0 |
| C2 | 参照整合 | 全 `scene`/`next`/`skip`/`sceneIfFlag.scene`/`objects[].scene` が既存 id に解決。id 重複なし（`check_scenes` 相当） |
| C3 | スライス walk シーン存在 | id `slice_ch01_walk` が `type:"walk"` で存在し、`startX`・`worldWidth`・`objects`(≥3) を持つ |
| C4 | M03A 導線 | `slice_ch01_walk.objects` に `talk`(配列・各要素 `text` あり) を持つ要素が **≥1** |
| C5 | M04 導線 | 同 objects に `vn`(配列・各要素 `text` あり) を持つ要素が **≥1** |
| C6 | M04 DOM | HTML に id `walk-vn` / `walk-vn-portrait` / `walk-vn-name` / `walk-vn-text` / `walk-vn-white` が存在 |
| C7 | M04 エンジン | HTML に `VNO.start` / `VNO.end` の定義が存在 |
| C8 | ディスパッチ結線 | `WK.doAction` 内で `t.vn` を参照し `VNO.start(` を呼ぶ |
| C9 | Map 復帰 | M04 経路で `WK.resume(` を呼ぶ（同じ位置で探索へ戻る）ことがコード上確認できる |
| C10 | 非破壊 | 既存 walk シーン `ch01_walk_plaza` が引き続き存在（削除・リネームしていない） |

> 現時点（実装前）は C3〜C9 が未達のため **FAIL** する。これは正しい状態＝「実装 PR が緑にすべきゲート」を意味する。スクリプトは各項目の ✅/❌ を一覧表示する。

---

## 9. リスクと最小実装

| # | リスク | 対策 |
| --- | --- | --- |
| R1 | SCENES が巨大1行。手編集で JSON 破壊・参照切れ | additive 追加のみ。`check_scenes.py` で PASS 必須 |
| R2 | M04 を全画面遷移で作ると Ib型（Map 保持）に反する | `#S-walk` 内 overlay として実装（§4/§5）。`show('S-scene')` を使わない |
| R3 | 復帰時にプレイヤー位置がリセットされる | `VNO.end()`→`WK.resume()` は `WK.playerX` を変更しない（`resume` は `dir`/`nearTarget` のみリセット） |
| R4 | 顔アイコン/立ち絵素材が未整備で表示崩れ | `portrait` 無しはテキストのみで進行（§3-3/§3-4/§5-1.4）。既存 `mio_sprite_front.png` を暫定流用可 |
| R5 | overlay の keydown が探索の keydown と二重発火 | `VNO.start` で `WK.pause()`（探索 keydown 解除）済みを前提。`VNO.end` で自身の keydown を解除してから `WK.resume()` |
| R6 | フラグ非永続（`CH01_STATE.flags`）で跨セッション回収不可 | 本スライスはフラグを立てる（記録）のみ。回収は範囲外 |

---

## 付録: 参照した既存実装（`docs/rewrite-dev/index.html`）

- walk：`showWalk()` / `wkTick()`（近接 `Math.abs(playerX-obj.x)<8`）/ `wkRender()` / `WK.pause/resume/doAction/gotoScene`
- M03A：`M03A.start/render/next/end`、DOM `#m03a-dialog` / `#m03a-name` / `#m03a-portrait` / `#m03a-text` / `#m03a-next`
- フラグ：`setCh01Flag` / `hasCh01Flag` / `CH01_STATE.flags`
- 全画面 VN（本スライスでは不使用）：`showVN()` → `show('S-scene')`
- 既存 walk シーン：`ch01_walk_plaza`（`objects[].talk` / `objects[].scene` / `sceneIfFlag` の実例）
