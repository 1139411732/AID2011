from socket import *
import re

chat = []


def answer():
    file = open('chat.txt', 'r')
    for lien in file:
        info = re.findall(r'(\w+)\S(.*)', lien)
        chat.extend(info)
    file.close()

def find(q):
    for key,value in chat:
        if key in q:
            return value
    return '人家还小不知道'


def main():
    answer()
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    ADDR = ('172.40.83.120', 8888)
    tcp_socket.bind(ADDR)
    tcp_socket.listen(1024)
    # dict01 = {'你好': '你好我是三号技师',
    #           '男的女的': '我是机器人没有性别'}
    while True:
        print('等待连接... ...')
        connfd, addr = tcp_socket.accept()  # connfd-3次握手，建立连接

        data = connfd.recv(1024)
        info=find(data.decode())
        connfd.send(info.encode())

    connfd.close()  # 4次挥手，断开连接


    tcp_socket.close()

main()
