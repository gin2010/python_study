# -*- coding: utf-8 -*-
# @Date : 2019-12-27
# @Author : water
# @Version  : v1.0
# @Desc  :

class Parent(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food,water):
        print("parent eat ",food)
        print("parent eat ",water)


class Child_LBJ(Parent):

    def __init__(self,name):
        super().__init__(name)

    def eat(self,food,water,milk):
        super().eat(food,water)
        print("child eat ", milk)
        super().eat(food,water)


def main():
    father = Parent("ligang")
    child = Child_LBJ('liyi')
    #father.eat("bread","coffee")
    child.eat("none",'water','a2')


if __name__ == "__main__":
    main()
