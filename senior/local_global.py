# -*- coding: utf-8 -*-
# File  : local_global.py
# Author: water
# Date  : 2019/12/28
# Desc  : 

a = 100

def f():
    print(a)


def g():
    a =200
    print(a)


def main():
    print(a)
    f()
    g()
    print(a)


if __name__ == "__main__":
    main()
