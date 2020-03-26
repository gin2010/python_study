# -*- coding: utf-8 -*-
# File  : origin_class.py
# Author: water
# Date  : 2020/1/5
# Desc  : 元类与类的控制器
#       1.type创建类：type(类名，(父类,可为空)，{包含属性的字典})，无法实现创建时初始化时传入值
#       2.metaclass元类为函数:
#           class Demo(object,metaclass=upper_attr)
#           编译器解析到类的名字、父类名、属性组成 ==> (class_name,parent_class,attr)，传入到元类的__new__中，
#           因此从上到下执行upper_attr方法中语句，最后type(class_name,parent_class,new_attr)创建类，
#           如果metaclass后面指定为一个函数，也会将(class_name,parent_class,attr)变量传入到这个函数中，
#       3.metaclass元类为类:实现__new__方法
#       4.一种控制器的实现

# 第一：
Test1 = type("Test1",(object,),{"name":'xiaoming',"age":22})
def eat(self):
    print("eat----")
Test2 = type("Test2",(object,),{"name":"xiaobai","age":0,"eat":eat})
# Test3 = type("Test3",(object,),dict(name=name))

def main1():
    t1 = Test1()
    print(t1.name)
    print(t1.age)
    t2 = Test2()
    t2.eat()
    # t3 = Test3('xiaobai') #type无法实现

# 第二：
def upper_attr(class_name,class_parent,class_attr):
    new_attr = dict()
    print('class_attr--->',class_attr)
    # {'__module__': '__main__', '__qualname__': 'Demo', 'name': 'xiaoming'}
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    return type(class_name,class_parent,new_attr) #最终返回一个type类对象即可


class Demo(object,metaclass=upper_attr):
    name = "xiaoming"

def main2():
    d = Demo()
    # print(d.name) # 报错
    print(d.NAME)
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

def main3():
    d = Demo()
    # print(d.name) # 报错
    print(d.NAME)


#第四--控制器的实现
def controller(interface):
    if interface =="fpcx":
        class FPCX(object):
            def __init__(self):
                print('fpcx--class')
            def eat(self):
                print("---eat---")
        return FPCX()
    else:
        class SINGLE(object):
            def __init__(self):
                print('single --class')
        return SINGLE

def main4():
    new_class = controller("fpcx")
    print(new_class)
    new_class.eat()


if __name__ == "__main__":
    # main1()
    # main2()
    # main3()
    main4()