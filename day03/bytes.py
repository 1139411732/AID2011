"""
字节串
    b''(字节串语法）
    #将字符串或变量转化为字节串（字节串.encode)
    #将字节串或变量转化为字符串（字符串.decode)
        所有的字符串都可以转化为字节串


"""


result='带了成'
print(type(result))


result = b'dailecheng,JJ'
print(type(result))

#将字符串或变量转化为字节串
result='张无忌'.encode()
print(type(result))
print(result)
#将字节串转化为字符串
print(result.decode())


