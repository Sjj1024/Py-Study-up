from datetime import date, timedelta


# 计算日期的小算法
def add_time(d, md):
    y = md // 12
    mt = d.month + md % 12
    if mt != 12:
        y = mt // 12
        mt = mt % 12
    return date(d.year + y, mt, d.day)

start = date(2019, 9, 10)

for i in range(10):
    # 月份累加
    new_time = add_time(start, i)
    print(new_time)
    # 日期累加
    new2_time = date(start.year, start.month, start.day + i)
    # 年份累加
    new3_time = date(start.year + i, start.month, start.day)

print(start)
