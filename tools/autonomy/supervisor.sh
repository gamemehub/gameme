#!/usr/bin/env bash
# RewriteMemory Supervisor（監視エージェント・Phase1）
# 役割: Runner のハートビート監視 / 24h以上停止で通知 / 日次コスト監視 / CI失敗率監視 /
#       PAUSE 誘発条件の検知。launchd で定期起動する（例: 600s ごと）。
# 「Agentを監視するAgent」の最小実装。異常はまず通知＋PAUSE、復旧は人間 or launchd。
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
[ -f "$HERE/config.sh" ] && source "$HERE/config.sh" || { echo "config.sh が無い"; exit 1; }
mkdir -p "$REWRITE_LOG" "$REWRITE_STATE"
ts(){ date +%Y-%m-%dT%H:%M:%S; }
log(){ echo "[$(ts)] $*" | tee -a "$REWRITE_LOG/supervisor.log"; }
notify(){ [ -n "$REWRITE_NOTIFY_WEBHOOK" ] && curl -fsS -X POST -H 'Content-Type: application/json' -d "{\"text\":\"[RewriteMemory/Supervisor] $1\"}" "$REWRITE_NOTIFY_WEBHOOK" >/dev/null 2>&1 || true; }
pause_all(){ touch "$REWRITE_PAUSE_FLAG"; log "PAUSE を設定（全停止）"; }

now=$(date +%s)

# 1) ハートビート: Runner が長時間動いていないか（launchdが生きていれば定期更新される）
HB="$REWRITE_STATE/runner.heartbeat"
if [ -f "$HB" ]; then
  last=$(date -j -f "%Y-%m-%dT%H:%M:%S" "$(cat "$HB")" +%s 2>/dev/null || echo 0)
  age=$(( now - last ))
  if [ "$age" -gt 86400 ]; then
    log "Runner が 24h 以上ハートビートなし (age=${age}s)"; notify "Runnerが24h停止。要確認。"
  fi
else
  log "ハートビート未生成（Runner 未起動 or 初回）"
fi

# 2) 日次コスト監視
COST_FILE="$REWRITE_STATE/cost-$(date +%Y%m%d).txt"
SPENT=$(cat "$COST_FILE" 2>/dev/null || echo 0)
if awk "BEGIN{exit !($SPENT >= $REWRITE_DAILY_USD_LIMIT)}"; then
  log "日次コスト上限到達 (\$$SPENT)"; notify "日次コスト上限 (\$$SPENT) → PAUSE"; pause_all
fi

# 3) CI 失敗率監視（直近10 PR の godot-check 失敗が多すぎたら通知）
if command -v gh >/dev/null 2>&1; then
  FAILS=$(gh run list --repo "$REWRITE_GH_REPO" --workflow godot-check.yml --limit 10 --json conclusion --jq '[.[]|select(.conclusion=="failure")]|length' 2>/dev/null || echo 0)
  if [ "${FAILS:-0}" -ge 5 ]; then
    log "godot-check 直近10件中 $FAILS 件失敗"; notify "godot-check 失敗率が高い ($FAILS/10)。実装品質か基盤を確認。"
  fi
fi

# 4) 無限ループ/暴走の簡易検知: 1時間で作られた自動ブランチ数が多すぎないか
if command -v gh >/dev/null 2>&1; then
  RECENT=$(gh pr list --repo "$REWRITE_GH_REPO" --state open --json headRefName,createdAt --jq "[.[]|select(.headRefName|startswith(\"claude/issue-\"))]|length" 2>/dev/null || echo 0)
  if [ "${RECENT:-0}" -ge 15 ]; then
    log "自動PRが多すぎる ($RECENT)。暴走の可能性 → PAUSE"; notify "自動PRが $RECENT 件。暴走検知 → PAUSE"; pause_all
  fi
fi

log "supervisor チェック完了 (spent=\$$SPENT)"
