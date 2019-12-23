# -*- coding: utf-8 -*-
# @Date : 2019-12-16
# @Author : water
# @Version  : v1.0
# @Desc  :使用greenlet

import time
from greenlet import greenlet

def task1():
    while True:
        print("---1---")
        gr2.switch()
        time.sleep(0.2)


def task2():
    while True:
        print("---2---")
        gr1.switch()
        time.sleep(0.2)


if __name__=="__main__":
    gr1 = greenlet(task1)
    gr2 = greenlet(task2)
    gr1.switch()



