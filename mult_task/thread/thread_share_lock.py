# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

import threading,time

sum = 0

def test1(num):
    global sum
    # mutex.acquire() #但这种方式无法两个线程同时进行
    for i in range(num):
        mutex.acquire() #这种方式会两个进程同步进行
        sum += 1
        mutex.release()
    # mutex.release()
    print("----test1----:",sum)

def test2(num):
    global sum
    # mutex.acquire()
    for i in range(num):
        mutex.acquire()  # 这种方式会两个进程同步进行
        sum += 1
        mutex.release()
    # mutex.release()
    print("----test2----:",sum)

mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("---main---:",sum)


if __name__ =="__main__":
    main()