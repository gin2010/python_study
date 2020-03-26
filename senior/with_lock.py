# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version : v1.0
# @Desc : with metux:  的用法
import threading
import time

# 未加锁
class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance

    # 定义一个函数来模拟取钱操作
    def draw(self, draw_amount):
        # 账户余额大于取钱数目
        if self.balance >= draw_amount:
            # 吐出钞票
            print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
            time.sleep(1)
            # 修改余额
            self.balance -= draw_amount
            print("\t余额为: " + str(self.balance))
        else:
            print(threading.current_thread().name + "取钱失败！余额不足！")

def no_lock():
    # 创建一个账户
    acct = Account("1234567", 1000)
    # 模拟两个线程对同一个账户取钱
    threading.Thread(name='甲', target=acct.draw, args=(800,)).start()
    threading.Thread(name='乙', target=acct.draw, args=(800,)).start()

class AccountLock:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()
    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法

    def getBalance(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        with self.lock: #相当于下面两条语句
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(1)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")

        

def have_lock():
    # 创建一个账户
    acct = AccountLock("1234567", 1000)
    # 模拟两个线程对同一个账户取钱
    threading.Thread(name='甲', target=acct.draw, args=(800,)).start()
    threading.Thread(name='乙', target=acct.draw, args=(800,)).start()

def main():
    # no_lock()
    have_lock()

if __name__ == "__main__":
    main()

