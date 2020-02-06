import sys
from PyQt5.Qt import *
from shouye_pan import Shou_Ye
from login_pan import Login
from regist_pan import Regist


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Shou_Ye()
    # 点击登录按钮发射的信号
    def show_login_pan():
        print("开始展示登录界面")
        login_obj = Login(win)
        # login_obj.move(win.height(), win.wight())
        login_obj.show()

    win.show_login_pan_signel.connect(show_login_pan)

    win.show()
    sys.exit(app.exec_())
