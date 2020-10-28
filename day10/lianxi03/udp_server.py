from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

addr = ('0.0.0.0', 8888)
udp_socket.bind(addr)
while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f'{addr},收到的是:{data.decode()}')

    n = udp_socket.sendto(b'TTT', addr)
    print(f'发送了{n}个字节')

udp_socket.close()

