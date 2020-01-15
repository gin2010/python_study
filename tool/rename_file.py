# -*- coding: utf-8 -*-
# @Date : 2020-01-15
# @Author : water
# @Version  : v1.0
# @Desc  :

import os,time

FILE_PATH = "F:\pic"


def time_to_string(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y%m%d', timeStruct)

# 获取文件时间
def get_file_time(file_path):
    # t = os.path.getctime(file_path) # 创建时间
    # t = os.path.getatime(file_path) # 访问时间
    t = os.path.getmtime(file_path) # 修改时间
    return time_to_string(t)

def main():
    files_list = os.listdir(FILE_PATH)
    for file in files_list:
        old_file = os.path.join(FILE_PATH,file)
        file_time = get_file_time(old_file)
        new_file = os.path.join(FILE_PATH,file_time + "_" + file)
        # print(old_file,file_time,new_file)
        os.rename(old_file, new_file)

if __name__ == "__main__":
    main()