from pony.orm import Set, Optional, Required

from model.DataBase import db


class Basket(db.Entity):
    products = Set('Product')
    order = Optional('Order')
    price = Required(int, default=0)

    def add_product(self, product):
        self.products.add(product)
        self.price += product.get_price()

    def get_products(self):
        return self.products

    def get_price(self):
        return self.price
