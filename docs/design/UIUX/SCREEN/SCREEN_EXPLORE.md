# SCREEN_EXPLORE v0.3（ドラフト）

**対象画面: M02 探索モード（付随: M03 探索会話・M04 VN への遷移）**

> 役割: M02 探索画面の具体仕様。上位 `MODE_DEFINITION` の構造を、`COMPONENT_DEFINITIONS` / `DESIGN_TOKEN` の正本を使って画面へ落とす中間層。
> 状態: 本PRで新規作成（ドキュメントのみ・ドラフト v0.1）。
> 正本ルール: 数値は `DESIGN_TOKEN`、部品は `COMPONENT_DEFINITIONS` を参照する。生値・独自部品を本書で発明しない。

---

## 1. 対象モード
- 主: **M02 探索モード**（移動・調査・自由行動）
- 遷移先: M03 探索会話（独り言・NPC会話） / M04 VN オーバーレイ（記憶・白層化演出）
- 本書は M02 の画面に限定。M03 会話窓の中身と M04 演出は各 SCREEN に委譲する。

---

## 2. 目的
`MODE_DEFINITION` の UI 原則「**画面を見るのではなく、世界を見る**」を、画面として実現する。

- 常時 UI を最小化し、世界（背景・スプライト）へ視線を集める。
- 違和感・調査対象を **微発光（GlowTarget）** と **近接インジケータ（ExploreIndicator）** で静かに誘導する。
- 決定入力で会話／演出へ橋渡しする。

体験の核: 「ただ歩く画面」ではなく「**世界の違和感を探す画面**」にする。

---

## 3. 画面状態モデル
探索画面は 4 状態を遷移する。

| 状態 | 説明 | UI |
|---|---|---|
| idle（通常） | 移動のみ。対象に未接近 | 常時UIなし（移動UI・位置表示のみ） |
| near（近接） | 調査対象/NPCに近づいた | 微発光、ExploreIndicator強調、ExploreActionButton出現 |
| act（決定） | 決定入力を受けた | 入力ロック、M03/M04へ遷移開始 |
| dialog（会話） | M03会話窓表示中 | DialogBox表示、探索入力ロック |

---

## 4. レイアウト（z 順・下＝奥）
1. 背景（世界）
2. ワールド／レイヤー（スプライト配置）
3. プレイヤー（高さ `--rm-explore-player-height`）
4. NPC / オブジェクト（`--rm-explore-npc-height` / `--rm-explore-object-size`）
5. GlowTarget / ExploreIndicator（近接対象に付随）
6. 位置・時刻表示（上部・常時・低主張）
7. 移動 UI（下部・モバイル操作用）
8. ExploreActionButton（下部・**近接時のみ**）
9. DialogBox（M03 時・下部）

接地ライン: `--rm-explore-ground-bottom`。

---

## 5. 推奨 CSS（TOKEN 参照のみ・生値直書き禁止）
```css
.rm-explore-root {
  background: var(--rm-bg-black);
  color: var(--rm-text-main);
}

/* 微発光誘導（GlowTarget） */
.rm-explore-target.near,
.rm-glow-target.near {
  filter: drop-shadow(var(--rm-glow-soft));
}

/* 近接インジケータ（ExploreIndicator） */
.rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-idle);
  transition: opacity var(--rm-fade-fast);
}
.rm-explore-target.near .rm-explore-indicator {
  opacity: var(--rm-indicator-opacity-near);
}
```

---

## 6. 使用コンポーネント（`COMPONENT_DEFINITIONS` 参照）
- **ExploreIndicator** … 近接対象を示す（`✦` 調査 / `…` NPC / `?` 不明）。遠距離は非表示／極薄、近接時のみ強調。
- **GlowTarget** … 違和感・調査対象の微発光誘導。弱く静かに。
- **ExploreActionButton** … 近接時の決定行動（「調べる」「話しかける」「見上げる」等）。常時／複数／遠距離表示は禁止。
- **DialogBox** … M03 会話窓（本書では呼び出しのみ）。
- **NamePlate** … 探索中の独り言の名前表示（任意）。

※ M02 では **Portrait を使わない**（探索スプライトを使用）。

---

## 7. 入力
- 移動: 画面の移動 UI（↑↓←→）＋キーボード（↑↓←→ / WASD）。
- 決定: **near 時のみ有効**。A / Space / タップ → ExploreActionButton 発火 → M03 / M04。
- `idle` 時は決定入力を無効化する。
- 初回チュートリアル時のみ「調べる方法」を案内し、以降は非表示。

---

## 8. 誘導表現の原則
- 発光は弱く静か（`--rm-glow-soft` を基準、強調が要る箇所のみ `--rm-glow-strong`）。
- インジケータは遠距離で非表示／極薄、近接で強調。頭上長文・下部ボタンとの二重文言は禁止。
- パーティクルは探索通常時に多用しない（M04 の白層化へ温存）。

---

## 9. 位置・時刻表示
- 上部に低主張で常時表示（既存実装の位置表示を踏襲）。
- 主張を抑え、世界より目立たせない。

---

## 10. 遷移
- M02 → M03: 調査 / NPC 接近＋決定（短い独り言・会話）。終了後 M02 復帰、**探索位置を保持**。
- M02 → M04: 記憶・白層化など重要演出。OverlayDim で探索画面を保持したまま暗幕、探索入力ロック。
- M02 → M07: 分岐発生時（選択肢）。

