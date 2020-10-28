"""
数据库写操作示例2      批量插入
"""
import pymysql

# 生成数据库链接对象,链接数据库
database = {'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'stu',
            'charset': 'utf8'}

db = pymysql.connect(**database)
# 生成游标
cur = db.cursor()
#批量写操作示例
l=[
    ('D',16,'m',81),
    ('A',13,'w',70),
   ]
sql= f'insert into cls (name,age,sex,score) values (%s,%s,%s,%s);'
try:
    cur.executemany(sql,l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库链接
cur.close()
db.close()
