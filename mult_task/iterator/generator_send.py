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
        result = yield a
        print("----result----:",result)
        a, b = b, a + b
        index += 1
    return "okkkkkkkkk"

if __name__ =="__main__":
    # print(fabi(20))
    # for i in fabi(20):
    #     print(i)
    fa = fabi(15)
    print(next(fa))

    send_result = fa.send("hahaha") # 可以设置yield a 的结果
    # 但第一次直接用send会报异常，因为第一次不会执行将yield a值赋给result
    # 如果第一次要用send，则里面只能传None
    print(send_result)

