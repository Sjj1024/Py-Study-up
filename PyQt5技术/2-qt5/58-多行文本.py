import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是多行文本")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("退出我是爱你的，我真的爱你的，我是真的")
        label.setMaximumSize(200, 40)
        label.setWordWrap(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
