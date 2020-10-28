#
# 练习2： 文件拷贝
# 编写一个copy函数，传入一个具体文件. 将传入
# 的文件以当前日期为名字，拷贝当程序所在的文件夹下
# 假设文件比较大，不许一次性读取
#
# def copy(filename): -> 2020-09-29.jpg
#     pass
#
# copy("./timg.jpg")
#
# 提示： import time    localtime()
#       从源文件读取内容，写入到新文件


import time
def copy(filename):
    fr = open(filename, 'rb')
    n =time.localtime()[:3]
    fw = open(f'{n[0]}-{n[1]}-{n[2]}.jpeg', 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()


copy('/home/tarena/下载/timg.jpeg')
