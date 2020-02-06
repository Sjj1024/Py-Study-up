import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class First(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("界面跳转", self)
        self.btn.move(30, 50)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Event sender')
        self.show()


class Second(QMainWindow):
    def __init__(self, main_pan):
        super().__init__()
        self.main_pan = main_pan
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Get sender')

    def closeEvent(self, *args, **kwargs):
        self.main_pan.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = First()
    a.show()
    b = Second(a)
    def show_2():
        a.close()
        b.show()
    a.btn.clicked.connect(show_2)
    sys.exit(app.exec_())