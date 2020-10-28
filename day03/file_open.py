"""
打开文件
"""
#打开文件
# file=open('file.txt','w')  #文件不存在，将创建文件
file=open('file.txt','r') #文件必须存在，才能读
# file=open('file.txt','a')#文件必须存在，然后会在文件的末尾进行追加内容



#读写文件
print(file)

#关闭文件
file.close()
