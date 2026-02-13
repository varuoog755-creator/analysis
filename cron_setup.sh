#!/bin/bash
# Cron setup script for TrendPulse Autonomous Fleet

# 1. Get current directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
VENV="$DIR/venv/bin/python"

# 2. Add to Crontab (Run every 4 hours)
(crontab -l 2>/dev/null; echo "0 */4 * * * $VENV $DIR/fleet_engine.py >> $DIR/fleet_log.txt 2>&1") | crontab -

echo "✅ Autonomous Fleet Pulse scheduled (Every 4 hours)."
echo "Log file: $DIR/fleet_log.txt"
