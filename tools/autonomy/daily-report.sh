#!/usr/bin/env bash
# RewriteMemory AI Studio Daily Report（運用フェーズ・メトリクス収集）
# GPTレビュー指定の項目を毎日集計してログに残す。gh由来は自動集計、エージェント由来は
# state カウンタから読む（未配線は n/a と表示。Runner/Cross/Human 側で加算するのが今後の配線点）。
# launchd で1日1回（例: 毎日09:00）実行。
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
[ -f "$HERE/config.sh" ] && source "$HERE/config.sh" || { echo "config.sh が無い"; exit 1; }
REPO="${REWRITE_GH_REPO:-gamemehub/gameme}"
STATE="${REWRITE_STATE:-$HOME/rewrite-autonomy/state}"
LOG="${REWRITE_LOG:-$HOME/rewrite-autonomy/logs}"
mkdir -p "$STATE" "$LOG"
TODAY="$(date +%Y-%m-%d)"
REPORT="$LOG/daily-report-$TODAY.md"

# state カウンタ読取（無ければ n/a）
ctr(){ f="$STATE/$1-$TODAY.txt"; [ -f "$f" ] && cat "$f" || echo "n/a"; }

# gh 由来（当日）— 失敗時 n/a
ghn(){ v="$("$@" 2>/dev/null)"; [ -n "$v" ] && echo "$v" || echo "n/a"; }
PR_CREATED=$(ghn bash -c "gh pr list --repo '$REPO' --state all --json createdAt --jq '[.[]|select(.createdAt|startswith(\"$TODAY\"))]|length'")
PR_MERGED=$(ghn bash -c "gh pr list --repo '$REPO' --state merged --json mergedAt --jq '[.[]|select(.mergedAt|startswith(\"$TODAY\"))]|length'")
ISSUE_CLOSED=$(ghn bash -c "gh issue list --repo '$REPO' --state closed --json closedAt --jq '[.[]|select(.closedAt|startswith(\"$TODAY\"))]|length'")
CI_TOTAL=$(ghn bash -c "gh run list --repo '$REPO' --workflow godot-check.yml --limit 30 --json conclusion,createdAt --jq '[.[]|select(.createdAt|startswith(\"$TODAY\"))]|length'")
CI_OK=$(ghn bash -c "gh run list --repo '$REPO' --workflow godot-check.yml --limit 30 --json conclusion,createdAt --jq '[.[]|select(.createdAt|startswith(\"$TODAY\") and .conclusion==\"success\")]|length'")

COST=$(cat "$STATE/cost-$(date +%Y%m%d).txt" 2>/dev/null || echo "n/a")

{
echo "# AI Studio Daily Report — $TODAY"
echo
echo "## スループット"
echo "- Issue完了数: $ISSUE_CLOSED"
echo "- PR作成数: $PR_CREATED"
echo "- Merge数: $PR_MERGED"
echo "- レビュー待ち件数: $(ghn bash -c "gh pr list --repo '$REPO' --state open --json isDraft --jq 'length'")"
echo
echo "## 品質"
echo "- CI(godot-check) 当日: 成功 $CI_OK / 実行 $CI_TOTAL"
echo "- Self Review 検出件数: $(ctr selfreview)   （要Runner側加算）"
echo "- Cross AI Review 指摘件数: $(ctr crossreview)   （要レビュアー側加算）"
echo "- 人間レビュー指摘件数: $(ctr humanreview)   （要記録）"
echo "- Revert率(バグ率): $(ctr revert)   （要記録）"
echo
echo "## 稼働・コスト"
echo "- AI稼働時間: $(ctr uptime)   （要Runner側記録）"
echo "- 停止回数: $(ctr pausecount) / 自動復旧回数: $(ctr recover)   （要記録）"
echo "- 停止理由: $(cat "$STATE/pause-reasons-$TODAY.txt" 2>/dev/null || echo 'n/a')"
echo "- コスト(当日 USD目安): $COST"
echo
echo "## 時間"
echo "- 平均Issue処理時間: $(ctr issue_avg)   （要記録）"
echo "- 平均PR作成時間: $(ctr pr_avg)   （要記録）"
echo "- 平均レビュー時間(PR→承認): $(ctr review_avg)   （要記録）"
echo
echo "## 進捗"
echo "- CH01進捗率 / 計画との差異: 手動記入 or 別集計   （要定義）"
echo
echo "> n/a はエージェント側カウンタ未配線。運用しながら Runner/Supervisor/レビュー処理で"
echo "> state/<name>-$TODAY.txt に加算していく。課題は docs/project/AI_OPS_BACKLOG.md へ。"
} > "$REPORT"

echo "[daily-report] $REPORT を生成"
# 任意: 通知
[ -n "${REWRITE_NOTIFY_WEBHOOK:-}" ] && curl -fsS -X POST -H 'Content-Type: application/json' \
  -d "{\"text\":\"[RewriteMemory] Daily Report $TODAY: Issue完了 $ISSUE_CLOSED / PR $PR_CREATED / Merge $PR_MERGED / CI $CI_OK-$CI_TOTAL / cost \$$COST\"}" \
  "$REWRITE_NOTIFY_WEBHOOK" >/dev/null 2>&1 || true
