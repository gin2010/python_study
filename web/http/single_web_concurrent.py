# -*- coding: utf-8 -*-
# File  : mult_web_thought.py
# Author: water
# Date  : 2019/12/22
# Desc  : 单进程、单线程实现并发
import socket
import time


##version 3.0
## 实现单进程、单线程并发服务器
def main():
    tcp_server_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_tcp.bind(("",7899))
    tcp_server_tcp.listen(128)
    tcp_server_tcp.setblocking(False) # 设置套接字为非堵塞的方式
    client_socket_list = list()
    while True:
        # 下面代码实现了只要有请求，就加入到服务列表中（client_socket_list），后面将为此客户端服务
        time.sleep(1)
        try:
            new_socket, new_addr = tcp_server_tcp.accept()
        except Exception as ret:
            print("------没有客户端的到来-------")
        else:
            print("------只要没有产生异常，就意味着有客户端的到来")
            client_socket_list.append(new_socket)

        # 下面这段代码实现为client_socket_list里的每个客户服务

        for client in client_socket_list:
            try:
                recv_data = client.recv(1024)
            except Exception as ret:
                print("-----客户端未发送数据过来----")
            else:
                if recv_data:
                    print("-----处理客户端发送来的数据---")
                else:
                    print("----没有数据返回，对方已关闭了连接----")
                    client_socket_list.remove(client)
                    client.close()



if __name__ == "__main__":
    main()