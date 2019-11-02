import sys
import shan
from PyQt5.QtWidgets import QApplication, QMainWindow
# 栅格布局中尽量将各组件排放成栅格形式
# 不然系统有时候识别不出来是栅格布局

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = shan.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    app.exec_()