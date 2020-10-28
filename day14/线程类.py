from threading import Thread
import time


class MyYhread(Thread):
    def __init__(self, song):
        self.song = song
        super().__init__()  # 加载父类方法

    def run(self):
        for i in range(3):
            print(f'playing{self.song}:{time.ctime()}')
            time.sleep(2)


t = MyYhread('凉凉')
t.start()  # 会自动运行run方法,作为一个线程执行
t.join()
