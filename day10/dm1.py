"""
UDP协议  套接字使用基础示例
"""
import socket

# 穿件一个UDP套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

#1.如果绑定的地址是127.0.0.1 或者 localhost 那么另外一段只能在同一个计算机上通过127.0.0.1访问
#2.绑定自己的网络IP，另一端可以在任何位置通过ip访问  前提是要嘛在同一个局域网内
#3.绑定自己的网络地址为0.0.0.0 另一端使用则可以在任何位置访问
udp_socket.bind(('172.40.83.120', 8888))



