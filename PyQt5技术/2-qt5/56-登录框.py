import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是登录框")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        line1 = QLineEdit(self)
        line1.move(100, 100)
        line2 = QLineEdit(self)
        line2.move(100, 150)
        line2.setEchoMode(QLineEdit.Password)
        line1.setPlaceholderText("请输入账号")
        line1.setClearButtonEnabled(True)
        completer = QCompleter(["song", "wang", "songjiang", "shun"], line1)
        line1.setCompleter(completer)
        # 设置掩码格式为IP地址
        line1.setInputMask("999.999.999.999;*")
        line2.setClearButtonEnabled(True)
        action1 = QAction(line2)
        action1.setIcon(QIcon("close.jpg"))
        def change_yan():
            print("行为被点击了")
            if line2.echoMode() == QLineEdit.Password:
                line2.setEchoMode(QLineEdit.Normal)
                action1.setIcon(QIcon("open.jpg"))
            else:
                line2.setEchoMode(QLineEdit.Password)
                action1.setIcon(QIcon("close.jpg"))
        action1.triggered.connect(change_yan)
        line2.addAction(action1, QLineEdit.TrailingPosition)

        def echo_data():
            print("按钮被点击了")
            print(line1.text(), line2.text())
        but1 = QPushButton(self)
        but1.setText("登录")
        but1.move(120, 200)
        but1.clicked.connect(echo_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
