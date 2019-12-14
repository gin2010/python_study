# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

import os,time,random
from multiprocessing import Pool

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号：%d"%(msg,os.getpid()))
    # getpid(): 返回当前进程的id
    # getppid(): 返回当前进程父进程的id
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))


if __name__ =="__main__":

    po = Pool(3)  #定义一个进程池，数据代表最大进程数
    for i in range(10):
        po.apply_async(worker,(i,))
        print("----------",i)
    print("-----start------")
    po.close()  #关闭进程池，关闭后不会再接收新的进程请求
    print("-----close------")
    po.join()  # join是加入到主进程，等待所有未执行的进程执行完毕后，主进程再关闭
    print("-------end----------")
