import pandas as pd
import os

columns = [10, 20, 30]  # 用以校准线损的列表
xlsx_columns = columns  # 用以保存到xlsx文档中的列名称
print(columns, xlsx_columns)
# str_nowtime = datetime.datetime.now().strftime("%Y%m%d")
# loss_file_name = f"../捷希线损文件{str_nowtime}.xlsx"
loss_file_name = "线损文件.xlsx"
if not os.path.exists(loss_file_name):
    df = pd.DataFrame()
    df["name"] = [10, 20, 30]
    df.to_excel(loss_file_name, index=False)

df = pd.read_excel(loss_file_name)
df["age"] = [10, 20, 30]
df.to_excel(loss_file_name, index=False)
