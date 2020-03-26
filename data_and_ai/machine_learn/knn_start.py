# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : K-近邻算法
#       1.入门案例：根据身高、体重、鞋码预测男女
#       2.yuan尾花分类练习
#       3.随机生成一些数值，然后转成对应的sin函数结果，再随机写入一些噪点，进行回归
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.externals import joblib #很快就移除了
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_iris
from matplotlib import font_manager
# 引入中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

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
    knn = KNeighborsClassifier(n_neighbors=3)  # 距离最近的K个点
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
    # 7.保存模型
    joblib.dump(knn,'lib/iris_sort_knn.m')
    # 8.加载模型
    iris_knn = joblib.load('lib/iris_sort_knn.m')
    print(iris_knn.score(x_test,y_test))

def knn3():
    '''回归应用：随机生成一些数值，然后转成对应的sin函数结果，再随机写入一些噪点，进行回归'''
    # 1.获取数据
    x_train = np.sort(5*np.random.rand(40,1),axis=0)
    y_train = np.sin(x_train)
    y_train[::5] += np.random.randn(8,1)
    print(y_train.flatten())
    print(x_train.shape,y_train.shape)
    plt.subplot(1,2,1)
    plt.scatter(x_train,y_train)
    x_test = np.linspace(0,5,50).reshape((50,1))
    print(x_test)
    # 2.建模
    knn = KNeighborsRegressor(5)
    # 3.训练模型
    knn.fit(x_train,y_train)
    # 4.预测数据
    y_preditc = knn.predict(x_test)
    plt.subplot(1,2,2)
    plt.scatter(x_test,y_preditc)
    plt.show()



def main():
    # knn1()
    knn2()
    # knn3()


if __name__ == "__main__":
    main()

