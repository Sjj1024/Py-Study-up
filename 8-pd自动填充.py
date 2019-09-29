import pandas as pd
from datetime import date,timedelta

# dtype 可以设置ID的类型，如果这一列中有NaN的数据，pandas就会将其默认设为float类型，而且不能直接标为int
data = pd.read_excel("5G.xlsx", index_col=None, dtype={"ID": str, "type": str})
print(type(data["ID"]))
data["ID"].at[0] = 100
start = [2018, 1, 1]
for i in data.index:
    data["ID"].at[i] = i + 1
    data['type'].at[i] = "YES" if i % 2 == 0 else "No"
print(data)
