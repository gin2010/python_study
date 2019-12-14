# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :多进程之间的通信（queue），下面程序可能会出问题，
#           如果analysis_data调度的快，则可能在没下载完就结束了

import multiprocessing

def download_from_web(q):
    #模拟从网上下载数据
    data = [11,12,13,14]
    # 将数据写入队列中
    for d in data:
        q.put(d)
    print("下载数据完成！！")


def analysis_data(q):
    #数据处理
    anal_datas = list()
    while True:
        data = q.get()
        anal_datas.append(data)
        if q.empty():
            break
    print("数据处理成功：",anal_datas)


def main():
    q = multiprocessing.Queue()
    t1 = multiprocessing.Process(target=download_from_web,args=(q,))
    t2 = multiprocessing.Process(target=analysis_data,args=(q,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()