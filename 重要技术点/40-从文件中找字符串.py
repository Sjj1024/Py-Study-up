import os


def find_file():
    file_list = []
    for root, path, file in os.walk(os.path.dirname(__file__)):
        for i in file:
            file_list.append(os.path.join(root, i))
    return file_list


def find_str(file_list, fstr):
    for i in file_list:
        if i.endswith("php") or i.endswith("js"):
            print(f"开始搜查文件{i}..........")
            with open(i, "r", encoding="utf-8") as f:
                content = f.read()
                if fstr in content:
                    print(f"{i}此文件中包含有------------->{fstr}")


if __name__ == '__main__':
    fstr = "mouseover"
    f_list = find_file()
    find_str(f_list, fstr)
    print("程序执行完成----------->")
