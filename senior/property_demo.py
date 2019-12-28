# -*- coding: utf-8 -*-
# File  : property_demo.py
# Author: water
# Date  : 2019/12/28
# Desc  : 使用了property属性进行装饰后，直接把方法当成属性来调用
class Page(object):

    def __init__(self,page):
        self.page = page
        # 每页显示的记录数
        self.per_item = 10


    @property
    def start(self):
        start_page = (self.page - 1) * self.per_item
        return start_page


    @property
    def end(self):
        end_page = (self.page ) * self.per_item
        return end_page


def main():
    p = Page(2)
    print(p.start)
    print(p.end)


if __name__ == "__main__":
    main()
