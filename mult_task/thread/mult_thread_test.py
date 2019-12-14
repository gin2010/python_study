# -*- coding: utf-8 -*-
# @Date : 2019-12-13
# @Author : water
# @Version  : v1.0
# @Desc  :验证线程是在start之后才开始创建

import threading
import time


import threading,time

def sing():
    print("--------sing---------")



def main():
    print("Thread before:",threading.enumerate())
    th1 = threading.Thread(target=sing)
    print("Thread after:",threading.enumerate())
    th1.start()
    print("start after:",threading.enumerate())


if __name__ == "__main__":
    main()
