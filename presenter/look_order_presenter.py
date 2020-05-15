from view.cheque_view import ChequeView


class LookOrderPresenter:
    def __init__(self, view):
        self.view = view

    def select_all_row(self):
        index = self.view.get_selected_row_index()
        self.view.table.selectRow(index)

    def look(self):
        order = self.get_order()
        if order is not None:
            cheque_view = ChequeView(order=self.get_order())
            cheque_view.show()

    def get_order(self):
        index = self.view.get_selected_row_index()
        if index is not None:
            current_order = self.view.client_orders[index]
            return current_order

    def fill_table(self):
        self.view.set_table_row(len(self.view.client_orders))

        for r, o in enumerate(self.view.client_orders):
            self.fill_row(r, o)

    def fill_row(self, row, obj):
        self.view.set_item(row, 0, str(obj.id))
        self.view.set_item(row, 1, obj.date.strftime("%Y-%m-%d %H:%M"))
