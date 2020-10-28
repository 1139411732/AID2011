# 练习1： 基于单词本完成
# 编写一个函数，传入一个单词，返回单词对应的解释
#
# 提示：  每行一个单词
#        单词与解释之前有空格
#        单词按顺序排列
#
#        split()
data = open("dict.txt")
def find_word(x):
    for item in data:
        tmp = item.split(' ',1)
        if x == tmp[0]:
            data.close()
            return tmp[1].split()
        else:
            return '输入错误'
print(find_word("a"))

