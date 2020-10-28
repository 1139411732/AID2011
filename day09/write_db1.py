"""
数据库写操作示例1
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
cur = db.cursor()
# 数据操作
# 写操作示例 insert delete update
try:
    name = input('请输入学生姓名')
    # sql = 'update cls set score = %s where name = "%s";'
    sql = f'update cls set score={100} where name = "{name}";'
    print(sql)
    cur.execute(sql)
    # cur.execute(sql, [90, name])
    db.commit()  # 事物提交
except Exception as e:
    print(e)
    db.rollback()  # 事物回滚

# 关闭游标和数据库链接
cur.close()
db.close()
