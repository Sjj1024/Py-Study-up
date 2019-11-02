import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("pd操作.xlsx")
# 使用去除数据的方法，指定列明，多列的话可以是列表,
# keep属性意思：保留前面重复的还是后面重复的
# data.drop_duplicates(subset="Name", inplace=True, keep="last")

# 找出重复数据
dupe = data.duplicated(subset="Name")
dupe = dupe[dupe]
print(dupe.index)
# 使用iloc来定位元素，iloc传递索引参数
print(data.iloc[dupe.index])
