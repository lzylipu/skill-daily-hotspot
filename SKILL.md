---
name: daily-hotspot
description: "Daily hotspot brief - Bing/Google search based news summary (legacy, prefer daily-morning-brief)"
version: 1.0.0
author: lzylipu
license: MIT
platforms: [linux]
status: deprecated
replaced_by: daily-morning-brief
prerequisites:
  services:
    - name: curl/web_fetch
      description: "HTTP client for search engine access"
metadata:
  hermes:
    tags: [daily, hotspot, news, bing, google, 热点, 新闻]
    related_skills: [daily-morning-brief, newsnow-skill]
    homepage: https://github.com/lzylipu/openclaw-skill-daily-hotspot
    category: personal
    skill_type: cron
---

# Daily Hotspot - 每日热点速览

每日自动生成热点新闻简报，不依赖Brave Search API。

## 功能特性

- **多搜索引擎支持**: 使用必应、谷歌搜索
- **无API密钥需求**: 不需要Brave Search或其他付费API
- **分类精准**: 时政、社会、科技、财经等分类
- **格式规范**: 符合简报格式要求
- **定时任务**: 支持每日自动生成

## 使用方法

### 命令行使用

```bash
# 生成每日热点简报
python3 daily-hotspot-brief.py

# 使用webfetch方式
python3 daily-hotspot-webfetch.py
```

### OpenClaw定时任务

```yaml
- name: "daily-hotspot"
  schedule: "0 7 * * *"  # 每天7点
  command: "python3 /path/to/daily-hotspot/daily-hotspot-brief.py"
  channel: "openclaw-weixin"
```

## 配置

无需API密钥配置，直接使用搜索引擎。

## 输出格式

```
《每日热点速览》 YYYY年MM月DD日 星期X HH:mm

一、时政要闻
• 标题1：简介
• 标题2：简介

二、社会民生
• 标题1：简介
• 标题2：简介

三、科技创新
• 标题1：简介
• 标题2：简介

四、财经动态
• 标题1：简介
• 标题2：简介

今日关注：一句话总结当天重点
```

## 依赖

- Python 3.6+
- curl 或 web_fetch 工具

## 技术实现

- 使用必应/谷歌搜索API
- 本地HTML解析
- 结构化输出

## 许可证

MIT License