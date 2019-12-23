# -*- coding: utf-8 -*-
# File  : gil_demo.py
# Author: water
# Date  : 2019/12/22
# Desc  : gil 全局解释锁，只对多线程有作用。
#         由于C语言编译器历史遗留原因，导致多线程是假并行。
#         但由于gil存在，如果一个线程中间堵塞，则会切换到另一个线程，因此多线程应用于I/O操作时会提升效率（线程有延时）
#         如果是计算操作，只能用多进程提升效率，因为计算过程中不会停顿。


#使用python 调用C语言库
#1.先写好.c文件
#2.gcc XXXX.c -shared -o xxxx.so

from ctypes import *
from threading import Thread

# 加载C语言生成的动态库
lib = cdll.LoadLibrary("./libdeed_loop.so")

# 创建一个子线程
t = Thread(target=lib.DeadLoop)
t.start()

# 主线程
while True:
    pass