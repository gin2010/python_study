# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :自己实现list类型的迭代器
#       可迭代：只有__iter__函数
#       迭代器：可迭代 + __next__，可以用for来遍历
from collections import Iterable
from collections import Iterator

class MyList(object):

    def __init__(self):
        self.names = list()
        self.index = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.names):
            ret = self.names[self.index]
            self.index += 1
            return ret
        else:
            raise StopIteration


if __name__ == "__main__":
    mylist = MyList()
    mylist.add('a')
    mylist.add('b')
    mylist.add('c')
    for i in mylist:
        print(i)