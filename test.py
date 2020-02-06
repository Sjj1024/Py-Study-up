import os
import re


def re_name():
    res_list = os.listdir(".")
    mp4_list = [i for i in res_list if i.endswith(".mp4")]
    re_res = re.compile(r"\(.*?\)")
    for x in mp4_list:
        res = re_res.search(x).group()
        new_name = x.replace(res, "")
        os.renames(x, new_name)
        print(f"文件{x}已经替换成{new_name}--->")


if __name__ == '__main__':
    re_name()