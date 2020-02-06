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


def extractzip():
    ziplist = os.listdir("packzip")
    source_path = os.path.join(os.path.dirname(__file__), "source")
    if not os.path.exists(source_path):
        os.makedirs(source_path)
    for i in ziplist:
        i = "./packzip/" + i
        f = zipfile.ZipFile(i, 'r')
        f.extractall(source_path)
        f.close()


if __name__ == '__main__':
    # filelist = find_file()
    # pack_zip(filelist)
    extractzip()
