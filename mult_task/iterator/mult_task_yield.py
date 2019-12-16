# -*- coding: utf-8 -*-
# @Date : 2019-12-16
# @Author : water
# @Version  : v1.0
# @Desc  :使用yield实现协程，并行

import time

def task1():
    while True:
        print("---1---")
        time.sleep(0.2)
        yield

def task2():
    while True:
        print("---2---")
        time.sleep(0.2)
        yield


def main():
    t1 = task1()
    t2 = task2()
    while True:
        next(t1)
        next(t2)


if __name__=="__main__":
    main()