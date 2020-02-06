# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#要注意的是跳转界面第二个必须使用QDialog类，不能使用QWidget，我也不知道为什么，特别注意
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import Dialog1
import Dialog2
import sys


class Ui_Form(object):  #这是用PyQt Designer生成的代码，很简单的，拖动控件，生成ui文件，然后UIC转换成py文件
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 310)
        self.form = Form
        self.btn_d1 = QtWidgets.QPushButton(Form)
        self.btn_d1.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.btn_d1.setObjectName("btn_d1")
        self.btn_d2 = QtWidgets.QPushButton(Form)
        self.btn_d2.setGeometry(QtCore.QRect(180, 140, 75, 23))
        self.btn_d2.setObjectName("btn_d2")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.btn_exit.setObjectName("btn_exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_d1.setText(_translate("Form", "Demo1"))
        self.btn_d1.clicked.connect(self.jump_to_demo1)
        self.btn_d2.setText(_translate("Form", "Demo2"))
        self.btn_d2.clicked.connect(self.jump_to_demo2)
        self.btn_exit.setText(_translate("Form", "Exit"))
        self.btn_exit.clicked.connect(self.exit)

    def jump_to_demo1(self):        #这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面
        self.form.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
        form1 = QtWidgets.QDialog()
        ui = Dialog1.Ui_Dialog1()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_demo2(self):
        self.form.hide()
        form2 = QtWidgets.QDialog()
        ui = Dialog2.Ui_Dialog2()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        self.form.show()

    def exit(self):
        self.form.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())