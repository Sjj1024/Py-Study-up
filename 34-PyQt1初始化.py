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

    
    
    
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 使用QWidget编写与一个独立的窗口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()  # 创建一个窗体对象
    w.resize(400, 600)  # 设置窗体的大小
    w.setWindowTitle("我喜欢你")  # 设置窗体标题
    w.move(600, 300)  # 设置窗体第一次出现的位置
    w.show()  # 窗体显示
    sys.exit(app.exec_())

    
    
    
    
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wg = QWidget()
    # app设置窗体图标的话，所有窗体自动使用这个额图标
    app.setWindowIcon(QIcon("4.png"))
    # 单独窗体设置图标的话，是对这个窗体有效，这个优先于app
    wg.setWindowIcon(QIcon("3.png"))
    wg.setWindowTitle("我爱你")

    wg.show()
    sys.exit(app.exec_())

    
    
    
    
    
 # 设置提示框文字等
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wg = QWidget()
    wg.resize(500, 600)
    # 设置提示内容的文字大小等属性, 显示的内容等都是在QTGui中的
    QToolTip.setFont(QFont("微软雅黑", 20))
    wg.setWindowTitle("我爱你")
    wg.setWindowIcon(QIcon("4.png"))
    # 设置鼠标悬停提示，基本上所有的空间都包含这个setToolTip函数
    wg.setToolTip("我是谁，我在哪，我在干什么")

    # 设置一个按钮, 名字是登陆，wg是父类容器对象
    button = QPushButton("登陆", wg)
    button.setToolTip("请输入账号")  # 设置这个按钮的提示框

    wg.show()
    sys.exit(app.exec_())

    
    

    
    
# 封装类添加点击事件
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Widgetobj(QWidget):
    def __init__(self):
        # 因为要使用到父类qwidget初始化方法，所以super
        super().__init__()
        self.initUi()

    def initUi(self):
        # 因为已经继承了Qwigdet，所以没必要再实例化一个wg对象了
        # wg = QWidget()
        self.setWindowTitle("我爱你")
        # 设置gui的位置和大小的函数setGeometry,前两个是位置
        self.setGeometry(30, 40, 400, 300)
        # self.resize(400, 200)
        # 设置一个按钮
        button = QPushButton("登陆", self)
        button.move(20, 20)

        button2 = QPushButton("退出", self)
        # connect是信号槽，这个槽里放上要执行的代码
        # 信号源.信号.信号槽(执行代码不能加括号)
        button2.clicked.connect(self.close)
        button2.move(100, 20)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 配置窗体的都要封装
    wg_obj = Widgetobj()
    app.exec_()
    # sys.exit(app.exec_())

