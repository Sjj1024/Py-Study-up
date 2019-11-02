import pandas as pd

# 导入数据
data1 = pd.read_excel("pd操作.xlsx", sheet_name="Student")
data2 = pd.read_excel("pd操作.xlsx", sheet_name="Cprice")

# 追加数据.reset_index是重新设置索引，drop是丢掉旧的索引
student = data1.append(data2).reset_index(drop=True)
#  再单独添加一行
stru1 = pd.Series({"ID": 41, "Name": "WO", "Score1": 99})
# 将数据添加到原表中,ignore_index是自动生成索引的意思
student = student.append(stru1, ignore_index=True)
# student.append(stru1, ignore_index=True)

# 修改表里的数据,直接修改
student.at[42, "Name"] = "daniu"
student.at[42, "Score1"] = "100"
# 或者另外修改数据的方式.替换
stru2 = pd.Series({"ID": 41, "Name": "cai", "Score1": 110})
student.iloc[41] = stru2

# 插入操作,使用切片的概念
stru3 = pd.Series({"ID": 100, "Name": "song", "Score1": 110})
part1 = student[:20]
part2 = student[20:]
student = part1.append(stru3, ignore_index=True).append(part2, ignore_index=True)

# 删除数据行
# student.drop(index=[0, 1, 2], inplace=True)
# student.drop(index=range(10), inplace=True)

# 使用切片删除范围数据
student.drop(index=student[:10].index, inplace=True)

# 按条件删除,先配置上一些空数据
for i in range(5, 15):
    student["Name"].at[i] = ""

# 筛选出这部分数据
missing = student.loc[student["Name"] == ""]
student.drop(index=missing.index, inplace=True)
print(student)
