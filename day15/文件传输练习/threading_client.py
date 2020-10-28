from threading import Thread
from socket import *

ADDR=("127.0.0.1",8888)
def main():
    sock = socket()
    sock.connect(ADDR)
    while True:
        print('1. 查看文件夹内所有内容')
        print('2. 从文件库中下载文件到本地')
        print('3. 上传一个本地文件到文件库')
        print('4. 退出')
        cmd = input(">>")

        if cmd == '1':
            pass
        # tcp_socket.send(msg.encode())
        # data = tcp_socket.recv(1024)
        # print("从服务器收到:", data.decode())


    tcp_socket.close()