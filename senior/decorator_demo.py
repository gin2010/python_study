# -*- coding: utf-8 -*-
# File  : decorator_demo.py
# Author: water
# Date  : 2020/1/2
# Desc  : 装饰器的实现与应用
# 应用于在原函数前后增加新功能，如日志功能等
# 使用add_func(*args,**kwargs)这种定义类型，可以兼容全部类型

def func(demo):
    def add_func(*args,**kwargs):
        print("-------before-------")
        demo(*args,**kwargs)
        print("-------after-------")
    return add_func

@func
def test():
    print("------test------")

@func
def my_sum(a,*args,**kwargs):
    print("------a--:",a)
    print("------args--:" ,args)
    print("------kwargs--:", kwargs)


def main1():
    test()
    my_sum(100,200,300,mm=111)


def add_h1(func):
    def h1():
        print("-------add h1------")
        return "<h1>" + func() +"</h1>"
    return h1

def add_body(func):
    def body():
        print("-------add body-----")
        return "<body>" + func() +"</body>"
    return body

@add_body
@add_h1
def data():
    print("-------data-------")
    return "hello world"

def main2():
    print(data())


if __name__ == "__main__":
    # main1() # 装饰器应用
    main2() # 多个装饰器顺序
