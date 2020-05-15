from dto.dto import DTO
from dto.order_dto import OrderDTO
from dto.product_dto import ProductDTO


class BasketDTO(DTO):
    classes = {'order': OrderDTO,
               'products': ProductDTO}

    def __init__(self, id=None, order=None, price=None, products=None):
        self.id = id
        self.order = order
        if products:
            self.products = products
        else:
            self.products = []

        if price:
            self.price = price
        else:
            self.price = 0

    def add_product(self, product):
        self.products.append(product)
        product.quantity -= 1
        product.quantity_in_basket += 1
        self.price += product.price

    def update_product(self, product):
        for prd in self.products:
            if prd == product:
                prd.quantity -= 1
                prd.quantity_in_basket += 1
                self.price += product.price

    def remove_product(self, product):
        self.products.remove(product)
        product.quantity += 1
        product.quantity_in_basket -= 1
        self.price -= product.price

    def remove_updated_product(self, product):
        for prd in self.products:
            if prd == product:
                prd.quantity += 1
                prd.quantity_in_basket -= 1
                self.price -= product.price

    @staticmethod
    def class_by_name(name):
        return BasketDTO.classes[name]

    def __str__(self):
        return f'Basket id:{self.id} order:{self.order} products:{" ".join([str(i) for i in self.products])} price{self.price}'


def get_basket_dto() -> BasketDTO:
    return BasketDTO()
