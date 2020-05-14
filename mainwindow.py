# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from updateWindow import *
from generateWindow import *
from change import *
from startupwindow import *


class Ui_MainWindow(object):
    def new_window(self):
        self.update_window.show()

    def gen(self):
        self.generate_window.show()

    def change(self):
        self.change_window.show()

    def setupUi(self, MainWindow):

        self.start_up_window = QtWidgets.QMainWindow()
        self.ui_start = Ui_StartUpWindow()
        self.ui_start.setup2(self.start_up_window)

        self.change_window = QtWidgets.QMainWindow()
        self.ui_change = UiChange()
        self.ui_change.setup3(self.change_window)

        self.update_window = QtWidgets.QWidget()
        self.ui_update = Ui_Form()
        self.ui_update.setup(self.update_window)

        self.generate_window = QtWidgets.QWidget()
        self.ui_generate = Ui_Form1()
        self.ui_generate.setup1(self.generate_window)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 558)
        MainWindow.setBaseSize(QtCore.QSize(100, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/240_F_40168915_iAdNkVXaarz2aMDnHnEC4Y2b0KwdbQ69.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.show = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.show.sizePolicy().hasHeightForWidth())
        self.show.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.show.setFont(font)
        self.show.setObjectName("show")
        self.gridLayout.addWidget(self.show, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.show_all = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.show_all.sizePolicy().hasHeightForWidth())
        self.show_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.show_all.setFont(font)
        self.show_all.setObjectName("show_all")
        self.gridLayout.addWidget(self.show_all, 2, 1, 1, 2)
        self.new_2 = QtWidgets.QPushButton(self.centralwidget)
        self.new_2.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.new_2.setFont(font)
        self.new_2.setObjectName("new_2")
        self.gridLayout.addWidget(self.new_2, 4, 0, 1, 2)
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.copy.sizePolicy().hasHeightForWidth())
        self.copy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        self.gridLayout.addWidget(self.copy, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.update.setFont(font)
        self.update.setObjectName("update")
        self.gridLayout.addWidget(self.update, 4, 2, 1, 2)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        self.menuinfo = QtWidgets.QMenu(self.menubar)
        self.menuinfo.setObjectName("menuinfo")
        self.menuname = QtWidgets.QMenu(self.menuinfo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/name.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuname.setIcon(icon1)
        self.menuname.setObjectName("menuname")
        self.menuphone = QtWidgets.QMenu(self.menuinfo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/240_F_223214507_mocKVnVwSHgiwJSx6lGqh0rr1penAqJm.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuphone.setIcon(icon2)
        self.menuphone.setObjectName("menuphone")
        self.menugithub = QtWidgets.QMenu(self.menuinfo)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/240_F_250305943_sDC6la1N1fDl3bLgfLxOkQwItIodsdMb.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menugithub.setIcon(icon3)
        self.menugithub.setObjectName("menugithub")
        self.menutwitter = QtWidgets.QMenu(self.menuinfo)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/twitter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menutwitter.setIcon(icon4)
        self.menutwitter.setObjectName("menutwitter")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.generate = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/keepass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generate.setIcon(icon5)
        self.generate.setObjectName("generate")
        self.actionshow = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./images/visible.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionshow.setIcon(icon6)
        self.actionshow.setObjectName("actionshow")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncopy.setIcon(icon7)
        self.actioncopy.setObjectName("actioncopy")
        self.actionshow_list = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./images/show-property.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionshow_list.setIcon(icon8)
        self.actionshow_list.setObjectName("actionshow_list")
        self.actionnew = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew.setIcon(icon9)
        self.actionnew.setObjectName("actionnew")
        self.actionupdate = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./images/240_F_160797417_qRtSGL5d8aLRmyXkgTQrFwDtDGVcf2lL.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionupdate.setIcon(icon10)
        self.actionupdate.setObjectName("actionupdate")
        self.actionexit = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./images/240_F_238878356_MEtXA2GdF94LwiD4X9PmKQbe78Vvn1j0.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionexit.setIcon(icon11)
        self.actionexit.setObjectName("actionexit")
        self.actionmohamed_alghaly = QtWidgets.QAction(MainWindow)
        self.actionmohamed_alghaly.setIcon(icon1)
        self.actionmohamed_alghaly.setObjectName("actionmohamed_alghaly")
        self.action_201002929690 = QtWidgets.QAction(MainWindow)
        self.action_201002929690.setIcon(icon2)
        self.action_201002929690.setObjectName("action_201002929690")
        self.actional_ghaly = QtWidgets.QAction(MainWindow)
        self.actional_ghaly.setIcon(icon3)
        self.actional_ghaly.setObjectName("actional_ghaly")
        self.actionmohamed32093140 = QtWidgets.QAction(MainWindow)
        self.actionmohamed32093140.setIcon(icon4)
        self.actionmohamed32093140.setObjectName("actionmohamed32093140")
        self.about = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./images/240_F_198708731_7yig2XvymXxS81SmMiETKBphaVRhvEst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon12)
        self.about.setObjectName("about")
        self.menumenu.addAction(self.generate)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionshow)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actioncopy)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionshow_list)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionnew)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionupdate)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionexit)
        self.menuname.addAction(self.actionmohamed_alghaly)
        self.menuphone.addAction(self.action_201002929690)
        self.menugithub.addAction(self.actional_ghaly)
        self.menutwitter.addAction(self.actionmohamed32093140)
        self.menuinfo.addAction(self.menuname.menuAction())
        self.menuinfo.addSeparator()
        self.menuinfo.addAction(self.menuphone.menuAction())
        self.menuinfo.addSeparator()
        self.menuinfo.addAction(self.menugithub.menuAction())
        self.menuinfo.addSeparator()
        self.menuinfo.addAction(self.menutwitter.menuAction())
        self.menuhelp.addAction(self.about)
        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menuinfo.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionshow.triggered.connect(self.show.click)
        self.actioncopy.triggered.connect(self.copy.click)
        self.actionshow_list.triggered.connect(self.show_all.click)
        self.actionupdate.triggered.connect(self.update.click)
        self.actionnew.triggered.connect(self.new_2.click)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.name, self.copy)
        MainWindow.setTabOrder(self.copy, self.show_all)
        MainWindow.setTabOrder(self.show_all, self.show)
        MainWindow.setTabOrder(self.show, self.new_2)
        MainWindow.setTabOrder(self.new_2, self.update)

        self.new_2.clicked.connect(self.gen)
        self.update.clicked.connect(self.new_window)
        self.ui_start.pushButton_2.clicked.connect(self.change)
        self.start_up_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.show.setStatusTip(_translate("MainWindow", "show the generated password"))
        self.show.setText(_translate("MainWindow", "Show"))
        self.label.setText(_translate("MainWindow", "name"))
        self.show_all.setStatusTip(_translate("MainWindow", "show all existed info"))
        self.show_all.setText(_translate("MainWindow", "Show All"))
        self.new_2.setStatusTip(_translate("MainWindow", "generate a new account record"))
        self.new_2.setText(_translate("MainWindow", "Generate New"))
        self.copy.setStatusTip(_translate("MainWindow", "copy the generated password to the clipboard"))
        self.copy.setText(_translate("MainWindow", "Copy"))
        self.update.setStatusTip(_translate("MainWindow", "update an existing account"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.name.setStatusTip(_translate("MainWindow", "inter your account name here"))
        self.menumenu.setTitle(_translate("MainWindow", "menu"))
        self.menuinfo.setTitle(_translate("MainWindow", "about me"))
        self.menuname.setStatusTip(_translate("MainWindow", "my name"))
        self.menuname.setTitle(_translate("MainWindow", "name"))
        self.menuphone.setStatusTip(_translate("MainWindow", "my phone number"))
        self.menuphone.setTitle(_translate("MainWindow", "phone"))
        self.menugithub.setStatusTip(_translate("MainWindow", "github username"))
        self.menugithub.setTitle(_translate("MainWindow", "github"))
        self.menutwitter.setStatusTip(_translate("MainWindow", "twitter username"))
        self.menutwitter.setTitle(_translate("MainWindow", "twitter"))
        self.menuhelp.setStatusTip(_translate("MainWindow", "about the application"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.generate.setText(_translate("MainWindow", "generate"))
        self.generate.setStatusTip(_translate("MainWindow", "generate a new password"))
        self.generate.setShortcut(_translate("MainWindow", "Return"))
        self.actionshow.setText(_translate("MainWindow", "show"))
        self.actionshow.setStatusTip(_translate("MainWindow", "show the generated password"))
        self.actionshow.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actioncopy.setStatusTip(_translate("MainWindow", "copy the password"))
        self.actioncopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionshow_list.setText(_translate("MainWindow", "show list"))
        self.actionshow_list.setStatusTip(_translate("MainWindow", "show all records"))
        self.actionshow_list.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionnew.setStatusTip(_translate("MainWindow", "add new account"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionupdate.setText(_translate("MainWindow", "update"))
        self.actionupdate.setStatusTip(_translate("MainWindow", "update an account"))
        self.actionupdate.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionexit.setStatusTip(_translate("MainWindow", "quit the application"))
        self.actionexit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionmohamed_alghaly.setText(_translate("MainWindow", "mohamed alghaly"))
        self.action_201002929690.setText(_translate("MainWindow", "+201002929690"))
        self.actional_ghaly.setText(_translate("MainWindow", "al-ghaly"))
        self.actionmohamed32093140.setText(_translate("MainWindow", "mohamed32093140"))
        self.about.setText(_translate("MainWindow", "about the app"))
        self.about.setShortcut(_translate("MainWindow", "Ctrl+A"))
