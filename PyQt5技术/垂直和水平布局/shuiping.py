import sys
import shui
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = shui.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    app.exec_()