# RewriteMemory 開発指針：クオリティ課題の突破ロードマップ

> 位置づけ：**開発指針ドキュメント**。AI駆動開発の実事例と技術調査（2025-2026）に基づき、
> 現在の5つの課題（クオリティ低・画像未実装・マップ品質・テンポ悪・ゲーム未成立）の
> 根本原因と解決順序を定める。MODE_DEFINITION v1.2 / ASSET_SPEC / DESIGN_TOKEN と併読。

- バージョン: v1.0
- 作成日: 2026-07-21

---

## 0. 結論（先に読む）

**5つの課題は並列ではない。「⑤ゲームとして成立していない」が根本であり、他は従属する。**

```
⑤ コアループ未成立（根本）
 ├─ ④ テンポ・面白さ → ループがないので「操作→結果→報酬」のリズムが作れない
 ├─ ② 画像未実装   → ASSET_SPECはあるが制作パイプラインが運用されていない
 ├─ ③ マップ品質   → 「タイルを敷く」発想自体がMOTHER風と不整合
 └─ ① 全体クオリティ → 上記の合成結果。個別に磨いても解決しない
```

成功事例に共通するパターンは一つ：**「小さく完結したループを先に作り、磨き込みで面白さを検証してから拡張する」**。
逆に失敗事例に共通するのは「AIに一気に大量生成させ、遊んで面白いかの検証を後回しにする」こと。

**最優先タスク：CH01の「探索→違和感発見→会話→記憶書き換え→世界が変化→探索」の1周（5分）を、
仮素材のままでいいので通しで遊べる状態にする。** 磨くのはその後。

---

## 1. 現状の実装評価（2026-07 時点）

| 領域 | 現状 | 評価 |
|---|---|---|
| 設計ドキュメント | MODE_DEFINITION v1.2 / ASSET_SPEC / Character Bible / DESIGN_TOKEN 完備 | ◎ 強み。多くの成功事例が「仕様書でAIを制御」を挙げており、既に実践できている |
| エンジン | Vanilla DOM 単一HTML（1159行） | △ VN・会話UIには適するが、探索・バトルの拡張で限界が来る（§6） |
| 探索（M02） | CSSグラデ背景＋絶対配置スプライト、1画面横スクロール | △ タイルマップ以前の状態。ただしこれは弱みではなく選択肢（§4） |
| 画像 | スプライト2枚のみ。顔アイコン0枚（ASSET_SPEC #2b 未着手） | ✗ パイプライン未運用 |
| バトル（M05/M06） | モード定義のみ、実装なし | ✗ コアループの穴 |
| 音 | WebAudio生成トーン | ○ 方向性は正しい（§5でZzFX化を推奨） |

---

## 2. 課題⑤「ゲームとして成立していない」→ コアループ最優先

### 指針
1. **1周5分の垂直スライス（Vertical Slice）を最優先で完成させる**
   - ループ：`M02探索 → 違和感発見 → M03/M04会話 → 記憶書き換え → 世界の変化を目視 → M02探索`
   - 「記憶を書き換えると探索マップ上の何かが変わる」を最低1箇所実装する。
     これがこのゲーム固有の「操作→結果→報酬」であり、VNの読み進めだけでは代替できない。
2. **仮素材で作る**。CSS矩形キャラのままでよい。見た目より先にループの手触りを検証する
   （EarthBound型RPGの試作は「グレーボックスで戦闘が面白いか」から始めるのが定石）。
3. **M05バトルは垂直スライス完成後**。RewriteMemoryの核は「記憶書き換え」であり、
   バトルは第2のループ。順序を間違えない。
4. **デバッグワープを初日に作る**（シーンID指定でジャンプ）。ソロ開発の検証速度が数倍変わる。
   自分の序盤を何十回も通しでやると感覚が麻痺する（事例§7参照）。

### 完成判定（Definition of Done）
- 初見の人がスマホで5分遊び、「記憶を書き換えたら世界が変わった」ことを説明できる
- 途中で操作に迷って止まらない（詰まったら導線の敗北）

---

## 3. 課題②「画像を実装できない」→ アセットパイプラインの確立

