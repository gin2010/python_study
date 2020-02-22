# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class KylinosPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=33306,  # 数据库端口
            db='scrapyData',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = """insert into kylinos (position,num,location,duty,request) value (%s,%s,%s,%s,%s)"""

        self.cursor.execute(sql,(item['position'],item['num'],item['location'],item['duty'],item['request']))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回

    def close(self):
        self.cursor.close()
        self.connect.close()