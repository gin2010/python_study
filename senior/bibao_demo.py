# -*- coding: utf-8 -*-
# File  : bibao_demo.py
# Author: water
# Date  : 2020/1/2
# Desc  : 闭包的实现
#         闭包的优势：函数的嵌套，且拥有可以传递数据，不同对象用同一个函数处理后的数据整理归类
#         使用闭包实现y=kx + b 值的计算
#

def f(k,b):
    def inner_f(x):
        return k*x+b
    return inner_f

def main():
    f1 = f(3,4)
    print(f1(4))
    print(f1(5))
    f2 = f(-2,4)
    print(f2(3))
    print(f2(0))


if __name__ == "__main__":
    main()
