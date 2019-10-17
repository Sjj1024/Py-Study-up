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
