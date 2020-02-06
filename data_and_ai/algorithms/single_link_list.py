# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  : 实现单向链表

class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self,node=None):
        self._head = node

    def length(self):
        cur = self._head
        index = 0
        while cur != None:
            index += 1
            cur = cur.next
        return index

    def is_empty(self):
        return self._head == None

    def travel(self):
        # 打印出全部元素
        if self.is_empty():
            print("空")
        else:
            cur = self._head
            while cur != None:
                print(cur.elem,end=',')
                cur = cur.next

    def append(self,item):
        # 在尾部插入元素
        node = Node(item)
        if self.is_empty():
            # 首次增加元素时
            self._head = node
        else:
            # 非首次
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self,item):
        # 在头部插入元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next,self._head = self._head,node

    def insert(self,pos,item):
        # 在特定的位置pos插入item
        node = Node(item)
        cur = self._head
        index = 1
        while pos > index:
            cur = cur.next
            index += 1
        cur.next,node.next = node,cur.next

    def remove(self,item):
        if self.is_empty():
            print("列表为空，错误")
        elif self._head.elem == item:
            # 第一个元素是item
            self._head = self._head.next
        else:
            cur = self._head
            while True:
                if cur.next.elem == item:
                    cur.next = cur.next.next
                    break
                cur = cur.next

    def search(self,item):
        index = 0
        if self.is_empty():
            print("列表为空，错误")
        else:
            cur = self._head
            while True:
                if cur.elem == item:
                    return index
                index += 1
                cur = cur.next

def main():
    sl = SingleLinkList()
    # print(sl.is_empty())
    # print(sl.length())
    # print(sl.travel())
    sl.append("a")
    sl.append("b")
    sl.append("c")
    print(sl.length())
    sl.travel()
    print("")
    sl.add("1")
    sl.add(2)
    sl.travel()
    print("")
    sl.insert(2,'aa')
    print(sl.length())
    sl.travel()
    print("")
    sl.remove('aa')
    sl.travel()
    print("")
    print(sl.search('c'))


if __name__ == "__main__":
    main()

