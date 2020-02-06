import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是进度条")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.setRange(0, 100)
        pb.setValue(50)

        timer = QTimer(pb)

        def done():
            print("开始计时")
            pb.setValue(pb.value() + 1)

        timer.timeout.connect(done)
        timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
