#!/usr/bin/env python3
"""
Umami Analytics Stats Fetcher
Fetches website statistics and sends a formatted report.
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import umami
except ImportError:
    print("Error: umami-analytics package not installed.")
    print("Install with: pip install umami-analytics")
    sys.exit(1)


def load_config(config_path: str | None = None) -> dict:
    """Load configuration from file or environment variables."""
    config = {}
    
    # Try config file first
    if config_path and Path(config_path).exists():
        with open(config_path) as f:
            config = json.load(f)
    else:
        # Check default locations
        default_paths = [
            Path.cwd() / "umami-config.json",
            Path.home() / ".umami" / "config.json",
            Path(__file__).parent.parent / "references" / "umami-config.json",
        ]
        for path in default_paths:
            if path.exists():
                with open(path) as f:
                    config = json.load(f)
                break
    
    # Override with environment variables
    config["url_base"] = os.environ.get("UMAMI_URL_BASE", config.get("url_base"))
    config["username"] = os.environ.get("UMAMI_USERNAME", config.get("username"))
    config["password"] = os.environ.get("UMAMI_PASSWORD", config.get("password"))
    config["website_id"] = os.environ.get("UMAMI_WEBSITE_ID", config.get("website_id"))
    config["hostname"] = os.environ.get("UMAMI_HOSTNAME", config.get("hostname", ""))
    
    return config


def format_number(n: int) -> str:
    """Format number with K/M suffix for readability."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def fetch_stats(config: dict, days: int = 1) -> dict:
    """Fetch Umami statistics for the specified number of days."""
    # Configure Umami
    umami.set_url_base(config["url_base"])
    
    # Login for authenticated access
    if config.get("username") and config.get("password"):
        umami.login(config["username"], config["password"])
    
    # Set default website
    if config.get("website_id"):
        umami.set_website_id(config["website_id"])
    if config.get("hostname"):
        umami.set_hostname(config["hostname"])
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Fetch stats
    stats = umami.website_stats(
        start_at=start_date,
        end_at=end_date,
        website_id=config.get("website_id")
    )
    
    # Get active users
    try:
        active = umami.active_users(website_id=config.get("website_id"))
    except Exception:
        active = 0
    
    return {
        "pageviews": stats.pageviews.value if hasattr(stats.pageviews, 'value') else stats.pageviews,
        "visitors": stats.visitors.value if hasattr(stats.visitors, 'value') else stats.visitors,
        "visits": stats.visits.value if hasattr(stats.visits, 'value') else stats.visits,
        "bounces": stats.bounces.value if hasattr(stats.bounces, 'value') else stats.bounces,
        "bounce_rate": stats.bounce_rate.value if hasattr(stats, 'bounce_rate') and hasattr(stats.bounce_rate, 'value') else getattr(stats, 'bounce_rate', 0),
        "active_users": active,
        "period": f"过去 {days} 天",
        "date": end_date.strftime("%Y-%m-%d %H:%M"),
    }


def format_report(stats: dict, title: str = "📊 Umami 统计报告") -> str:
    """Format stats into a readable report."""
    lines = [
        title,
        f"📅 时间: {stats['date']} ({stats['period']})",
        "",
        f"👁️ 页面浏览: {format_number(stats['pageviews'])}",
        f"👥 访客数: {format_number(stats['visitors'])}",
        f"🔄 访问次数: {format_number(stats['visits'])}",
        f"⚡ 当前在线: {stats['active_users']}",
    ]
    
    # Add bounce rate if available
    if stats.get('bounce_rate'):
        rate = stats['bounce_rate']
        if hasattr(rate, 'value'):
            rate = rate.value
        lines.append(f"📉 跳出率: {rate:.1f}%" if isinstance(rate, (int, float)) else f"📉 跳出率: {rate}")
    
    return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fetch Umami analytics stats")
    parser.add_argument("--config", "-c", help="Path to config file")
    parser.add_argument("--days", "-d", type=int, default=1, help="Number of days to fetch (default: 1)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    parser.add_argument("--title", "-t", default="📊 Umami 统计报告", help="Report title")
    args = parser.parse_args()
    
    try:
        config = load_config(args.config)
        
        if not config.get("url_base"):
            print("Error: UMAMI_URL_BASE not configured")
            print("Set environment variable or add to config file")
            sys.exit(1)
        
        stats = fetch_stats(config, args.days)
        
        if args.json:
            print(json.dumps(stats, indent=2, ensure_ascii=False))
        else:
            print(format_report(stats, args.title))
            
    except Exception as e:
        print(f"Error fetching stats: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
