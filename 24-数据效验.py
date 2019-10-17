import pandas as pd
import matplotlib.pyplot as plt


def score_validation(row):
    # try:
    #     assert 0 <= row.Score <= 100
    # except:
    #     print(f"{row.ID} 学生有错误的成绩{row.Score}")
    # 或者使用第二种ifelse语句也可以
    if not 0 <= row.Score <= 100:
        print(f"{row.ID} 学生有错误的成绩{row.Score}")


# 自动化的数据校验的过程
data = pd.read_excel("pd操作.xlsx")
# print(data)
# datafrome有两个轴，0表示从上到下，1表示从左到右，因为咱们要比较一行一行的数据，所以设置1
data.apply(score_validation, axis=1)



# 数据分割
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("pd操作.xlsx")
#  data['Name']获取到的是一个序列，再转str字符串，再变换
df = data['Name'].str.split(expand=True)
data['Fname'] = df[0]
data['Lname'] = df[1]
print(data)
