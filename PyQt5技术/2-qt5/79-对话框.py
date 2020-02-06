import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是对话框")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        d = QDialog(self)
        but1 = QPushButton(d)
        but2 = QPushButton(d)
        but1.move(100, 100)
        but2.move(180, 100)
        but1.setText("确认")
        but2.setText("取消")
        but1.setDefault(True)

        def res_but1():
            d.accept()
            print(d.result(), 1111111111)

        but1.clicked.connect(res_but1)
        but2.clicked.connect(lambda: d.reject())
        # d.open()
        # res = d.result()
        # print("结果是：", res)
        but3 = QPushButton(self)
        but3.setText("弹出")
        but3.clicked.connect(lambda: d.show())

        d.accepted.connect(lambda :print("点击了接收按钮"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
