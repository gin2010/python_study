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


# 第二种实现
def upper_attr(class_name,class_parent,class_attr):
    new_attr = dict()
    print('class_attr--->',class_attr)
    # {'__module__': '__main__', '__qualname__': 'Demo', 'name': 'xiaoming', 'address': 'beijing'}
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    return type(class_name,class_parent,new_attr) #最终返回一个type类对象即可


class Demo(object,metaclass=upper_attr):
    '''编辑器解析到Demo()类的时候，就会将类的名字、父类名、属性组成 ==> (class_name,parent_class,attr)，
    传入指定的type(class_name,parent_class,attr)创建类，相当于先调用类里面的__new__方法，而不是在d=Demo()的时候才开始new。
    如果metaclass后面指定为一个函数，也会将(class_name,parent_class,attr)变量传入到这个函数中
    '''
    name = "xiaoming"
    address = "beijing"


def main2():
    d = Demo()
    # print(d.name) # 报错
    print(d.NAME)
    print(d.ADDRESS)
    print(Demo.__qualname__) # 显示类或类里面函数名称、所在的类、模块等梯级地址


#第三种实现
class TypeClass(type):

    def __new__(cls, class_name,class_parent,class_attr):
        new_attr = dict()
        print("3class_arrt--->",class_attr)
        for name,value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value
        # return type(class_name,class_parent,new_attr)
        # return type.__new__(cls,class_name,class_parent,new_attr) # oop思想
        return super(TypeClass,cls).__new__(cls,class_name,class_parent,new_attr) # oop思想


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
    main3()
    # main4()