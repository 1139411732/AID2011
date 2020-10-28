from multiprocessing import Queue,Process
q = Queue(5)
def request():
    name = '戴乐成的爷爷'
    passwd = '戴乐成'
    q.put(name)
    q.put(passwd)
def hal():
    name=q.get()
    passwd=q.get()
    print(name)
    print(passwd)

p1=Process(target=request)
p2=Process(target=hal)
p1.start()
p2.start()
p1.join()
p2.join()

