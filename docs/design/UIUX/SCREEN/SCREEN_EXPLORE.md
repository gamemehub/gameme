# SCREEN_EXPLORE v1.0

> 役割：M02 探索モードの画面仕様正本。  
> 思想は `../RewriteMemory_UIUX_BIBLE.md`、構造は `../RewriteMemory_MODE_DEFINITION.md`、数値は `../DESIGN_TOKEN.md`、部品は `../COMPONENT_DEFINITIONS.md` を参照する。  
> 俯瞰図は `../assets/mode_definition_v1.1.png` を参照する。

---

## 1. 対象モード

M02 探索モード。

探索画面は、プレイヤーが世界の中を移動し、違和感や記憶の痕跡を見つけるためのモードである。

M02 は「UIを見る画面」ではなく、「世界を見る画面」である。

---

## 2. 目的

Chapter01 で最初に成立させる探索体験は以下。

```text
探索する
↓
違和感を見つける
↓
対象に近づく
↓
微発光・インジケータが出る
↓
調べる
↓
M03 探索会話 or M04 VNオーバーレイへ
↓
終了後、同じ探索地点へ戻る
```

プレイヤーに「次に何を押せばいいか」ではなく、「何かがおかしい」と気づかせる。

---

## 3. 現在の正史

公開検証の正史は以下。

```text
gamemehub/gameme
docs/rewrite-stage/index.html
```

実験場・素材置き場は以下。

```text
gamemehub/gameme
docs/rewrite-dev/index.html
```

本番公開は以下。

```text
gamemehub/gameme
docs/rewrite/index.html
```

private 原本・計画側は以下。

```text
gamemehub/RewriteMemory
docs/index.html
```

M02 探索モードの仕様は、本書を正本とし、実装はまず `rewrite-stage` で検証する。

---

## 4. 画面の基本構成

### レイヤー順

```text
Layer 0: 背景
Layer 1: 地面・床・奥行き
Layer 2: オブジェクト
Layer 3: NPC
Layer 4: プレイヤー
Layer 5: 近接発光
Layer 6: 頭上インジケータ
Layer 7: 下部アクションボタン
Layer 8: M03 探索会話
Layer 9: M04 VNオーバーレイ
```

M04 は M02 の上に重なる。M02 を破壊しない。

---

## 5. 画面イメージ

```text
┌──────────────────────────────────────────────┐
│                                              │
│                 背景 / 世界                 │
│                                              │
│  ミオ                              5席目の跡 │
│  …                                  ✦        │
│ [NPC]                              [□]       │
│                                              │
│                 トウ                         │
│                [Player]                      │
├──────────────────────────────────────────────┤
│  近接時のみ: 「跡を調べる」                 │
└──────────────────────────────────────────────┘
```

遠距離ではボタンも説明文も出さない。

近接時のみ、対象物の発光・インジケータ・下部ボタンが現れる。

---

## 6. 探索中の表示ルール

### 通常時

表示するもの。

- 背景
- プレイヤー
- NPC
- オブジェクト
- 最小限の地名

表示しないもの。

- 常時ボタン
- 長い説明文
- メニュー
- ミニマップ
- クエストリスト
- SAVE / LOAD
- AUTO / SKIP / LOG
- 会話窓

---

### 近接時

対象に近づいた時だけ表示するもの。

- 対象物の微発光
- 頭上インジケータ
- 下部アクションボタン

頭上インジケータの使い分け。

| 対象 | 表示 |
|---|---|
| 調査対象 | `✦` |
| NPC | `…` |
| 不明 / 危険 | `?` |

頭上に長い文字を出さない。

文字説明は下部アクションボタンに集約する。

---

## 7. 操作

### PC

| 操作 | 内容 |
|---|---|
| ← / A | 左移動 |
| → / D | 右移動 |
| Space / Enter | 近接対象を調べる / 話す |
| Esc | M03 / M04 中断、またはメニュー系を閉じる |

### スマホ

| 操作 | 内容 |
|---|---|
| 左ボタン | 左移動 |
| 右ボタン | 右移動 |
| 対象タップ / 下部ボタン | 調べる / 話す |

375px 幅で破綻しないこと。

---

## 8. M02 からの遷移

