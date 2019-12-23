# -*- coding: utf-8 -*-
# File  : single_web_long_connect9.py
# Author: water
# Date  : 2019/12/22
# Desc  : epoll实现快速响应数据
#         epoll会将客户端请求的变量存放于单独的空间中（介于内核与程序之间的一块内存），内核可以直接调用里面的变量，还不需要将程序的变量先复制到内核空间中
#         epoll还会进行轮询，因此就无需每次循环已连接的客户端的列表，来判断哪个客户端发送了新的请求
#         通过epl.poll()方法来实现，此方法会堵塞并监听所有变量，如果有新的请求，会直接返回(变量文件符，event)
import socket
import re
import select #仅仅支持linux内核的，win10与mac都不支持


def service_client(client,request):
    # 1.获取客户访问的地址
    request_lines = request.splitlines()
    print('')
    print(">"*20)
    print(request_lines)
    '''request_lines
    ['GET / HTTP/1.1', 'Host: 127.0.0.1:7890', 'Connection: keep-alive', 'Cache-Control: max-age=0', 'Upgrade-Insecure-Requests: 1', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36', 'Sec-Fetch-User: ?1', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Sec-Fetch-Site: none', 'Sec-Fetch-Mode: navigate', 'Accept-Encoding: gzip, deflate, br', 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8', '']
    '''
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        print(file_name)
        if file_name == "/":
            file_name = "/index.html"
    # 2.返回地址下的内容给客户端，
    try:
        f = open("./template/index" + file_name,'rb')
    except:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header += "\r\n"
        response_body = "-----file not found----"
        response = response_header + response_body
        client.send(response.encode("utf-8"))  # 返回内容给客户端
    else:
        response_body = f.read()
        f.close()
        response_header = "HTTP/1.1 200 OK\r\n"
        # 指定长度后浏览器根据长度判断本次连接结束
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        print(response_header)
        response = response_header.encode('utf-8') + response_body
        client.send(response)


def main():
    # 1.新建套接字
    tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定ip
    # 使用下面这个参数后，bind操作是可以重复使用local address的
    tcp_server_tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_server_tcp.bind(("", 7890))
    # 3.变为监听套接字
    tcp_server_tcp.listen(128)
    tcp_server_tcp.setblocking(False)  # 非堵塞
    # 4.创建epoll对象
    epl = select.epoll()
    # 5.将监听套接字对应的fd注册到epoll中
    # fd:file desc文件描述符，是数字
    # fileno():获取当前套接字的文件描述符
    epl.register(tcp_server_tcp.fileno(),select.EPOLLIN)
    fd_event_dict = dict()

    while True:
        # 6.等待新客户端的连接
        fd_event_list = epl.poll() #epoll会堵塞，直接os监测到数据过来，将事件告知程序再解堵塞
        # fd_event_list 会返回[(fd,event),(fd,event)]类的列表
        for fd,event in fd_event_list:
            if fd == tcp_server_tcp.fillno():
                new_socket,client_addr = tcp_server_tcp.accept()
                epl.register(new_socket.fillno(),select.EPOLLIN)
                fd_event_dict[new_socket.fillno()] = new_socket
            elif event ==select.EPOLLIN:  # 7.判断已连接的客户端是否发送数据过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data: # 如果有数据，则处理客户请求，并在service_client里面保持长连接
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close() # 如果客户没有数据，则关闭客户请求
                    epl.unregister(fd) # 删除这个文件符
                    del fd_event_dict[fd] # 删除字典里对应的值
                    print("----close------")

    tcp_server_tcp.close()


if __name__ == "__main__":
    main()
