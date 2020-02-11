# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
import pandas as pd
import os


filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data','2019_nCoV_data.csv')

def knn():
    datas = pd.read_csv(filepath)
    print(datas.head(10))


def main():
    knn()


if __name__ == "__main__":
    main()

