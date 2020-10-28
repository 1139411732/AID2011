"""
web  server  程序
完成一个类，提供给使用者
可以通过这个类快速搭建服务
完成网页展示
"""
from threading import Thread
from socket import *
from select import select
import re


# 封装所有web 后端功能
class WebServer:
    # 对象初始化方法
    def __init__(self, host='0.0.0.0', port=8000, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.crrate_socket()
        self.bind()

    # 创建设置套接字
    def crrate_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 启动整个服务
    def start(self):
        self.sock.listen(5)
        print(f'Listen the port {self.port}')
        self.rlist.append(self.sock)  # 客户端连接
        # 循环监控IO对象
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    connfd, addr = self.sock.accept()
                    print(f"Connect from{addr}")
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    # 处理浏览器端发的请求
                    self.handle(r)
                    self.rlist.remove(r)
                    r.close()

    def handle(self, connfd):
        request = connfd.recv(1024 * 10).decode()
        # 使用正则表达式匹配中间内容
        pattern = r'[A-Z]+\s+(?P<info>/\S*)'
        result = re.match(pattern, request)
        if request:
            # 匹配到请求内容
            info = result.group('info')
            print(f'获取请求内容{info}')
            self.send_html(connfd, info)
        else:
            # 匹配不到请求内容
            return

    def send_html(self, connfd, info):
        if info == '/':
            filename = self.html + '/index.html'
        else:
            filename = self.html + info
        # 打开判断文件是否存在
        try:
            file = open(filename, 'rb')
        except:
            # 请求的网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            with open(self.html + '/404.html') as file:
                response += file.read()
            response=response.encode()
        else:
            data=file.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%dtext/html\r\n"%len(data)
            response += "\r\n"
            response = response.encode()+data
            file.close()
        finally:
            connfd.send(response)


if __name__ == '__main__':
    # 需要用户决定的: 地址 网页
    httpd = WebServer(host='0.0.0.0',
                      port=8001,
                      html='/home/tarena/month02/day17/static')
    # 启动服务
    httpd.start()
