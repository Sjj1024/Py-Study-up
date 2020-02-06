import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是省市联调")
        self.resize(600, 300)
        self.city = {
            "河南": {
                "洛阳": "1",
                "郑州": "2",
                "开封": "3",
                "禹州": "4"
            },
            "上海": {
                "浦东": "1",
                "惠济": "2",
                "市区": "3",
                "新蔡": "4"
            },
            "北京": {
                "朝阳": "1",
                "新开": "2",
                "南阳": "3",
                "国立": "4"
            }
        }
        self.setup_ui()

    def setup_ui(self):
        self.comb1 = QComboBox(self)
        self.comb2 = QComboBox(self)
        self.comb1.move(100, 100)
        self.comb2.move(200, 100)
        # 在下拉1中添加条目
        self.comb1.addItems(self.city.keys())

        # 监听当条目一改变的时候，触发条木二内容改变
        self.comb1.currentIndexChanged[str].connect(self.change2)
        self.change2(self.comb1.currentText())

    def change2(self, p_name):
        print("条目2被触发了", p_name)
        self.comb2.clear()
        self.comb2.addItems(self.city[p_name].keys())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
