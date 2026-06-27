# RewriteMemory DESIGN TOKEN v1.0

> 役割：色、余白、サイズ、透明度、時間、発光、モード画面の基本レイアウト数値の正本。  
> 思想は `RewriteMemory_UIUX_BIBLE.md`、構造は `RewriteMemory_MODE_DEFINITION.md`、部品は `COMPONENT_DEFINITIONS.md` を参照する。

---

## 1. 目的

RewriteMemory の色、余白、サイズ、透明度、時間、発光を一元管理する。

数値の正本は本書とする。

他文書やコードに生値を増やさない。

---

## 2. 基本原則

- 色は静かにする
- UI は目立ちすぎない
- 記憶演出は白く淡く
- 金枠は上品に使う
- 暗幕は世界を消さず、重なりを見せる
- 375px 幅で破綻しない

---

## 3. CSS Token 推奨定義

実装時は、可能な範囲で以下の `:root` を参照する。

```css
:root {
  /* Background */
  --rm-bg-black: #03050a;
  --rm-bg-deep: #081018;
  --rm-bg-navy: #0d1626;
  --rm-bg-panel: rgba(8, 10, 18, .92);

  /* Text */
  --rm-text-main: #f0f2f7;
  --rm-text-sub: #a8b0c6;
  --rm-text-muted: rgba(210, 220, 240, .55);
  --rm-name-cyan: #AEE6FF;

  /* Line / Accent */
  --rm-gold-border: rgba(190, 160, 90, .62);
  --rm-gold-soft: rgba(210, 180, 110, .35);
  --rm-line-blue: rgba(120, 150, 220, .38);

  /* Memory / White layer */
  --rm-white-memory: rgba(235, 245, 255, .92);
  --rm-white-glow: rgba(210, 235, 255, .72);

  /* Overlay */
  --rm-overlay-dim: rgba(0, 0, 0, .45);
  --rm-overlay-deep: rgba(4, 6, 12, .55);

  /* Window */
  --rm-window-bg: rgba(8, 10, 18, .92);
  --rm-window-border: rgba(255, 255, 255, .10);

  /* Dialog */
  --rm-dialog-height: 24vh;
  --rm-dialog-min-height: 132px;
  --rm-dialog-padding-x: 18px;
  --rm-dialog-padding-y: 16px;
  --rm-dialog-radius: 6px;
  --rm-dialog-line-height: 1.7;

  /* M03 会話ボックス（SCREEN_EXPLORE_DIALOG） */
  --rm-dialog-m03-bg: #0B0D16;
  --rm-dialog-m03-border: #EDEDED;
  --rm-dialog-m03-text: #FFFFFF;

  /* Portrait */
  --rm-portrait-max-height: 48vh;
  --rm-portrait-max-width: 38vw;
  --rm-portrait-bottom: 23vh;
  --rm-portrait-right: 12vw;

  /* Explore */
  --rm-explore-player-height: 86px;
  --rm-explore-npc-height: 110px;
  --rm-explore-object-size: 28px;
  --rm-explore-ground-bottom: 62px;

  /* Glow */
  --rm-glow-soft: 0 0 8px rgba(170, 210, 255, .45);
  --rm-glow-strong: 0 0 16px rgba(190, 230, 255, .65);
  --rm-glow-white: 0 0 22px rgba(235, 245, 255, .75);

  /* Indicator */
  --rm-indicator-size: 12px;
  --rm-indicator-opacity-idle: .35;
  --rm-indicator-opacity-near: .95;

  /* M04 */
  --rm-m04-dim: rgba(4, 6, 12, .55);
  --rm-m04-dialog-height: 24vh;
  --rm-m04-safe-margin: 4%;
  --rm-m04-z-index: 60;

  /* Timing */
  --rm-fade-fast: .18s;
  --rm-fade-normal: .4s;
  --rm-fade-slow: .8s;
  --rm-text-speed: 40ms;
  --rm-pause-short: 150ms;
  --rm-pause-long: 400ms;

  /* White layer */
  --rm-white-layer-opacity: .72;
  --rm-white-layer-blur: 1.5px;
  --rm-white-layer-glow: 0 0 26px rgba(235, 245, 255, .8);

  /* Mobile */
  --rm-mobile-dialog-height: 28vh;
  --rm-mobile-safe-bottom: env(safe-area-inset-bottom);
  --rm-mobile-button-min: 44px;
}
```

---

## 4. 画面モード別の推奨サイズ

### M02 探索

```css
.rm-explore-root {
  background: var(--rm-bg-black);
  color: var(--rm-text-main);
}

.rm-explore-target.near {
  filter: drop-shadow(var(--rm-glow-soft));
}

.rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-idle);
}

.rm-explore-target.near .rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-near);
}
```

### M04 VN オーバーレイ

```css
.rm-vn-overlay {
  position: absolute;
  inset: 0;
  z-index: var(--rm-m04-z-index);
}

.rm-vn-overlay__dim {
  position: absolute;
  inset: 0;
  background: var(--rm-m04-dim);
}

.rm-vn-overlay__portrait {
  position: absolute;
  right: var(--rm-portrait-right);
  bottom: var(--rm-portrait-bottom);
  max-height: var(--rm-portrait-max-height);
  max-width: var(--rm-portrait-max-width);
  filter: drop-shadow(var(--rm-glow-soft));
}

.rm-vn-overlay__dialog {
  position: absolute;
  left: var(--rm-m04-safe-margin);
  right: var(--rm-m04-safe-margin);
  bottom: var(--rm-m04-safe-margin);
  height: var(--rm-m04-dialog-height);
  background: var(--rm-window-bg);
  border: 1px solid var(--rm-window-border);
  border-radius: var(--rm-dialog-radius);
  padding: var(--rm-dialog-padding-y) var(--rm-dialog-padding-x);
  line-height: var(--rm-dialog-line-height);
}
```

### White Layer

```css
.rm-white-layer {
  opacity: var(--rm-white-layer-opacity);
  filter:
    blur(var(--rm-white-layer-blur))
    drop-shadow(var(--rm-white-layer-glow));
}
```

---

## 5. 禁止

- コードへ数値を無秩序に直書きする
- 画面ごとに違う金色を使う
- 発光を強くしすぎる
- 暗幕で背景を完全に消す
- 立ち絵を画面いっぱいにする
- トークン名を画面ごとに増殖させる

---

## 6. 改訂履歴

- v1.0: 初版。色、サイズ、発光、M04、探索、モバイルの基本トークンと CSS 参照例を定義。
