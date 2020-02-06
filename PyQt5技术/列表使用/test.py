import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是列表")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        qlist = QListWidget(self)
        qlist.addItem("我是1号")
        qlist.addItem("我是2号")
        qlist.addItem("我是3号")
        qlist.addItem("我是4号")
        qlist.itemClicked.connect(self.get_some)
        self.qlist = qlist

    def get_some(self, evt):
        print("点击了")
        print(self.qlist.currentItem().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
