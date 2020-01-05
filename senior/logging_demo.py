# -*- coding: utf-8 -*-
# File  : logging_demo.py
# Author: water
# Date  : 2020/1/5
# Desc  : 
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARN)
# 创建handler fh用于写入日志文件
logfile = "./log.txt"
fh = logging.FileHandler(logfile,mode='a') # a表示追回，w表示覆盖写入
fh.setLevel(logging.DEBUG)
# 创建handler ch用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARN)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 将logger添加到handler中
logger.addHandler(fh)
logger.addHandler(ch)

# logging.basicConfig(level=logging.WARN,
#                              filename="./log.txt",
#                              filemode="a",
#                              format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')


def main():
    logger.debug("this is a debug log")
    logger.info("this is a info log")
    logger.warning("this is a warn log")
    logger.error("this is a error log")
    logger.critical("this is a critical log")

if __name__ == "__main__":
    main()
