# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:47:44 2026

@author: user
"""

# =============================================================================
# import re
# 
# receipt_number_input = input("請輸入統一編號八位數: ")
# receipt_number_pattern = r"^\d{8}$"
# match = re.findall(receipt_number_pattern, receipt_number_input)
# if match:
#     print("格式合法")
# else:
#     print("格式不符")
#     
# #簡潔一點，不用宣告pattern那行變數：
# #if re.match(r"\d{8}$", receipt_number_input)
# 
# =============================================================================

import os
from datetime import datetime

file_path = "mood_log.txt"

mood = input("請輸入你現在的心情: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8", newline='') as f:
        f.write("時間戳記,心情內容\n")

with open(file_path, "a", encoding="utf-8", newline='') as f:
    f.write(f"{timestamp},{mood}\n")