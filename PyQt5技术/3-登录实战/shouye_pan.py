import sys
from PyQt5.Qt import *
from shouye import Ui_Form
from login_pan import Login
from regist_pan import Regist


class Shou_Ye(QWidget, Ui_Form):
    show_login_pan_signel = pyqtSignal()

    def __init__(self, login_pan, regist_pan):
        super().__init__()
        self.resize(600, 300)
        self.setupUi(self)
        self.setWindowTitle("我是首页")

    def login_pan(self):
        print("我是登录页面阿牛")
        # self.show_login_pan_signel.emit()
        login_pan.get_parent(self)
        login_pan.show()
        self.close()

    def regist_pan(self):
        print("我是注册页面阿牛")
        regist_pan.get_parent(self)
        regist_pan.show()
        self.close()

    def tuichu(self):
        print("我是退出程序啊")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pan = Login()
    regist_pan = Regist()
    win = Shou_Ye(login_pan, regist_pan)
    win.show()
    sys.exit(app.exec_())
