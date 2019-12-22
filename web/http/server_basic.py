# -*- coding: utf-8 -*-
# File  : server_basic.py
# Author: water
# Date  : 2019/12/15
import socket


def service_client(new_socket):
    # 1.接收浏览器发来的请求内容
    request = new_socket.recv(1024)
    print('----client:',request)
    # 2.组装返回数据
    response = "HTTP /1.1 200 OK \r\n\r\n"
    response += "<h1>service is ok</h1>"
    # 3.发送数据给客户
    new_socket.send(response.encode('utf-8'))
    # 4.关闭套接字
    new_socket.close()


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 使用下面这个参数后，bind操作是可以重复使用local address的
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 2.绑定ip
    tcp_server_socket.bind(("",7890))
    # 3.监听端口--里面的数量表示socket排队的个数
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户的访问，返回客户套接字及ip
        new_socket, client_address = tcp_server_socket.accept()
        # 5.向客户返回内容
        service_client(new_socket)


if __name__ == "__main__":
    main()
