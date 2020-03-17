from model.Product import Product
from model.Client import Client


class Basket:
    def __init__(self, client: Client):
        self.product_list = []
        self.client = client
        self.price = 0

    def get_productList(self):
        return self.product_list

    def add_product(self, product: Product):
        self.price += product.get_price()
        self.product_list.append(product)

    def get_item(self, index: int):
        return self.product_list[index]

    def get_price(self):
        return self.price