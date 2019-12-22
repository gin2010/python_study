# -*- coding: utf-8 -*-
# File  : mult_web.py
# Author: water
# Date  : 2019/12/22
# Desc : 多协程的实现思路

import socket ,re
import gevent
from gevent import monkey

monkey.patch_all() # 将time.sleep换成gevent.sleep

def service_client(new_socket):
    # 接收客户端发送过来的请求（客户端使用浏览器）
    # 然后根据用户访问不同的页面，返回不同的内容（temp）
    # 1.接收浏览器发来的请求内容
    request = new_socket.recv(1024)
    # GET /index.html HTTP / 1.1
    request_line1 = request.decode("utf-8").splitlines()[0]
    path =re.match(r"[^/]+(/[^ ]*)",request_line1)
    # 2.组装返回数据
    response = "HTTP /1.1 200 OK \r\n\r\n"
    # 加载现成的模板并返回
    file_name = ""
    if path:
        file_name = path.group(1)
        if file_name =="/":
            file_name = "/index.html"
    try:
        with open("./template/index" + file_name,'rb') as f:
            data = f.read()
    except Exception:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += "\r\n"
        data = "<h1>server is wrong</h1>".encode('utf-8')
    finally:
        # 3.发送数据给客户
        new_socket.send(response.encode('utf-8'))
        new_socket.send(data)
        # 4.关闭套接字
        # print("zi:",id(new_socket))
        new_socket.close()


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 使用下面这个参数后，bind操作是可以重复使用local address的
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 2.绑定ip
    tcp_server_socket.bind(("",7890))
    # 3.监听端口
    tcp_server_socket.listen(128)
    while True:
        # 4.等待客户的访问，返回客户套接字及ip
        new_socket, client_address = tcp_server_socket.accept()
        # 5.向客户返回内容
        # service_client(new_socket)
        gevent.spawn(service_client,new_socket) #args要传入元组
        # print("main:",id(new_socket))
        # new_socket.close()
        # 多协程也不能关闭主线程中的new_socket，因为多协程之间是共享变量，不会复制，所以不能在主线程中关闭


if __name__ == "__main__":
    main()
