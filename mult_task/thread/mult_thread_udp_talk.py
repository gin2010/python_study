# -*- coding: utf-8 -*-
# @Date : 2019-12-14
# @Author : water
# @Version  : v1.0
# @Desc  :f完成udp聊天工具的整体控制

import threading,socket

def recv_msg(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket,dest_ip,dest_port):
    # 发送数据
    while True:
        send_data = input("send msg:")
        udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2.绑定本地信息(ip,port）
    udp_socket.bind(("",7890))
    # 3.获取对方ip
    dest_ip = "192.168.0.1"
    dest_port = 8080
    # 4.创建两个线程分别控制收发信息
    t_recv = threading.Thread(target=recv_msg,args=(upd_socket,))
    t_send = threading.Thread(target=send_msg,args=(upd_socket,dest_ip,dest_port))
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()