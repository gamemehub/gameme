#!/usr/bin/env bash
# RewriteMemory 自律基盤 設定サンプル。
# コピーして config.sh を作り、Mac mini の実値を入れる（config.sh は Git 管理しない）。
#   cp config.example.sh config.sh && chmod 600 config.sh

# --- リポジトリ ---
export REWRITE_REPO="$HOME/gameme"                 # clone 済みリポジトリのパス
export REWRITE_GH_REPO="gamemehub/gameme"

# --- タスク源 ---
export REWRITE_READY_LABEL="ai-ready"              # このラベルの Issue を自律実装対象にする
export REWRITE_INPROGRESS_LABEL="ai-in-progress"

# --- エージェント実行系（★要設定：Claude Code CLI か Codex）---
# プロンプトは第1引数で渡す。実装→commit まで行い、変更をワークツリーに残すコマンドにする。
# 例(Claude Code CLI 非対話): claude -p "$1" --allowedTools "Read,Grep,Glob,Edit,Write,Bash(git *)"
# 制約は CLAUDE.md と append-system-prompt で付与し、game/ と docs 以外を触らせない。
export REWRITE_AGENT_CMD=""                         # 空なら runner はドライラン（実装せず検知のみ）

# --- 認証（★安全に。config.sh は 600 / Keychain 推奨）---
export ANTHROPIC_API_KEY=""                         # or Keychain 参照
# gh CLI は事前に `gh auth login` 済みであること

# --- 予算・停止条件 ---
export REWRITE_DAILY_USD_LIMIT="20"                # 1日のコスト上限(USD 目安)。超過で停止
export REWRITE_MAX_TASKS_PER_RUN="1"               # 1回の起動で扱うタスク数
export REWRITE_PAUSE_FLAG="$HOME/rewrite-autonomy/PAUSE"  # このファイルがあれば全停止

# --- 通知（任意：Slack Webhook 等）---
export REWRITE_NOTIFY_WEBHOOK=""                    # 空なら通知しない（ログのみ）

# --- ログ ---
export REWRITE_LOG="$HOME/rewrite-autonomy/logs"
export REWRITE_STATE="$HOME/rewrite-autonomy/state"
