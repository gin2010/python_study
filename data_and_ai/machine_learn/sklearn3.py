# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : 特征选择
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

def main1():
    '''
    方差
    :return:
    '''
    data = [
    [0,2,0,3],
    [0,1,4,3],
    [0,1,1,3]
    ]
    # var = VarianceThreshold(threshold=0)  # 去掉方差为0的列
    var = VarianceThreshold(threshold=1)  # 去掉方差为1的列
    new_data = var.fit_transform(data)
    print(new_data)

def main():
    '''
    pca降维
    :return:
    '''
    # pca = PCA(n_components=0.9)
    pca = PCA(n_components=1)
    data = [[2,8,4,5],[6,3,0,8],[5,4,9,1]]
    new_data = pca.fit_transform(data)
    print(new_data)


if __name__ == "__main__":
    main()

