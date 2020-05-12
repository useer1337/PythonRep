import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QVBoxLayout, QApplication, QWidget, QHBoxLayout


class LoginOrPasswordView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.setWindowTitle("Вход в программу")
        self.resize(300, 150)

        self.line_edit_name = QLineEdit()
        self.line_edit_login = QLineEdit()
        self.line_edit_password = QLineEdit()

        self.line_edit_name.setValidator(QRegExpValidator(QRegExp(r"^[A-Za-z]*$")))
        self.line_edit_login.setValidator(QRegExpValidator(QRegExp(r"^[A-Za-z0-9]*$")))
        self.line_edit_password.setValidator(QRegExpValidator(QRegExp(r"^[A-Za-z0-9]*$")))
        self.line_edit_password.setEchoMode(QLineEdit.Password)

        self.label_name = QLabel("Name")
        self.label_login = QLabel("Login")
        self.label_password = QLabel("Password")

        self.button_login = QPushButton("Login")
        self.button_registration = QPushButton("Registration")

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.label_name)
        vbox_layout.addWidget(self.line_edit_name)
        vbox_layout.addWidget(self.label_login)
        vbox_layout.addWidget(self.line_edit_login)
        vbox_layout.addWidget(self.label_password)
        vbox_layout.addWidget(self.line_edit_password)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.button_login)
        btn_layout.addWidget(self.button_registration)

        vbox_layout.addLayout(btn_layout)

        self.setLayout(vbox_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_or_password = LoginOrPassword()
    login_or_password.show()

    app.exec_()
