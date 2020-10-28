import os
def func01(dir):
    for item in os.listdir(dir):
        filename=dir+'/'+item
        if os.path.isfile(filename) and os.path.getsize(filename) < 1024*10:
            os.remove(filename)
            print('删了')


func01('/home/tarena/下载')
