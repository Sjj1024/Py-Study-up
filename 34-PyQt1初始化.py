import sys
import test
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # QtWidgets是所有的控件的父类，QApplication是用来控制程序的进程，QMainWindow是控制窗口的
    app = QApplication(sys.argv)  # 这一步是必须的，意思是创建一个app进程对象
    mainWindow = QMainWindow()  # 这是创建窗口对象
    ui = test.Ui_MainWindow()  # 创建test中的ui对象
    ui.setupUi(mainWindow)  # 将窗口对象穿进去，因为这个方法需要这个窗体对象
    mainWindow.show()  # 让窗体对象显示出来
    sys.exit(app.exec_())  # 当点击叉叉退出的时候，关闭程序
    print("niaho")
