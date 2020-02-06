import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是消息盒子")
        self.resize(600, 300)
        self.setWindowIcon(QIcon("close.jpg"))
        self.setup_ui()

    def setup_ui(self):
        but1 = QPushButton("点击开始", self)

        def message():
            role = QMessageBox.question(self, "确定仪表:", "确认仪表曲线正常么？", QMessageBox.Ok | QMessageBox.Discard)
            if role == QMessageBox.Ok:
                print("点击了确认按钮")
            elif role == QMessageBox.Discard:
                print("点击率取消按钮")
        but1.move(100, 100)
        but1.clicked.connect(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
