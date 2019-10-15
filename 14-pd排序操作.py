import pandas as pd


data = pd.read_excel("pd操作.xlsx", index_col="ID")
# 排序操作使用sort_values
data.sort_values(by=["Cate", "Lprice"], inplace=True, ascending=[True, False])
print(data)
