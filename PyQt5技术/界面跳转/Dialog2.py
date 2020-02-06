# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
import sys


class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(400, 300)
        self.dialog = Dialog2
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.pushButton.setText(_translate("Dialog2", "Jump to main"))
        self.pushButton.clicked.connect(self.go_main)

    def go_main(self):
        self.dialog.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())