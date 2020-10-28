import pymysql
import re
# # 生成数据库链接对象,链接数据库
database = {'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'dict',
            'charset': 'utf8'}

db = pymysql.connect(**database)
# 生成游标
cur = db.cursor()
# 数据操作
file = open('dict.txt')
l = []
for lien in file:
    tup = re.findall(r'(\w+)\s+(.*)', lien)
    l.append(tup[0])
try:
    sql = 'insert into words (word,mean) values (%s,%s);'
    cur.executemany(sql, l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库链接
cur.close()
db.close()
