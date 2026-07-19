# 📰 Daily Hotspot - OpenClaw Skill / 每日热点速览技能

> 🌐 English | [简体中文](./README.md)
> Daily hotspot briefing using Google and Bing Search, no paid Brave Search API required.
> 基于必应/谷歌搜索抓取生成的每日热点速览，无需 Brave Search 等付费 API。

## ✨ 功能特性 / Features

- 🔍 多搜索引擎 / Multi-engine (Bing + Google)
- 💸 免付费 API / No API key required
- 📊 分类精准 / Precise categories (时政·社会·科技·财经)
- 🔄 支持定时 / Cron-ready

## 🚀 安装 / Installation

```bash
cp -r daily-hotspot /path/to/openclaw/skills/
```

无需 API 配置，开箱即用。

## 📖 使用方法 / Usage

```bash
# CLI / 命令行
python3 daily-hotspot-brief.py
python3 daily-hotspot-webfetch.py
```

定时任务 / Cron:

```yaml
- name: "daily-hotspot"
  schedule: "0 7 * * *"  # daily 7 AM / 每天早7点
  command: "python3 /path/to/daily-hotspot/daily-hotspot-brief.py"
```

## 📊 输出格式 / Output

```
《每日热点速览》 YYYY年MM月DD日 星期X HH:mm

一、时政要闻 / Politics
• 标题：简介

二、社会民生 / Society
• 标题：简介

三、科技创新 / Technology
• 标题：简介

四、财经动态 / Finance
• 标题：简介

今日关注 / Today's Focus：总结
```

## 📁 文件说明 / Structure

```
daily-hotspot/
├── SKILL.md                  # 技能定义
├── README.md                 # 本文件
├── daily-hotspot-brief.py    # 主脚本
└── daily-hotspot-webfetch.py # Webfetch版
```

## 📄 许可证 / License

MIT

## 🔗 相关链接 / Links

- [OpenClaw](https://github.com/openclaw/openclaw)
- [multi-search-engine](https://github.com/lzylipu/skill-no-brave-search)
