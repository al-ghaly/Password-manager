# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main\new.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setup1(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 484)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 3, 0, 1, 2)
        self.ok = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 8, 1, 1, 1)
        self.email = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.email.setFont(font)
        self.email.setText("")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.redo = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.redo.setFont(font)
        self.redo.setObjectName("redo")
        self.gridLayout.addWidget(self.redo, 8, 0, 1, 1)
        self.do_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.do_2.setFont(font)
        self.do_2.setObjectName("do_2")
        self.gridLayout.addWidget(self.do_2, 4, 0, 1, 2)
        self.password = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 6, 0, 1, 2)
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setStatusTip(_translate("Form", "account name"))
        self.ok.setStatusTip(_translate("Form", "accept this password"))
        self.ok.setText(_translate("Form", "accept"))
        self.email.setStatusTip(_translate("Form", "account e-mail"))
        self.label.setText(_translate("Form", "name"))
        self.label_2.setText(_translate("Form", "e-mail"))
        self.redo.setStatusTip(_translate("Form", "generate a different one"))
        self.redo.setText(_translate("Form", "regenerate"))
        self.do_2.setStatusTip(_translate("Form", "generate a password"))
        self.do_2.setText(_translate("Form", "generate"))
        self.do_2.setShortcut(_translate("Form", "Return"))
        self.password.setStatusTip(_translate("Form", "your password is here"))
        self.title.setText(_translate("Form", "your password goes here :"))
