# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main\update.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(666, 484)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.redo = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.redo.setFont(font)
        self.redo.setObjectName("redo")
        self.gridLayout.addWidget(self.redo, 13, 0, 1, 2)
        self.password = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic Semilight")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 9, 0, 1, 2)
        self.name = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.ok = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 12, 0, 1, 2)
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic Semilight")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 7, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.do_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.do_2.setFont(font)
        self.do_2.setObjectName("do_2")
        self.gridLayout.addWidget(self.do_2, 6, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 10, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.redo.setStatusTip(_translate("Form", "generate a different one"))
        self.redo.setText(_translate("Form", "regenerate"))
        self.password.setStatusTip(_translate("Form", "your password is here"))
        self.name.setStatusTip(_translate("Form", "account name"))
        self.ok.setStatusTip(_translate("Form", "accept this password"))
        self.ok.setText(_translate("Form", "accept"))
        self.title.setText(_translate("Form", "your password goes here : "))
        self.label.setText(_translate("Form", "name          "))
        self.do_2.setStatusTip(_translate("Form", "generate a password"))
        self.do_2.setText(_translate("Form", "generate"))
        self.do_2.setShortcut(_translate("Form", "Return"))