---

## 11. 現状実装とのギャップ＆反映チェックリスト
`docs/rewrite/index.html` の現状を確認した結果の差分。**実装PRはこのリストを反映項目とする。**

実装済み（定義と整合）:
- [x] 移動 UI（`walk-dpad` / `startMove`）
- [x] 近接時のみの決定ボタン（`walk-act` が `display:none` → 近接表示, `doAction`）
- [x] プレイヤー／世界スプライト（`walk-player` ほか）
- [x] 位置表示（`walk-info`）

未反映・要確認（定義にあるが実装で確認できなかった）:
- [ ] **ExploreIndicator（✦/…/? 近接インジケータ）**: 実装に該当クラスが見当たらない → 追加、または既存 `near` 判定への紐付けを確認
- [ ] **GlowTarget（微発光誘導）**: `drop-shadow(glow)` の付与が確認できない → 近接対象への発光適用を確認
- [ ] **命名の対応**: 実装は `walk-*`、定義は `rm-explore-*`。**改名は必須ではない**。本書に対応関係を持たせ、実装は機能で満たす（命名統一は任意・別タスク）
- [ ] **縦移動（↑↓）/ WASD**: 現行 `walk-dpad` は ←→ のみ。本書で入力を 4 方向＋WASD に拡張したため、縦移動の追加要否を実機で確認

> 注: 上記「未反映」は grep 範囲での未確認であり断定ではない。実装PR着手時に `index.html` の `near` 判定周辺を実機確認して確定する。

---

## 12. 受け入れ条件
- `idle` 時に余計な常時ボタン（移動 UI・位置表示を除く）が出ていない。
- 調査対象 / NPC に近づくと、微発光＋インジケータ強調＋決定ボタン出現が起こる。
- 決定で M03 / M04 へ遷移し、戻ると探索位置が保たれる。
- 数値・色はすべて TOKEN 変数経由（生値直書きが無い）。

---

## 13. 禁止事項
- 常時ボタン（移動 UI・位置表示を除く）の表示。
- インジケータ頭上の長文表示／下部ボタンとの二重文言。
- 探索通常時のパーティクル多用。
- 本書での新規数値・新規部品の発明（TOKEN / COMPONENT を更新してから参照する）。
- 物語・世界観・キャラクター設定の追加（本書は UI 仕様に限定）。

---

## 14. 未確認事項
- ExploreIndicator / GlowTarget が実機で機能しているか（`near` 周辺の実装確認が必要）。
- map 表現の扱い（単一横スクロールか複数 map か）。本書は単一探索画面前提で記述。複数 map / 画面遷移が必要なら別途仕様化。
- 会話（M03 / `EXPLORE_DIALOG`）の窓仕様は本書対象外（次 SCREEN で作成）。

---

## 15. 実装対応名
本仕様上の名称と既存実装名は以下の対応とする。

| 仕様名 | 既存実装名 | 備考 |
|---|---|---|
| rm-explore-root | walk-screen / walk-area | 改名必須ではない |
| ExploreActionButton | walk-act | 近接時のみ表示 |
| 移動UI | walk-dpad | モバイル操作用 |
| 位置表示 | walk-info | 上部低主張 |
| near判定 | 現行JSの近接判定 | Glow / Indicator をここに接続 |
| GlowTarget | 未実装または未確認 | 追加対象 |
| ExploreIndicator | 未実装または未確認 | 追加対象 |

---

## 16. 探索モードの正規化（walk 一本化）

**決定**: 探索は walk(M02) に一本化する。`type:'explore'`（hotspots 方式）は非採用とする。

理由: hotspots 方式（画面に常時ボタンを散在＋巨大立ち絵）は MODE_DEFINITION の「常時ボタン禁止／画面ではなく世界を見る」に正面から反するため。

対象（要移行・全1件）:
- `ch01_explore_bench`（`type:'explore'`）

移行ルール（hotspots → objects）:
| explore (hotspots) | walk (objects) |
|---|---|
| label | action |
| x（画面%） | x（worldWidth 基準で再配置） |
| y | 廃止（横移動・接地のため） |
| next | scene |
| 対象種別 | type: npc / obj |

確認が必要（ChatGPT / Miya 判断・物語フロー）:
- `ch01_explore_bench` は `ch01_walk_plaza` と対象（ミオ / 5席目の跡 / 時計塔）が重複している。
  - 案A: explore_bench を廃止し、フローを walk_plaza に集約
  - 案B: 会話後の「2周目探索」として walk 化し、別状態で残す
- `skip:ch01_1717` / `skipLabel:"17:17 →"` の「次へ進む」導線を walk でどう表現するか

実装方針: 上記確認が済むまで `showExplore` / `hotspot-btn` は残す（即削除しない）。移行は 1 PR = 1 目的、データ変更（hotspots→objects）は中リスクとして人間レビュー前提。

---

## 17. 改訂履歴
- v0.1: 初版ドラフト。M02 探索画面の状態モデル・レイアウト・誘導・遷移・実装ギャップを定義。
- v0.2: 入力を 4 方向（↑↓←→ / WASD）へ拡張。状態表を整形。実装対応名（§15）を追加。タイトルを v0.2 に更新。
- v0.3: 探索モードの正規化方針（walk 一本化・hotspots 非採用、対象 `ch01_explore_bench`）を §16 に追加。
