# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib.dates as mdates
import json,time,os

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
filename = "virus_data_{}.json".format(time.strftime("%Y%m%d"))
filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data',filename)
def get_virus_datas():
    # 获取每日数据并保存
    appid = 88125575
    appsecret = "x72rl0qy"
    version = "epidemic"
    url = f"https://tianqiapi.com/api?version={version}&appid={appid}&appsecret={appsecret}"
    # url = "https://tianqiapi.com/api?version=epidemic&appid=23035354&appsecret=8YvlPNrz"
    # url = "https://tianqiapi.com/api?version=epidemic&appid=23035354&appsecret=8YvlPNrz"
    # print(url)
    datas_json = requests.get(url)
    with open(filepath,'w') as file:
        file.write(datas_json.text)

def read_data_and_analysis():
    with open(filepath,'r') as file:
        all_datas = json.loads(file.read(),encoding='utf-8')
    # print(type(all_datas))
    history_datas = all_datas['data']['history']
    area_datas = all_datas['data']['area']
    # 数据清洗
    histories = pd.DataFrame(history_datas)
    ax = histories['date'].sort_values()
    histories['date'] = pd.to_datetime(histories['date'])
    histories.sort_values(by='date',inplace=True,ascending=True)
    histories.set_index('date',inplace=True)
    histories['confirmedNumAdd'] = histories['confirmedNum'].diff()
    histories['confirmedNumAdd'].fillna(0,inplace=True)
    print(area_datas)
    return histories,ax

def total_pic():
    histories,ax = read_data_and_analysis()
    # 绘制疫情走势表
    plt.figure(figsize=(10,6))
    # 每日总数
    # plt.plot(range(histories.shape[0]),histories['confirmedNum'])
    # 每日增长数
    plt.plot(range(histories.shape[0]),histories['confirmedNumAdd'])
    plt.xticks(range(histories.shape[0]),ax,rotation=45)
    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.title("全国疫情总数走势图",fontproperties=my_font)
    plt.xlabel("日期",fontproperties=my_font)
    plt.ylabel("人数",fontproperties=my_font)
    plt.legend(["确诊",],prop=my_font,markerfirst=True)
    plt.grid(alpha=0.3)
    plt.show()

def main():
    # get_virus_datas()
    # total_pic()
    read_data_and_analysis()

if __name__ == "__main__":
    main()

