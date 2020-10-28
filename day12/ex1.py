from multiprocessing import Process
import os
size = os.path.getsize("dict.txt")
def copy1():
    fr = open('dict.txt', 'r')
    fw = open('dixt.txt', 'w')
    n = size // 2  # 从头开始复制n个字节
    while n >= 1024:
        fw.write(fr.read(1024))
        n-=1024
    else:
        fw.write(fr.read(n))
    fw.close()
    fr.close()

def copy2():
    fr = open('dict.txt', 'r')
    fw = open('dipt.txt', 'w')
    fr.seek(size // 2, 0)
    while True:
        # 从一般开始复制
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    fr.close()

jobs = []
for th in [copy1, copy2]:
    p = Process(target=th)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
