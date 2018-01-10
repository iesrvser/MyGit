# -*- coding: utf-8 -*-
import tushare as ts
import traceback

def get_price(code):
    dic = {}
    df = ts.get_k_data(code)
    price_20days_avg = float(df.tail(20)["close"].sum()/20)
    price_today_low = df.tail(1)["low"].item()
    price_today_high = df.tail(1)["high"].item()
    price_today_open = df.tail(1)["open"].item()
    price_today_close = df.tail(1)["close"].item()
    dic["MA20"] = price_20days_avg
    dic["low"] = price_today_low
    dic["high"] = price_today_high
    dic["open"] = price_today_open
    dic["close"] = price_today_close
    return dic

def get_code_list(file):
    code_list = []
    file_object = open(file)
    try:
         all_the_text = file_object.read()
    finally:
         file_object.close()
    items = all_the_text.split("\n")
    for item in items:
        if item != "":
            code_list.append(item[1::])
    return code_list

file = "~/MyGit/WW1801.EBK"
code_list = get_code_list(file)
for code in code_list:
    dic = get_price(code)
    if dic["low"] <= dic["MA20"] and dic["close"] >= dic["MA20"]:
        print(code)
        print("MA20: " + str(dic["MA20"]))
        print("Close: " + str(dic["close"]))
        print("Low: " + str(dic["low"]))
        print("---------------------------")
    