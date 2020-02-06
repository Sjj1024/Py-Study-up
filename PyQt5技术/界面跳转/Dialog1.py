# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(400, 300)
        self.dialog=Dialog1
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Dialog"))
        self.pushButton.setText(_translate("Dialog1", "Jump to main"))
        self.pushButton.clicked.connect(self.jump_to_main)

    def jump_to_main(self):
        self.dialog.close()