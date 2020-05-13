from dto.dto import DTO
import dto.order_dto as OrderDTO


class BasketDTO(DTO):
    classes = {'order': OrderDTO}

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
        self.price += product.price

    def remove_product(self, product):
        self.products.remove(product)
        product.quantity += 1
        self.price -= product.price

    @staticmethod
    def class_by_name(name):
        return BasketDTO.classes[name]

    def __str__(self):
        return f'Basket id:{self.id} order:{self.order} products:{self.products} price{self.price}'
