# -*- coding: utf-8 -*-
# File  : single_web_long_connect9.py
# Author: water
# Date  : 2019/12/22
# Desc  : 单进程、单线程、非堵塞、长连接实现方式
import socket
import re

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

    client_socket_list = list()
    while True:
        # 4.接受客户端的连接
        try:
            new_socket, client_addr = tcp_server_tcp.accept()
        except Exception as ret:
            # 如果没有连接，则继续
            pass
        else:
            # 如果有客户连接，服务器会自动堵塞，等待为此客户服务
            # 因此这里要转为非堵塞，继续接受新的客户连接，并把已接家的客户加入到列表里
            new_socket.setblocking(False)  # 客户连接转为非堵塞
            client_socket_list.append(new_socket)

        # 循环已连接的客户端列表，为每个客户服务
        for client in client_socket_list:
            try:
                # 接受客户端的数据，并保持长连接
                # 然后再次while True循环，收到client的再次发送请求，再次处理客户请求
                # 直到这个client没有请求，client.close（关闭）
                recv_data = client.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data: # 如果有数据，则处理客户请求，并在service_client里面保持长连接
                    service_client(client, recv_data)
                else:
                    client.close() # 如果客户没有数据，则关闭客户请求
                    client_socket_list.remove(client)
                    print("----close------")
    tcp_server_tcp.close()


if __name__ == "__main__":
    main()
