# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startUp\chabge.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiChange(object):
    def setup3(self, StartUpWindow):
        StartUpWindow.setObjectName("StartUpWindow")
        StartUpWindow.resize(675, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartUpWindow.sizePolicy().hasHeightForWidth())
        StartUpWindow.setSizePolicy(sizePolicy)
        StartUpWindow.setMinimumSize(QtCore.QSize(675, 400))
        StartUpWindow.setMaximumSize(QtCore.QSize(675, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/240_F_40168915_iAdNkVXaarz2aMDnHnEC4Y2b0KwdbQ69.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartUpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StartUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.old = QtWidgets.QLineEdit(self.centralwidget)
        self.old.setGeometry(QtCore.QRect(280, 20, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.old.setFont(font)
        self.old.setText("")
        self.old.setAlignment(QtCore.Qt.AlignCenter)
        self.old.setObjectName("old")
        self.new_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(280, 90, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.new_2.setFont(font)
        self.new_2.setText("")
        self.new_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_2.setObjectName("new_2")
        self.confirm = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(280, 160, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.confirm.setFont(font)
        self.confirm.setText("")
        self.confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm.setObjectName("confirm")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 270, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        StartUpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartUpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 21))
        self.menubar.setObjectName("menubar")
        StartUpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartUpWindow)
        self.statusbar.setObjectName("statusbar")
        StartUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartUpWindow)
        QtCore.QMetaObject.connectSlotsByName(StartUpWindow)

    def retranslateUi(self, StartUpWindow):
        _translate = QtCore.QCoreApplication.translate
        StartUpWindow.setWindowTitle(_translate("StartUpWindow", "StartUpWindow"))
        self.label.setText(_translate("StartUpWindow", "old password"))
        self.label_2.setText(_translate("StartUpWindow", "new password"))
        self.label_3.setText(_translate("StartUpWindow", "confirm"))
        self.old.setStatusTip(_translate("StartUpWindow", "enter your old password here"))
        self.new_2.setStatusTip(_translate("StartUpWindow", "enter your new password here"))
        self.confirm.setStatusTip(_translate("StartUpWindow", "confirm your new password"))
        self.pushButton.setStatusTip(_translate("StartUpWindow", "confirm changes"))
        self.pushButton.setText(_translate("StartUpWindow", "confirm"))
        self.pushButton.setShortcut(_translate("StartUpWindow", "Return"))