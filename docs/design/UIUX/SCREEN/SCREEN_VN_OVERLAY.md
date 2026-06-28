# SCREEN_VN_OVERLAY v1.0

> **M04 VN Overlay は「重要イベント専用」。通常会話は M03 Talk Window（顔アイコン式 / SCREEN_TALK_WINDOW.md）で扱う。**  
> 旧 M01（VN 会話向き）と旧 M03B（立ち絵イベント会話）の用途は本モードに統合する。  
> 対象: 記憶断片・白層化・章ラスト・ボス前後・感情が大きく動く重要会話。

> 役割：M04 VN オーバーレイモードの画面仕様。  
> 構造定義は `RewriteMemory_MODE_DEFINITION.md`、数値は `DESIGN_TOKEN.md`、部品は `COMPONENT_DEFINITIONS.md` を参照する。

---

## 1. 対象モード

M04 VN オーバーレイモード。

構造定義は `RewriteMemory_MODE_DEFINITION.md` を参照する。

本書は M04 の画面仕様を定義する。

---

## 2. 目的

探索画面から本編 VN 画面へ切り替えるのではなく、探索画面の上に記憶が重なる体験を作る。

RewriteMemory の核。

```text
探索
↓
違和感
↓
記憶が重なる
↓
ミオ
↓
探索へ戻る
```

---

## 3. 基本構成

レイヤー順。

1. 探索画面
2. 暗幕
3. 粒子 / 白層化
4. ミオ立ち絵
5. 名前プレート
6. 下部会話窓
7. 入力ヒント

---

## 4. 推奨 HTML 構造

```html
<div class="rm-vn-overlay" id="walk-vn" hidden>
  <div class="rm-vn-overlay__dim"></div>
  <div class="rm-vn-overlay__particles" aria-hidden="true"></div>

  <img
    class="rm-vn-overlay__portrait"
    id="walk-vn-portrait"
    alt=""
    aria-hidden="true"
  />

  <div class="rm-vn-overlay__dialog">
    <div class="rm-name-plate" id="walk-vn-name"></div>
    <div class="rm-dialog-text" id="walk-vn-text"></div>
    <div class="rm-input-hint">クリック / Space で進む ・ Esc で閉じる</div>
  </div>
</div>
```

---

## 5. 推奨 CSS

```css
.rm-vn-overlay {
  position: absolute;
  inset: 0;
  z-index: var(--rm-m04-z-index);
  display: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.rm-vn-overlay.is-active {
  display: block;
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
  object-fit: contain;
  pointer-events: none;
  user-select: none;
  filter: drop-shadow(var(--rm-glow-soft));
}

.rm-vn-overlay__portrait.is-white-layer {
  opacity: var(--rm-white-layer-opacity);
  filter:
    blur(var(--rm-white-layer-blur))
    drop-shadow(var(--rm-white-layer-glow));
}

.rm-vn-overlay__dialog {
  position: absolute;
  left: var(--rm-m04-safe-margin);
  right: var(--rm-m04-safe-margin);
  bottom: var(--rm-m04-safe-margin);
  height: var(--rm-m04-dialog-height);
  box-sizing: border-box;
  background: var(--rm-window-bg);
  border: 1px solid var(--rm-window-border);
  border-radius: var(--rm-dialog-radius);
  padding: var(--rm-dialog-padding-y) var(--rm-dialog-padding-x);
  color: var(--rm-text-main);
  line-height: var(--rm-dialog-line-height);
}
```

---

## 6. M04 第1段階

実装済み対象。

- walk2d 探索画面
- 空席イベント
- 暗幕
- 下部テキストボックス
- クリック / Space 送り
- Esc 終了
- 探索復帰

含めないもの。

- 立ち絵
- 名前表示
- 粒子
- 選択肢
- AUTO
- LOG

---

## 7. M04 第2段階

次に実装するもの。

- ミオ立ち絵
- 表情差分
- 名前表示
- 白層化
- 粒子
- フェード
- DESIGN_TOKEN 反映
- COMPONENT 反映

---

## 8. 表示ルール

M04 中は探索画面を完全に消さない。

暗幕で沈めるが、背景の存在は残す。

プレイヤーは「別画面に飛んだ」のではなく、「同じ場所に記憶が重なった」と感じる必要がある。

---

## 9. ミオ立ち絵

対象。

- `mio_neutral`
- `mio_smile`
- `mio_surprised`
- `mio_sad`
- `mio_angry`
- `mio_troubled`
- `mio_serious`
- `mio_white_layer`

配置。

- 中央〜やや右
- 最大 48vh
- 探索背景を完全に塞がない

禁止。

- 顔アップ
- 巨大表示
- 複数立ち絵
- 集合絵

---

## 10. 名前表示

表示する場合。

- ミオが明確に話している
- 話者が確定している

非表示。

- ナレーション
- ？？？
- 記憶の声
- 白層化中の曖昧な声

---

## 11. 会話窓

下部固定。

探索画面に重なる。

高さは DESIGN_TOKEN を参照。

文字は読みやすく、静かに。

---

## 12. 入力

対応。

- クリック
- タップ
- Space
- Enter
- Esc

動作。

- クリック / タップ / Space / Enter: 次へ
- Esc: 閉じる
- 最後まで読む: 自動的に閉じる
- 閉じたら探索へ戻る

---

## 13. 探索入力ロック

M04 中は探索入力を停止する。

- 左右移動停止
- 決定入力停止
- 対象物判定停止

M04 終了後に探索入力を復帰する。

二重入力禁止。

---

## 14. 推奨 JS インターフェース

実装名は既存コードに合わせてよいが、責務は以下を満たすこと。

```js
function startVNOverlay(sceneId) {
  // 1. 対象シーンを取得
  // 2. 探索入力を停止
  // 3. overlay を表示
  // 4. 最初の beat を描画
}

function nextVNOverlayBeat() {
  // 1. 次の beat へ進む
  // 2. 最後なら closeVNOverlay()
}

function closeVNOverlay() {
  // 1. overlay を非表示
  // 2. portrait / text / name を初期化
  // 3. 探索入力を復帰
}
```

### ガード条件

- M04 中に M02 探索入力を受け付けない
- M04 中に二重起動しない
- 画像読み込み失敗で停止しない
- 終了後は同じ探索位置に戻る

---

## 15. 白層化

`white_layer` 表情では、以下を使う。

- 低コントラスト
- 白発光
- 粒子
- ゆっくりしたフェード
- 静かな消失感

白層化は恐怖ではなく喪失。

---

## 16. onerror

画像読み込みに失敗しても、M04 を止めない。

画像が無ければ立ち絵を非表示にし、テキストだけで進行する。

---

## 17. 受け入れ条件

- 探索画面から空席イベントを開始できる
- 画面遷移せず暗幕が重なる
- 下部会話窓が出る
- テキストが送れる
- Esc で閉じられる
- 最後まで読むと閉じる
- 探索へ戻れる
- 立ち絵が無くても壊れない
- 375px 幅で破綻しない

---

## 18. 禁止事項

- M04 中に探索移動できる
- 背景を完全に消す
- 巨大立ち絵を出す
- 通常 VN 画面へ飛ばす
- M01 と M04 を混同する
- M04 第2段階で M02 探索 UI まで変更する
- SCREEN_EXPLORE の範囲を混ぜる

---

## 19. 改訂履歴

- v1.0: 初版。M04 VN オーバーレイの目的、レイヤー、入力、ミオ立ち絵、白層化、受け入れ条件、HTML/CSS/JS 参照仕様を定義。
