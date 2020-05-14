# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startUp\startupwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartUpWindow(object):
    def setup2(self, StartUpWindow):
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
        icon.addPixmap(QtGui.QPixmap("./images/240_F_40168915_iAdNkVXaarz2aMDnHnEC4Y2b0KwdbQ69.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartUpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StartUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.passwordit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.passwordit.setFont(font)
        self.passwordit.setText("")
        self.passwordit.setObjectName("passwordit")
        self.gridLayout.addWidget(self.passwordit, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 4)
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
        self.passwordit.setStatusTip(_translate("StartUpWindow", "enter your password here"))
        self.label.setText(_translate("StartUpWindow", "password"))
        self.pushButton.setStatusTip(_translate("StartUpWindow", "log into your account"))
        self.pushButton.setText(_translate("StartUpWindow", "log in"))
        self.pushButton.setShortcut(_translate("StartUpWindow", "Return"))
        self.pushButton_2.setStatusTip(_translate("StartUpWindow", "change your password"))
        self.pushButton_2.setText(_translate("StartUpWindow", "change password"))
        self.pushButton_2.setShortcut(_translate("StartUpWindow", "Esc"))
