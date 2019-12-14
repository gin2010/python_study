# -*- coding: utf-8 -*-
# @Date : 2019-8-29
# @Author : water
# @Desc  :
# @Version  : v0.1


l = [
    [0,2,4,1,3,5],
    [0,2,4,1,3,5],
    [0,2,4,1,3,5],
    [0,2,4,1,3,5],
    [0,2,4,1,3,5],
    [0,2,4,1,3,5]]

for i in range(5):

    if l[0][i]<l[0][i+1]:
        e=l[0][i]
        l[0][i] =l[0][i+1]
        l[0][i+1] = e
        print("第{}次结果".format(i),l)
    if l[1][i]<l[1][i+1]:
        e=l[1][i]
        l[1][i] =l[1][i+1]
        l[1][i+1] = e
        print("第{}次结果".format(i),l)
    if l[2][i]<l[2][i+1]:
        e=l[2][i]
        l[2][i] =l[2][i+1]
        l[2][i+1] = e
        print("第{}次结果".format(i),l)
    if l[3][i]<l[3][i+1]:
        e=l[3][i]
        l[3][i] =l[3][i+1]
        l[3][i+1] = e
        print("第{}次结果".format(i),l)
    if l[4][i]<l[4][i+1]:
        e=l[4][i]
        l[4][i] =l[4][i+1]
        l[4][i+1] = e
        print("第{}次结果".format(i),l)