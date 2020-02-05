# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : fit与transform的作用
from sklearn.preprocessing import StandardScaler

def main1():
    s1 = StandardScaler()
    data = [[1,2,3],[4,5,6]]
    new_data = s1.fit_transform(data) # 直接传入数据并转换
    print(new_data)

def main2():
    s1 = StandardScaler()
    data = [[1,2,3],[4,5,6]]
    data2 = [[11,12,13],[24,25,26]]
    # 先输入数据，计算平均值与方差等
    s1.fit(data)
    # 再进行数据转换
    new_data = s1.transform(data)
    print(new_data)

def main():
    s1 = StandardScaler()
    data = [[1,2,3],[4,5,6]]
    data2 = [[11,12,13],[24,25,26]]
    # 先输入数据data2，计算平均值与方差等(由于标准变成data2，所以结果也不一样)
    s1.fit(data2)
    # 再进行数据转换data
    new_data = s1.transform(data)
    print(new_data)

if __name__ == "__main__":
    main()

