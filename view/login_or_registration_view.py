from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox

from presenter.login_or_registration_presenter import LoginOrRegistrationPresenter


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

        self.button_login.clicked.connect(self.login)
        self.button_registration.clicked.connect(self.registration)

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

        self.presenter = LoginOrRegistrationPresenter(self)

    def get_name(self):
        return self.line_edit_name.text()

    def get_login(self):
        return self.line_edit_login.text()

    def get_password(self):
        return self.line_edit_password.text()

    def get_message_box(self, text: str):
        messageBox = QMessageBox()
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.exec_()

    def login(self):
        self.presenter.login()

    def registration(self):
        self.presenter.registration()
