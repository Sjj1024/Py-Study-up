import sys
from PyQt5.Qt import *


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是消息盒子")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        but1 = QPushButton("点击开始", self)
        ms = QMessageBox(self)
        ms.setWindowTitle("请确认:")
        ms.setText("请确认仪表的曲线正常？")
        ms.setInformativeText("（确认无误再操作哦）")
        ms.addButton("确认", QMessageBox.YesRole)
        ms.addButton("取消", QMessageBox.NoRole)

        def message():
            ms.show()
        but1.move(100, 100)
        but1.clicked.connect(message)
        def queren(but):
            print("按钮被点击了", but)
            role = ms.buttonRole(but)
            if role == QMessageBox.YesRole:
                print("点击了确认按钮")
            else:
                print("点击了取消按钮")
        ms.buttonClicked.connect(queren)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window2()
    win.show()
    sys.exit(app.exec_())
