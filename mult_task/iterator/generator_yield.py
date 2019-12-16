# -*- coding: utf-8 -*-
# @Date : 2019-12-16
# @Author : water
# @Version  : v1.0
# @Desc  :


def fabi(num):
    a = 0
    b = 1
    index = 1
    while index <= num:
        yield a
        a, b = b, a + b
        index += 1
    return "okkkkkkkkk"

if __name__ =="__main__":
    # print(fabi(20))
    # for i in fabi(20):
    #     print(i)
    fa = fabi(15)
    while True:
        try:
            print(next(fa))
        except Exception as e:
            print(e.value)  # 打出return后面的值
            break


