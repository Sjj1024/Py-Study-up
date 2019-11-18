import os
import zipfile


# 遍历此文件夹中的文件
def find_file():
    file_list = os.listdir(os.getcwd())
    file_list.remove(os.path.relpath(__file__))
    print(file_list)
    return file_list


def pack_zip(file_list):
    """
    将文件压缩到指定文件夹中
    :param file_list:
    :return:
    """
    for i in file_list:
        filename = i.split(".")[0]
        zippath = "packzip/" + filename + ".zip"
        if not os.path.exists("packzip"):
            os.makedirs("packzip")
        f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
        f.write(i)
        f.close()


if __name__ == '__main__':
    filelist = find_file()
    pack_zip(filelist)