「画像を実装できない」の実体は、(a) スタイルが揃わない、(b) 透過・サイズ処理が毎回手作業、
(c) ゲームに読み込む規約がない、の3点。ツールと規約で解決する。

### 推奨パイプライン
```
1. スタイル固定   PixelLab (pixellab.ai) または Retro Diffusion (retrodiffusion.ai)
                  ※Midjourney/DALL-E は「コンセプト画」用。ゲーム用スプライト
                    （歩行4方向・フレーム位置合わせ・パレット統一）には不向き
2. 一貫性の担保   Scenario (scenario.com) でスタイルLoRAを学習（画像10-20枚で30-60分）
                  → 全キャラ・タイル・小物を同一モデルから生成
3. 仕上げ         Aseprite でパレット統一（Indexed化）・フレーム整列
                  → AI出力をそのまま使わない。2割の手仕上げが「意図された絵」を作る
4. 透過・切り出し  Sprite Buff (spritebuff.com) / I Love Sprites (ilovesprites.com)
                  ※写真用背景除去ツールはピクセル輪郭が滲むため使わない（色キー方式を使う）
5. 命名・配置     ASSET_SPEC の命名規則に従い assets/characters/<name>/<view>/ へ
```

### 直近の実行順
1. **ASSET_SPEC #2b を最優先で消化**：ミオ顔アイコン最小3枚（normal / anxious / empty）。
   仕様上3枚で全会話が成立する設計になっており、費用対効果が最大
2. トウ・ミオの歩行スプライト（まず左右2方向で十分。現状の探索は横移動のみ）
3. 探索シーン背景（§4の方針に従い「一枚絵」として生成）

### 規約
- 表示サイズの2倍で書き出し（Retina）、`image-rendering: pixelated` はドット絵のみに適用
- 1画像1PNG・RGBA・命名はASSET_SPEC準拠。例外を作らない
- 生成プロンプト・使用モデル・シード値を `assets/PROMPTS.md` に記録（再生成・追加生成のため）

---

## 4. 課題③「マップがマス目貼りで低品質」→ タイルを捨てるか、賢く使う

### 重要な事実：MOTHER 2 は「マス目に見えないタイル」で作られている
EarthBound の街は斜投影（oblique projection：壁面＋斜めの上面をタイル自体に描き込む）、
斜めに走る道路、複数タイルにまたがる手描きの大型建物で構成され、
ほぼ何も「繰り返しスタンプ」に見えない。つまり**タイルを敷き詰める発想のままAIに
タイルセットを生成させても、MOTHER風には決してならない**。

### 本プロジェクトの推奨：Plan A「シーン一枚絵」方式
現在のゲームは横スクロール探索＋VNであり、シーン数も限られる（CH01で数シーン）。
この規模なら**タイルマップを作らず、シーンごとに1枚の背景画（横長・パララックス2-3層）を
AI生成＋手直しで用意する**のが、工数最小・品質最大。
Kentucky Route Zero が舞台美術のような「一枚のステージセット」で高い雰囲気を出した方式に近く、
「世界を見る」というUI哲学（MODE_DEFINITION）とも整合する。

- 構成：奥景（空・街並み）／中景（建物・木）／近景（地面・小物）の2-3層PNG
- スクロール時に `transform: translateX(scroll × 深度係数)` で視差を付ける
- 違和感オブジェクト（eerie演出対象）は背景に焼き込まず、現行どおり個別スプライトで配置

### 将来タイルが必要になった場合：Plan B「賢いタイル」
見下ろし型マップを作る段階が来たら、以下をセットで導入する（単品では効果が出ない）：
1. **LDtk (ldtk.io)**：無料マップエディタ。オートレイヤールールで地形の縁を自動処理し、
   装飾バリアントを自動散布できる。JSON出力はVanilla JSでもPhaserでも読める
2. **デュアルグリッド・オートタイル**：表示グリッドを論理グリッドから半タイルずらすと、
   47枚必要な縁タイルが最少5〜16枚で済む（Excalibur blogの手法。工数削減が劇的）
