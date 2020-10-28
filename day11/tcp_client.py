"""
tcp 客户端套接字
"""
from socket import *
#声明服务器地址
server_addr=('172.40.83.120',8899)
#创建tcp套接字
tcp_socket=socket()
#连接服务器
tcp_socket.connect(server_addr)
#向服务器发送消息
while True:
    msg=input('>>')
    tcp_socket.send(msg.encode())
    #发送##告知服务端自己退出
    if msg == '##':
        break
    data=tcp_socket.recv(1024)
    print(f'从服务器接收到的:{data.decode()}')

#关闭客户端
tcp_socket.close()




