# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

class Fiba(object):

    def __init__(self,total):
        self.total_index = total
        self.n0 = 0
        self.n1 = 1
        self.index = 0

    def __iter__(self):
        return self


    def __next__(self):
        if self.total_index > self.index:
            ret = self.n0
            self.n0,self.n1 = self.n1,self.n0 + self.n1
            self.index += 1
            return ret
        else:
            raise StopIteration


if __name__ =="__main__":
    fb = Fiba(10)
    for f in fb:
        print(f)
