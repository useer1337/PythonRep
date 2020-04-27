from model.ProductType import ProductType
from model.DataBase import db
from pony.orm import Required, Optional, Set


class Product(db.Entity):
    size = Required(int)
    color = Required(str)
    price = Required(int)
    quantity = Required(int)
    product_type = Required('ProductType')
    basket = Set('Basket')

    def set_size(self, size: int):
        self.size = size

    def set_color(self, color: str):
        self.color = color

    def set_price(self, price: int):
        self.price = price

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def set_productType(self, product_type):
        self.product_type = product_type

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_productType(self):
        return self.product_type

    '''
    def __init__(self, size: int, color: str, price: int, quantity: int, product_type: ProductType):
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.product_type = product_type
    '''
