from socket import *
tcp_socket = socket(AF_INET, SOCK_STREAM)
ADDR = ('172.40.83.120', 8899)
tcp_socket.bind(ADDR)
tcp_socket.listen(1024)

while True:
    print('等待连接... ...')
    connfd, addr = tcp_socket.accept() #connfd-3次握手，建立连接
    print('连接了:', addr)

    data = connfd.recv(1024)
    print(f'收到:',data.decode())
    connfd.send(b'TTT')

    connfd.close()#4次挥手，断开连接


tcp_socket.close()
