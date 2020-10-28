"""
udp 客户端基础示例
"""
from socket import *
#服务端地址
# ADDR=('172.40.83.121',31501)
ADDR=('172.40.83.120',5201)
#创建套接字
udp_client=socket(AF_INET,SOCK_DGRAM)
#发送内容
while True:
    msg= input('>>')
    # msg为空则执行break跳出循环
    if not msg:
        break
    udp_client.sendto(msg.encode(),ADDR)

#接受反馈
    data,addr= udp_client.recvfrom(1024)
    print(f'from server:{data.decode()}')

udp_client.close()


