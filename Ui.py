# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        Form.setMinimumSize(QtCore.QSize(300, 400))
        Form.setMaximumSize(QtCore.QSize(300, 400))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setObjectName("btn")
        self.gridLayout.addWidget(self.btn, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "окружность"))
        self.btn.setText(_translate("Form", "ОКРУЖНОСТЬ"))
