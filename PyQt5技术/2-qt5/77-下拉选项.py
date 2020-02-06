import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是下拉选项")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        combox = QComboBox(self)
        combox.addItems(["1", "2", "3", "4"])
        combox.move(100, 100)
        combox.resize(100, 20)
        # print(combox.currentText())
        combox.setEditable(True)


        but1 = QPushButton(self)
        but1.setText("获取内容")
        but1.move(100, 200)
        def get_t():
            print(combox.currentText())
            print(combox.count())
        but1.clicked.connect(get_t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
