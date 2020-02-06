import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是颜色对话框")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        cd = QColorDialog(self)
        cd.open()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
