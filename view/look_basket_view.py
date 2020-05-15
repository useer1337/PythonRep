from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QPushButton, QTableWidgetItem, QLabel, QHeaderView

from presenter.look_basket_presenter import LookBasketPresenter


class LookBasketView(QWidget):
    def __init__(self, parent=None, basket=None):
        self.basket = basket

        QWidget.__init__(self, parent=parent)
        self.setWindowTitle("Корзина")

        self.resize(438, 200)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)

        self.table = QTableWidget()
        self.del_button = QPushButton("Delete")
        self.label_price = QLabel()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.label_price)
        main_layout.addWidget(self.del_button)

        self.setLayout(main_layout)

        self.presenter = LookBasketPresenter(self)
        self.table.itemClicked.connect(self.select_all_row)

        self.init_table()
        self.fill_table()

        self.del_button.clicked.connect(self.delete)

    def select_all_row(self):
        self.presenter.select_all_row()

    def delete(self):
        self.presenter.delete_product()
        self.fill_table()

    def get_selected_row_index(self):
        index = self.table.selectedIndexes()
        if not index:
            return None
        return index[0].row()

    def fill_table(self):
        self.presenter.fill_table()
        self.label_price.setText("Стоимость всех товаров в корзине " + str(self.basket.price) + " рублей")

    def set_item(self, row, column, value):
        item = QTableWidgetItem(value)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table.setItem(row, column, item)

    def set_table_row(self, row):
        self.table.setRowCount(row)

    def init_table(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ['id', 'Размер', 'Цвет', 'Цена', 'Кол-во', 'Кол-во в корзине', 'Тип товара'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

