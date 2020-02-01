# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
import pandas as pd
import numpy as np


def main():
    data = [
        {'name':'hocket','grade':'a,c,d'},
        {'name':'la','grade':'a,e,f'},
        {'name':'buck','grade':'b,c,g'},
        {'name':'76','grade':'d,e,f'},
        {'name':'thunder','grade':'c,e,g'},
        {'name':'bull','grade':'e,f,h'}
    ]

    data = pd.DataFrame(data)
    # print(data)
    grade_data = data['grade'].tolist()
    print(grade_data)
    grades = set()
    for i in grade_data:
        for j in i.split(","):
            grades.add(j)

    print(grades)
    grade_numpy = pd.DataFrame(np.zeros([data.shape[0],len(grades)]),columns=grades)
    print(grade_numpy)
    for i in range(data.shape[0]):
        grade_numpy.loc[i,grade_data[i].split(",")] =1

    print(grade_numpy)
    data1.merge(data2,left_on='a',right_on='b')


if __name__ == "__main__":
    main()

