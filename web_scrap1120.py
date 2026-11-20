# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:03:49 2026

@author: user
"""

# =============================================================================
# import requests
# from bs4 import BeautifulSoup
# 
# url = "https://www.python.org/blogs/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# 
# news_ul = soup.find('ul', class_='menu')
# news_items = news_ul.find_all('li')
# 
# for item in news_items:
#     # 抓標題與日期
#     title = item.find('h3').text.strip()
#     date = item.find('time').text.strip()
#     print(f"{date} - {title}")
# =============================================================================


# =============================================================================
# import requests
# from bs4 import BeautifulSoup
# 
# url = "https://www.python.org/blogs/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# 
# news_section = soup.find('div', class_='shrubbery')
# 
# if news_section:
#     news_items = news_section.find_all('li')
#     for item in news_items:
#         title = item.find('h3').text.strip()
#         date = item.find('time').text.strip()
#         print(f"{date} - {title}")
# else:
#     print("找不到指定區塊，請確認網頁結構是否變更。")
# =============================================================================

import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime

def run_ptt_scraper():
    url = "https://www.pttweb.cc/bbs/movie"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"連線失敗，狀態碼：{response.status_code}")
        return
        
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="e7-container")
    
    good_movies = []
    
    for article in articles:
        # 尋找 pttweb.cc 的文章標題連結
        a_tag = article.find("a", class_="e7-article-default")
        if not a_tag:
            continue
            
        raw_title = a_tag.text
        link = "https://pttweb.cc" + a_tag["href"]
        
        if re.search(r"\[好雷\]", raw_title):
            clean_title = re.sub(r"\[好雷\]", "", raw_title).strip()
            clean_title = re.sub(r"\s+", " ", clean_title)
            
            good_movies.append({
                "標題": clean_title,
                "網址": link
            })
            
    csv_filename = "ptt_good_movies.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["標題", "網址"])
        writer.writeheader()
        writer.writerows(good_movies)
        
    log_filename = "scraping_log.txt"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{now_str}] 執行完成，共抓取到 {len(good_movies)} 篇 [好雷] 文章。\n"
    
    with open(log_filename, mode="a", encoding="utf-8") as f:
        f.write(log_message)
        
    print("任務執行完畢！")
    print(log_message.strip())

if __name__ == "__main__":
    run_ptt_scraper()






