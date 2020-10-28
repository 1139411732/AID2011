import pymysql
import re

# # 生成数据库链接对象,链接数据库
database = {'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'stu',
            'charset': 'utf8'}

db = pymysql.connect(**database)
# 生成游标
cur = db.cursor()
# 数据操作
sql = 'select name,age,score from cls where score > 50;'
cur.execute(sql)

# for row in cur:
#     print(row)

one=cur.fetchone()
print(one)
one=cur.fetchmany(3)
print(one)
one=cur.fetchall()
print(one)


# 关闭游标和数据库链接
cur.close()
db.close()
