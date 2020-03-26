# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc:1.单例模式，创建的三个对象都指向同一个地址
#       2.__new__方法用法，不带参数
#       3.__new__方法用法，带参数

class Foo:  # 单例模式
    __single = None

    @classmethod
    def get_object(cls):
        if cls.__single == None:
            cls.__single = Foo()
            return cls.__single
        else:
            return cls.__single


def main1():
    f1 = Foo.get_object()
    print(f1)
    f2 = Foo.get_object()
    print(f2)

class Good(object):
    '''__new__方法'''
    # 如果没有return一个父类object的对象，g1就是None
    # def __new__(cls, *args, **kwargs):
    #     print('---new--')

    # 需要return一个父类的对象
    def __new__(cls, *args, **kwargs):
        print('---new--')
        instance = object.__new__(cls,*args,**kwargs)
        return instance

    def __init__(self):
        print('---init----')
        self.name = 'apple'

def main2():
    g1 = Good()
    print('g1',g1)


class Person(object):
    #需要return一个父类的对象--带参数
    def __new__(cls,name,age,*args, **kwargs):
        print("in __new__")
        # instance = object.__new__(cls,*args, **kwargs)
        # instance = super(Person,cls).__new__(cls,*args, **kwargs)
        instance = super().__new__(cls,*args, **kwargs)
        return instance

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age

def main3():
    p1 = Person("xiaoming",22)
    print(p1)



if __name__ == "__main__":
    # main1()
    # main2()
    # main3()
    main4()

