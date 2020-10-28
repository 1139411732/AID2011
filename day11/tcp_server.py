from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
ADDR = ('172.40.83.120', 8899)
tcp_socket.bind(ADDR)
# 设置监听----在监听队列等待被客户端连接
tcp_socket.listen(1024)
# 等待客户端连接
while True:
    print('等待连接... ...')
    connfd, addr = tcp_socket.accept() #connfd-3次握手，建立连接
    print('连接了:', addr)
    while True:
    # 收消息
        data = connfd.recv(1024)
        #当客户端close断开连接，此时recv会返回一个空字节串
        if not data:
            break
        #收到了##表示客户端已经退出
        # elif data.decode() == "##":
        #     break
        print(f'接收到：{data.decode()}')
        # 发消息
        connfd.send(b'TTT')
    connfd.close()#4次挥手，断开连接


tcp_socket.close()