3. **繰り返し感の破壊（効果の大きい順）**：
   - 退屈タイル（草・床）に3-4種のランダムバリアント
   - グリッド外に置く装飾レイヤー（花・ヒビ・看板・影）
   - グリッドのリズムを壊す大型一点物（家・木＝AI生成の斜投影ビル画像を「プロップ」として配置）
   - 画面全体のビネット＋色調オーバーレイ（div1枚で最安の雰囲気向上）
   - パララックス背景

---

## 5. 課題④「面白さ・テンポが悪い」→ リズムはデータで制御する

### 5-1. テキストのリズム（最優先・工数小・効果大）
MOTHER/Undertale の面白さの大半は**間（ま）のコントロール**にある。コード変更なしで
ライターが間を制御できるよう、**セリフ内マークアップを導入する**：

```
例：「……もう、[pause:500]思い出せないの。[speed:0.5]ごめんね。」
```

- 基準速度：20-40文字/秒。読点+100ms、句点+300ms、三点リーダー+500ms
- 1-2文字ごとにキャラ固有ブリップ音（既存のtypewrite+blipを拡張）
- **タップで即全文表示→再タップで次へ** を全ビートで保証（待たせるUIは全廃）
- オチのセリフは独立ビートに分ける（1ボックス1情報）

### 5-2. カットシーンの上限
- 重要シーン（M04）でも**5分以内**、通常は大幅に下回る。SNES期FFのオープニングですら
  場面転換を細かく挟んで約5分
- 長いVNの連続を避け、**テキストビートの間に「歩く・選ぶ」操作ビートを挟む**
  （M02→M04→M02のループ設計そのものが正解。1回のM04を短くする）
- スプライトは会話中も動かす（まばたき・歩き回り・エモート）

### 5-3. ジュース（ゲームフィール）チェックリスト
参照：Juice it or Lose it (Jonasson & Purho) / The Art of Screenshake (Nijman) / Game Feel (Swink)
- [ ] 入力から反応まで**100ms以内**（Swinkの法則。`pointerdown`で拾う。`click`禁止＝遅延源）
- [ ] 全ての状態変化にトゥイーン（出現・消滅・選択。CSS transition済みの箇所は維持）
- [ ] 記憶書き換え確定時：画面フラッシュ＋微シェイク（trauma²減衰、200-300ms）
- [ ] ヒットストップ（バトル実装時：ヒット瞬間に2-4フレーム停止）
- [ ] SE：**ZzFX**（1KB・コード1行・ jsfxr系のWebツールで音作り）へ移行。
    現行WebAudioトーンより語彙が圧倒的に増える
- [ ] BGM：ZzFXM（コードのみチップチューン）または OpenGameArt CC0 チップチューン集
- [ ] `touch-action: none`、タッチ領域44px以上、単一rAFループ＋デルタタイム

### 5-4. エンカウント設計の原則（M05実装時）
EarthBound 自身の発明がそのままチェックリストになる：
- シンボルエンカウント（敵が見える。ランダム戦闘なし）
- 格下の敵は戦闘スキップで自動勝利（テンポ維持）
- ドラム式HP（被弾の緊張を演出に変換）
- Undertale拡張：**全ての戦闘に「ジョーク1つ・選択1つ・世界の情報1つ」のどれかを入れる。
  入らない戦闘はカットする**。RewriteMemoryならM06（説得・記憶提示）がこれに当たる——
  つまりM05単体ではなくM05⇄M06セットで初めて実装する価値がある

---

## 6. エンジン戦略：段階的に Phaser へ（DOM併用）

技術調査の結論：AI駆動開発では**AIの学習データに最も多く含まれるフレームワークを選ぶこと自体が
品質戦略**になる。Phaser はドキュメント・作例量で他を圧倒し、Claude/GPTが正確なコードを生成する
（Kaplay/Excalibur はAPIのハルシネーションが頻発する報告あり）。

