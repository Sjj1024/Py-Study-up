import pandas as pd
import matplotlib.pyplot as plt

# 多表联合查询
student = pd.read_excel("pd操作.xlsx", sheet_name="Student", index_col="ID")
price = pd.read_excel("pd操作.xlsx", sheet_name="Cprice", index_col="ID")
# print(student)
# print(price)
# 两张表关联操作,以students表为主，关联price表，关联的列是ID，
# 如果左边表和右边表关联的列名字不一样的话， 需要再加left_on和right_on
# 如果两种表中有一样的列名字，也可以不写on，默认会将名字相同的列关联。不然报错
# how表示如果没有数据关联的时候，就以左边的为准，关联不到的显示NaN
# table = student.merge(price, how="left", on="ID").fillna(0)

# 如果读的时候配上了index属性，推荐使用join关联, 但是join没有left_on和right_on属性
table = student.join(price, how="left").fillna(0)
# fillna表示关联不到的数据用0填充，但是填充出来是浮点数，改成整数如下
table.Cprice = table.Cprice.astype(int)
print(table)
