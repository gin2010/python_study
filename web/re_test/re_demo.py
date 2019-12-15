# -*- coding: utf-8 -*-
# File  : re_demo.py
# Author: water
# Date  : 2019/12/15

import re

# s1 = "hello world"
# print(re.match('hello',s1)) #如果有返回值则表明查找到
# s2 = "Hello world"
# print(re.match('[hH]ello',s2))

# 匹配单个字符
## 单个数字：\d 或[0123] 或 [1-8]
# print(re.match("速度与激情\d",'速度与激情3').group())
# print(re.match("速度与激情[123]",'速度与激情3').group())
# print(re.match("速度与激情[123]",'速度与激情4').group())
# print(re.match("速度与激情[1-36-8]",'速度与激情4').group())
# print(re.match("速度与激情[1-36-8]",'速度与激情7').group())

## 单个字母：[a-z]或[abcd]或[A-Z]
# print(re.match("速度与激情[abcd]",'速度与激情b').group())
# print(re.match("速度与激情[a-d]",'速度与激情b').group())
# print(re.match("速度与激情[A-Z]",'速度与激情A').group())

## 单个字符：\w 字母与数字、汉字也支持（除了特殊符号不支持）
# print(re.match("速度与激情[\w]",'速度与激情1').group())
# print(re.match("速度与激情[\w]",'速度与激情一').group())

# 空白字符：\s
# print(re.match("速度与激情[\s]",'速度与激情 ').group())

# 匹配多个字符
# {1,3} 前面的出现1到3次
# print(re.match("速度与激情\d{1,3}",'速度与激情71').group())
# print(re.match("\d{11}",'1234567890').group()) #手机号为11位
# print(re.match("\d{11}",'1234567890').group()) #手机号为11位

# # ？：前面出现一次或0次
# print(re.match("021-\d{8}",'021-12345678').group()) #
# print(re.match("021-?\d{8}",'021-12345678').group()) #可以有- ，也可以没有
# print(re.match("021-?\d{8}",'02112345678').group()) #可以有- ，也可以没有
# print(re.match("\d{3,4}-?\d{7,8}",'0531-1234567').group()) #匹配全国电话
# print(re.match("\d{3,4}-?\d{7,8}",'0531-12314567').group()) #匹配全国电话
# *：前面出现0次或一次或多次
# +：前面出现一次或多次
# .：匹配任意字符（除了换行\n）
# content = """abcd
#             efb
#             hijkdl
#             mlopeaz"""
#
# print(re.match(".*",content).group())  # 只能匹配到abcd
# print(re.match(".*", content, re.S).group())  # 能匹配到全部内容
# ^：匹配开头
# $：匹配结尾
# | 的作用相当于或，但是必须配合括号使用，指定范围。
# () 的作用用于分组，并且可以对数据进行分组，可以单独取出括号里的值
# () 还可以用于控制后面匹配的字符与前面一样
# html1 = "<h1>123abc</h1>"
# html2 = "<h1>123abc</h2>"
# print(re.match(r"<\w+>.*</\w+>$", html1))
# print(re.match(r"<\w+>.*</\w+>$", html2))  # 也会匹配到
# print(re.match(r"<(\w+)>.*</\1>$", html2))  # 不会匹配到，后面用  \1  来取()里的值
# html3 = "<body><h1>123abc</h1></body>"
# html4 = "<body><h1>123abc</h2></body>"
# print(re.match(r"<(\w+)><(\w+)>.*</\2></\1>$", html3))
# print(re.match(r"<(\w+)><(\w+)>.*</\2></\1>$", html4))
# # ()里分组可以指定分组的名字：
# # ()里使用  ?P<name> 来定义此分组的名字
# # ()里使用  ?P=name 来使用此分组变量的值
# print(re.match(r"<(?P<body>\w+)><(?P<h1>\w+)>.*</(?P=h1)></(?P=body)>$", html3))
