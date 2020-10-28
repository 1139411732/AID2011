# """
# 练习1： 基于单词本完成
# 编写一个函数，传入一个单词，返回单词对应的解释
#
# 提示：  每行一个单词
#        单词与解释之前有空格
#        单词按顺序排列
#
#        split()
# """
def world(x):
    fr=open('dict.txt','r')
    for itme in fr :
        data=itme.split(' ',1)
        if x == data[0]:
            print(data[1].strip())

world('a')


"""
练习2： 文件拷贝
编写一个copy函数，传入一个具体文件. 将传入
的文件以当前日期为名字，拷贝当程序所在的文件夹下
假设文件比较大，不许一次性读取

def copy(filename): -> 2020-09-29.jpg
    pass

copy("./timg.jpg")

提示： import time    localtime()
      从源文件读取内容，写入到新文件
"""
import time
def copy(x):
    fr=open(x,'rb')
    n=time.localtime()[:3]
    fw=open(f'{n[0]},{n[1]},{n[2]}.jpeg','wb')
    while True:
        data=fr.read(1024)
        fw.write(data)
        if not data:
            break
copy('/home/tarena/下载/timg.jpeg')

"""
练习3：
写一个程序，向一个文件  my.log 中不断写入内容
每隔2秒写入一次， 序号 + 当前时间
要求，当程序终止重新启动后，会继续写，并且序号能够衔接

   1. 2020-10-10  12:12:12
   2. 2020-10-10  12:12:14
   3. 2020-10-10  12:12:16
   4. 2020-10-10  12:12:18
   5. 2020-10-10  12:15:11
   6. 2020-10-10  12:15:13

提示 ： sleep(2)
       使用什么方式打开
       序号如何衔接 ——-》有多少行
"""
# import time
# fw=open('my.log','a+',buffering=1)
# count=1
#
#
# fw.seek(0,0)
# for line in fw:
#     count+=1
#
# while True:
#     time.sleep(2)
#     n=time.localtime()[:6]
#     fw.write(f"{count}  {n[0]}-{n[1]}-{n[2]}  {n[3]}:{n[4]}:{n[5]}\n")
#     count+=1
#
#
#
#
#
#


