import errno, os, stat, shutil
import git
# 电脑上必须安装有git，并且已经配置到系统环境变量中
"""
获取本地仓的版本号，再获取远程仓中的版本号，进行对比，如果不一样，开始更新，一样就不更新
更新流程：执行命令git pull,更新后还会自动重启start.py
"""


class GitServer:
    def __init__(self):
        # 创建一个git仓库对象
        self.path = os.path.split(__file__)[0]
        self.file_name = os.path.split(__file__)[1]
        # 因为要用本地仓repo对象拉取库上代码，而拉取的时候，又需要删除本地仓代码，所以两者位置不能在一起，
        # 不然删除本地仓代码的时候，repo对象还在使用，就会报错，所以分开存储两个数据
        self.git_path = self.path + "\\repo"
        self.update = self.path + "\\update"
        self.repo = git.Repo(self.git_path)
        # 抓取远程仓库的源信息
        self.repo.remotes.origin.fetch()
        # 获取仓库的信息
        head = self.repo.references[0].commit
        fetch_head = self.repo.references[1].commit
        # 获取本地仓id
        print("本机版本:" + head.hexsha)
        self.local_id = head.hexsha
        # 获取远程仓最新版本号
        print("库上版本:" + fetch_head.hexsha)
        self.remote_id = fetch_head.hexsha
        # 获取库地址
        print("版本库地址:" + self.repo.remotes.origin.url)
        self.repo_url = self.repo.remotes.origin.url
        hcommit = self.repo.head.commit
        self.diff = hcommit.diff(None)

    # 创建错误处理handle，解决read only文件
    def handle_remove_read_only(self, func, path, exc):
        excvalue = exc[1]
        if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
            func(path)

    def pull(self, repo_url):
        # 拉取远程仓代码到本地
        print("开始拉取远程仓库代码")
        if os.path.exists(self.update):
            # 删除update文件夹
            shutil.rmtree(self.update, onerror=self.handle_remove_read_only)
        # clone完后会重新建一个updata文件夹
        clone_repo = git.Repo.clone_from(self.repo_url, self.update)  # 拉取远程代码
        clone_repo.close()
        self.repo.close()

    def del_files(self):
        # 删除原文件夹中无用的文件，除了app，本文件，updata和repo文件外，都删除
        filter_file = ["update", "app", ".idea", "repo", self.file_name]
        source_files = os.listdir(self.path)
        print(source_files, 11111111111111111)
        for remove in filter_file:
            if remove in source_files:
                source_files.remove(remove)
        print(source_files, 22222222222222)
        # 删除过滤后的没有用的源文件文件
        for file in source_files:
            if os.path.isfile(file):
                os.remove(file)
            else:
                shutil.rmtree(file)

    def move_files(self):
        print("开始复制data文件到外层，除了.git文件夹和app文件夹，")
        if os.path.exists(self.update):
            update_files = os.listdir(self.update)
            # 开始拷贝升级文件到外层文件夹中
            # 先过滤掉不要复制的文件或文件夹
            filter_file = [".git", "app", ".idea", self.file_name]
            for remove in filter_file:
                update_files.remove(remove)
            print(update_files)
            for file in update_files:
                src_path = os.path.join(self.update, file)
                dist_path = os.path.join(self.path, file)
                if os.path.isfile(src_path):
                    print(f"开始拷贝文件{src_path}到{dist_path}")
                    if os.path.exists(dist_path):
                        os.remove(dist_path)
                    shutil.copy(src_path, dist_path)
                else:
                    print(f"开始拷贝文件夹{src_path}到{self.path}")
                    if os.path.exists(dist_path):
                        # 如果目标路径存在原文件夹的话就先删除
                        shutil.rmtree(dist_path)
                    shutil.copytree(src_path, dist_path)
            # 更新完成后删除升级文件夹
            shutil.rmtree(self.git_path, onerror=self.handle_remove_read_only)
            os.renames(self.update, self.git_path)

    def run_start(self):
        print("更新完成后重新开始运行外层项目")
        cmd = "python start.pyc"
        os.system(cmd)

    def del_temp(self):
        # 删除缓存repo中的缓存文件，除了.git文件所有的都删除
        if os.path.exists(self.git_path):
            update_files = os.listdir(self.update)
            # 开始拷贝升级文件到外层文件夹中
            # 先过滤掉不要复制的文件或文件夹
            filter_file = [".git", "app", ".idea", self.file_name]

    def run(self):
        # 判断版本是否一致
        if self.local_id != self.remote_id:
            print("本地文件与库上文件有差异")
            self.pull(self.repo_url)
            self.del_files()
            self.move_files()
            self.run_start()
        else:
            print("没有差异")


if __name__ == '__main__':
    gitserver = GitServer()
    gitserver.run()
