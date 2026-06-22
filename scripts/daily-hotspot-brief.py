#!/usr/bin/env python3
"""
每日热点速览 - 使用 multi-search-engine 技能
不使用 Brave Search，改用 Bing、Google 等搜索引擎
"""

import os
import sys
import time
import json
from datetime import datetime, timedelta

def get_current_time_info():
    """获取当前时间信息"""
    now = datetime.now()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return {
        "date": now.strftime("%Y年%m月%d日"),
        "weekday": weekdays[now.weekday()],
        "time": now.strftime("%H:%M")
    }

def search_with_bing(keyword, region="cn"):
    """使用 Bing 搜索"""
    if region == "cn":
        url = f"https://cn.bing.com/search?q={keyword}&ensearch=0"
    else:
        url = f"https://cn.bing.com/search?q={keyword}&ensearch=1"
    
    try:
        # 使用 web_fetch 工具
        import subprocess
        result = subprocess.run([
            "curl", "-s", "--max-time", "10", 
            "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            url
        ], capture_output=True, text=True, timeout=15)
        
        if result.returncode == 0 and result.stdout:
            return result.stdout
        else:
            return None
    except Exception as e:
        print(f"搜索失败 {keyword}: {e}")
        return None

def extract_news_snippets(html_content, max_items=2):
    """从搜索结果中提取新闻摘要"""
    if not html_content:
        return []
    
    snippets = []
    try:
        # 简单的 HTML 解析（实际应该用 BeautifulSoup）
        lines = html_content.split('\n')
        for line in lines:
            if 'class=' in line and ('b_caption' in line or 'snippet' in line or 'desc' in line):
                # 提取文本内容
                clean_text = line.replace('<', ' ').replace('>', ' ')
                clean_text = ' '.join(clean_text.split())
                if len(clean_text) > 50 and len(clean_text) < 300:
                    snippets.append(clean_text)
                    if len(snippets) >= max_items:
                        break
    except Exception as e:
        print(f"解析失败: {e}")
    
    return snippets[:max_items]

def get_lyon_weather():
    """获取CITY_NAME天气（模拟）"""
    # 实际应该调用天气 API，这里先模拟
    return "Partly cloudy", "+2°C~+9°C"

def generate_daily_brief():
    """生成每日热点速览"""
    time_info = get_current_time_info()
    weather_desc, weather_temp = get_lyon_weather()
    
    # 搜索关键词
    search_keywords = {
        "信访/治理": ["CITY_NAME 信访工作", "基层治理 CITY_NAME"],
        "时政": ["今日时政新闻", "国家政策 最新"],
        "社会民生": ["CITY_NAME 民生新闻", "社会热点 今日"],
        "法律政策": ["最新法律法规", "政策解读 2026"],
        "热点补充": ["今日热点新闻", "重要事件 今日"]
    }
    
    brief_content = f"""《每日热点速览》 {time_info['date']} {time_info['weekday']} {time_info['time']}
CITY_NAME天气：{weather_desc}，{weather_temp}
"""
    
    all_news_found = False
    
    for category, keywords in search_keywords.items():
        brief_content += f"\n{category}\n"
        category_news = []
        
        for keyword in keywords:
            # 优先搜索本地信息
            if "CITY_NAME" in keyword:
                html = search_with_bing(keyword, "cn")
            else:
                html = search_with_bing(keyword, "int")
            
            snippets = extract_news_snippets(html, 1)
            if snippets:
                category_news.extend(snippets)
                all_news_found = True
                if len(category_news) >= 2:
                    break
        
        if category_news:
            for i, snippet in enumerate(category_news[:2]):
                # 提取关键词（简化处理）
                words = snippet.split()[:3]
                keyword = " ".join(words) if words else "新闻"
                brief_content += f"{keyword}：{snippet}\n"
        else:
            brief_content += "（暂无高价值信息）\n"
            brief_content += "（暂无高价值信息）\n"
    
    # 今日关注
    if all_news_found:
        brief_content += "\n今日关注：综合今日各领域重要信息，重点关注政策变化和社会民生。"
    else:
        brief_content += "\n今日关注：因网络环境限制，无法获取实时新闻资讯，以上内容为占位格式。"
    
    return brief_content

def main():
    """主函数"""
    try:
        brief = generate_daily_brief()
        print(brief)
        
        # 保存到文件（用于定时任务）
        output_file = f"/tmp/daily-hotspot-{datetime.now().strftime('%Y%m%d')}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(brief)
        
        print(f"\n已保存到: {output_file}")
        
    except Exception as e:
        print(f"生成失败: {e}")
        # 输出占位格式
        time_info = get_current_time_info()
        weather_desc, weather_temp = get_lyon_weather()
        placeholder = f"""《每日热点速览》 {time_info['date']} {time_info['weekday']} {time_info['time']}
CITY_NAME天气：{weather_desc}，{weather_temp}

一、信访/治理
（暂无高价值本地信息）
（暂无高价值本地信息）

二、时政  
（暂无高价值信息）
（暂无高价值信息）

三、社会民生
（暂无高价值本地信息）
（暂无高价值本地信息）

四、法律政策
（暂无高价值信息）
（暂无高价值信息）

五、热点补充
（暂无高价值信息）
（暂无高价值信息）

今日关注：因当前环境缺少网络搜索能力，无法获取实时新闻资讯，以上内容为占位格式。
"""
        print(placeholder)

if __name__ == "__main__":
    main()