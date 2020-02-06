import sys
from PyQt5.Qt import *
from regist import Regist_Form

class Regist(QWidget, Regist_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=None, *args, **kwargs)
        self.resize(600, 300)
        self.setupUi(self)
        self.setWindowTitle("我是注册框")

    def get_parent(self, main_pan):
        self.main_pan = main_pan

    def login(self):
        print("我是登录页的登录按钮")

    def closeEvent(self, QCloseEvent):
        self.main_pan.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Regist()
    win.show()
    sys.exit(app.exec_())
