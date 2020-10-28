"""
chat room 客户端代码
"""
from multiprocessing import Process
from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8000)


def login(sock):
    while True:
        # 进入聊天室
        name = input("Name:")
        # 发送姓名
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        # 接收结果
        result, addr = sock.recvfrom(128)
        if result.decode() == 'OK':
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")

#接受消息
def recv_msg(sock):
    while True:
        data,addr=sock.recvfrom(1054*10)
        print(data.decode())
#发送消息
def send_msg(sock,name):
    while True:
        content=input('>>输入消息')
        msg='CHAT ' + f"{content} " + name
        sock.sendto(msg.encode(),ADDR)

# 网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    name=login(sock)  # 进入聊天室
    #创建子进程 用于接受消息
    p = Process(target= recv_msg(sock),args=(sock,))
    p.start()
    send_msg(sock,name)  #父进程发送消息

    p.join()


if __name__ == '__main__':
    main()
