import pandas as pd

# 默认读取的是表中第一个表单的数据
data = pd.read_excel("5G.xlsx", sheet_name="N78_15kHz")
print(data.head())

# 通过索引获取指定表单数据
data2 = pd.read_excel("5G.xlsx", sheet_name=0)
print(data2.head())

# 可以获取多个表单数据
data3 = pd.read_excel("5G.xlsx", sheet_name=["N1_15kHz", "N78_15kHz"])
# print(data2.values)

# 读取指定行的数据,不包含表头信息
print(3333333333333333333)
print(data2.iloc[0].values)

# 读取指定的多行数据
print(4444444444444444444444)
print(data2.iloc[[2, 4]].values)

# 读取指定行列的数据
print(55555555555555555)
print(data2.iloc[5, 3])

# 读取指定行列数据,注意是loc
print(data2.loc[[5, 3], ["Bandwidth [MHz]", "offsetToPointA"]])

# 获取所有行的指定列
print(data2.loc[:, ["Bandwidth [MHz]", "offsetToPointA"]])

# 获取所有行号，并打印出来, 是一个列表
print(data2.index.values)

# 获取所有列名，并打印出来
print(data2.columns.values)

# 获取指定列的值
print(data2['offsetToPointA'].values)
