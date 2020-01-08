# -*- coding: utf-8 -*-
# File  : controller_method.py
# Author: water
# Date  : 2020/1/5
# Desc  : 控制器的两种实现思路
# 第一种使用装饰器来实现
ROUTE = dict()
def controller(url):
    def dict_func(func):
        ROUTE[url] = func
        def call_func():
            return func()
        return call_func
    return dict_func


@controller("/index.html")
def index():
    print("-----index------")

@controller("/home.html")
def home():
    print("------home------")

@controller("/title.html")
def title():
    print("-----title-----")

@controller("/user.html")
def user():
    print("------user------")


def main1():
    filepath = "/user.html"
    ROUTE[filepath]()


# 第二种使用类来实现
def controller(interface):
    if interface =="fpcx":
        class FPCX(object):
            def __init__(self):
                print('fpcx--class')
        return FPCX
    else:
        class SINGLE(object):
            def __init__(self):
                print('single --class')
        return SINGLE

def main2():
    new_class = controller("fpcx")
    # new_class = controller("12345")
    new_class()


# 第三种元类来实现(orm.py)




if __name__ == "__main__":
    main1()
    # main2()