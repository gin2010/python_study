# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
import time

def main():
    start_time = time.time()
    for a in range(1001):
        for b in range(1001):
            c = 1000 - a - b
            if a**2 + b**2 ==c**2:
                print("a,b,c:",(a,b,c))
    end_time = time.time()
    print('total time:',end_time-start_time)

if __name__ == "__main__":
    main()


