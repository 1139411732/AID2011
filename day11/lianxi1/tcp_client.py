from  socket import *
# 服务器地址
server_addr = ("172.40.83.120",8895)
# 创建tcp套接字
tcp_socket = socket()
tcp_socket.connect(server_addr)

file = open("timg.jpeg",'rb') # 二进制打开
# 边读取边发送
while True:
    data = file.read(2048)
    if not data:
        break
    tcp_socket.send(data)
file.close()

tcp_socket.send(b"##")
# 接收通知
msg = tcp_socket.recv(2048)
print(msg.decode())
# 关闭套接字
tcp_socket.close()