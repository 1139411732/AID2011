"""
pymysql 数据库处理结构示例
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
# 数据操作
cur.execute()
# 关闭游标和数据库链接
cur.close()
db.close()
