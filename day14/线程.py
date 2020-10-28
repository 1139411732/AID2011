"""
线程基本使用示例
"""
import threading
from time import sleep
a=1
def music():
    for i in range(3):
        sleep(2)
        print('播放:甜蜜蜜')
    global a
    a=10000
    print(a)

# 创建线程对象
t = threading.Thread(target=music)

#启动线程
t.start()

for i in range(4):
    sleep(1)
    print('葫芦娃')

#阻塞等待关闭线程，直到线程运行结束后将线程进行回收给进程
t.join()
print(a)