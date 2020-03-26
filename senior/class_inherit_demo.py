# -*- coding: utf-8 -*-
# @Date : 2019-12-27
# @Author : water
# @Version  : v1.0
# @Desc:1.继承顺序与多态：
#       2.Python的类如果继承了多个类：深度优先与 广度优先（python3是广度优先)
#          下面的 GCHIL分别继承于Child_LBJ,Child_AD，如果GCHIL调用drink方法，
#          会按照继承的顺序，依次在Child_LBJ,Child_AD,Parent中查找
#       3.广度优先继承的应用
#       4.继承父类方法来实现装饰器功能
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

#2.继承的顺序
def main_inherit():
    #测试广度优先的继承
    gchile = GCHILD('dw')
    gchile.drink()

# 3.广度优先继承应用：
# 因为是广度优先的继承顺序，所以先在Tiger类中找eat方法，然后Zoo中找到eat，
# 又需要调用父亲的eat方法，继续向上查找Animal类的eat，找到之后直接返回。整个过程不需要调object类方法
class Animal(object):
    '''eat相当于某个框架的内置函数'''
    @staticmethod
    def eat():
        return 'eat - food'


class Zoo(object):
    '''自定义一个类对内置eat函数进行装饰'''
    @classmethod
    def eat(cls):
        food = super(Zoo,cls).eat()
        # 对 eat的返回值food进行装饰
        food = "food+ " + food
        return food


class Tiger(Zoo,Animal):
    '''使用装饰后的eat函数'''
    pass


def main3():
    print(Tiger.eat())  # --> food+ eat - food


# 4.继承实现装饰器功能
class Animal(object):
    '''eat相当于某个框架的内置函数'''
    def eat(self):
        return 'eat - food'

class Tiger(Animal):
    pass


class Lion(Animal):

    def eat(self):
        print('before lion')
        # res = Animal.eat()
        # res = super().eat()
        res = super(Lion,self).eat()
        print('after lion')
        return res


def main4():
    t = Tiger()
    print(t.eat())
    l = Lion()
    print(l.eat())



if __name__ == "__main__":
    # main()
    # main_inherit()
    # main3()
    main4()



