from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
ADDR = ('172.40.83.120', 8888)

while True:
    msg= input('>>')
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)


    data,addr=udp_socket.recvfrom(1024)
    print(data.decode())

udp_socket.close()

