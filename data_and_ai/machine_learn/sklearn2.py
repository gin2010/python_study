# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :归一化
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
import numpy as np

def main1():
    '''
    归一化处理
    :return:
    '''
    mm = MinMaxScaler(feature_range=(1,2))
    data = [
        [90,2,10,40],
        [60,4,15,45],
        [75,3,13,46]
    ]
    new_data = mm.fit_transform(data)
    print(new_data)

def main2():
    '''
    标准差处理
    :return:
    '''
    data = [
        [1,-1,3],
        [2,4,2],
        [4,6,-1]
    ]
    std = StandardScaler()
    new_data = std.fit_transform(data)
    print(data)
    print(new_data)

def main():
    '''
    缺失值的处理
    :return:
    '''
    data=[
        [1,2,3],
        [np.nan,5,6],
        [7,8,9]
    ]
    im = Imputer(missing_values='nan',strategy='mean',axis=0)
    new_data = im.fit_transform(data)
    print(new_data)

if __name__ == "__main__":
    main()

