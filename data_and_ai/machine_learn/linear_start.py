# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : 最小二乘法做线性回归的预测
#       1.使用线性回归预测糖尿病，选取的是第四个参数(列表里实际是3)
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def linear1():
    # 1.导入数据
    datas = load_diabetes()
    x = datas.data[:,np.newaxis,3]
    y = datas.target[:,np.newaxis]
    # print(x)  # <class 'numpy.ndarray'>
    # print(y.shape)
    # print(datas.DESCR)
    # 2.数据加工
    x_train = x[:-40]
    y_train = y[:-40]
    print(x_train.shape)
    x_test = x[-40:]
    y_test = y[-40:]
    # 3.建模
    linear = LinearRegression()
    # 4.训练模型
    linear.fit(x_train,y_train)
    # 5.结果
    y_predict = linear.predict(x_test)
    print(linear.score(x_test,y_test))
    # 6.图
    plt.scatter(x_test,y_test)
    plt.plot(x_test,y_predict)
    plt.show()

def linear2():
    '''
    求解方程组
    x+y=3
    x-y=1
    x=2,y=1 -->result是
    :return:
    '''
    x_train = np.array([[1,1],[1,-1]])
    y_train = np.array([3,1])
    result = np.dot(np.linalg.inv(x_train),y_train)
    print(result)
    linear = LinearRegression()
    linear.fit(x_train,y_train)
    x_test = np.array([[1,0],[0,1]])
    print(linear.coef_)
    y_predict = linear.predict(x_test)
    print(y_predict)


def main():
    # linear1()
    linear2()


if __name__ == "__main__":
    main()

