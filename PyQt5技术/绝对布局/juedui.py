import sys
import jue
from PyQt5.QtWidgets import QApplication, QMainWindow

# 默认的组件都是绝对布局，不会随着窗体变化而移动
# 放到容器或窗体布局中的会自动变化大小
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = jue.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    app.exec_()