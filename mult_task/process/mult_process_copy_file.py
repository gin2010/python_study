# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :

import multiprocessing
import os


def copy_file(q,file,old_folder_name,new_folder_name):
    old_f = open(old_folder_name + "/"+ file,'rb')
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/"+ file,'rb')
    new_f.write(content)
    new_f.close()
    # 拷贝完成了就往队列中写入一个消息
    q.put(file)


def main():
    # 1.获取要复制的文件夹的名字
    old_folder_name = "test"
    # 2.创建一个新文件夹
    try:
        new_folder_name = old_folder_name + "——new"
        os.mkdir(new_folder_name)
    except :
        pass
    # 3.获取文件夹的所有的文件的名字
    file_names = os.listdir(old_folder_name)
    # 4.创建进程池
    po = multiprocessing.Pool(2)
    # 5.创建一个队列，控制什么时候操作完成
    q = multiprocessing.Manager().Queue()
    # 6.向进程池中添加copy文件
    for file in file_names:
        po.apply_async(copy_file,args=(q,file,old_folder_name,new_folder_name))
        print(file)
    po.close()
    # po.join()
    all_file_num =len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        print("\r拷贝的进度为：%.2f %%"%(copy_ok_num/all_file_num),end="")
        if copy_ok_num >= all_file_num:
            break
    print("--end--")



if __name__ == "__main__":
    main()