### M02 → M03 探索会話

短い反応、独り言、軽い調査結果。

例。

```text
机の上に、古いノートがある。
```

特徴。

- 探索画面は維持
- 立ち絵なし
- 下部会話枠のみ
- 短く終わる
- 終了後 M02 へ戻る

---

### M02 → M04 VNオーバーレイ

記憶、白層化、ミオに関わる重要イベント。

例。

```text
ここに、誰かがいた。
けれど、その名前だけが思い出せない。
```

特徴。

- 探索画面の上に暗幕
- 立ち絵や粒子が重なる
- 探索入力を一時停止
- 終了後 M02 へ戻る

---

### M02 → M05 バトル

敵・記憶の影との接触。

本PRでは対象外。

---

## 9. Chapter01 探索対象の初期正史

### 時計塔前の広場

初期対象。

| 対象 | 種別 | 表示 | 遷移 |
|---|---|---|---|
| トウ | プレイヤー | 探索スプライト | - |
| ミオ | NPC | 探索スプライト / `…` | M03 or M01 |
| 5席目の跡 | 調査対象 | `□` + `✦` | M04 |
| 時計塔 | 調査対象 | 時計塔表現 + `✦` | M03 or M04 |

優先する体験。

```text
5席目の跡を見つける
↓
近づく
↓
✦ と微発光
↓
跡を調べる
↓
M04
↓
ミオの記憶
↓
探索へ戻る
```

---

## 10. キャラクター表示ルール

### トウ

M02 では探索スプライトで表示する。

禁止。

- VN立ち絵をそのまま使う
- 画面を覆う大きさにする
- 探索中に顔アップ表示する

### ミオ

M02 では NPC 探索スプライトで表示する。

M04 では立ち絵を使用してよい。

M02 と M04 のミオ表示を混同しない。

---

## 11. 背景

背景は探索の「世界」を作る最重要要素。

優先順位。

1. 視認性
2. 静けさ
3. 奥行き
4. 記憶の痕跡
5. 操作対象の見つけやすさ

背景が強すぎて対象物が見えない場合、対象物発光とコントラストを優先する。

---

## 12. 推奨 HTML 構造

実装名は既存コードに合わせてよいが、責務は以下を満たすこと。

```html
<section id="S-walk" class="rm-explore-screen">
  <div class="rm-explore-world">
    <div class="rm-explore-bg"></div>
    <div class="rm-explore-ground"></div>

    <div class="rm-explore-object" data-kind="object">
      <div class="rm-explore-indicator">✦</div>
      <div class="rm-explore-object-icon">□</div>
    </div>

    <div class="rm-explore-npc" data-kind="npc">
      <div class="rm-explore-indicator">…</div>
      <img class="rm-explore-npc-sprite" src="assets/mio_sprite_front.png" alt="">
    </div>

    <div class="rm-explore-player">
      <img class="rm-explore-player-sprite" src="assets/tou_sprite_front.png" alt="">
    </div>
  </div>

  <div class="rm-explore-hud">
    <button class="rm-explore-move rm-explore-move-left">←</button>
    <button class="rm-explore-move rm-explore-move-right">→</button>
    <button class="rm-explore-action" hidden>跡を調べる</button>
  </div>
</section>
```

---

## 13. 推奨 CSS

