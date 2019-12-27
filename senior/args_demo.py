# -*- coding: utf-8 -*-
# @Date : 2019-12-27
# @Author : water
# @Version  : v1.0
# @Desc  :

def test2(a, b, *args, **kwargs):
    print("--------test2---------")
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a,b,*args,**kwargs)

def main():
    test1(10,11,12,13,name="xiaoxin")


if __name__ == "__main__":
    main()