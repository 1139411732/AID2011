"""
含有参数的进程示例
"""
from multiprocessing import Process
from time import sleep
from signal import *

def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print(f'I’m{name}')
        print("I'm working")
#忽略子进程退出---处理僵尸进程的另一种方式
# signal(SIGCHLD,SIG_IGN)
#位置传参 args=()
# p = Process(target=worker, args=(2, 'Levi'))
#关键字传参 kwargs
p = Process(target=worker,args=(2,),kwargs={'name':'Levi'})
# p.daemon=True

p.start()
p.join()
print('===========')

