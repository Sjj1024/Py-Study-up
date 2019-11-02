import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("pd操作.xlsx")
# 添加一列Total，是前三列的和
data['Total'] = data['Lprice'] + data['Rprice'] + data['Cprice']
print(data)
data.sort_values(by='Total', inplace=True, ascending=False)
# 添加一个属性stacked就是设置的叠加柱状图
# data.plot.bar(x="Name", y=["Lprice", "Rprice", "Cprice"], stacked=True)
# 改成水平显示的方式，barh，h就是水平的意思
data.plot.barh(x="Name", y=["Lprice", "Rprice", "Cprice"], stacked=True)
# 紧凑型显示
plt.title("woaini")
plt.tight_layout()
plt.show()
