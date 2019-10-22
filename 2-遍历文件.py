ospath_file = []
    # root是文件根目录，dirname是这个根目录下的文件夹列表，filename是这个根目录下文件列表
    for root, dirname, filename in os.walk(os.path.dirname(__file__)):
        for i in filename:
            # 所以才可以使用os.path.join将root和dirname连接起来
            print(root)
            print(11111111111111111)
            print(dirname)
            ospath_file.append(os.path.join(root, i))
