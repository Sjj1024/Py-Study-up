import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, Qlabel


# 相对布局会随着窗体的变化而变化。
# 绝对布局不会随着窗体的变化而变化
class Mycount(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("我爱你")
        self.setGeometry(400, 300, 600, 300)
        lbcode = Qlabel


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = Mycount()
    app.exec_()
