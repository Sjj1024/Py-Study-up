import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
# 电脑上必须安装有git，并且已经配置到系统环境变量中


class GitServer:
    def __init__(self):
        # 创建一个git仓库对象
        print(os.path.split(__file__)[0])
        self.repo = git.Repo(os.path.split(__file__)[0])
        commit_message = [str(i.message) for i in self.repo.iter_commits()]
        print(commit_message)
        print(len(commit_message))
        commit_ids = [str(i.hexsha) for i in self.repo.iter_commits()]
        print(commit_ids)
        print(len(commit_ids))



    def run(self):
        print(os.path.split(__file__)[0])


if __name__ == '__main__':
    gitserver = GitServer()
    gitserver.run()
