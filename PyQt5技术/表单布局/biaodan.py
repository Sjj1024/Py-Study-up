import sys
import biao
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = biao.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    app.exec_()