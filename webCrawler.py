# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:31:57 2026

@author: user
"""

import requests
from bs4 import BeautifulSoup

custom_headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# =============================================================================
# target_url = "https://quotes.toscrape.com/"
# 
# try:
#     response = requests.get(target_url, headers=custom_headers, timeout=10)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "html.parser")
# # =============================================================================
# #         quote_blocks = soup.find_all("div", class_="quote")
# #         print(f"成功抓取 {len(quote_blocks)} 則名言：\n")
# #         for block in quote_blocks:
# #             content = block.find("span", class_="text").text
# #             author = block.find("small", class_="author").text
# #             print(f"『{content}』")
# #             print(f"－ {author}\n")
# # =============================================================================
#         tag_blocks = soup.find_all("a", class_="tag")
#         for tag in tag_blocks:
#             print(tag.text)
#     else:
#         print(f"請求失敗，錯誤代碼：{response.status_code}")
# 
# except Exception as error:
#     print(f"網路連線發生異常：{error}")
# =============================================================================
    
    
target_url = "https://www.python.org/blogs/"

try:
    response = requests.get(target_url, headers=custom_headers, timeout=20)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        news_blocks = soup.find("div", class_="shrubbery")
        news_items = news_blocks.find_all("li")
        for item in news_items:
            title = item.find("h3").text.strip()
            date = item.find("time").text.strip()
            if date and title:
                print(f"日期：{date}")
                print(f"標題：{title}\n")
    else:
        print(f"請求失敗，錯誤代碼：{response.status_code}")

except Exception as error:
    print(f"網路連線發生異常：{error}")
