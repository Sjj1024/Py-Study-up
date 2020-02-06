import sys
from PyQt5.Qt import *
from mess import Window2
from mess2 import Window3


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是堆叠布局")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        sl = QStackedLayout()
        self.setLayout(sl)
        # 在布局中添加子控件
        # 设置一个水平布局对象，添加到最上方
        h_layout = QHBoxLayout()
        but1 = QPushButton("首页")
        but2 = QPushButton("文件")
        but3 = QPushButton("视图")
        h_layout.addWidget(but1)
        h_layout.addWidget(but2)
        h_layout.addWidget(but3)

        label1 = QLabel("我是首页")
        label2 = QLabel("我是图片")
        label3 = QLabel("我是视频")

        # 将子控件添加到堆叠布局中
        menu = QMenuBar(self)
        menu.resize(400, 30)
        menu.addAction("首页")
        menu.addAction("图片")
        menu.addAction("视频")
        sl.setMenuBar(menu)
        # sl.addWidget(label1)
        # sl.addWidget(label2)
        # sl.addChildLayout(h_layout)
        win2 = Window2()
        sl.addWidget(win2)
        win3 = Window3()
        sl.addWidget(win3)
        sl.addWidget(label3)
        def menu_click(action):
            print(1111111, action.text())
            if action.text() == "首页":
                sl.setCurrentWidget(win2)
            elif action.text() == "图片":
                self.setWindowTitle("我是图片页面")
                sl.setCurrentWidget(win3)
            elif action.text() == "视频":
                sl.setCurrentWidget(label3)
        menu.triggered.connect(menu_click)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
