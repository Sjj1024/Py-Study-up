import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("pd操作.xlsx")
data.sort_values(by="Rprice", inplace=True, ascending=False)
print(data)
# 设置图的xy坐标和颜色
data.plot.bar(x="NAME", y=["Lprice", "Rprice"], color=["red", "orange"])
# 设置标题和左右坐标轴的名字，并粗体显示
plt.title("my name", fontsize=18, fontweight="bold")
plt.xlabel("Name", fontweight="bold")
plt.ylabel("Price", fontweight="bold")
# 处理横坐标的文字旋转，轴就是axis,所以想改变轴的属性就得先获取轴
ax = plt.gca()
# 拿到这个轴的属性后，就需要重新设置一下轴属性,旋转45度，对齐方式是右对齐
ax.set_xticklabels(data.NAME, rotation=45, ha="right")
# 让图形显示全
# plt.tight_layout()
# 单独调整图形显示的属性,让图形显示全，gcf是获取当前图形的缩写
f = plt.gcf()
f.subplots_adjust(left=0.12, bottom=0.2)  # 调整图的左边界和底部边界
plt.show()
