class LookBasketPresenter:
    def __init__(self, view):
        self.view = view

    def select_all_row(self):
        index = self.view.get_selected_row_index()
        self.view.table.selectRow(index)

    def fill_table(self):
        self.view.set_table_row(len(self.view.basket.products))

        for r, o in enumerate(self.view.basket.products):
            self.fill_row(r, o)

    def delete_product(self):
        index = self.view.get_selected_row_index()
        if index is not None:
            current_product = self.view.basket.products[index]
            if current_product.quantity_in_basket == 1:
                self.view.basket.remove_product(current_product)
            else:
                self.view.basket.remove_updated_product(current_product)

    def fill_row(self, row, obj):
        self.view.set_item(row, 0, str(obj.id))
        self.view.set_item(row, 1, str(obj.size))
        self.view.set_item(row, 2, obj.color)
        self.view.set_item(row, 3, str(obj.price))
        self.view.set_item(row, 4, str(obj.quantity))
        self.view.set_item(row, 5, str(obj.quantity_in_basket))
        self.view.set_item(row, 6, obj.product_type.name)
