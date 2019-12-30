# -*- coding: utf-8 -*-
# @Date : 2019-12-30
# @Author : water
# @Version  : v1.0
# @Desc  : 类方法与实例方法的主要区别在于存在类变量的时候
#          修改类变量（ancient）的值时，子类对象通过实例方法访问的就是修改后的值，通过类方法访问的就是类的初始值；
#          父类通过类方法可以直接访问类变量初始值，无法通过实例方法访问ancient的值

class Person():
    ancient = "yuanren"

    def __init__(self, name, gender):
        self.gender = gender
        self.name = name

    @classmethod
    def print_ancient(cls):
        print(cls.ancient)

    def print_ancient2(self):
        print(self.ancient)


def main():
    p1 = Person("xiaoxin", 'man')
    p1.ancient = "xingxing"
    print(p1.ancient)  # xingxing
    p1.print_ancient()  # yuanren
    p1.print_ancient2()  # xingxing
    Person.print_ancient()  # yuanren
    Person.print_ancient2()  # 异常(Person没有self)


if __name__ == "__main__":
    main()
