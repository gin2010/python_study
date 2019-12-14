# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

import threading,time

sum = 0

def test1(num):
    global sum
    for i in range(num):
        sum += 1
    print("----test1----:",sum)

def test2(num):
    global sum
    for i in range(num):
        sum += 1
    print("----test2----:",sum)


def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print("---main---:",sum)


if __name__ =="__main__":
    main()