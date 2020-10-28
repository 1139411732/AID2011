"""
tcp 客户端套接字
"""
from socket import *
server_addr=('172.40.83.120',8888)
while True:
    msg = input('>>')
    if not msg:
        break
    tcp_socket = socket()
    tcp_socket.connect(server_addr)
    tcp_socket.send(msg.encode())

    data=tcp_socket.recv(1024)
    print(f'小美:{data.decode()}')

#关闭客户端
    tcp_socket.close()





