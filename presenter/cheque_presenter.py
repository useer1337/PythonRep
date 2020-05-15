from service.basket_service import BasketService
from service.client_service import ClientService
from service.order_service import OrderService
from service.pay_type_service import PayTypeService
from service.product_type_service import ProductTypeService


class ChequePresenter:
    def __init__(self, view):
        self.view = view
        self.product_service = ProductTypeService()
        self.pay_type_service = PayTypeService()
        self.order_service = OrderService()
        self.client_service = ClientService()
        self.basket_service = BasketService()

    def pull(self, order):
        self.view.text_edit.append("Дата заказа - " + order.date.strftime("%Y-%m-%d %H:%M"))
        self.view.text_edit.append("Тип оплаты - " + self.get_product_types(order))
        self.view.text_edit.append("Состояние оплаты - " + str(order.payed))
        self.view.text_edit.append("Имя и логин клиента - " + self.get_client_name(order))

        self.view.text_edit.append("Товары:")
        self.order_service.load_basket(order)

        products = self.get_basket(order)
        for product in products:
            self.product_service.load_product_type(product)
            self.view.text_edit.append('\t' + product.color + " " + product.product_type.name + " "
                                       + str(product.size) + " размер")

        self.view.text_edit.append("Цена - " + str(order.basket.price) + " рублей")
        self.view.text_edit.setReadOnly(True)

    def get_product_types(self, order):
        for type in self.pay_type_service.get_all():
            if order.pay_type.id == type.id:
                return type.name

    def get_client_name(self, order):
        for client in self.client_service.get_all():
            if order.client.id == client.id:
                return client.name + " " + client.login

    def get_basket(self, order):
        baskets = self.basket_service.get_all()
        for basket in baskets:
            self.basket_service.load_products(basket)
            if order.basket.id == basket.id:
                print(basket)
                return basket.products
