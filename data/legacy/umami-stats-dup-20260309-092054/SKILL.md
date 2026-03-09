---
name: umami-stats
description: "Fetch and report Umami analytics statistics. Use when user wants to check website analytics, view visitor stats, or schedule periodic Umami reports."
---

# Umami Stats

Fetch website statistics from Umami Analytics and generate formatted reports.

## Quick Start

```bash
# Fetch today's stats
python scripts/fetch_stats.py

# Fetch last 7 days
python scripts/fetch_stats.py --days 7

# Output as JSON
python scripts/fetch_stats.py --json
```

## Configuration

Create `umami-config.json` or set environment variables:

| Variable | Description |
|----------|-------------|
| `UMAMI_URL_BASE` | Umami instance URL (e.g., https://analytics.example.com) |
| `UMAMI_USERNAME` | Umami username |
| `UMAMI_PASSWORD` | Umami password |
| `UMAMI_WEBSITE_ID` | Target website ID |
| `UMAMI_HOSTNAME` | Website hostname (optional) |

## Sample Output

```
📊 Umami 统计报告
📅 时间: 2026-03-07 11:00 (过去 1 天)

👁️ 页面浏览: 1.2K
👥 访客数: 856
🔄 访问次数: 920
⚡ 当前在线: 12
📉 跳出率: 35.2%
```

## Scheduled Reports with Cron

To run daily at 9:00 AM:

```bash
# Edit crontab
crontab -e

# Add line
0 9 * * * cd /path/to/umami-stats && python scripts/fetch_stats.py >> /var/log/umami-report.log 2>&1
```

For OpenClaw cron integration, add to HEARTBEAT.md or use OpenClaw's cron scheduling.

## Requirements

```bash
pip install umami-analytics
```
