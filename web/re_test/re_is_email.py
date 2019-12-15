# -*- coding: utf-8 -*-
# File  : re_is_email.py
# Author: water
# Date  : 2019/12/15
import re

# | 的作用相当于或，但是必须配合括号使用，指定范围。
# () 的作用用于分组，并且可以对数据进行分组，可以单独取出括号里的值
def main():
    email = input("163.com 的email:")
    ret = re.match(r'[0-9a-zA-Z]{4,20}@(163|126)\.com$',email)

    if ret:
        print("email:{} is right.".format(email))
        print(ret.group()) # 与group(0)结果一样
        print(ret.group(1))

    else:
        print('email:{} is wrong'.format(email))

if __name__ == "__main__":
    main()
