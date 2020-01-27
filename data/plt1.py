# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :

from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# 引入中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

# 折线图
def main1():

    # 设置图片大小及清晰度
    plt.figure(figsize=(10,6),dpi=120)
    x = range(19)
    # 天津气温
    y = [2, 4, 6, 9, 4, 1, 2, 4, 5, 5, 0, 3, 0, 1, 2, 2, 3, 0, 5]
    plt.plot(x,y,color="#F08080",linestyle="-",linewidth=8,alpha=0.5)
    # 设置X轴刻度间隔
    plt.xticks(x,['%s 时'%x for x in range(19)],rotation=45,fontproperties=my_font)
    # 设置y轴刻度间隔
    plt.yticks(range(min(y),max(y)+1))
    # x轴传入字符串
    # 保存图片
    # plt.savefig('./pic/2.png')
    # 设置标题
    plt.xlabel("时间",fontproperties=my_font)
    plt.ylabel('温度',fontproperties=my_font)
    plt.title('天津气温',fontproperties=my_font)
    plt.show()

# 直方图
def main2():
    movies = ['战狼2',"速度与激情8","功夫熊猫","西游伏妖","变形金刚5","摔跤吧"]
    moneys = [56.01,26.94,17.53,16.49,15.45,12.96]
    plt.bar(range(len(movies)),moneys)
    plt.xticks(range(len(movies)),movies,rotation=45,fontproperties=my_font)

    plt.show()

# 条形图
def main3():
    movies = ['战狼2',"速度与激情8","功夫熊猫","西游伏妖","变形金刚5","摔跤吧"]
    moneys = [56.01,26.94,17.53,16.49,15.45,12.96]
    plt.barh(range(len(movies)),moneys,height=0.3)
    plt.yticks(range(len(movies)),movies,rotation=45,fontproperties=my_font)
    # 增加网格
    plt.grid(alpha=0.3)
    plt.show()

def main4():
    a = ['战狼2',"速度与激情8","功夫熊猫","西游伏妖"]
    b16 = [15777,312,4497,319]
    b15 = [12357,156,2045,168]
    b14 = [2358,399,2358,362]
    bar_width = 0.3
    x14 = range(len(a))
    x15 = [i + bar_width for i in x14]
    x16 = [i + bar_width*2 for i in x14]
    plt.figure(figsize=(20,8),dpi=80)
    plt.bar(x14,b14,width=bar_width,label='14日',color="black")
    plt.bar(x15,b15,width=bar_width,label='15日')
    plt.bar(x16,b16,width=bar_width,label='16日')

    # 设置图例
    plt.legend(prop=my_font)
    plt.xticks(x15,a,fontproperties=my_font)
    plt.title('每日票房',fontproperties=my_font)
    plt.show()

def main5():
    # data = list()
    data = [130, 98, 129, 102, 101, 132, 114, 96, 86, 94, 124, 121, 129, 107, 102, 136, 84, 130, 109, 131, 114, 114, 121, 126, 95, 128, 93, 100, 128, 128, 84, 101, 95, 121, 82, 92, 81, 89, 126, 137, 87, 110, 103, 130, 117, 111, 118, 97, 104, 93, 80, 106, 99, 110, 134, 127, 109, 104, 127, 135, 97, 132, 117, 120, 111, 124, 103, 120, 86, 105, 134, 103, 89, 101, 104, 130, 102, 91, 137, 136, 116, 132, 128, 86, 93, 84, 120, 106, 122, 84, 113, 117, 133, 97, 120, 89, 116, 102, 117, 113, 83, 103, 117, 107, 115, 88, 122, 128, 86, 113, 89, 112, 116, 102, 100, 103, 129, 126, 97, 105, 137, 95, 117, 88, 107, 128, 111, 134, 133, 97, 113, 121, 124, 113, 107, 80, 86, 138, 117, 120, 119, 80, 126, 80, 130, 104, 118, 127, 90, 92, 114, 133, 133, 127, 137, 93, 91, 93, 95, 129, 139, 119, 91, 106, 121, 114, 90, 112, 99, 123, 101, 131, 126, 137, 94, 96, 110, 127, 95, 80, 101, 87, 95, 91, 81, 98, 117, 87, 87, 80, 136, 106, 91, 133, 120, 103, 104, 87, 121, 109, 108, 121, 135, 100, 131, 111, 82, 119, 135, 123, 102, 128, 130, 96, 91, 96, 114, 134, 139, 93, 86, 91, 86, 129, 110, 121, 127, 104, 84, 84, 133, 87, 114, 112, 103, 95, 83, 82, 87, 130, 122, 99, 87, 120, 120, 128, 88, 110, 107, 93]
    # for i in range(250):
    #     data.append(random.randrange(80,140))
    # print(data)
    # 频数分布直方图
    plt.hist(data)

    plt.show()


if __name__ == "__main__":
    # main1()
    # main2()
    # main3()
    # main4()
    main5()