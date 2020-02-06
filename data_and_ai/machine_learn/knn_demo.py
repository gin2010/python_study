# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : K-近邻算法
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV

def main():

    # 1 读取数据
    '''
    数据集：https://www.kaggle.com/c/facebook-v-predicting-check-ins/data
    数据集背景：您将根据用户的位置，准确性和时间戳预测用户正在检查的业务
    '''

    data = pd.read_csv("./data/train.csv")

    # 2 处理数据
    # 2.1 缩小数据查询数据的范围
    '''
    减少数据量
    '''
    data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 2.2 处理数据时间
    '''
    脏数据：数据集时间戳只有时间没有年月日
    data.loc[:, 'day'] = time_value.day
    data.loc[:, 'weekday'] = time_value.weekday
    pandas axis 1：列
    '''

    time_value = pd.to_datetime(data['time'], unit='s')
    time_value = pd.DatetimeIndex(time_value)
    data.loc[:, 'hour'] = time_value.hour
    data = data.drop(['time'], axis=1)

    # 2.3 把签到数量少于n个目标位置删除
    '''
    脏数据：数据集登记位置数少的数据造成特征异常
    '''
    place_count = data.groupby('place_id').count()
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    # 2.4 清理无效特征
    data = data.drop(['row_id'], axis=1)
    data = data.drop(['accuracy'], axis=1)

    # 3 训练集与测试集分离
    y = data['place_id']
    x = data.drop(['place_id'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 4 特征工程
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.fit_transform(x_test)

    # 5 算法
    '''
    算法思想：求特征间距离（欧式距离），目标特征间距离与训练集特征间距离最近的样本分类倾向性更强
    数学原理：欧式距离 = (（x1 - x2）^ + (x2 - x3)^ + ...)平方根
    knn = KNeighborsClassifier(n_neighbors=10)
    knn.fit(x_train, y_train)
    y_predict = knn.predict(x_test)
    print("预测测试集：", y_predict)
    print("预测评估：", knn.score(x_test, y_test))
    '''
    knn = KNeighborsClassifier()

    # 6 模型评估
    '''
    验证核心思想：交叉验证 + 网格搜索
    交叉验证：数据集 = 训练集（训练集 + 验证集） + 测试集，训练集与验证按比例（通用标准0.25）交替拆分，并求出验证
        每次的平均值做为最终的准确率，通常为10折交叉（10等份）
    网格搜索：组合超参数搜索评估最佳超参数配置
    cv:交叉验证折数
    '''
    param = {"n_neighbors": [10, 12, 13, 15, 17, 19, 21, 23, 25, 27, 29]}
    gc = GridSearchCV(knn, param_grid=param, cv=2)
    gc.fit(x_train, y_train)

    print("测试集上准确率:", gc.score(x_test, y_test))
    print("在交叉验证中最好的结果：", gc.best_score_)
    print("选择最好的模型：", gc.best_estimator_)
    print("每个超参数每次交叉验证的结果:", gc.cv_results_)


if __name__ == "__main__":
    main()

