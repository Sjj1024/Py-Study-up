import sys
import jian
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = jian.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    app.exec_()