# -*- coding: utf-8 -*-
# File  : origin_class.py
# Author: water
# Date  : 2020/1/5
# Desc  : 元类与类的控制器
#第一种应用
Test = type("Test",(object,),{"name":'xiaoming',"age":22})

def main1():
    t1 = Test()
    print(t1.name)
    print(t1.age)

# 第二种应用
def upper_attr(class_name,class_parent,class_attr):
    new_attr = dict()
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    return type(class_name,class_parent,new_attr)


class Demo(object,metaclass=upper_attr):
    name = "xiaoming"
    address = "beijing"


def main2():
    d = Demo()
    # print(d.name) # 报错
    print(d.NAME)
    print(d.ADDRESS)


#第三种应用
class TypeClass(type):

    def __new__(cls, class_name,class_parent,class_attr):
        new_attr = dict()
        for name,value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value
        return type(class_name,class_parent,new_attr)


class Demo(object,metaclass=TypeClass):
    name = "xiaoming"
    address = "beijing"


def main3():
    d = Demo()
    # print(d.name) # 报错
    print(d.NAME)
    print(d.ADDRESS)

#第四种--手动创建类
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

def main4():
    new_class = controller("fpcx")
    # new_class = controller("12345")
    new_class()


if __name__ == "__main__":
    # main1()
    # main2()
    # main3()
    main4()