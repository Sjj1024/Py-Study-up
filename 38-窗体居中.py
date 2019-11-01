import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyCount(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("我爱你")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.desktop()就是一个窗体对象，通过这个对象可以获取到屏幕信息
    # wd = app.desktop()
    # print(wd.width())
    mc = MyCount()
    # mc.move(wd.width()/2, 50)
    app.exec_()
