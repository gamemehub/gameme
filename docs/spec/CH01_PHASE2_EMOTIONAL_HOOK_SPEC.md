# CH01 Phase2 感情フック統合仕様書

> 対象: `docs/rewrite-dev/index.html`（SCENES）
> ステータス: **仕様のみ / 実装しない（docsのみ）**
> 目的: 「誰も覚えてない」「忘れないでね」の2モチーフを Chapter01 の導線に統合する際の、安全な接続点・変更範囲・最小実装案を確定する。

---

## 0. 前提（調査で確定した現状）

### 0-1. 2モチーフは「テキストとしては既に存在する」

| モチーフ | 既存の出現箇所（scene id） | 種別 | 現状の扱い |
| --- | --- | --- | --- |
| 「誰も覚えてない」 | `legacy_ch01_030_missing_chair` | vn | ミオの台詞「でも、誰も覚えてない」。清掃員・通行人・店員が皆「そんな椅子ありましたっけ」と答える、椅子（＝記録）消失の目撃シーン |
| 「忘れないで」（グリッチ） | `ch01_anlog_flood` | phone | 白く抜けたブランクメッセージ「でも、忘れないで」。アンログ氾濫の演出 |
| 「…ないでね」（章末・半欠落） | `legacy_ch01_090_phone` | phone | 章末の最終メッセージ「ねえ、わたしの＿＿＿こと、＿＿＿＿＿ないでね。」＝ "わたしのこと、忘れないでね" の "忘れ" 等がブランクで欠落した状態。**章末フックは既にここに実装済み** |
| 「じゃあ、忘れないでね」（完全版） | `ending_unlog` / `after_unlog`（Ch07エンディング系） | vn | ミオが本物の笑顔で言う完全版。**ペイオフ（回収）として終盤に予約済み** |

→ Phase2 の本質は「新規テキストの追加」ではなく、**既に点在する2モチーフを導線（フラグ）で結び、章末フックの意味を強める**こと。

### 0-2. Chapter01 終盤の導線（確定）

```
ch01_anlog_flood   (phone: 「でも、忘れないで」グリッチ)
  → ch01_anlog_end
  → legacy_ch01_030_missing_chair   ← 「誰も覚えてない」目撃   ★接続点A
  → ch01_060_choice         (memory: どうする？)
  → ch01_070{a|b|c|d}       (vn: 観察/回避/質問/待機)
  → ch01_070_reconstruction (memory: 断片を再構成)
  → ch01_080_truth          (vn: 真相「椅子に座っていた人が消えた」)
  → legacy_ch01_090_phone   ← 章末「…ないでね」半欠落フック   ★発火点B
  → ch01_099_continued      (continued: 章区切り)
  → ch02_001_morning_log ...
```

※ `legacy_ch01_030_missing_chair` は末尾 beat に `next` を持たず、配列順フォールスルー（`ns()` → `si++`）で `ch01_060_choice` に進む。`legacy_` 接頭辞だが**現行アクティブ導線上**にある（孤立シーンではない）。

### 0-3. 再利用できる既存フラグ機構（エンジン改修なし）

| 機構 | 実体 | 発火タイミング |
| --- | --- | --- |
| シーンの `setFlag` | `runScene()`: `if (s.setFlag) setCh01Flag(s.setFlag)` | そのシーンに**入った瞬間** |
| walkオブジェクトの `setFlag` / `sceneIfFlag:{flag,scene}` | `WK.doAction()` | アクション実行時に立て、フラグ有りなら分岐先を差し替え |
| showMemory option の `setFlag` / `intent` / `next` | `showMemory()` btn.onclick | 選択確定時 |
| `CH01_STATE.flags` | `setCh01Flag(name)` / `hasCh01Flag(name)` | 任意 |

- 状態本体: `CH01_STATE = { observation, trust, choseNotToLook, fragments, flags:{} }`
- **重要な制約:** `sceneIfFlag` による「フラグ分岐」は **`walk` オブジェクトでのみ**サポート。`vn` / `phone` / `memory` / `continued` は静的 `next`（または配列順）のみで、**フラグによる分岐を持たない**。
- `CH01_STATE.flags` は localStorage に保存しない（章内・セッション内のみ）。

---

## 1. 「誰も覚えてない」をどの既存シーンに接続するのが安全か

**結論: 新規シーンを作らず、既存の `legacy_ch01_030_missing_chair` をそのまま正規の目撃点として再利用する。**

- このシーンは既に「椅子（記録）が消え、誰もそれを覚えていない」という本モチーフの中核台詞を含む。テーマ的にも導線的にもここが唯一の自然な接続点。
- 安全策として、このシーンに**シーンレベル `setFlag: "ch01_no_one_remembers"` を1つ追加するだけ**にする。プレイヤーがこの目撃を通過した事実を記録し、章末フック（§2）および Phase3 の回収（§4）に渡す。
- 補強の余地（任意・Phase2範囲内）: ミオの「誰も覚えてない」に対するトウの応答 beat を1つ追加し、「僕は覚えてる」系の対比を置くと、章末「忘れないでね」への伏線が締まる。**ただし最小実装ではフラグ追加のみで成立する**ため、beat 追加は任意とする。
- 種まきは `ch01_hook`（冒頭「誰もいない」「あなたは、誰ですか？」）や `ch01_anlog_flood`（グリッチ）に既に存在するため、**新たな種まきシーンは不要**。

---

## 2. 「忘れないでね」を章末のどこで発火させるのが安全か

**結論: 既存の章末フック `legacy_ch01_090_phone`（半欠落メッセージ）をそのまま発火点とする。位置の移動・新規追加はしない。**