### 推奨：ハイブリッド移行（一括書き換え禁止）
```
現在    ：全部DOM（単一HTML）
Step 1  ：現状維持のままコアループ完成（§2）。エンジン移行はループ検証の後
Step 2  ：探索ワールド（M02）だけ Phaser canvas 化
          - カメラ（シェイク・フェード内蔵）、タイル/LDtk読み込み、トゥイーンが無料で手に入る
Step 3  ：VN・会話UI（M03/M04/phone）は DOM のまま canvas に重ねる
          - DOMはテキストUIに本当に強い。既存コードと日本語組版資産を捨てない
          - 「DOM UI over Phaser canvas」は標準パターンで資料が豊富
```

### やってはいけないこと
- 面白さ未検証のままのエンジン移行（動くものを壊して数週間失う典型パターン）
- 単一HTMLへのこだわりの継続拡大：シナリオデータ（SCENES）は早期にJSON分離する。
  AIにシナリオ追加を指示する際も、コード全体ではなくJSONだけ触らせる方が事故が減る

---

## 7. AI駆動開発の運用指針（事例からの教訓）

### 7-1. 失敗事例が示す「品質の壁」の正体

| 事例 | 何が起きたか | 修正法 |
|---|---|---|
| [紙の上では良いのに画面では退屈](https://dev.to/seagamesai/my-first-ai-generated-game-looked-great-on-paper-and-boring-on-screen-5eo4) | AI生成ゲームが「初対面の機能の寄せ集め」になった | **人間がコアループを手で調整して「既に楽しい型」を作り、AIはその型の中で量産だけ担当**。AIにコアループを発案させない |
| [vibe codingで作ったが楽しくない](https://www.laptopmag.com/ai/i-tried-vibe-coding-with-claude-sonnet-and-wasnt-impressed) | 「もっと良くして」の指示では出力が頭打ち | フィードバックは具体的なプレイ観察にする（「回避が100ms遅い」「レベル2に意思決定がない」）。そのために**定期的に自分で遊ぶ** |
| [Why Vibe Coding Fails（Columbia DAPLab）](https://daplab.cs.columbia.edu/general/2026/01/07/why-vibe-coding-fails-and-how-to-fix-it.html) | 一発生成は7割まで到達し、機能追加で劣化する | **「vibesで探索し、仕様で構築する」**——プロトタイプ後は仕様駆動に切り替える |
| [見た目は動くアプリの罠](https://dev.to/shayy/why-your-vibe-coded-app-will-fail-and-how-to-fix-it-369p) | 「動いて見える」と「実際に動く」の差でプロジェクトが死ぬ | 完了条件を「コンパイルが通り表示される」ではなく**「遊んで期待通りに振る舞う」**にする |
| [vibe codingの不都合な真実（Red Hat）](https://developers.redhat.com/articles/2026/02/17/uncomfortable-truth-about-vibe-coding) | 初稿は綺麗、反復で壊れる | 機能追加バーストの間に**リファクタリング回**を定期挿入する |

→ 本プロジェクトへの適用：**設計ドキュメント群が既にあるのは大きな強み**。足りないのは
(a) 人間が手で磨いた「楽しい1シーン」の原型、(b) 遊んで判定する完了条件、の2つ。

### 7-2. 成功事例が示す共通パターン

- **[Undertale](https://gamedesigning.org/gaming/toby-fox-and-the-making-of-undertale/)**（ジャンルの原点）：面白さは「システム」ではなく**1体1体手作りのエンカウント個性**から生まれる。汎用のステータス交換戦闘をAIコードで磨いても解決しない。新機能より先に「個性ある敵/違和感イベントを10個書く」
- **[Dreamed Away](https://nicolaspetton.itch.io/dreamed-away)**（2025年ソロ発売のMOTHER系）：勝因は具体的で個人的な舞台設定（90年代ブルターニュ）。**「いつ・どこ」の具体性が全アセット・全セリフの採用フィルタになる**。RewriteMemoryなら「学園・17:17・白層化」の世界観規約を全生成物の判定基準にする
- **[Catvivors](https://pchojecki.medium.com/ai-helped-me-solo-dev-a-game-on-steam-f84a2425be10)**（Claude CodeでSteam EA到達）：AI全面活用でも**24レベル全て手作業配置**。タイルや構造はAI生成、セットピースとペース配分は人間が置く
- **[fly.pieter.com](https://levels.io/fly-pieter-com-vibecoded-flight-simulator)**：荒くても即公開→毎日プレイヤー観察で反復。**「大きく作って判定」から「小さく変えて1人に遊ばせて観察」へ**
- **[Vibe Coding Game Jam 2025](https://jam.pieter.com/)**（1,170作品）：上位入賞は全て**「1つの明快な動詞×ジュース」**（タクシー運転・ミニタスク・管制）。RPGスケールではない。ゲームとして成立させたければ、まず1つの動詞（＝記憶書き換え）をジャム優勝級に締める
- **[AIにゲームをプレイさせる](https://blog.jeffschomay.com/letting-ai-play-my-game)**（2026年4月）：ゲーム状態と入力をCLI/HTTPで公開し、**Claude自身に毎機能プレイテストさせる**。人間のテストは「感触とペース」に集中できる。「AIは動いているゲームが見えない」盲点への直接の解

### 7-3. 日本語圏の実践事例

- [Claude Codeだけでモンスター78体のブラウザRPGをitch.io公開（Zenn）](https://zenn.dev/itamoko/articles/55ccb137aa922e)：ボトルネックは「コードが書けるか」から「一貫した構造でコンテンツを量産できるか」へ移動。**1モンスター/1マップをデータスキーマとして先に定義し、AIにはスキーマへの流し込みだけさせる**
- [Claude Code + Opus 4.6で4日でTRPG×LLMゲーム（Qiita）](https://qiita.com/gyokuro338/items/cf774b1d65270796e1c4)：**着手前の計画3時間が最大のレバレッジ**だったと報告
- [バイブコーディング×ドキュメント駆動の実践（note）](https://note.com/nice_llama936/n/nd6d0ac9bb548)：GAME_DESIGN.mdを正本にし、**仕様と実装の乖離を Gap.md で常時追跡**。品質ドリフトへの安価で強力な対策
- [Claude CodeでRPG：戦闘シミュレーション200-300回で難易度調整（Zenn）](https://zenn.dev/kozoka_ai/articles/a95e5c2316bc59)：**人間プレイテスト前にAIにモンテカルロで戦闘数百回を回させ、勝率からバランス調整**
- [CLAUDE.mdをインセプションデッキで作る（Qiita）](https://qiita.com/kyuko/items/316d30901f20a0b8be4c)：**「このゲームは何でないか」を明記**（例：「オープンワールドではない。マップは手置きの数シーン」）してAIのスコープ暴走を防ぐ。CLAUDE.mdは300行以内・コードと一緒に更新
- [AIの「ドット絵風」を本物のドット絵にする（note）](https://note.com/bamboo8_storage/n/n8a3e2f3d53b7)：AI出力の「ドット絵風」は偽物（1ドットに見える部分が実際は約100ピクセル）。**Pixel Snapper等で真のピクセルグリッドに量子化→パレット削減→取り込み**を必須工程にする
- [ドット絵特化AI「PixelLab」レビュー（note）](https://note.com/gameshin_saga/n/nb32c2d374d2b)：汎用画像モデルをやめてピクセルネイティブのツールに揃えると、解像度とパレットが構造的に一致する
- [素材のAI生成を中心にしたドット風ゲーム制作（Qiita）](https://qiita.com/H20/items/81d58ccaef2febae0e3d)：一貫性は「最良の1枚を選ぶ」ことからではなく、**同一モデル・同一会話・同一スタイル規約の継続**から生まれる

### 7-4. 本プロジェクトの運用ルール（上記の適用）

1. **CLAUDE.md を作る**（300行以内）：ゲームの本質・「何でないか」・技術規約（解像度・パレット・
   入力遅延100ms・タイルサイズ）・完了条件（「遊んで判定」）を明記し、全AI作業の参照先にする
2. **Gap.md を作る**：MODE_DEFINITION / 各SCREEN仕様と現実装の乖離を一覧化し、PR毎に更新
3. **完了条件は「遊んで期待通り」**：スマホ実機で該当シーンを通しプレイしてからPRを出す
4. **ヘッドレステスト**：SCENES進行・状態遷移をNode/CLIで駆動できるテストハーネスを用意し、
   Claude自身に全シーン通し検証をさせる（M05実装後は戦闘勝率のモンテカルロも）
5. **量産はスキーマ経由**：シーン・NPC・違和感イベントはJSONスキーマを先に固定し、
   AIにはデータの流し込みだけを指示する（コード全体を触らせない）
6. **アセットは同一ツール・同一スタイル規約で継続生成**し、Pixel Snapper量子化を必須工程にする

---

## 8. 実行順サマリー（この順で着手する）

| # | タスク | 対応課題 | 目安 |
|---|---|---|---|
| 1 | デバッグワープ実装（シーンIDジャンプ） | ⑤④ | 小 |
| 2 | 垂直スライス：記憶書き換え→世界変化のループ1周（仮素材） | ⑤ | 中 |
| 3 | テキストマークアップ（[pause]/[speed]）＋タップ即送り保証 | ④ | 小 |
| 4 | ZzFX導入（SE差し替え） | ④① | 小 |
| 5 | ミオ顔アイコン3枚（ASSET_SPEC #2b、PixelLab/Retro Diffusion） | ② | 小 |
| 6 | シーン一枚絵背景×パララックス2層を1シーンに適用 | ③① | 中 |
| 7 | 初見プレイテスト（スマホ実機・口出し禁止で観察）→課題票に反映 | ④⑤ | 小 |
| 8 | 歩行スプライト左右2方向＋会話中の待機アニメ | ②① | 中 |
| 9 | M02のPhaser化検証（別ブランチ・1シーンのみ） | ①③ | 中 |
| 10 | M05⇄M06バトル（説得・記憶提示とセットで） | ⑤ | 大 |

1〜7 が「ゲームとして成立させる」フェーズ、8〜10 が「クオリティを上げる」フェーズ。
**フェーズ順を入れ替えない**こと。

---

## 参考リンク（技術）

- PixelLab: https://www.pixellab.ai/ ／ Retro Diffusion: https://retrodiffusion.ai/
  ／ 比較: https://gamedevaihub.com/retro-diffusion-vs-pixellab/
- Scenario スタイルLoRA: https://help.scenario.com/en/articles/train-a-style-model/
- Aseprite: https://www.aseprite.org/ ／ 透過: https://spritebuff.com/
- オートタイル解説（Red Blob Games）: https://www.redblobgames.com/articles/autotile/claude/
- タイルセット分類（BorisTheBrave）: https://www.boristhebrave.com/2021/11/14/classification-of-tilesets/
- デュアルグリッド法: https://excaliburjs.com/blog/Dual%20Tilemap%20Autotiling%20Technique/
- LDtk: https://ldtk.io/ ／ Tiled: https://www.mapeditor.org/
- EarthBoundの斜投影: https://forum.starmen.net/forum/Games/Mother3/Oblique-Projection
- KRZ舞台美術（GDC）: https://www.gdcvault.com/play/1020596/Scenography-of-Kentucky-Route
- Juice it or Lose it: https://www.youtube.com/watch?v=Fy0aCDmgnxg
- The Art of Screenshake: https://www.youtube.com/watch?v=AJdEqssNZ-U
- カメラ数学（trauma²）: https://www.youtube.com/watch?v=tu-Qe66AvtY
- ZzFX: https://github.com/KilledByAPixel/ZzFX ／ jsfxr: https://sfxr.me/
  ／ ZzFXM: https://github.com/keithclark/ZzFXM
- CC0チップチューン: https://opengameart.org/content/audio-cc0-8bit-chiptune
- EarthBound→Undertale設計系譜: https://mechanicsofmagic.com/2023/06/13/how-undertale-pays-homage-to-earthbound-and-the-mother-series/
- Phaser: https://phaser.io/ ／ フレームワーク比較: https://phaser.io/news/2026/04/phaser-vs-kaplay-vs-excalibur-2d-web-game-framework
  ／ 実測レビュー: https://jslegenddev.substack.com/p/i-tried-3-web-game-frameworks-so
