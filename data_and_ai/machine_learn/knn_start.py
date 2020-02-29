# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : K-近邻算法
#       1.入门案例：根据身高、体重、鞋码预测男女
#       2.yuan尾花分类练习
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_iris

def knn1():
    '''根据身高、体重、鞋码预测男女'''
    x_train = [
        [183,90,44],
        [175,78,42],
        [170,73,42],
        [160,50,37],
        [163,53,39],
        [166,60,38],
        [170,62,40],
        [168,68,40],
    ]
    y_train = ['男','男','男','女','女','女','女','男']
    # 1.创建模型（建模）
    knn = KNeighborsClassifier(n_neighbors=3)  # 初始几个点
    # 2.传入训练数据，训练算法
    knn.fit(x_train,y_train)
    # 3.传入测试数据，预测结果
    x_test = [[190,100,46],[162,58,38]]
    y_predict = knn.predict(x_test)
    print(y_predict)

def knn2():
    '''yuan尾花iris分类练习'''
    # 1.获取数据
    iris_datas = load_iris()
    # print(iris_datas)
    # print(iris_datas.keys())
    x = iris_datas.data
    y = iris_datas.target
    # print(x)
    # print(y)
    # 2.将数据拆分成训练数据与测试数据
    x_train = x[::2]
    y_train = y[::2]
    x_test = x[1::2]
    y_test = y[1::2]
    # 3.建模，可多次尝试输入n_neighbors的值
    knn = KNeighborsClassifier(n_neighbors=5)
    # 4.传入训练数据
    knn.fit(x_train,y_train)
    # 5.输入测试数据获得预测结果
    y_predict = knn.predict(x_test)
    print("predict:",y_predict)
    print("test:",y_test)
    # 6.评估模型正确率
    point = knn.score(x_test,y_test) # 直接输入测试数据的x、y即可
    print("score:",point)


def main():
    # knn1()
    knn2()


if __name__ == "__main__":
    main()

