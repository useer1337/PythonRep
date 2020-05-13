import sys
from binding import *

from PyQt5.QtWidgets import QApplication

from view.login_or_registration_view import LoginOrPasswordView

app = QApplication(sys.argv)

login_or_password = LoginOrPasswordView()
login_or_password.show()

app.exec_()
