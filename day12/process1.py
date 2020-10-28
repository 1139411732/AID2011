"""
process  实例
"""
import multiprocessing as mp
from time import sleep

a=1
# 1.进程的执行函数
def fun():
    print('开始执行一个进程内容')
    sleep(3)
    global a
    a=10000
    print('一个任务假装执行了3秒')
# 2.创建进程对象
p = mp.Process(target=fun)

# 3.启动进程  这是 进程产生,进程执行fun函数
p.start()
print('我也要干点事情')
sleep(2)
print('我做了2秒的事情')

# 4.阻塞等待回收进程  将资源释放  归还给操作系统
p.join()
print(a)


















