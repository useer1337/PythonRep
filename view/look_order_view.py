from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QPushButton, QVBoxLayout, QTableWidgetItem, QHeaderView

from presenter.look_order_presenter import LookOrderPresenter


class LookOrderView(QWidget):
    def __init__(self, parent=None, client_orders=None):
        self.client_orders = client_orders

        super(QWidget, self).__init__(parent=parent)

        self.resize(177, 200)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowTitle("Все заказы")

        self.table = QTableWidget()
        self.look_button = QPushButton("Посмотреть")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.look_button)

        self.setLayout(main_layout)

        self.presenter = LookOrderPresenter(self)

        self.init_table()
        self.fill_table()

        self.look_button.clicked.connect(self.look)
        self.table.itemClicked.connect(self.select_all_row)

    def select_all_row(self):
        self.presenter.select_all_row()

    def look(self):
        self.presenter.look()

    def get_selected_row_index(self):
        index = self.table.selectedIndexes()
        if not index:
            return None
        return index[0].row()

    def fill_table(self):
        self.presenter.fill_table()

    def set_item(self, row, column, value):
        item = QTableWidgetItem(value)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table.setItem(row, column, item)

    def set_table_row(self, row):
        self.table.setRowCount(row)

    def init_table(self):
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(
            ['id', 'Дата'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

