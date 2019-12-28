# -*- coding: utf-8 -*-
# File  : property_function.py
# Author: water
# Date  : 2019/12/28
# Desc  : 

class Foo():
    def __init__(self,name):
        self.name = name


    def get_bar(self):
        return self.name


    def set_bar(self,name):
        self.name = name


    def del_bar(self):
        del self.name


    BAR = property(get_bar,set_bar,del_bar)


def main():
    f = Foo("xiaoxin")
    print(f.BAR)
    f.BAR = "xiaobai"
    print(f.BAR)
    del f.BAR
    print(f.BAR)


if __name__ == "__main__":
    main()
