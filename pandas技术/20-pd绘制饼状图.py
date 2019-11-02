import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("pd操作.xlsx", index_col="ID")
# data.sort_values(by="ID", inplace=True, ascending=True)
print(data)
# pie是饼的意思，所以是绘制饼状图
data["Lprice"].sort_values(ascending=False).plot.pie(fontsize=8, startangle=-270)
# 设置标题等
plt.title("woaini", fontsize=18, fontweight="bold")
plt.ylabel("Lprice", fontsize=12, fontweight="bold")
plt.show()
