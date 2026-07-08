#!/usr/bin/env bash
# RewriteMemory 自律エージェント Runner（Phase1）
# Ready Issue を1件取得 → claude/ ブランチ作成 → エージェント起動(実装) → commit → push。
# push 後は既存の auto-pr が PR を作り、godot-check(CI) が検証する。
# 安全弁: PAUSE フラグ / 日次コスト上限 / 変更なしなら中断 / game・docs 以外は触らせない(エージェント側制約)。
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
[ -f "$HERE/config.sh" ] && source "$HERE/config.sh" || { echo "config.sh が無い。config.example.sh からコピーして設定して"; exit 1; }
mkdir -p "$REWRITE_LOG" "$REWRITE_STATE"
ts(){ date +%Y-%m-%dT%H:%M:%S; }
log(){ echo "[$(ts)] $*" | tee -a "$REWRITE_LOG/runner.log"; }
notify(){ [ -n "$REWRITE_NOTIFY_WEBHOOK" ] && curl -fsS -X POST -H 'Content-Type: application/json' -d "{\"text\":\"[RewriteMemory] $1\"}" "$REWRITE_NOTIFY_WEBHOOK" >/dev/null 2>&1 || true; }

# --- 停止条件 ---
[ -f "$REWRITE_PAUSE_FLAG" ] && { log "PAUSE フラグあり。停止。"; exit 0; }
echo "$(ts)" > "$REWRITE_STATE/runner.heartbeat"   # Supervisor 用ハートビート

# 日次コストガード（state/cost-YYYYMMDD.txt に加算していく想定。実測値は agent 側で書き込む）
COST_FILE="$REWRITE_STATE/cost-$(date +%Y%m%d).txt"; [ -f "$COST_FILE" ] || echo "0" > "$COST_FILE"
SPENT=$(cat "$COST_FILE" 2>/dev/null || echo 0)
if awk "BEGIN{exit !($SPENT >= $REWRITE_DAILY_USD_LIMIT)}"; then
  log "日次コスト上限 (\$$SPENT >= \$$REWRITE_DAILY_USD_LIMIT)。今日は停止。"; notify "日次コスト上限で停止 (\$$SPENT)"; exit 0
fi

cd "$REWRITE_REPO" || { log "repo not found: $REWRITE_REPO"; exit 1; }
git fetch origin -q

# --- Ready Issue を1件取得 ---
ISSUE=$(gh issue list --repo "$REWRITE_GH_REPO" --label "$REWRITE_READY_LABEL" --state open --limit 1 --json number,title --jq '.[0] // empty')
[ -z "$ISSUE" ] && { log "Ready Issue なし。アイドル。"; exit 0; }
NUM=$(echo "$ISSUE" | jq -r .number); TITLE=$(echo "$ISSUE" | jq -r .title)
log "取得: Issue #$NUM: $TITLE"

# --- ブランチ作成 & 二重取得防止 ---
BR="claude/issue-$NUM-$(date +%Y%m%d-%H%M)"
git checkout -B "$BR" origin/main -q
gh issue edit "$NUM" --repo "$REWRITE_GH_REPO" --remove-label "$REWRITE_READY_LABEL" --add-label "$REWRITE_INPROGRESS_LABEL" >/dev/null 2>&1 || true

# --- プロンプト生成 ---
PROMPT="$(gh issue view "$NUM" --repo "$REWRITE_GH_REPO" --json title,body --jq '.title + "\n\n" + .body')
【制約】CLAUDE.md と docs/project の方針に厳密に従う。編集は Godot プロジェクト(game/ または prototype/godot-1room/)と docs のみ。本番/.github/セーブ核心は触らない。変更後は必ず動くようにし、参照切れ0。1 Issue=1 まとまった実装。完了したら変更をワークツリーに残す(commitは runner が行う)。"

# --- エージェント起動（本体）---
if [ -z "$REWRITE_AGENT_CMD" ]; then
  log "REWRITE_AGENT_CMD 未設定 → ドライラン(実装せず)。config.sh にエージェントコマンドを設定して。"
  exit 0
fi
log "エージェント起動 #$NUM …"
( eval "$REWRITE_AGENT_CMD \"\$PROMPT\"" ) >> "$REWRITE_LOG/issue-$NUM.log" 2>&1
RC=$?; log "エージェント終了 rc=$RC (log: $REWRITE_LOG/issue-$NUM.log)"

# --- 変更が無ければ中断 ---
if git diff --quiet && git diff --cached --quiet; then
  log "変更なし。ブランチはそのまま、Issueを ready へ戻す。"; notify "#$NUM 実装で変更が出ませんでした（要確認）"
  gh issue edit "$NUM" --repo "$REWRITE_GH_REPO" --remove-label "$REWRITE_INPROGRESS_LABEL" --add-label "$REWRITE_READY_LABEL" >/dev/null 2>&1 || true
  exit 0
fi

# --- commit & push（auto-pr が PR を作成、godot-check が検証）---
git add -A
git commit -q -m "auto(#$NUM): $TITLE" -m "自律エージェントによる実装。詳細は Issue #$NUM。人間レビュー前提。" || true
for i in 1 2 3 4; do git push -u origin "$BR" && break || { log "push 失敗 リトライ $i"; sleep $((2**i)); }; done
log "push 完了: $BR → auto-pr が PR 作成 / godot-check 検証 / 人間レビュー待ち。"
notify "#$NUM 実装 → PR作成。CI/レビュー待ち。"
