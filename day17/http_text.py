"""
http: 请求响应实例
"""
from socket import *

s = socket()
s.bind(('0.0.0.0', 8802))
s.listen(5)

#接受浏览器发送的HTTP请求
c, addr = s.accept()
print('连接成功', addr)

#http响应
response="""HTTP/1.1 200 ok 
Content-Type:text/html 

Hello world 凌晨
"""

c.send(response.encode())


data = c.recv(1024 * 10)
print(data.decode())

c.close()
s.close()
