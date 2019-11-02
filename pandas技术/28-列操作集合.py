import pandas as pd
import numpy as np


# 将两个数据表连接到一起
student = pd.read_excel("pd操作.xlsx", sheet_name="Student")
peice = pd.read_excel("pd操作.xlsx", sheet_name="Cprice")
# 连接到一起的方式是concat,axis默认为0表示纵向添加，为1表示横向添加
# student1 = pd.concat([student, peice], axis=1)

# 追加列,直接将Score2追加到后面了
student2 = pd.concat([student, peice]).reset_index(drop=True)
student2["Score2"] = np.arange(0, len(student2))

# 插入一列,就差进去了ID      Name  ALL  Score1  Score2
student2.insert(2, column="ALL", value=np.repeat("foo", len(student2)))

# 修改列名字
student2.rename(columns={"Name": "NAME", "Score1": "SCORE1"}, inplace=True)
# 打印出所有列的名字
print(student2.columns)

# 将一列中数据是空值的删除掉,例如NaN的数据
student2["ID"] = student["ID"].astype(float)
# dropna会删除掉行中只要有NaN的行
student2.dropna(inplace=True)
print(student2)
