"""
udp 客户端基础示例
"""
from socket import *

#服务端地址
# ADDR=('172.40.83.121',31501)
ADDR=('172.40.83.120',8888)
#创建套接字
udp_client=socket(AF_INET,SOCK_DGRAM)

#发送内容
while True:
    word= input('输入')
    # msg为空则执行break跳出循环
    if not word:
        break
    udp_client.sendto(word.encode(),ADDR)

# 接收服务器发来的解释
    data,addr= udp_client.recvfrom(1024)
    print(f'对应的解释是:{word,data.decode()}')

udp_client.close()


