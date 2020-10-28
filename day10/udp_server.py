"""
udp 服务端基础示例
"""
from socket import *
# 创建
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('172.40.83.120', 5201))
# 接收
while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f'收到的消息是{data.decode()},端口是{addr}')

# 回复
    n = udp_socket.sendto(b'Thanks', addr)
    print(f'回复发送{n}个字节')

# 关闭
udp_socket.close()
