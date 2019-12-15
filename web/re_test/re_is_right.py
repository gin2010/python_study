# -*- coding: utf-8 -*-
# File  : re_is_right.py
# Author: water
# Date  : 2019/12/15
import re


def main():
    # 最后三个变量名是不正确的
    names = ['age','_age','1age','a_age','age_1_','age1','age!','a#123']

    for name in names:
        ret = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*$',name)
        if ret:
            print("attr [%s] is right:"%(name))
        else:
            print("attr [%s] is wrong:"%(name))




if __name__ == "__main__":
    main()