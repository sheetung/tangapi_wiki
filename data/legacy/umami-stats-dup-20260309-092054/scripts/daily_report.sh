#!/bin/bash
# Umami Daily Report Script
# Runs at 9:00 AM daily to fetch previous day's stats

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"
CONFIG_FILE="$SCRIPT_DIR/references/umami-config.json"
LOG_FILE="$SCRIPT_DIR/daily_report.log"

# Run the fetch script
OUTPUT=$($VENV_PYTHON "$SCRIPT_DIR/scripts/fetch_stats.py" --config "$CONFIG_FILE" --days 1 --title "📊 moontung.top 昨日统计" 2>&1)
EXIT_CODE=$?

# Log the output
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Exit code: $EXIT_CODE" >> "$LOG_FILE"
echo "$OUTPUT" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"

# Output for cron to capture
echo "$OUTPUT"
exit $EXIT_CODE
