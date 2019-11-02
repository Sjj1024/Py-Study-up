import pandas as pd
import matplotlib.pyplot as plt

# 文不如表，表不如图，表妹就是处理excel的妹子


data = pd.read_excel("pd操作.xlsx")
data.sort_values(by="Lprice", inplace=True, ascending=False)
print(data)
# 在pandas中柱状图是bar,x,y是横纵坐标轴，color是柱状图颜色
# data.plot.bar(x="NAME", y="Lprice", color="red", title="my bar")
# 让横坐标的文字显示全,也就是紧凑型显示
#  第二种使用plt显示bar的方式
plt.bar(data.NAME, data.Lprice, color="red")
# 但是横坐标的名字叠加到一起了，需要处理一下
plt.xticks(data.NAME, rotation="90")
# 添加xy轴的名字，和图表的名字z字号
plt.xlabel("name")
plt.ylabel("price")
plt.title("student price", fontsize=18)
plt.tight_layout()
plt.show()
