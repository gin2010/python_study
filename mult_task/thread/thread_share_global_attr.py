# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

import threading,time

num =10

def test1():
    global num
    num = num + 1
    print("-----1-----:",num)


def test2():
    print("----2----:",num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()

    t2.start()
    print("----main----:",num)

if __name__ == "__main__":
    main()