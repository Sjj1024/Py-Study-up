import pandas as pd

data = pd.read_excel("pd操作.xlsx", index_col="ID")
# 计算列相乘,运算符重载，前面行和后面每一行一一对应相乘
# data["Price"] = data['Lprice'] * data['Cate']
# 只对指定行的数据做运算
for i in range(1, 6):
    data["Price"].at[i] = data["Lprice"].at[i] * data["Cate"].at[i]


def add_2(x):
    return x + 2

# 可以对每一项做函数调用计算操作
# data["Lprice"] = data["Lprice"].apply(lambda x: x + 2)
data["Lprice"] = data["Lprice"].apply(add_2)

print(data)
