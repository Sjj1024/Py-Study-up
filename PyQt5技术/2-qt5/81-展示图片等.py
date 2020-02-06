import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是展示图片的")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        # pic = QPixmap("close.jpg")
        # label.setPixmap(pic)
        gif = QMovie("timg.gif")
        gif.setScaledSize(QSize(600, 300))
        label.setMovie(gif)
        gif.start()
        # 设置速度的
        gif.setSpeed(200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
