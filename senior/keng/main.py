# -*- coding: utf-8 -*-
# File  : main.py
# Author: water
# Date  : 2019/12/28
# Desc  : 
from handle import modify_flag
#这种方式导入的只是FLAG变量，FLAG指向的是common里FLAG值的内存地址，在其他模块FLAG=True只会将值的指向变为True的内存地址
# from common import FLAG
import common

def my_main():
    modify_flag()
    # print("main:",FLAG)
    print("main:",common.FLAG)

if __name__ == "__main__":
    my_main()

