# -*- coding: utf-8 -*-
# @Date : 2019-12-27
# @Author : water
# @Version  : v1.0
# @Desc  :子类继承父类方法，并增加自己的功能
#        Python的类如果继承了多个类：深度优先与广度优先（python3)
#        下面的 GCHIL分别继承于Child_LBJ,Child_AD，如果GCHIL调用drink方法，
#       会按照继承的顺序，依次在Child_LBJ,Child_AD,Parent中查找
#

class Parent(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food,water):
        print("parent eat ",food)
        print("parent eat ",water)
        return "parent"

    def drink(self):
        print('drink a')

class Child_LBJ(Parent):

    def __init__(self,name):
        super().__init__(name)

    def eat(self,food,water,milk):
        super().eat(food,water)
        print("child eat ", milk)

    # def drink(self):
    #     print("drink lbj")


class Child_AD(Parent):

    def __init__(self, name):
        super().__init__(name)

    def eat(self, food, water, milk):
        super().eat(food, water)
        print("child eat ", milk)

    # def drink(self):
    #     print("drink ad")


class GCHILD(Child_LBJ,Child_AD):

    def __init__(self, name):
        super().__init__(name)

    def eat(self, food, water, milk):
        super().eat(food, water)
        print("child eat ", milk)

def main():
    father = Parent("ligang")
    child = Child_LBJ('liyi')
    #father.eat("bread","coffee")
    child.eat("none",'water','a2')

def main_inherit():
    #测试广度优先的继承
    gchile = GCHILD('dw')
    gchile.drink()


if __name__ == "__main__":
    # main()
    main_inherit()