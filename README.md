# Daily Hotspot - OpenClaw Skill

每日热点速览技能，使用必应/谷歌搜索生成每日热点简报，无需Brave Search API。

## 功能特性

- **多搜索引擎支持**: 使用必应、谷歌搜索
- **无API密钥需求**: 不需要Brave Search或其他付费API
- **分类精准**: 时政、社会、科技、财经等分类
- **格式规范**: 符合简报格式要求
- **定时任务**: 支持每日自动生成

## 安装

### 1. 安装到OpenClaw

```bash
cp -r daily-hotspot /path/to/openclaw/skills/
```

### 2. 无需配置API密钥

直接使用搜索引擎，无需任何API配置。

## 使用方法

### 命令行使用

```bash
# 生成每日热点简报
python3 daily-hotspot-brief.py

# 使用webfetch方式
python3 daily-hotspot-webfetch.py
```

### OpenClaw对话中使用

```
用户: 今日热点
AI: 正在获取热点新闻...

《每日热点速览》 2026年03月31日 星期一 07:00

一、时政要闻
• 国务院发布新政策：促进经济高质量发展
• 人大代表建议：加强网络安全立法

二、社会民生
• 教育部：推进教育公平新举措
• 医保改革：扩大报销范围

三、科技创新
• AI技术突破：新一代大模型发布
• 新能源汽车销量再创新高

四、财经动态
• 股市行情：科技股领涨
• 央行政策：稳健货币政策持续

今日关注：AI技术发展引领新一轮产业变革
```

### 定时任务配置

```yaml
# OpenClaw 定时任务配置
- name: "daily-hotspot"
  schedule: "0 7 * * *"  # 每天7点
  command: "python3 /path/to/daily-hotspot/daily-hotspot-brief.py"
  channel: "openclaw-weixin"
```

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

## 支持的新闻分类

| 分类 | 说明 | 示例关键词 |
|------|------|-----------|
| **时政要闻** | 国家政策、政府工作 | 国务院政策、人大建议 |
| **社会民生** | 教育、医疗、住房 | 教育改革、医保政策 |
| **科技创新** | 科技发展、互联网 | AI技术、新能源 |
| **财经动态** | 经济、金融、股市 | 央行政策、股市行情 |

## 技术实现

- **搜索引擎**: 使用必应/谷歌搜索
- **HTML解析**: 本地解析搜索结果
- **内容提取**: 提取标题和摘要
- **格式化输出**: 生成结构化简报

## 与NewsNow的区别

| 特性 | Daily Hotspot | NewsNow |
|------|--------------|---------|
| **数据源** | 搜索引擎 | NewsNow API |
| **API需求** | 无需API | 需要NewsNow服务 |
| **实时性** | 实时搜索 | 预聚合数据 |
| **本地化** | 通用 | 支持本地新闻 |

## 文件说明

```
daily-hotspot/
├── SKILL.md                  # 技能说明
├── README.md                 # 本文件
├── daily-hotspot-brief.py    # 主要脚本
└── daily-hotspot-webfetch.py # Webfetch版本
```

## 依赖

- **Python 3.6+**
- **curl** 或 **web_fetch工具**

## 注意事项

- 网络连接稳定
- 搜索结果可能受地区限制
- 建议配置定时任务实现自动化

## 许可证

MIT License

## 作者

OpenClaw Community

## 相关链接

- [OpenClaw](https://github.com/openclaw/openclaw)
- [multi-search-engine技能](https://github.com/lzylipu/openclaw-skill-no-brave-search)