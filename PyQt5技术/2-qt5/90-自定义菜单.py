import sys
from PyQt5.Qt import *
from shouye import Ui_Form
from mess import Window2
from mess2 import Window3


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setupUi(self)
        self.setWindowTitle("我是首页")
        self.setup_ui()

    def setup_ui(self):
        # win2和win3都是QWidget页面
        self.sl = QStackedLayout()
        self.win_main.setLayout(self.sl)
        self.win2 = Window2()
        self.sl.addWidget(self.win2)
        self.win3 = Window3()
        self.sl.addWidget(self.win3)
        self.label3 = QLabel("我是视频")
        self.sl.addWidget(self.label3)

    def shouye_click(self):
        print("首页被点击了")
        self.sl.setCurrentWidget(self.win2)

    def tupian_click(self):
        print("图片被点击了")
        self.sl.setCurrentWidget(self.win3)

    def shipin_click(self):
        print("视频被点击了")
        self.sl.setCurrentWidget(self.label3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
