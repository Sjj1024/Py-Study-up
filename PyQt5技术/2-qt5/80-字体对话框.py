import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是字体对话框")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        fnt = QFont("宋体", 36)
        fd = QFontDialog(fnt, self)
        fd.open()

        fd.fontSelected.connect(lambda: print("字体被选中了", fd.selectedFont()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
