from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QLabel

from presenter.cheque_presenter import ChequePresenter


class ChequeView(QWidget):
    def __init__(self, parent=None, order=None):
        self.order = order

        QWidget.__init__(self, parent=None)

        self.resize(300, 250)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowTitle("Чек")

        self.text_edit = QTextEdit()

        self.label = QLabel("Ваш чек")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

        self.presenter = ChequePresenter(self)

        self.pull()

    def pull(self):
        self.presenter.pull(self.order)


