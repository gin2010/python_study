# -*- coding: utf-8 -*-
# File  : property_use.py
# Author: water
# Date  : 2019/12/28
# Desc  : 修改私有变量的值，保护、隐藏私有变量

# 第一种实现方法
class Money1():
    def __init__(self,money):
        self.__money = money


    def get_money(self):
        return self.__money

    def set_money(self,money):
        self.__money = money

    my_money = property(get_money,set_money)


# 第二种
class Money2():
    def __init__(self,money):
        self.__money = money

    @property
    def get_money(self):
        return self.__money


    @get_money.setter
    def set_money(self,money):
        self.__money = money


def main():
    # 第一种
    # m = Money1(100)
    # print(m.my_money)
    # m.my_money = 200
    # print(m.my_money)
    # 第二种
    m = Money2(100)
    print(m.get_money)
    m.set_money = 200
    print(m.get_money)


if __name__ == "__main__":
    main()
