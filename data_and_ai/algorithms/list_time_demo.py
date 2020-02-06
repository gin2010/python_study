# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
from timeit import Timer

def t1():
    l1 = []
    for i in range(10000):
        l1.append(i)

def t2():
    l2 = []
    for i in range(10000):
        l2 += [i]

def t3():
    l3 = [i for i in range(10000)]

def t4():
    l4 = list(range(10000))

def t5():
    l5 = []
    for i in range(10000):
        l5.extend([i])

def main():
    timer1 =Timer("t1()","from __main__ import t1")
    print("t1:",timer1.timeit(100))

    timer2 =Timer("t2()","from __main__ import t2")
    print("t2:",timer2.timeit(100))

    timer3 =Timer("t3()","from __main__ import t3")
    print("t3:",timer3.timeit(100))

    timer4 =Timer("t4()","from __main__ import t4")
    print("t4:",timer4.timeit(100))

    timer5 =Timer("t5()","from __main__ import t5")
    print("t5:",timer5.timeit(100))


if __name__ == "__main__":
    main()

