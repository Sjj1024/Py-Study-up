import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是文件选择")
        self.resize(600, 300)
        self.setup_ui()

    def setup_ui(self):
        def click_but():
            file = QFileDialog(self)
            file.setAcceptMode(QFileDialog.AcceptSave)
            file.setDefaultSuffix("txt")
            file.open() 
            file.fileSelected.connect(lambda x:print("文件选择了", x))
            # res = file.getOpenFileName(self, "请选择文件", "./", "ALL(*.*);;Image(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # res = file.getOpenFileNames(self, "请选择文件", "./", "ALL(*.*);;Image(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # res = file.getSaveFileName(self, "请选择文件", "./", "ALL(*.*);;Image(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # res = file.getExistingDirectory(self, "请选择文件夹", "./")
            # print(res)
        but1 = QPushButton(self)
        but1.setText("选择文件")
        but1.clicked.connect(click_but)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
