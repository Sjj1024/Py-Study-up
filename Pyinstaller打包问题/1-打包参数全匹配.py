import datetime
import inspect
import json
import os
import sys
import time
import uuid
from configparser import ConfigParser
from app.app import App


def find_txt(dir_name="app", cls_name="App"):
    # 遍历app目录中的文件，找到app路径和名字
    APP_DIR = os.path.abspath(os.path.split(__file__)[0]) + "\\app"
    file_class_dic = {}
    # 找出app文件夹下app目录
    for root, dirs, files in os.walk(APP_DIR):
        for dir in dirs:
            if "__pycache__" == dir:
                continue
            print(f"扫描路径{root}\\{dir}")
            # 从app的具体路径中加载app模块
            # Check and fix the path
            sub_module = load_app(root + "\\" + dir, App)
            file_class_dic.update(sub_module)
    return file_class_dic


def edit_applist_txt(file_class_dic):
    # 修改applist文件内容
    app_lines = ["# 此文件是自动打包EXE时必备文件，勿删！\n"]
    for name, value in file_class_dic.items():
        app_lines.append(f"from {value} import {name}\n")
    app_txt = os.path.abspath(os.path.split(__file__)[0]) + "\\applist.py"
    with open(app_txt, "w+", encoding="utf-8") as f:
        f.writelines(app_lines)
        f.close()
        print("App列表文件已经生成----------->")


def clean_applist():
    # 打包完成后，删除applist.py文件
    app_txt = os.path.abspath(os.path.split(__file__)[0]) + "\\applist.py"
    os.remove(app_txt)


def load_app(path, class_type, init_params=None):
    # Get a list of files in the directory, if the directory exists
    if not os.path.exists(path):
        raise OSError("Directory does not exist: %s" % path)
    app_dict = {}
    # Add path to the system path
    sys.path.append(path)
    # Load all the files in path
    for f in os.listdir(path):
        # Ignore anything that isn't a .py file
        if len(f) > 3 and (f[-3:] == '.py' or f[-4:] == '.pyc'):
            module_name = ''
            if f[-3:] == '.py':
                module_name = f[:-3]
            if f[-4:] == '.pyc':
                module_name = f[:-4]
            # Import the module
            __import__(module_name, globals(), locals(), [], 0)
            module = sys.modules[module_name]
            module_attrs = dir(module)
            for name in module_attrs:
                var_obj = getattr(module, name)
                if inspect.isclass(var_obj):
                    if issubclass(var_obj, class_type) and var_obj.__name__ != class_type.__name__:
                        if init_params == None:
                            app_dict[name] = "app" + path.split("\\app")[-1:][0].replace("\\", ".") + "." + module_name
                        else:
                            app_dict[name] = "app" + path.split("\\app")[-1:][0].replace("\\", ".") + "." + module_name
                        print(f"注入 {class_type.__name__} 模块 {var_obj.__name__} 成功")
    return app_dict


def package_exe(res='True'):
    root_path = os.path.abspath(os.path.split(__file__)[0])
    dist_path = root_path + "\\dist"
    spec_path = root_path + "\\start.py"
    version_path = root_path + "\\version.txt"
    exe_name = "Breeze"
    app_path = root_path + "\\app"
    business_common_lib_path = root_path + "\\business_common_lib"
    utils_path = root_path + "\\utils"
    add_data_path = f"--add-data {app_path};app --add-data {business_common_lib_path};business_common_lib --add-data {utils_path};utils"
    exe_path = dist_path + "\\Breeze.exe"
    if res:
        cmd = f"pyinstaller -F {spec_path} --distpath {dist_path} --version-file {version_path} -n {exe_name} {add_data_path} --specpath {root_path} --workpath {root_path}"
        os.system(cmd)
        while True:
            time.sleep(3)
            if os.path.exists(exe_path):
                print("打包成功！")
                return True
            else:
                print("打包中,请稍后------->")
    else:
        print("打包失败")


def get_config(section, key):
    '''
    @summary:读取工程初始化配置文件
    :param section:
    :param key:
    :return:返回的都是字符串类型
    '''
    root_path = os.path.split(__file__)[0]
    ini_path = os.path.join(root_path, "Config", "configuration.ini")  # 配置文件的地址
    print(ini_path)
    # ini_path = r'D:\02项目代码\11_传导\主干新架构\breeze-app2\Config\configuration.ini'
    config = ConfigParser()
    config.read(ini_path, encoding="utf-8")
    value = config.get(section, key)  # 获取子项
    value = value.split("#")[0].strip()
    return value


def prodect_info():
    # 生成打包信息并保存到config中
    now_time = datetime.datetime.now()
    exe_uuid = "".join(str(uuid.uuid4()).split("-"))
    print("测试用的UUID：" + exe_uuid)
    # 还应该将应用商店的IP保存下载，并生成身份校验接口
    check_url = get_config('APPSTORE', 'check_url')
    json_info = {"time": str(now_time), "uuid": exe_uuid, "check_url": check_url}
    version_file = os.path.abspath(os.path.split(__file__)[0]) + "\\utils\\exe_info"
    with open(version_file, "w", encoding="utf-8") as f:
        json.dump(json_info, f)


# 再执行打包exe命令
if __name__ == '__main__':
    prodect_info()
    app_list = find_txt()
    edit_applist_txt(app_list)
    end = package_exe()
    clean_applist()
