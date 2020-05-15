from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QComboBox, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QLineEdit, QHeaderView, QLabel, QSizePolicy, QMessageBox

from presenter.main_view_presenter import MainViewPresenter


class MainView(QWidget):
    def __init__(self, parent=None, client=None):
        QWidget.__init__(self, parent=parent)
        self.client = client

        self.resize(670, 200)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowTitle("StillBerries")

        self.combobox_position = QComboBox()
        self.combobox_body = QComboBox()
        self.combobox_items = QComboBox()

        self.combobox_pay_type = QComboBox()
        self.combobox_delivery_type = QComboBox()
        self.combobox_shops = QComboBox()

        self.address_line_edit = QLineEdit()

        self.add_button = QPushButton("Add")
        self.look_button = QPushButton("Look basket")
        self.look_order_button = QPushButton("Look orders")
        self.buy_button = QPushButton("Buy")

        self.add_button.clicked.connect(self.get_product)
        self.look_button.clicked.connect(self.get_basket)
        self.buy_button.clicked.connect(self.buy)
        self.look_order_button.clicked.connect(self.look_orders)

        self.type_pay_label = QLabel("Тип оплаты")
        self.type_delivery_label = QLabel("Тип доставки")
        self.greeting_label = QLabel("Здраствуйте " + self.client.name.title())

        self.table_widget = QTableWidget()
        self.init_table()

        self.table_widget.itemClicked.connect(self.select_all_row)

        main_layout = QHBoxLayout()

        layout_combobox = QVBoxLayout()
        layout_combobox.addWidget(self.combobox_position)
        layout_combobox.addWidget(self.combobox_body)
        layout_combobox.addWidget(self.combobox_items)

        layout_bot_right = QHBoxLayout()
        layout_bot_right.addWidget(self.look_order_button)
        layout_bot_right.addWidget(self.buy_button)

        self.layout_right = QVBoxLayout()
        self.layout_right.addWidget(self.add_button)
        self.layout_right.addWidget(self.look_button)
        self.layout_right.addWidget(self.type_pay_label)
        self.layout_right.addWidget(self.combobox_pay_type)
        self.layout_right.addWidget(self.type_delivery_label)
        self.layout_right.addWidget(self.combobox_delivery_type)
        self.layout_right.addWidget(self.address_line_edit)
        self.layout_right.addWidget(self.combobox_shops)

        self.address_line_edit.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        # self.address_line_edit.setMinimumWidth(150)

        self.address_line_edit.hide()
        self.combobox_shops.hide()

        self.layout_right.addLayout(layout_bot_right)

        central_layout = QVBoxLayout()
        central_layout.addWidget(self.table_widget)
        central_layout.addWidget(self.greeting_label)

        main_layout.addLayout(layout_combobox)
        main_layout.addLayout(central_layout)
        main_layout.addLayout(self.layout_right)

        self.setLayout(main_layout)

        self.presenter = MainViewPresenter(self)

        self.add_pay_types()
        self.combobox_delivery_type.addItems(['Доставка в магзин', 'Доставка по адресу'])

        self.appear()

        self.combobox_position.addItem(self.presenter.product_types[0].name, self.presenter.product_types[0])
        self.combobox_position.addItem(self.presenter.product_types[1].name, self.presenter.product_types[1])

        self.combobox_position.currentTextChanged.connect(self.add_body_combobox)
        self.combobox_body.currentTextChanged.connect(self.add_items_combobox)
        self.combobox_items.currentTextChanged.connect(self.fill_table)
        self.combobox_delivery_type.currentTextChanged.connect(self.appear)

    def get_message_box(self, text: str):
        messageBox = QMessageBox()
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Ошибочка")
        messageBox.exec_()

    def select_all_row(self):
        self.presenter.select_all_row()

    def look_orders(self):
        self.presenter.look_orders()

    def get_address(self):
        return self.address_line_edit.text()

    def get_delivery_text(self):
        return self.combobox_delivery_type.currentText()

    def buy(self):
        self.presenter.buy()

    def appear(self):
        if self.combobox_delivery_type.currentText() == "Доставка в магзин":
            self.address_line_edit.hide()
            self.combobox_shops.show()
            self.get_shops()
        else:
            self.combobox_shops.hide()
            self.address_line_edit.show()

    def get_shops(self):
        self.combobox_shops.clear()
        for shop in self.presenter.get_shops():
            self.combobox_shops.addItem(shop.address, shop)

    def get_shop_text(self):
        return self.combobox_shops.currentText()

    def get_pay_type(self):
        return self.combobox_pay_type.currentText()

    def get_client(self):
        return self.client

    def get_basket(self):
        self.presenter.get_basket()

    def get_product(self):
        self.presenter.get_product()
        self.fill_table(self.combobox_items.currentText())

    def get_selected_row_index(self):
        index = self.table_widget.selectedIndexes()
        if not index:
            return None
        return index[0].row()

    def set_item(self, row, column, value):
        item = QTableWidgetItem(value)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_widget.setItem(row, column, item)

    def fill_table(self, text):
        self.presenter.fill_table(text)

    def set_table_row(self, row):
        self.table_widget.setRowCount(row)

    def add_body_combobox(self, text):
        self.combobox_body.clear()
        for type in self.presenter.get_types(text):
            self.combobox_body.addItem(type.name, type)

    def add_items_combobox(self, text):
        self.combobox_items.clear()
        for type in self.presenter.get_types(text):
            self.combobox_items.addItem(type.name, type)

    def add_pay_types(self):
        for pt in self.presenter.pay_types:
            self.combobox_pay_type.addItem(pt.name, pt)

    def init_table(self):
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(
            ['Цвет', 'Тип товара', 'Размер', 'Цена', 'На складе шт.', 'В корзине шт.'])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
