# -*- coding: utf-8 -*-
# File  : content_demo.py
# Author: water
# Date  : 2019/12/28
# Desc  : content上下文管理器，必须用with才能关闭
from contextlib import contextmanager

# 第一种使用装饰器来实现上下文管理器
@contextmanager
def my_open(path,mode):
    f = open(path,mode)
    yield f
    f.close()  # 出现异常的时候会直接调用此方法


def main():
    with my_open("loop.c",'r') as f:
        data = f.read()
        print(data)

def wrong():
    with my_open("loop.c",'r') as f:
        data = f.read()
        raise ValueError
        print(data)

def write_wrong():
    with my_open("123.txt",'w') as f:
        f.write("123456")
        f.write("abcdeef")
        raise ValueError

# 使用魔法方法
class File(object):
    def __init__(self,file,mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        print("__exit___")
        self.f = open(self.file,self.mode)
        return self.f

    def __exit__(self, *args):
        print("__exit___")
        self.f.close()

def file_main():
    with File("22.txt",'w') as f :
        f.write("hello world")
        raise NameError

def demo_main():
    f = File('demo.txt','w')
    del f
if __name__ == "__main__":
    # main()
    # print("-"*10)
    # write_wrong() # 出现异常的时候只会调close()方法，保证之前的内容写到文件中
    # wrong() #读取的时候如果报异常会调用close()
    # file_main()
    demo_main()