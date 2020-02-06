# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : sklearn中字典特征值
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

data = [
    {'city':'beijing',"pm25":100},
    {'city':'shanghai',"pm25":50},
    {'city':'shenzhen',"pm25":30}
]

def main1():
    '''
    字典特征抽取
    :return:
    '''
    dict = DictVectorizer(sparse=False)
    # 将字典转为二维数组
    dv_data = dict.fit_transform(data)
    # 展示每列标题
    # ['city=beijing', 'city=shanghai', 'city=shenzhen', 'pm2.5']
    print(dict.get_feature_names())
    # 将特征值转回字典(会有部分不同)
    # [{'city=beijing': 1.0, 'pm25': 100.0}, {'city=shanghai': 1.0, 'pm25': 50.0}, {'city=shenzhen': 1.0, 'pm25': 30.0}]
    print(dict.inverse_transform(dv_data))

    print(dv_data)


def main2():
    '''
    文本特征抽取，统计文本中词出现的数量
    用于文本分类与情感分析
    对于单个英文字母不统计（因为对于应用没有作用）
    :return:
    '''
    data = [
        'life is short ,i like python',
        'life is long,i dislike python'
    ]
    cv = CountVectorizer()
    cv_data = cv.fit_transform(data)
    print(cv.get_feature_names())
    print(cv_data.toarray())

def main():
    '''
    因为英文单词中间有空格，所以中文可以手动加空格也可以使用jieba自动分词
    :return:
    '''
    data = [
        '人生 苦短，我 喜欢 python',
        '人生 漫长，我 不喜欢 python'
    ]
    cv = CountVectorizer()
    cv_data = cv.fit_transform(data)
    print(cv.get_feature_names())
    print(cv_data.toarray())


if __name__ == "__main__":
    main()

