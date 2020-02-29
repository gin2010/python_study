# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :1.__int__与__str__使用
#         2.迭代器与生成器
class Person(object):
    def __init__(self,name):
        self.name = name

    def __int__(self):
        return 1

    def __str__(self):
        return self.name


def main():
    p = Person('xiaoming')
    print(int(p))
    print(str(p))

class Mylist():

    def __init__(self,data):
        self.data = data
        self.index = len(data) #倒序输出

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

    def __call__(self, *args, **kwargs):
        print(self.data)


def main_mylist():
    mylist = Mylist('abcdef')
    mylist()
    for i in mylist:
        print(i)

if __name__ == "__main__":
    # main()
    main_mylist()