```css
.rm-explore-screen {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--rm-bg-black);
  color: var(--rm-text-main);
}

.rm-explore-world {
  position: absolute;
  inset: 0;
}

.rm-explore-ground {
  position: absolute;
  left: 0;
  right: 0;
  bottom: var(--rm-explore-ground-bottom);
  height: 1px;
  background: var(--rm-line-blue);
}

.rm-explore-player,
.rm-explore-npc,
.rm-explore-object {
  position: absolute;
  transform: translateX(-50%);
  transition:
    filter var(--rm-fade-fast),
    opacity var(--rm-fade-fast);
}

.rm-explore-player-sprite {
  height: var(--rm-explore-player-height);
  object-fit: contain;
  pointer-events: none;
  user-select: none;
}

.rm-explore-npc-sprite {
  height: var(--rm-explore-npc-height);
  object-fit: contain;
  pointer-events: none;
  user-select: none;
}

.rm-explore-object-icon {
  width: var(--rm-explore-object-size);
  height: var(--rm-explore-object-size);
  display: grid;
  place-items: center;
}

.rm-explore-indicator {
  position: absolute;
  left: 50%;
  bottom: 100%;
  transform: translateX(-50%);
  opacity: 0;
  font-size: var(--rm-indicator-size);
  color: var(--rm-white-memory);
  transition: opacity var(--rm-fade-fast);
  pointer-events: none;
}

.rm-explore-object.near,
.rm-explore-npc.near {
  filter: drop-shadow(var(--rm-glow-soft));
}

.rm-explore-object.near .rm-explore-indicator,
.rm-explore-npc.near .rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-near);
}

.rm-explore-action[hidden] {
  display: none;
}

.rm-explore-action {
  position: absolute;
  right: 4%;
  bottom: calc(4% + var(--rm-mobile-safe-bottom));
  min-height: var(--rm-mobile-button-min);
  background: var(--rm-window-bg);
  color: var(--rm-text-main);
  border: 1px solid var(--rm-window-border);
  border-radius: var(--rm-dialog-radius);
}
```

---

## 14. 推奨 JS 責務

実装名は既存コードに合わせてよい。

```js
const Explore = {
  active: false,
  playerX: 0,
  nearTarget: null,
  objects: []
};

function enterExplore(sceneId) {
  Explore.active = true;
  Explore.nearTarget = null;
  renderExplore();
  bindExploreInput();
}

function leaveExplore() {
  Explore.active = false;
  unbindExploreInput();
}

function tickExplore() {
  if (!Explore.active) return;

  const near = findNearTarget(Explore.playerX, Explore.objects);
  if (near !== Explore.nearTarget) {
    Explore.nearTarget = near;
    renderExplore();
  }
}

function doExploreAction() {
  if (!Explore.active) return;
  if (!Explore.nearTarget) return;

  const target = Explore.nearTarget;

  if (target.mode === "M03") {
    startExploreDialog(target.scene);
    return;
  }

  if (target.mode === "M04") {
    startVNOverlay(target.scene);
    return;
  }
}
```

---

## 15. 近接判定

推奨。

```js
function findNearTarget(playerX, objects) {
  return objects.find(obj => Math.abs(playerX - obj.x) < 8) || null;
}
```

ルール。

- 近接対象は1つだけ
- 複数重なる場合は最も近いもの
- 遠距離ではボタン非表示
- 停止中も近接状態が更新されること

---

## 16. M04 との関係

M04 開始時。

```text
M02入力停止
↓
M04表示
↓
M04入力有効
```

M04 終了時。

```text
M04非表示
↓
M04入力解除
↓
M02入力復帰
↓
同じ探索位置へ戻る
```

禁止。

- M04中に左右移動できる
- M04終了後に初期位置へ戻る
- M04中にM02ボタンが押せる
- M04とM01を混同する

---

## 17. 受け入れ条件

### 通常探索

- トウが表示される
- ミオが表示される
- 5席目の跡が存在する
- 遠距離ではボタンが出ない
- 近接時だけインジケータが出る
- 近接時だけボタンが出る

### 調査

- Space / Enter / タップで調べられる
- `5席目の跡` から M04 に遷移できる
- M04終了後に探索へ戻る

### 画面

- PCで破綻しない
- 375px幅で破綻しない
- 画像が読めなくても最低限壊れない

---

## 18. 禁止事項

- 常時ボタンを復活させる
- 頭上に長文を出す
- 下部ボタンと頭上文字を二重表示する
- 探索中にVN立ち絵を表示する
- M02とM04を混同する
- SCREEN_VN_OVERLAYの責務を本書へ移す
- コード変更と文書変更を同じPRに混ぜる

---

## 19. 実装順序

```text
PR35: 本書 SCREEN_EXPLORE.md
↓
PR36: M04第2段階
↓
PR37: 探索背景・小物
↓
PR38: Chapter01通しプレイ調整
```

---

## 20. 改訂履歴

- v1.0: 初版。M02探索モードの正史、表示ルール、レイヤー、HTML/CSS/JS参照仕様、M04との関係、受け入れ条件を定義。
