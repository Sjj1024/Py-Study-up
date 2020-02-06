import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是标题")
        self.resize(600, 300)
        # self.setup_ui()
        self.panduan()


    def setup_ui(self):
        label = QLabel(self)
        label.setText("退出")

    def panduan(self):
        obj1 = QObject()
        qbut = QPushButton()
        qlabel = QLabel()
        print(obj1.isWidgetType())
        print(qbut.isWidgetType())
        print(qlabel.isWidgetType())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
