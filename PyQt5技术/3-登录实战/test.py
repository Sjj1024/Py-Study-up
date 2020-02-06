import sys
from PyQt5.Qt import *
from shouye import Ui_Form

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setupUi(self)
        self.setWindowTitle("我是首页")

    def login_pan(self):
        print("我是登录页面阿牛")

    def regist_pan(self):
        print("我是注册页面阿牛")

    def tuichu(self):
        print("我是退出程序啊")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
