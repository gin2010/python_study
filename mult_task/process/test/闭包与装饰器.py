coding:utf-8
f = open('123.txt','r')
for l in f.readlines():
    print(l)
    print(f.tell())
    print("----------------------")


# 闭包

def f1(a,b):
    def f2(a,b):
        print(a+b)
    return f2(a,b)

f1(1,2)

##装饰器--不带参数
def add_dec(f):
    def ff():
        print("start")
        f()
        print("end!!!!")
    return ff


@add_dec
def add():
    print("now")

add()

##装饰器--带参数
def add_dec(f):
    def ff(a,b):
        print("start")
        f(a,b)
        print("end!!!!")
    return ff


@add_dec
def add(a,b):
    print(a+b)

add(22,33)