import pandas as pd


def age18_30(a):
    return 18 <= a < 90

def level_a(s):
    return 90 <= s < 100

data = pd.read_excel("pd操作.xlsx", index_col="ID")
# loc是定位的意思，定位我们想要的数据，然后保留下来，data['']获取到一列数据
# 获取到的一列数据是serious，可以使用apply方法
# data = data.loc[data["Lprice"].apply(age18_30)].loc[data['Cate'].apply(level_a)]
# data['']有另外一种表示方法data.Lprice
# data = data.loc[data.Lprice.apply(age18_30)].loc[data.Cate.apply(level_a)]
# 或者apply里可以使用lambda表达式
data = data.loc[data.Lprice.apply(lambda x:18 <= x < 90)]\
    .loc[data.Cate.apply(lambda s:90 <= s < 100)]
print(data)
