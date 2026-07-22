# CLAUDE.md — RewriteMemory 開発の必読ルール

> このファイルは Claude Code / AI が作業開始時に自動で読み込む。
> ここに書かれた参照ドキュメントは**作業前に必ず確認すること**。

## 🚨 最優先・必読（MUST READ FIRST）

本プロジェクト RewriteMemory は **SQUARE ENIX GAME CONTEST 2026（GC2026）応募作品**。
コード・アセット・文章の生成や変更を行う前に、**必ず以下を読み、遵守すること**：

1. **`docs/contest/GC2026_COMPLIANCE.md`** — 応募規約・AI利用ガイドラインの遵守チェックリスト（必読）
2. **`docs/contest/GC2026_APPLICATION_TERMS.md`** — 規約・AIガイドライン原文（一次資料）

### 特に違反すると「審査対象外／失格」になる事項（要約）
- **特定作品・作家のスタイルを模倣しない**。画像/音/文の生成プロンプトに
  `EarthBound` `MOTHER` 等の固有名詞・実在作家名・作品名を入れない。
  成果物が特定作品と識別されてはならない（設計上「MOTHER風」と説明するのは可、成果物の絵柄はNG）。
- **第三者の権利を侵害しない**。使用AI・素材・フォント・音楽は商用利用可・改変可のもののみ。
- **AI使用ログを残す**（ツール名・モデル・バージョン・工程・時期）。
  `assets/PROMPTS.md` と `docs/contest/AI_USAGE_LOG.md` を継続更新する。
- **オリジナル・未発売・未受賞**を維持。公開はパスワード保護のプロトタイプに限定。

## プロジェクトの本質
- 「**記憶を書き換えると世界が変わる**」探索アドベンチャー（VN＋横スクロール探索）。
- Vanilla HTML/CSS/JS 単一ファイル（依存ゼロ）。実体は `docs/rewrite-dev/index.html` ほか。

## このゲームは「何でないか」（スコープ防壁）
- タイルマップRPGではない（マップはシーン一枚絵＋パララックス方式）。
- オープンワールドではない。
- 汎用ステータス戦闘はない（M05はM06=説得/記憶提示とセットになるまで作らない）。
- 新規画面モードを勝手に作らない（M00〜M13の組み合わせのみ）。

## 技術・実装規約
- 入力は `pointerdown`（`click`禁止＝遅延源）、反応は100ms以内、タッチ領域44px以上。
- 色・サイズ・余白・時間は `DESIGN_TOKEN.md` 経由（マジックナンバー直書き禁止）。
- 画面モードは `docs/design/UIUX/RewriteMemory_MODE_DEFINITION.md`（v1.2）に従う。
- 1 Issue = 1 PR・最小変更。main/develop へ直接 push 禁止・自動マージ禁止・人間レビュー前提。
- 物語・世界観・キャラ設定・章構成・優先順位の判断はしない（仕様/人間承認に従う）。
- 完了条件は「ビルドが通る」ではなく「**実機で遊んで期待通りに振る舞う**」。

## 開発の進め方（詳細は各ドキュメント）
- 課題分析と解決順序：`docs/design/DEVELOPMENT_GUIDELINES.md`
- 製法・品質ライン：`docs/design/BENCHMARK_AND_PRODUCTION.md`
- 領域別の制作手順：`docs/design/PRODUCTION_FLOW.md`
- アセット仕様：`docs/design/ASSET_SPEC.md`

**フェーズ順（入れ替えない）**：Phase0 準備 → Phase1 ゲーム性（垂直スライス）→
Phase2 見た目（キャラ→UI/UX→マップ）→ Phase3 量産 → Phase4 調整。
