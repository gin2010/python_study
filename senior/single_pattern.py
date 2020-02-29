# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :单例模式，创建的三个对象都指向同一个地址


class Foo:  # 单例模式
    __v=None

    @classmethod
    def ge_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

def main():
    obj1 = Foo.ge_instance()
    print(obj1)
    obj2 = Foo.ge_instance()
    print(obj2)
    obj3 = Foo.ge_instance()
    print(obj3)


if __name__ == "__main__":
    main()

