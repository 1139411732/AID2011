"""
求100000以内质数之和，写成一个函数
写一个装饰器求一个这个函数运行时间

将100000分成4等份 分别使用4个进程求
每一份的质数之和，四个进程同时执行
记录时间

将100000分成10等份 分别使用10个进程求
每一份的质数之和，10个进程同时执行
记录时间
"""

list_number = []
for i in range(2, 1000 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list_number.append(i)

print(list_number)






