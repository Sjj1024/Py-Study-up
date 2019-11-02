import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 读取数据
data = pd.read_excel("pd操作.xlsx")
print(data)
# 计算现行回归方程,slope坡度，斜率，intercept为截距，
slope, intercept, r, p, std_err = linregress(data.index, data.Score1)
exp = data.index*slope + intercept

# 绘图, scatter是散点图，plot是线形图
plt.scatter(data.index, data.Score1)
plt.plot(data.index, exp, color="red")
plt.title(f"y={slope}*x+{intercept}")
plt.xticks(data.index, data.Score1, rotation=90)
plt.tight_layout()
plt.show()
