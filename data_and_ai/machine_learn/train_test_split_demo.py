# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : 拆分数据为训练集、测试集
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris  # 里面有内置分类数据
from sklearn.datasets import load_boston  # 里面有内置回归数据（房价数据）
import pandas as pd
import

def main1():
    '''
    将load_iris返回的数据处理为dataframe格式
    :return:
    '''
    li = load_iris()
    # 返回字典类型
    # 'data'：存放样本的特征值
    # 'target'：存放目标值(属于哪一类)
    # 'target_names'：target中数字对应的哪一种花
    # 'DESCR'：存放描述
    # 'feature_names'：特征的名称
    # 'filename'：当前文件所有的文件夹
    datas = pd.Da

def main2():
    li = load_iris()
    # print(li.target)  #支持直接读取值
    # 进行数据分割，依次返回训练样本、训练目标值、测试样本、测试目标值
    # data_train,data_test,target_train,target_test = train_test_split(li.data,li.target,test_size=0.25)
    # print("训练数据")
    # print(data_train)
    # print(target_train)
    # print("测试集数据")
    # print(data_test)
    # print(target_test)

def main3():
    lb = load_boston()
    print(lb.keys())
    # 'data'
    # 'target'
    # 'feature_names'
    # 'DESCR'
    # 'filename



if __name__ == "__main__":
    main()

