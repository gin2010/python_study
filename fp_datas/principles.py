# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : 定义规则类



class KPLX():

    def __init__(self):
        self.blue = 0
        self.red = 1
        self.invalid = 2

class FPZL():

    def __init(self):
        self.ptdz = 0
        self.zp = 1
        self.pt = 2
        self.jp = 3

class SL():

    def __init(self):
        self.sl0 = 0
        self.sl1 = 0.01
        self.sl3 = 0.03
        self.sl6 = 0.06
        self.sl9 = 0.09

class SPBM():

    def __init__(self):
        self.sp0 = ['10601','10602']
        self.sp1 = ['10501','10502']
        self.sp3 = ['10401','10402']


class Principles(object):

    def __init__(self,case):
        self.case = case  # case为dict类型

    def get_rigth(self,case):
        return True

    def get_wrong(self,case):
        return False

    def sp_sl_principle(self,sp1,sl1):
        for sp1 in self.sp1:
            return True
        else:
            return False


def main():
    pass


if __name__ == "__main__":
    main()