- `legacy_ch01_090_phone` は `ch01_080_truth`（真相）直後、`ch01_099_continued`（章区切り）直前に置かれた章末 phone であり、**「わたしのこと、忘れないでね」が "忘れ" を欠落させた形で既に発火している**。導線上もっとも安全な発火点。
- Phase2 ではここに**シーンレベル `setFlag: "ch01_dont_forget_shown"` を追加**し、章末フックを通過した事実を記録する（テキスト変更は不要）。
- **やってはいけないこと:**
  - Ch07 エンディング系（`ending_unlog` / `after_unlog`）の完全版「じゃあ、忘れないでね」を Chapter01 に前倒し・複製すること。終盤ペイオフを潰すため不可。
  - `phone` シーンに対しフラグ条件で章末を分岐させること（§0-3 の制約によりエンジン改修が必要 → Phase3）。

---

## 3. 既存SCENESのどのIDを変更対象にするか

**変更は既存2シーンへの「フィールド追加（additive）」のみ。新規ID追加・既存IDのリネーム/削除はしない。**

| scene id | 変更内容 | 種別 |
| --- | --- | --- |
| `legacy_ch01_030_missing_chair` | `setFlag: "ch01_no_one_remembers"` を追加（＋任意でトウの応答 beat 1つ） | additive |
| `legacy_ch01_090_phone` | `setFlag: "ch01_dont_forget_shown"` を追加（テキスト変更なし） | additive |

- `legacy_` 接頭辞のIDは現行導線の `next` / 配列順フォールスルーに組み込まれているため、**リネーム・削除厳禁**（参照切れの原因になる）。
- Phase2 では**新規 scene id を追加しない**（dangling `next` のリスク回避）。

---

## 4. Phase2でやる範囲 / Phase3に回す範囲

### Phase2（この仕様の実装対象・小さなPR）
- `legacy_ch01_030_missing_chair` に `setFlag: "ch01_no_one_remembers"` を追加。
- `legacy_ch01_090_phone` に `setFlag: "ch01_dont_forget_shown"` を追加。
- （任意）目撃シーンにトウの応答 beat を1つだけ追加。
- 制約: **エンジン改修なし / 新規ID なし / フラグ分岐なし**。`docs/rewrite-dev/index.html` のみ・最小diff。
- 完了条件: `python3 tools/check_scenes.py docs/rewrite-dev/index.html` が **PASS（参照切れ0件）**。

### Phase3（別タスク・規模大）
- 立てたフラグの**回収（ペイオフ）**:
  - 後続章で `hasCh01Flag('ch01_dont_forget_shown')` / `ch01_no_one_remembers` を参照し、演出・台詞を分岐。
  - 章末「…ないでね」の欠落文字を、回収シーンで**復元表示**する感情的コールバック。
  - Ch07 エンディング「じゃあ、忘れないでね」完全版への橋渡し。
- `vn` / `phone` でフラグ分岐が必要な箇所（§0-3 の制約）→ **汎用ヘルパー（例: vn シーンの `sceneIfFlag` 対応）の要否を別途設計**。導入是非を含め Phase3 で判断。
- SE / 視覚エフェクト強化、`CH01_STATE.flags` を跨セッションで使う必要が出た場合の永続化方針。

---

## 5. 想定されるリスクと最小実装案

### リスクと対策
| # | リスク | 対策 |
| --- | --- | --- |
| R1 | SCENES が巨大な1行のため、手編集で JSON 破壊・参照切れが起きうる | **追加（additive）編集のみ**。実装後に `check_scenes.py` で PASS / 参照切れ0件を必須確認 |
| R2 | `legacy_` IDのリネーム/削除で `next`・配列順チェーンが切れる | リネーム・削除しない。Phase2は新規IDも作らない |
| R3 | `vn`/`phone` はフラグ分岐不可（walkのみ対応）。章末を条件分岐させようとするとエンジン改修が必要 | Phase2では**フラグを立てるだけ**に留め、分岐・回収はPhase3へ |
| R4 | エンディング限定の「じゃあ、忘れないでね」を前倒しすると終盤ペイオフを潰す | Ch07エンディング系テキストは一切触らない |
| R5 | `CH01_STATE.flags` は localStorage 非保存。跨セッションの回収には使えない | Phase3で跨セッション回収が必要になった時点で永続化方針を別途検討（Phase2では章内利用のみ） |

### 最小実装案（Phase2・実装は別PR）
- 変更ファイル: `docs/rewrite-dev/index.html` のみ。
- 変更量: 既存2シーンへ `setFlag` を各1つ追加（＋任意beat1つ）。実質 2〜4 行程度の additive diff。
- 立てるフラグ:
  - `ch01_no_one_remembers` … 「誰も覚えてない」目撃の通過記録（`legacy_ch01_030_missing_chair`）。
  - `ch01_dont_forget_shown` … 章末「…ないでね」フック通過の記録（`legacy_ch01_090_phone`）。
- これらのフラグは Phase2 では**記録のみ（消費しない）**。消費・回収は Phase3。
- 検証: `python3 tools/check_scenes.py docs/rewrite-dev/index.html` → PASS（参照切れ0件・id重複なし）。

---

## 付録: 参考にした実装箇所（`docs/rewrite-dev/index.html`）

- `runScene()` のシーンレベル `setFlag` 適用: `if (s.setFlag) setCh01Flag(s.setFlag);`
- walk分岐: `WK.doAction()` 内 `if (WK.nearTarget.sceneIfFlag && hasCh01Flag(...)) next = ...sceneIfFlag.scene;`
- memory選択の `setFlag`/`intent`/`next`: `showMemory()` の `btn.onclick`
- 状態定義: `var CH01_STATE = { observation, trust, choseNotToLook, fragments, flags:{} };`
- `setCh01Flag(name)` / `hasCh01Flag(name)`
