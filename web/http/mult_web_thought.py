# -*- coding: utf-8 -*-
# File  : mult_web_thought.py
# Author: water
# Date  : 2019/12/22
# Desc  : 如何使用单线程实现处理多个客户端请求的思路（并发），代码无法运行
import socket

##version 3.0
## 实现单进程、单线程并发服务器
client_socket_list = list()
while True:
    # 下面代码实现了只要有请求，就加入到服务列表中（client_socket_list），后面将为此客户端服务
    #
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


##version 2.0
client_socket_list = list()
while True:
    # 下面代码实现了只要有请求，就加入到服务列表中（client_socket_list），后面将为此客户端服务
    try:
        new_socket,new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print("------没有客户端的到来-------")
    else:
        print("------只要没有产生异常，就意味着有客户端的到来")
        client_socket_list.append(new_socket)

    # 下面这段代码实现为client_socket_list里的每个客户服务
    # 但是在下面这段代码里，可能有些client已经服务完，关闭连接了，但是还存在client_socket_list中
    # 这样会造成client_socket_list越来越大
    for client in client_socket_list:
        try:
            client.recv()
        except Exception as ret:
            print("-----客户端未发送数据过来----")
        else:
            print("-----处理客户端发送来的数据---")


# version 1.0
# 设置套接字为非堵塞状态，可以为多个客户端来服务
# 但是下面这种方式会出现问题
tcp_server_tcp.setblocking(False) # 设置套接字为非堵塞的方式
while True:
    try:
        new_socket,new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print("------没有客户端的到来-------")
    else:
        print("------只要没有产生异常，就意味着有客户端的到来")
        try:
            new_socket.recv()
            # 此时有客户端连接，但是如果客户第一次没有发送消息，由又会执行一次while True
            # 这时又会等待新的客户端连接，第一次连接上来的客户端就会在一直在堵塞（recv()）
            # 因此使用上面的version 2.0来解决这个问题
        except Exception as ret:
            print("-----客户端未发送数据过来----")
        else:
            print("-----处理客户端发送来的数据---")




if __name__ == "__main__":
    main()