import pandas as pd
import matplotlib.pyplot as plt


# 让所有列都显示出来的设置
# pd.options.display.max_columns = 777
# 数据分析就是将杂乱无章的数据通过分析绘制出一张图来
data = pd.read_excel("pd操作.xlsx", index_col="ID")
print(data)
# 绘制散点图的方式：scatter是散点的意思，
# data.plot.scatter(x="Lprice", y="Yprice")
# 绘制直方图,统计数据出现的概率
# data.Lprice.plot.hist(bins=10)
# 表达出列数据之间的相关性，
print(data.corr())
# plt.show()
