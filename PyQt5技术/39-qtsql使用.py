from PyQt5 import QtSql

# 连接数据库，第一步是创建数据库连接，参数是连接的数据库类型，第二步是设置数据库名字，如果这个数据库没有，则重新创建一个
db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName("test.db")

# 打开数据库，成功则返回true
if db.open():
    print("打开数据库成功")

# 创建数据表,名为student,包含id，name，age三个属性，其中id为主键
query = QtSql.QSqlQuery()  # 创建查询对象
# 不设置id，则默认添加主键id，
query.prepare("create table student(name varchar(30), age int)")
if not query.exec():
    query.lastError()
else:
    print("创建了一个数据表")

# 插入数据到其中,exec是执行sql语句的操作，不用设置id，则会自增id主键
insert_sql = "insert into student values('songjiang',18)"
if not query.exec(insert_sql):
    print(query.lastError())
else:
    print("插入成功！")

# 查询数据
query_sql = "select name, age from student"
if query.exec(query_sql):
    # query.record().indexOf是获取索引值
    name_index = query.record().indexOf("name")
    age_index = query.record().indexOf("age")
    print(name_index, age_index, query.next())
    while query.next():
        print("开始打印查询到的数据")
        # 通过query.value(int)来获取值
        # print(query.value(name_index), query.value(age_index))
        print(name_index, age_index)
