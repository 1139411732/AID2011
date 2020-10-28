"""
tcp 客户端套接字
"""
from socket import *
server_addr=('172.40.83.120',8899)
while True:
    msg = input('>>')
    if not msg:
        break
    tcp_socket = socket()
    tcp_socket.connect(server_addr)
    tcp_socket.send(msg.encode())

    data=tcp_socket.recv(1024)
    print(f'从服务器接收到的:{data.decode()}')

#关闭客户端
    tcp_socket.close()





