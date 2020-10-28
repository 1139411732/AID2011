"""
文件写方法
"""
# 写方式打开文件
file = open('file.txt', 'w')
# 写入内容
n = file.write('祝福祖国的孙子,戴乐成节日快乐.\n')
print(f"共输入了{n}个字符")
u=file.write('戴了成吃防腐剂\n')
print(f"共输入了{u}个字符")
# n = file.write('祝福祖国的孙子,戴乐成节日快乐.\n')
# print(f"共输入了{n}个字符")
# data=['哈喽,戴了成,\n','sb,了啦\n']
# file.writelines(data)


# 关闭文件
file.close()
