from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()
def number():
    for i in range(1,53,2):
        lock1.acquire()
        print(f'{i}{i+1}')
        lock2.release()


def eg():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))#ascii码转换 数字转字母A-Z
        lock1.release()

t1 = Thread(target=number)
t2 = Thread(target=eg)
lock2.acquire() #让打印数字先执行
t1.start()
t2.start()
t1.join()
t2.join()
