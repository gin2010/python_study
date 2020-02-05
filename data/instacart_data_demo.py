# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : https://www.kaggle.com/psparks/instacart-market-basket-analysis#products.csv
# products.csv:product_id,product_name,aisle_id,department_id
# orders.csv:order_id,user_id,eval_set,order_number,order_dow,order_hour_of_day,days_since_prior_order
# aisles.csv:aisle_id,aisle
# o_p_p.csv:order_id,product_id,add_to_cart_order,reordered
# o_p_p.csv的order_id,product_id 分别与orders.csv的order_id、products.csv的product_id连接
# products.csv的aisle_id与aisles.csv的aisle_id连接
# 这个只是对数据进行降维处理，并未进行分析

import pandas as pd
from sklearn.decomposition import PCA



def main():
    # 读取四张表中的数据
    products = pd.read_csv("./data/products.csv")
    products.head(5)
    aisles = pd.read_csv('./data/aisles.csv')
    aisles.head(5)
    orders = pd.read_csv('./data/orders.csv')
    orders.head(4)
    opps = pd.read_csv("./data/order_products__prior.csv")
    opps.head(10)
    # 合并四张表数据
    _mg1 = pd.merge(opps, orders, on=['order_id', 'order_id'])
    _mg2 = pd.merge(products, aisles, on=['aisle_id', 'aisle_id'])
    mg = pd.merge(_mg1, _mg2, on=['product_id', 'product_id'])
    mg.head(10)
    mg.columns
    # 创建交叉表(行为user_id,列(特征)为aisle）
    cross = pd.crosstab(mg['user_id'], mg['aisle'])
    cross.head(10)
    pca = PCA(n_components=0.9)
    datas = pca.fit_transform(cross)
    datas[:10] # 为numpy.ndarray


if __name__ == "__main__":
    main()

