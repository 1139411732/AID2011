"""
多进程网络并发模型
"""
from multiprocessing import Process
from socket import *
from signal import *

HOST = "172.40.83.120"
PORT = 8800
ADDR = (HOST, PORT)

#实现具体的业务功能，客户端请求都在这里处理
def handle(connfd):
    #与客户端配合测试
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'ok')
    connfd.close()


# 在函数中编写并发服务
def main():
    sock = socket()  # 创建Tcp套接字
    sock.bind(ADDR)
    sock.listen(5)  # 绑定监听
    print(f'Listen the port {PORT}')
    signal(SIGCHLD, SIG_IGN)  # 处理僵尸进程
    while True:
        # 循环接收客户端连接
        try:
            connfd, addr = sock.accept()
            print(f'Connect from {addr}')
        except KeyboardInterrupt:
            #当按下ctrl+c时 服务端退出
            sock.close()
            break
        # 为已连接的客户端创建新进程
        p = Process(target=handle, args=(connfd,))
        p.daemon = True  #客户端随服务端退出
        p.start()
        # p.join()  # ----------
if __name__ == '__main__':
    main()