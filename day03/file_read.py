"""
读取文件
"""
# 打开文件
file=open('file.txt','r')
# file = open('/home/tarena/下载/timg.jpeg', 'rb')

# 读取文件
# 1.不加参数则默认读取全部内容
# 2.加参数代表读取参数内的字符
# data=file.read(6)
# print(data)
#
# data=file.read()
# print(data)
#
#方法1 read对于大文件,建议循环读取,而不是一次性读取
# while True:
#     data = file.read(1024*10)
#     if not data:
#         break
#     print(data,end="")


# # 方法2 readline  一次读取1行的2个字节的内容
# data = file.readline(2)
# print(data)
#


#  readlines 一次读取多行
# data=file.readlines()
# print(data)

#方法4 可以用for循环提取内容
for item in file:
    print(item,end="")


# 关闭文件
file.close()
