# -*- coding: utf-8 -*-
# File  : decorator_realise_case.py
# Author: water
# Date  : 2020/1/2
# Desc  : 实现switch-case，根据传过来的路径自动调用对的函数
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



def main():
    filepath = "/user.html"
    ROUTE[filepath]()


if __name__ == "__main__":
    main()
