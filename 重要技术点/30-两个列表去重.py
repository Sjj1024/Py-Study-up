list1 = ["2\n", "3242\n", "dfvd\n"]
list2 = ["2\n", "3242\n", "dfvd\n", "dfsdf"]

# 两个列表快速去重, 不要使用遍历对比，因为遍历对比pop删除后，后面元素会向前进一位，导致输出错
dif = set(list2).difference(set(list1))

# 在文件开头新增加内容，使用方式
with open("badreq.txt", "r+", encoding="utf-8") as f:
    content = f.readlines()
    # 将指针设置到开头
    f.seek(0)
    # 将内容清空
    f.truncate()
    new_con = list1 + content
    f.writelines(new_con)
