import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("pd操作.xlsx", index_col="ID")
print(data)
print(data.columns)
# 折线图只需要使用plot就可以，叠加折线图使用plot.area。重在表现什么时候淡旺季
# data.plot(y=['Lprice', 'Rprice', 'Cprice', 'Yprice'])
data.plot.area(y=['Lprice', 'Rprice', 'Cprice', 'Yprice'])
# 叠加柱状图,重在表达在某个点上叠加起来是一个什么高度，
data.plot.bar(y=['Lprice', 'Rprice', 'Cprice', 'Yprice'], stacked=True)
plt.title("woaini", )
plt.ylabel("Price", fontsize=8)
plt.show()
