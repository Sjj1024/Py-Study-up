参考链接:https://blog.csdn.net/Tri_C/article/details/99862201

应用实例:删除.git文件夹时报权限异常


import os
import shutil
import errno, os, stat, shutil
import git
# 电脑上必须安装有git，并且已经配置到系统环境变量中
"""
获取本地仓的版本号，再获取远程仓中的版本号，进行对比，如果不一样，开始更新，一样就不更新
更新流程：执行命令git pull,更新后还会自动重启start.py
"""


# 创建错误处理handle， 解决read only文件
def handle_remove_read_only(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)


class GitServer:
    def __init__(self):
        # 创建一个git仓库对象
        self.path = os.path.split(__file__)[0]
        self.update = self.path + "\\update"
        self.repo = git.Repo(self.path)
        # 取远程仓库的源信息
        self.repo.remotes.origin.fetch()

        # 获取仓库的信息
        head = self.repo.references[0].commit
        fetch_head = self.repo.references[1].commit
        # 获取本地仓id
        print("本机版本:" + head.hexsha)
        # 获取远程仓最新版本号
        print("库上版本:" + fetch_head.hexsha)
        # 获取库地址
        print("版本库地址:" + self.repo.remotes.origin.url)
        self.repo_url = self.repo.remotes.origin.url
        hcommit = self.repo.head.commit
        self.diff = hcommit.diff(None)

    def pull(self, repo_url):
        # 拉取远程仓代码到本地
        print("开始拉取远程仓库代码")
        if os.path.exists(self.update):
            # 删除update文件夹
            shutil.rmtree(self.update, onerror=handle_remove_read_only)
        # clone完后会重新建一个updata文件夹
        clone_repo= git.Repo.clone_from(self.repo_url, self.update) #拉取远程代码


    def move_data(self):
        print("开始剪切data文件到外层")
        if os.path.exists(self.update):
            print(os.listdir(self.update))

    def run_start(self):
        print("更新完成后重新开始运行外层项目")

    def run(self):
        # 判断版本是否一致
        if len(self.diff) > 0:
            print("本地文件与库上文件有差异")
            self.pull(self.repo_url)

        else:
            print("没有差异")


if __name__ == '__main__':
    gitserver = GitServer()
    gitserver.run()

