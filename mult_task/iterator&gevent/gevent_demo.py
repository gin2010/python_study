# -*- coding: utf-8 -*-
# @Date : 2019-12-16
# @Author : water
# @Version  : v1.0
# @Desc  :

import gevent,time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0.5) # 必须用此延时函数才会并发执行


if __name__ == "__main__":
    print("----1-----")
    g1 = gevent.spawn(f,5)
    print("----2-----")
    g2 = gevent.spawn(f,6)
    print("----3-----")
    g3 = gevent.spawn(f,7)
    print("----end-----")
    g1.join()
    g2.join()
    g3.join()

