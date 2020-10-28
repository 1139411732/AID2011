"""
创建线程实例2
"""
from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    print('含有参数的线程函数')
    sleep(sec)
    print(f'{name}线程执行完成')


# 一次性创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,
               args=(2,),
               kwargs={'name': f"Tom{i}"})
    jobs.append(t)
    t.start()

[i.join() for i in jobs]
