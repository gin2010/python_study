# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :

from matplotlib import pyplot as plt

def main():

    # 设置图片大小及清晰度
    plt.figure(figsize=(15,9),dpi=300)
    x = range(19)
    # 天津气温
    y = [2, 4, 6, 9, 4, 1, 2, 4, 5, 5, 0, 3, 0, 1, 2, 2, 3, 0, 5]
    plt.plot(x,y)
    # 设置X轴刻度间隔
    plt.xticks(range(19))
    # 设置y轴刻度间隔
    plt.yticks(range(min(y),max(y)+1))
    # x轴传入字符串
    # 保存图片
    # plt.savefig('./pic/2.png')
    plt.show()

if __name__ == "__main__":
    main()