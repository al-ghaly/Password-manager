import sys
from pyperclip import copy
from PyQt5 import QtWidgets as Widget
import mainwindow
from random import randint, shuffle, sample
from shelve import open

data_base = open('data_base', writeback=True)

key = {'A': 559, 'B': 372, 'C': 334, 'D': 805, 'E': 782, 'F': 803, 'G': 850, 'H': 193, 'I': 471, 'J': 608, 'K': 514,
       'L': 986, 'M': 67, 'N': 804, 'O': 876, 'P': 813, 'Q': 256, 'R': 310, 'S': 101, 'T': 474, 'U': 315, 'V': 968,
       'W': 726, 'X': 490, 'Y': 776, 'Z': 341, 'a': 719, 'b': 353, 'c': 160, 'd': 93, 'e': 658, 'f': 133, 'g': 56,
       'h': 723, 'i': 513, 'j': 669, 'k': 54, 'l': 592, 'm': 816, 'n': 992, 'o': 506, 'p': 547, 'q': 324, 'r': 713,
       's': 957, 't': 281, 'u': 143, 'v': 982, 'w': 493, 'x': 347, 'y': 150, 'z': 343, '0': 731, '1': 846, '2': 298,
       '3': 503, '4': 852, '5': 574, '6': 322, '7': 967, '8': 107, '9': 52, '@': 248, '#': 419, '$': 262, '%': 489}


def generate():
    size = randint(12, 20)
    symbols = ["@", "#", "$", "%"]
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = capitals.lower()
    numbers = "0123456789"
    portion = (size - 4) // 3
    numbers = sample(numbers, portion)
    capitals = sample(capitals, portion)
    small = sample(small, (size - 4 - 2 * portion))
    password = symbols + capitals + small + numbers
    for i in range(5):
        shuffle(password)
    return ''.join(password)


def encrypt(password):
    encrypted = [key[i] for i in password]
    return encrypted


def decrypt(encrypted):
    key_reversed = {j: i for i, j in key.items()}
    decrypted = [key_reversed[i] for i in encrypted]
    return ''.join(decrypted)


class MainWindow(Widget.QMainWindow):
    def __init__(self, parent=None):
        self.app = Widget.QApplication(sys.argv)
        super().__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.about.triggered.connect(self.info)
        self.ui.show.clicked.connect(self.show_password)
        self.ui.copy.clicked.connect(self.copy)
        self.ui.show_all.clicked.connect(self.show_all)
        self.ui.ui_update.do_2.clicked.connect(self.update_password)
        self.ui.ui_update.redo.clicked.connect(self.update_password)
        self.ui.ui_update.ok.clicked.connect(self.ok_update)
        self.ui.ui_generate.do_2.clicked.connect(self.generate)
        self.ui.ui_generate.redo.clicked.connect(self.generate)
        self.ui.ui_generate.ok.clicked.connect(self.ok_generate)
        self.ui.ui_change.pushButton.clicked.connect(self.confirm)
        self.ui.ui_start.pushButton.clicked.connect(self.login)
        self.ui.ui_start.passwordit.setEchoMode(Widget.QLineEdit.Password)
        self.ui.ui_change.old.setEchoMode(Widget.QLineEdit.Password)
        self.ui.ui_change.new_2.setEchoMode(Widget.QLineEdit.Password)
        self.ui.ui_change.confirm.setEchoMode(Widget.QLineEdit.Password)

    def show_password(self):
        name = self.ui.name.text()
        if name not in data_base:
            self.error()
            return
        password = data_base[name]["password"]
        password = decrypt(password)
        msg = Widget.QMessageBox()
        msg.setWindowTitle("Show")
        msg.setText(password)
        msg.setDetailedText("Your password is :\n\n\n" + password)
        msg.exec_()

    def copy(self):
        name = self.ui.name.text()
        if name not in data_base:
            self.error()
            return
        password = data_base[name]["password"]
        password = decrypt(password)
        copy(password)

    def show_all(self):
        details = ''
        for i in data_base:
            password = decrypt(data_base[i]["password"])
            details += f'{i}\n{data_base[i]["email"]}\n{password}\n\n'
        msg = Widget.QMessageBox()
        msg.setWindowTitle("ALL")
        msg.setText("all accounts")
        msg.setDetailedText(details.rstrip())
        msg.exec_()

    def update_password(self):
        email_name = self.ui.ui_update.name.text()
        if email_name not in data_base:
            self.error()
            return
        new_password = generate()
        self.ui.ui_update.password.setText(new_password)

    def ok_update(self):
        password = self.ui.ui_update.password.text()
        name = self.ui.ui_update.name.text()
        if name not in data_base:
            self.error()
            return
        data_base[name]["password"] = encrypt(password)
        self.ui.ui_update.name.setText("")
        self.ui.ui_update.password.setText("")
        self.ui.update_window.close()

    def generate(self):
        name = self.ui.ui_generate.name.text()
        if name in data_base:
            self.error("an")
            return
        new_password = generate()
        self.ui.ui_generate.password.setText(new_password)

    def ok_generate(self):
        email = self.ui.ui_generate.email.text()
        name = self.ui.ui_generate.name.text()
        password = self.ui.ui_generate.password.text()
        if name in data_base:
            self.error("an")
            return
        if not name:
            return
        data_base[name] = {"email": email, "password": encrypt(password)}
        self.ui.ui_generate.email.setText("")
        self.ui.ui_generate.name.setText("")
        self.ui.ui_generate.password.setText("")
        self.ui.generate_window.close()

    def info(self):
        msg = Widget.QMessageBox()
        msg.setWindowTitle('Help')
        msg.setText('Stay Safe')
        msg.setIcon(Widget.QMessageBox.Information)
        about = 'This app generates a 12-20 long \ncomplex password.\nchallenge any mother hacker!!'
        msg.setDetailedText(about)
        msg.exec_()

    def error(self, word="no"):
        msg = Widget.QMessageBox()
        msg.setWindowTitle("404")
        msg.setText("you have " + word + " accounts with this name!!")
        msg.setIcon(Widget.QMessageBox.Critical)
        msg.exec_()

    def login(self):
        if self.authenticate():
            self.ui.start_up_window.close()
            self.show()
        else:
            error = Widget.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Wrong password")
            error.setIcon(Widget.QMessageBox.Critical)
            error.exec_()

    def authenticate(self):
        if not data_base["password manager"]["password"]:
            password = self.ui.ui_start.passwordit.text()
            data_base["password manager"]["password"] = encrypt(password)
            return True
        else:
            password = self.ui.ui_start.passwordit.text()
            return encrypt(password) == data_base["password manager"]["password"]

    def confirm(self):
        old = self.ui.ui_change.old.text()
        password = data_base["password manager"]["password"]
        password = decrypt(password)
        if old != password:
            error = Widget.QMessageBox()
            error.setWindowTitle("Wrong Password")
            error.setText("Try another one !!")
            error.setInformativeText("mother hacker")
            error.setIcon(Widget.QMessageBox.Critical)
            error.exec_()
            return
        new = self.ui.ui_change.new_2.text()
        confirm = self.ui.ui_change.confirm.text()
        if new != confirm:
            msg = Widget.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("new password does not match !")
            msg.setIcon(Widget.QMessageBox.Warning)
            msg.exec_()
            return
        data_base["password manager"]["password"] = encrypt(new)
        self.ui.ui_change.old.setText("")
        self.ui.ui_change.new_2.setText("")
        self.ui.ui_change.confirm.setText("")
        self.ui.change_window.close()

    def exit(self):
        sys.exit(self.app.exec_())


window = MainWindow()
window.exit()

