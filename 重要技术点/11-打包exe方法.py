 # 安装app后，打包exe文件，返回exe文件路径
    def packageApp(self, params):
        # ips = params.get("ips")
        ips = '10.142.253.100'
        # path = params.get("path")
        path = "D:\Py_main"
        appid = params.get("appid")
        exename = params.get("appname")
        # 请求安装接口安装app:
        url = "http://10.151.40.233:8071/file/install"
        code_list = []
        appid_list = appid.split(",")
        for aid in appid_list:
            data = {"ips": ips, "appId": int(aid)}
            print(data)
            res = requests.post(url=url, data=data)
            print(res.content.decode())
            res_dict = json.loads(res.content.decode())
            code_list.append(res_dict["code"])
        # 确保上述app全部安装成功
        if not all(code_list):
            return False
        # 打包exe文件
        start_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "start.py")
        cmd = f"pyinstaller -F {start_path}"
        print(cmd)
        os.popen(cmd)
        # 将exe文件拷贝到指定文件夹中
        print(code_list)
        while not os.path.exists("dist/start.exe"):
            time.sleep(5)
            continue
        new_name = f"dist/{exename}.exe"
        os.rename("dist/start.exe", new_name)
        if not os.path.exists(path):
            return False
        rel_path = shutil.copy(new_name, path)
        # 删除app文件和exe垃圾文件
        if os.path.exists("dist"):
            shutil.rmtree("dist")
        if os.path.exists("start.spec"):
            os.remove("start.spec")
        if os.path.exists("build"):
            shutil.rmtree("build")
        file_list = os.listdir(os.path.dirname(os.path.dirname(__file__)))
        for i in file_list:
            if os.path.isdir(i):
                if i not in ["__pycache__", "tool_pypi"]:
                    shutil.rmtree(i)
        # 返回exe文件路径
        return True
