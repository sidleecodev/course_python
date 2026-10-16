# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:49:00 2026

@author: user
"""

if False:
    SBP = int(input("請輸入「收縮壓」數值："))
    if SBP > 140:
        print('提醒：您的收縮壓偏高，請列入自主健康管理並諮詢醫師')
        
if False:
    working_experience = int(input("請輸入你的年資："))
    if working_experience >= 2:
        print("符合面試資格")
    else:
        print("資歷尚未達標，您的履歷已存入人才庫備查")
        
# 接收數據並進行防錯轉換=========================================================
# try:
#     revenue = float(input("請輸入部門本季營業額 (單位：萬元)："))
# except ValueError:
#     print("輸入格式錯誤，系統將預設為 0。")
#     revenue = 0
# =============================================================================

if False:
    price = float(input("請輸入商品單價："))
    if price >= 5000:
        tier = "打8折"
        discount = 0.8
    elif price >= 3000:
        tier = "打9折"
        discount = 0.9
    else:
        tier = "不打折"
        discount = 1
    
    total = float(price * discount)
    print(f"\n商品{tier}，價格為{total:g}。")
    
if False:
    print("1~100之間，10的倍數依序是：", end="")
    for i in range(10,101,10):
        print(i, end=" ")

if False:
    deposit = 1000
    i = 0
    while deposit < 5000:
        i += 1
        deposit += 500
    print(f"需要{i}個月")

if True:
    price = [4000, 800, 15000, 500, 6200]
    stuff = ["光束粒子砲","加速推進劑","反物質核心","太空乾糧","隱形匿蹤斗篷"]
    price_discount = [int( p *0.9) if p > 2000 else p for p in price]
    total = 0
    total_discount = 0
    
    print("\n>>>歡迎來到黑市太空港自動結帳系統 V3.0 <<<")
    print(f"今日特價資產清單: {price_discount}")
    
    while True:
        try:
            choice = int(input("\n請輸入欲購買的物資索引(0-4)，結帳按-1:"))
            if choice == -1:
                break
            if choice < 0 or choice > 4:
                print("聯邦警訊】查無此物資代碼，請重新輸入！")
                continue
            if 0 <= choice <= 4:
                total += price_discount[choice]
                print(f"【成功裝載】目前累計金額：{total}星幣")
        except ValueError:
            print("【輸入錯誤】不准亂按控制台！請務必輸入整數編號！")
    
    if total >= 15000:
        tag = "【梟雄級大宗交易】現折2000星幣"
        total_discount = total - 2000
    elif total >= 8000:
        tag = "【狂徒級買賣】現折800星幣"
        total_discount = total - 800
    else:
        tag = "【小規模走私】不予額外折扣"
        total_discount = total
    
    print("\n=====聯邦邊境星區交易明細=====")
    print(f"交易評級：{tag}")
    
    if total_discount % 50 == 0:
        total_discount += 1
        print("【隱密協定】偵測到聯邦雷達共振！已加收 1 星幣發射干擾誘餌！")
    
    print(f"【最終應付星幣】：{total_discount}星幣")
    