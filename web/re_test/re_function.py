# -*- coding: utf-8 -*-
# File  : re_function.py
# Author: water
# Date  : 2019/12/15
import re


def main():
    # re.match() 从头开始匹配
    # re.search() 从中间开始匹配，如果匹配上则停止
    # re.findall()  匹配全部的字符，并返回匹配到的列表
    # re.sub() 匹配全部字符，并将匹配到的字符替换为另一个字符串，然后返回替换后的全部字符串
    # re.split() 切割字符串

    # print(re.match("速度与激情[\w]", '速度与激情1').group())
    # print(re.match("速度与激情[\w]", '1速度与激情1').group())
    # print(re.search("速度与激情[\w]", '1速度与激情1,2速度与激情2').group())
    # print(re.findall("速度与激情[\w]", '1速度与激情1,2速度与激情2'))
    # print(re.sub("速度与激情","passion",'1速度与激情1,2速度与激情2'))

    # add_one = lambda x: str(int(x.group()) + 100) # 匹配到了数字加100
    # print(re.sub("\d+",add_one,"python11"))

    # print(re.split(r" |:","name:xiaoming age:22 shangdong"))


if __name__ == "__main__":
    main()