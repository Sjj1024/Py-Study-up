import json
import os
import shutil
import zipfile
import requests

from common.Common import get_config


def local_app_version():
    oneself = os.path.split(__file__)[0]
    version_file = os.path.dirname(oneself) + "\\Config\\unpack_info.txt"
    with open(version_file, encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_app_info(local_app_info):
    appStoreUrl = get_config('APPSTORE', 'appStoreUrl')
    app_findall_url = f"{appStoreUrl}/app/findAll"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    data = {"appName": local_app_info["appName"]}
    res = requests.post(app_findall_url, headers=header, data=data)
    json_str = json.loads(res.content.decode())
    app_datas = json_str["data"][0]["results"]
    # 找出最大的版本号对应的app信息
    max_version_app = {'version': local_app_info["appVersion"], "update": False}
    for app in app_datas:
        max_version = tuple(int(val) for val in max_version_app["version"].split('.'))
        app_version = tuple(int(val) for val in app["version"].split('.'))
        if app_version > max_version:
            max_version_app = app
            max_version_app["update"] = True
    # print(max_version_app)
    return max_version_app


def down_new_app(appId):
    oneself = os.path.split(__file__)[0]
    app_zip_path = os.path.join(oneself, "app.zip")
    appStoreUrl = get_config('APPSTORE', 'appStoreUrl')
    app_down_url = f"{appStoreUrl}/app/downloadApp"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    data = {"appId": appId}
    res = requests.post(app_down_url, headers=header, data=data)
    with open(app_zip_path, "wb") as f:
        f.write(res.content)
    unzip(app_zip_path, oneself)


def unzip(sourceFile, targetPath):
    '''
    :param sourceFile: 待解压zip路径
    :param targetPath: 目标文件目录
    :return:
    '''
    file = zipfile.ZipFile(sourceFile, 'r')
    file.extractall(targetPath)
    # print('success to unzip file!')


def copy_app_dist(app_name):
    # print("将原app删除并移动最新版app到app目录下")
    oneself = os.path.split(__file__)[0]
    breeze_path = os.path.dirname(oneself)
    oneself_app = os.path.join(oneself, "breeze_pyc\\app", app_name)
    dist_app_path = os.path.join(breeze_path, "app", app_name)
    # print(oneself_app)
    # print(dist_app_path)
    # 判断原app文件夹是否存在，存在就删除
    if os.path.exists(dist_app_path):
        shutil.rmtree(dist_app_path)
    shutil.copytree(oneself_app, dist_app_path)
    # 拷贝unpack_info.txt到现框架中
    oneself_unpack_info = os.path.join(oneself, "breeze_pyc\\Config\\unpack_info.txt")
    dist_unpack_path = os.path.join(breeze_path, "Config\\unpack_info.txt")
    # print(oneself_unpack_info)
    # print(dist_unpack_path)
    if os.path.exists(dist_unpack_path):
        os.remove(dist_unpack_path)
    shutil.copy(oneself_unpack_info, dist_unpack_path)


def compare_version():
    v1 = '3.2.1'
    t1 = tuple(int(val) for val in v1.split('.'))
    v2 = '3.2'
    t2 = tuple(int(val) for val in v2.split('.'))
    res = t1 < t2
    print(res)


def del_update_temp():
    # print("删除更新app产生的垃圾文件")
    oneself = os.path.split(__file__)[0]
    app_zip_path = os.path.join(oneself, "app.zip")
    temp_pyc_path = os.path.join(oneself, "breeze_pyc")
    if os.path.exists(app_zip_path):
        os.remove(app_zip_path)
    if os.path.exists(temp_pyc_path):
        shutil.rmtree(temp_pyc_path)


def app_update_run():
    local_version = local_app_version()
    app_name = local_version["appName"]
    if app_name:
        max_version_app = get_app_info(local_version)
        if max_version_app["update"]:
            print(f"发现新版本APP，开始自动更新......")
            # app需要更新走的更新分支
            app_id = int(max_version_app["id"])
            app_name = max_version_app["name"]
            down_new_app(app_id)
            copy_app_dist(app_name)
            del_update_temp()
            print("APP更新完成，正在启动Breeze......")
        # else:
        #     print("APP是最新版本")


if __name__ == '__main__':
    app_update_run()
