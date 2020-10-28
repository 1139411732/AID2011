import pymysql
# alter table cls add image mediumblob;
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
with open('/home/tarena/下载/timg.jpeg','rb') as f:
    data=f.read()

sql='update cls set image=%s where id =1;'
cur.execute(sql,[data])
db.commit()

sql='select image from cls where id =1;'
cur.execute(sql)
data=cur.fetchone()
with open('timg.jpeg','wb') as f:
    f.write(data[0])

cur.execute(sql)


# 关闭游标和数据库链接
cur.close()
db.close()
