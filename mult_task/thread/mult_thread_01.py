# -*- coding: utf-8 -*-
# @Date : 2019-12-13
# @Author : water
# @Version  : v1.0
# @Desc  :

import threading,time

def sing():
    for i in range(5):
        print("--------sing---------")
        time.sleep(1)

def dance():
    for i in range(5):
        print("*********dance*********")
        time.sleep(1)

def main():
    th1 = threading.Thread(target=sing)
    th2 = threading.Thread(target=dance)
    th1.start()
    th2.start()


if __name__ == "__main__":
    main()
