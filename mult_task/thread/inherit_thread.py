# -*- coding: utf-8 -*-
# @Date : 2019-12-13
# @Author : water
# @Version  : v1.0
# @Desc  :

import threading,time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("i am " + self.name +"@" + str(i))

if __name__ == "__main__":
    t = MyThread()
    t.start()