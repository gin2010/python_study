# -*- coding: utf-8 -*-
# File  : property_set.py
# Author: water
# Date  : 2019/12/28
# Desc  : 
class Good():
    def __init__(self):
        self.label_price = 100
        self.discount = 0.8

    @property
    def price(self):
        t_price = self.label_price * self.discount
        return t_price

    @price.setter
    def price(self,value):
        self.label_price = value

    @price.deleter
    def price(self):
        del self.label_price


    # 未用property只能这样来修改价格
    # def set_price(self,value):
    #     self.label_price = value


def main():
    g1 = Good()
    print(g1.price)
    # g1.set_price(200)
    g1.price = 300
    print(g1.price)
    del g1.price
    print(g1.price)


if __name__ == "__main__":
    main()
