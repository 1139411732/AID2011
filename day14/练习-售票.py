from threading import Thread
import time

list_kets = []
for i in range(1, 501):
    list_kets.append(f'T{i}')
def sell_ticket(i):
    while list_kets:
        print(f'窗口{i}--{list_kets.pop(0)}')
        time.sleep(0.1)

jobs = []
for i in range(1,11):
    t = Thread(target=sell_ticket, args=(i,))
    t.start()

[i.join() for i in jobs]
