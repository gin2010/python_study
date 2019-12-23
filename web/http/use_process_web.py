# -*- coding: utf-8 -*-
# File  : mult_web.py
# Author: water
# Date  : 2019/12/22
# Desc : 多进程实现思路

import socket
import re,multiprocessing

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
        p = multiprocessing.Process(target=service_client,args=(new_socket,)) #args要传入元组
        p.start()
        # 为什么这里要加close()
        # 因为创建子线程以后，会自动复制主线程的相同部分，比如相同的代码、new_socket
        # 子线程多了一个new_socket，与主线程中的new_socket指向的是同一块内存地址
        # 所以如果这里不加new_socket.close()，则只有子线程中new_socket关闭后，new_socket仍在内存中且只指向主线程中new_socket
        # 因此只有先将主线程中的new_socket中关闭，这样才能保证这块内存地址只对应子线程中的new_socket
        # 这样当子线程中的new_socket关闭后，网页也就加载完毕。否则网页一直是加载中
        # print("main:",id(new_socket))
        new_socket.close()



if __name__ == "__main__":
    main()
