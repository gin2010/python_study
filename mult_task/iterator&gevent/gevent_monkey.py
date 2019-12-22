# -*- coding: utf-8 -*-
# @Date : 2019-12-16
# @Author : water
# @Version  : v1.0
# @Desc  :

import gevent,time
from gevent import monkey


monkey.patch_all() # 将time.sleep换成gevent.sleep
def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5) # 必须用此延时函数才会并发执行


if __name__ == "__main__":
    # print("----1-----")
    # g1 = gevent.spawn(f,5)
    # print("----2-----")
    # g2 = gevent.spawn(f,6)
    # print("----3-----")
    # g3 = gevent.spawn(f,7)
    # print("----end-----")
    gevent.joinall([
        gevent.spawn(f, 5),
        gevent.spawn(f, 6),
        gevent.spawn(f, 7)
    ])
