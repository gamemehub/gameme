# RewriteMemory COMPONENT DEFINITIONS v1.0

> 役割：共通 UI 部品の正本。  
> 数値は `DESIGN_TOKEN.md`、構造は `RewriteMemory_MODE_DEFINITION.md`、思想は `RewriteMemory_UIUX_BIBLE.md` を参照する。

---

## 1. 目的

RewriteMemory の共通 UI 部品を定義する。

部品の責務は本書を正本とする。

数値は DESIGN_TOKEN を参照する。

構造は MODE_DEFINITION を参照する。

---

## 2. Component 一覧

- DialogBox
- NamePlate
- PortraitSmall
- PortraitFull
- OverlayDim
- ChoiceList
- ExploreIndicator
- ExploreActionButton
- GlowTarget
- ParticleLayer
- WhiteLayer
- FadeLayer
- LogView
- RelationshipGraph

---

## 3. DialogBox

用途。

- M03 探索会話
- M04 VN Overlay

（注: 旧 M01 VN・旧 M03B イベント会話は M04 に統合）
- M06 バトル会話
- M13 対話

責務。

- テキストを読む場所
- 世界を邪魔しない
- 下部固定を基本とする

推奨 CSS。

```css
.rm-dialog-box {
  background: var(--rm-window-bg);
  border: 1px solid var(--rm-window-border);
  border-radius: var(--rm-dialog-radius);
  padding: var(--rm-dialog-padding-y) var(--rm-dialog-padding-x);
  color: var(--rm-text-main);
  line-height: var(--rm-dialog-line-height);
}
```

禁止。

- 画面中央を覆う
- 高すぎる
- 常時表示する

---

## 4. NamePlate

用途。

話者名を表示する。

M04 ではミオ表示時に使用する。

推奨 CSS。

```css
.rm-name-plate {
  color: var(--rm-name-cyan);
  letter-spacing: .08em;
}
```

非表示条件。

- ナレーション
- 誰の声か不明
- 探索中の短い独り言

---

## 5. Portrait

Portrait は M03 v0.2 に合わせて PortraitSmall / PortraitFull に分離する。

M02 探索では使わない。

M02 では探索スプライトを使う。

### 5.1 PortraitSmall

用途。

M03A 探索会話用。

顔グラ・小型表情用。

表示位置。

DialogBox 左側に表示。

推奨サイズ。

64〜96px 程度。

使用モード。

- M03A 探索会話

### 5.2 PortraitFull

用途。

正面立ち絵。

M04 VN（重要イベント）用。

使用シーン。

- 重要会話
- ボス会話
- 感情イベント

使用モード。

- M04 VN Overlay

（注: 旧 M01 VN・旧 M03B イベント会話は M04 に統合）

推奨 CSS。

```css
.rm-portrait {
  max-height: var(--rm-portrait-max-height);
  max-width: var(--rm-portrait-max-width);
  object-fit: contain;
  pointer-events: none;
  user-select: none;
}
```

禁止。

- 顔アップ
- 巨大表示
- 複数キャラを無秩序に並べる
- 探索画面を完全に隠す

---

## 6. OverlayDim

用途。

M04 で探索画面の上に重ねる暗幕。

責務。

- 記憶が重なったことを示す
- 背景を完全には消さない
- プレイヤーの探索位置を保つ

推奨 CSS。

```css
.rm-overlay-dim {
  position: absolute;
  inset: 0;
  background: var(--rm-overlay-deep);
}
```

---

## 7. ChoiceList

用途。

選択肢表示。

使用モード。

- M07
- M06

数。

- 2〜4個
- 基本3個

禁止。

- 6個以上
- 長文選択肢
- 画面を埋める

---

## 8. ExploreIndicator

用途。

探索中の近接対象を示す。

表示。

- 調査対象: `✦`
- NPC: `…`
- 不明: `?`

遠距離では非表示または極薄。

近接時のみ強調。

推奨 CSS。

```css
.rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-idle);
  transition: opacity var(--rm-fade-fast);
}

.rm-explore-target.near .rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-near);
}
```

禁止。

- 頭上に長文を表示する
- 下部ボタンと同じ文言を二重表示する

---

## 9. ExploreActionButton

用途。

近接時の決定行動。

例。

- 跡を調べる
- 話しかける
- 見上げる

表示条件。

- 対象に近づいた時のみ
- 操作可能な時のみ

禁止。

- 常時表示
- 複数同時表示
- 遠距離表示

---

## 10. GlowTarget

用途。

違和感や調査対象の誘導。

対象。

- 5席目の跡
- 時計塔
- 不自然な物
- 記憶の痕跡

推奨 CSS。

```css
.rm-glow-target.near {
  filter: drop-shadow(var(--rm-glow-soft));
}
```

発光は弱く、静かにする。

---

## 11. ParticleLayer

用途。

記憶、白層化、空気の変化。

使用モード。

- M04
- M10

探索通常時には多用しない。

---

## 12. WhiteLayer

用途。

白層化演出。

効果。

- 低コントラスト
- 白発光
- 粒子
- 淡い消失感

推奨 CSS。

```css
.rm-white-layer {
  opacity: var(--rm-white-layer-opacity);
  filter:
    blur(var(--rm-white-layer-blur))
    drop-shadow(var(--rm-white-layer-glow));
}
```

ホラーではなく喪失を表す。

---

## 13. FadeLayer

用途。

画面遷移。

M11 遷移中モードで使う。

入力ロックとセットで使用する。

---

## 14. LogView

用途。

M12 記録 / バックログ。

表示対象。

- 会話ログ
- 記憶断片
- 人物情報
- 用語集

---

## 15. RelationshipGraph

用途。

M12 相関図。

ルール。

- プレイヤーが知った情報だけ表示
- 未確定は `?`
- 嘘の関係も現在の認識として表示
- 真相判明後に線や説明が変化

---

## 16. コンポーネント共通禁止事項

- 常時表示しない
- 画面を埋めない
- 同じ情報を二重表示しない
- モードをまたいで勝手に使わない
- 数値を持たない
- DESIGN_TOKEN を参照する

---

## 17. 改訂履歴

- v1.0: 初版。DialogBox、Portrait、Overlay、探索インジケーター、M12 相関図などの共通部品と CSS 参照例を定義。
