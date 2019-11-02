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


import pandas as pd


# 让数据全部显示在控制台
pd.options.display.max_columns = 99
data = pd.read_excel("pd操作.xlsx")
# 旋转操作
table = data.transpose()
print(table)

      Name  Score1  Score2     Score3         Sum         Avg
0    lisi1    62.0    82.0  92.000000  236.000000  236.000000
1    lisi2    63.0    81.0  83.000000  227.000000  227.000000
2    lisi3    64.0    80.0  74.000000  218.000000  218.000000
3    lisi4    65.0    79.0  65.000000  209.000000  209.000000
4    lisi5    66.0    78.0  56.000000  200.000000  200.000000
5    lisi6    67.0    77.0  47.000000  191.000000  191.000000
6    lisi7    68.0    76.0  38.000000  182.000000  182.000000
7    lisi8    69.0    75.0  29.000000  173.000000  173.000000
8    lisi9    70.0    74.0  20.000000  164.000000  164.000000
9   lisi10    71.0    73.0  11.000000  155.000000  155.000000
10  lisi11    72.0    72.0   2.000000  146.000000  146.000000
11  lisi12    73.0    71.0   7.000000  151.000000  151.000000
12  lisi13    74.0    70.0  12.000000  156.000000  156.000000
13  lisi14    75.0    69.0  17.000000  161.000000  161.000000
14  lisi15    76.0    68.0  22.000000  166.000000  166.000000
15  lisi16    77.0    67.0  27.000000  171.000000  171.000000
16  lisi17    78.0    66.0  32.000000  176.000000  176.000000
17  lisi18    79.0    65.0  37.000000  181.000000  181.000000
