from threading import Thread
from socket import *
HOST = '0.0.0.0'
PROT = 8802
ADDR = (HOST, PROT)

ftp='/home/tarena/FTP/'

class MYThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def run(self):
        while True:
            data=self.connfd.recv(1024)
            print(data.decode())
            if not data:
                break
            print(data.decode())
            self.connfd.send(b'ok')
        self.connfd.close()


def funcion(sock):
    while True:
        connfd, addr = sock.accept()
        data = connfd.recv(1024)
        print(data.decode())
        MYThread(connfd)
        # tmp = data.decode().split(' ', 2)
        # if tmp[0] == 'LIST':
        #     MYThread(connfd)
        # elif tmp[0] == 'STOR':
        #     pass
        # elif tmp[0] == 'RETR':
        #     pass
        # elif tmp[0] == 'EXIT':
        #     pass

def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print(f'连接成功{PROT}')
    while True:
        # 循环接收客户端连接
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            # 退出服务
            sock.close()
            break
        # 使用自定义线程类为连接的客户端创建新线程
        t = MYThread(connfd)
        t.setDaemon(True)  # 客户端随服务端退出
        t.start()