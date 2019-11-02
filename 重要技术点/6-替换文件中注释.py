import re
import os

"""
删除文件中所有注释内容
"""


def get_path_py(file_py_list, path):
    # 方法一：获取到当前目录下所有以.py文件结尾的文件列表
    # print(os.listdir(path))
    for i in os.listdir(path):
        file_path = os.path.join(path, i)
        if os.path.isdir(file_path):
            get_path_py(file_py_list, file_path)
        if os.path.isfile(file_path):
            file_py_list.append(os.path.join(path, i))


def get1_path_py(file_py_list, path):
    # 方法二：通过os获取当前目录下的文件
    for root, filedir, filename in os.walk(path):  # root 是filename文件的根目录，filedir 是当前root目录下子文件夹列表， filename是root下的文件列表
        for i in filename:
            # print(os.path.join(root, i))
            file_py_list.append(os.path.join(root, i))
    # 剔除本文件的路径
    for x in file_py_list:
        if os.path.relpath(__file__) in x:
            file_py_list.pop(file_py_list.index(x))
    # 打印出要遍历的文件列表路径
    print(f"要遍历的文件路径列表是{file_py_list}")


def content_file(file_name):
    # 获取文件的内容，并替换掉匹配到的内容
    print(f"开始处理的文件{file_name}----------->")
    file = open(file_name, "r+", encoding="utf-8")
    re_obj = re.compile(r'# .*')
    contents = file.readlines()
    # print(contents)
    # 记录下纯注释行的元素列表
    pop_parms = []
    rep_str = []
    for index, row in enumerate(contents):
        # 判断如果是纯注释行，记录元素
        if row.strip().startswith("#"):
            pop_parms.append(row)
        # 判断一行既有代码又有注释的行
        elif "# " in row and re.search(r'[a-z]', row):
            if not row.strip().startswith("#"):
                new_str = re.sub(r"\s\s#\s.*", '', row)
                rep_str.append((row, new_str))
    # 遍历记录的纯注释行和有注释的行，然后替换
    for i in pop_parms:
        contents.pop(contents.index(i))
    for row, new in rep_str:
        contents[contents.index(row)] = new
    # 先关闭打开的文件，再重新保存没有注释的文件
    file.close()
    # 将替换后的没有注释的内容保存到新文件中
    with open(file_name, "w+", encoding="utf-8") as f:
        f.writelines(contents)
    print(f"处理完成的文件{file_name}***********>")


if __name__ == '__main__':
    # 获取到py文件的路径[.py 路径]
    file_py_list = []
    root_path = os.path.dirname(__file__)
    # 遍历要处理的文件
    get1_path_py(file_py_list, root_path)
    print(f"一共有{len(file_py_list)}个文件==========>")
    # 遍历py文件，处理文件中的内容
    for path in file_py_list:
        content_file(path)
    print(f"处理完成了{len(file_py_list)}个文件=========>")
