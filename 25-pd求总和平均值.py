import pandas as pd
import matplotlib.pyplot as plt

# 求和求平均值
data = pd.read_excel("pd操作.xlsx", sheet_name="Cprice", index_col="ID")
# 读取指定列的值
temp = data[["Score1", "Score2", "Score3"]]
# 求出每一行的和
row_sum = temp.sum(axis=1)
# 求出每一行的平均值,使用平均值是mean
row_avg = temp.sum(axis=1)

# 将求出来的总和和平均值数据添加到原表中
data['Sum'] = row_sum
data['Avg'] = row_avg

# 求出来列的平均值，然后添加到原表数据中
col_mean = data[["Score1", "Score2", "Score3", "Sum", "Avg"]].mean()
col_mean['Name'] = "总和"
data = data.append(col_mean, ignore_index=True)

print(data)
