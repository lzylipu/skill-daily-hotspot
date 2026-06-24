# Daily Hotspot - OpenClaw Skill

**[English](./README.en.md) | [中文](./README.md)**

Daily hotspot brief skill — generate daily news brief using Bing/Google search, no Brave Search API needed.

## Features

- **Multi-engine**: Bing, Google search support
- **No API Key**: No Brave Search or paid API required
- **Categorized**: Politics, society, tech, finance, etc.
- **Formatted**: Structured brief output
- **Scheduled**: Supports daily auto-generation via Cron

## Installation

### 1. Install to OpenClaw

```bash
cp -r daily-hotspot /path/to/openclaw/skills/
```

### 2. No API key needed

Uses search engines directly — zero API configuration.

## Usage

### Command Line

```bash
# Generate daily hotspot brief
python3 daily-hotspot-brief.py

# Using webfetch
python3 daily-hotspot-webfetch.py
```

### In OpenClaw Chat

```
User: 今日热点
AI: Fetching trending news...

《Daily Hotspot Brief》 2026-03-31 Monday 07:00

I. Politics
• Headline 1: Summary
• Headline 2: Summary

II. Society
• Headline 1: Summary

III. Tech
• Headline 1: Summary

IV. Finance
• Headline 1: Summary

Today's Focus: One-sentence highlight
```

### Cron Task

```yaml
- name: "daily-hotspot"
  schedule: "0 7 * * *"
  command: "python3 /path/to/daily-hotspot/daily-hotspot-brief.py"
  channel: "openclaw-weixin"
```

## News Categories

| Category | Description | Example Keywords |
|----------|-------------|------------------|
| **Politics** | National policy, government | State Council, NPC proposals |
| **Society** | Education, healthcare, housing | Education reform, Medicare |
| **Tech** | Tech development, internet | AI, renewable energy |
| **Finance** | Economy, banking, stock market | Central bank policy, stocks |

## Technical Implementation

- **Search Engine**: Uses Bing/Google search
- **HTML Parsing**: Local parsing of search results
- **Content Extraction**: Extract titles and summaries
- **Formatted Output**: Generate structured brief

## Comparison with NewsNow

| Feature | Daily Hotspot | NewsNow |
|---------|--------------|---------|
| **Data Source** | Search engines | NewsNow API |
| **API Required** | None | NewsNow service needed |
| **Freshness** | Real-time search | Pre-aggregated data |
| **Localization** | General | Supports local news |

## File Structure

```
daily-hotspot/
├── SKILL.md                  # Skill specification
├── README.md                 # Chinese README
├── README.en.md              # English README
├── daily-hotspot-brief.py    # Main script
└── daily-hotspot-webfetch.py # Webfetch version
```

## Requirements

- **Python 3.6+**
- **curl** or **web_fetch tool**

## Notes

- Stable internet connection recommended
- Search results may vary by region
- Configure Cron task for daily automation

## License

MIT License
