# -*- coding: utf-8 -*-
# File  : re_is_email.py
# Author: water
# Date  : 2019/12/15
import re


def main():
    email = input("163.com 的email:")
    ret = re.match(r'[0-9a-zA-Z]{4,20}@163\.com$',email)
    # r'[0-9a-zA-Z]{4,20}@163.com$' 会将laowang@1633com匹配通过
    # 此时需要将.转义为实际只匹配.  ，而不是作为匹配任意字符
    if ret:
        print("email:{} is right.".format(email))
    else:
        print('email:{} is wrong'.format(email))

if __name__ == "__main__":
    while True:
        main()
