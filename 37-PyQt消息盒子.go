import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 500, 600, 200)
        self.setWindowTitle("我爱你")
        btn1 = QPushButton("关闭窗体", self)
        btn1.move(100, 100)
        btn1.clicked.connect(self.close)
        self.show()

    # 定义自己的关闭窗体事件
    def closeEvent(self, event):
        print("关闭窗体的操作")
        # 弹出一个消息提示框，询问是否关闭，参数1是属于那个窗体，参数2是窗体名字，参数3是窗体内容
        res = QMessageBox.question(self, "老宋提示:", "你真的要关闭窗体么", QMessageBox.Yes|QMessageBox.No)
        # 判断通过窗体获得的结果是yes还是No，
        if res == QMessageBox.Yes:
            # 判断用户输入的是yes，那就执行关闭操作
            event.accept()
        else:
            # 利用传过来的参数， 阻止窗体关闭
            event.ignore()
            QMessageBox.information(self, "消息", "感谢饶命！")


# 消息对话框
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()
    
    
    
    
    
    
 C:\Users\swx829949\Envs\py_study\Scripts\python.exe D:/Pyup_study/PyQT学习/pyqt消息盒子/qt消息盒子.py
关闭窗体的操作
关闭窗体的操作
关闭窗体的操作

Process finished with exit code 0
