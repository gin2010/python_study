# -*- coding: utf-8 -*-
# @Date : 2020-01-16
# @Author : water
# @Version  : v1.0
# @Desc  :

import os


class Mysql(object):

    def __init__(self):
        self.host = "127.0.0.1"

    def connect(self):
        self.db = 'mysql'
        print('connect--->',self.host)

    def insert(self):
        print('insert--->',self.db)
        self.data = "insert into db....."

    def close(self):
        print("-----close----")
        print(self.data)


def main():
    mysql = Mysql()
    mysql.connect()
    mysql.insert()
    mysql.close()


if __name__ == "__main__":
    main()
