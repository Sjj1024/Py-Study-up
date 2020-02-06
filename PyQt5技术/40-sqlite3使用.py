import sqlite3


# 数据库文件路径
db_path = "test.db"
# 创建数据库连接
conn = sqlite3.connect(db_path)
# 创建游标对象
cur = conn.cursor()
# 查询数据库操作
sql_str = "select * from student"
# 执行sql语句
cur.execute(sql_str)
# 取出结果
res = cur.fetchall()
print(res)
name_list = []
for i in cur.description:
    name_list.append(i[0])
print(name_list.index("age"))
