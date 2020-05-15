from dto.order_dto import OrderDTO
from dto.product_type_dto import ProductTypeDTO

from service.basket_service import BasketService
from service.client_service import ClientService
from service.delivery_courier_service import DeliveryCourierService
from service.delivery_shop_service import DeliveryShopService
from service.order_service import OrderService
from service.pay_type_service import PayTypeService
from service.product_service import ProductService
from service.product_type_service import ProductTypeService
from service.shop_service import ShopService
from dto.basket_dto import BasketDTO
from dto.delivery_courier_dto import DeliveryCourierDTO
from dto.delivery_shop_dto import DeliveryShopDTO
from view.cheque_view import ChequeView
from view.look_basket_view import LookBasketView
from view.look_order_view import LookOrderView


class MainViewPresenter:
    def __init__(self, view):
        self.view = view
        self.client_service = ClientService()
        self.product_type_service = ProductTypeService()
        self.pay_type_service = PayTypeService()
        self.delivery_shop_service = DeliveryShopService()
        self.delivery_courier_service = DeliveryCourierService()
        self.product_service = ProductService()
        self.basket_service = BasketService()
        self.shops_service = ShopService()
        self.order_service = OrderService()

        self.product_types = self.product_type_service.get_all()
        self.pay_types = self.pay_type_service.get_all()
        self.products = self.product_service.get_all()

        self.return_products = []

        self.basket_dto = BasketDTO()

    def select_all_row(self):
        index = self.view.get_selected_row_index()
        self.view.table_widget.selectRow(index)

    def find_client(self):
        for client in self.client_service.get_all():
            if self.view.get_client().login == client.login:
                return client

    def look_orders(self):
        look_order_view = LookOrderView(client_orders=self.get_client_orders())
        look_order_view.show()
        '''
        for order in self.order_service.get_all():
            print(order)
        '''

    def get_client_orders(self):
        orders = []
        for order in self.order_service.get_all():
            client = self.view.get_client()
            if client.id == order.client.id:
                orders.append(order)

        return orders

    def get_delivery(self):
        text = self.view.get_delivery_text()

        if text == 'Доставка в магзин':
            for shop in self.get_shops():
                if self.view.get_shop_text() == shop.address:
                    delivery_shop_dto = DeliveryShopDTO(shop=shop)
                    self.delivery_shop_service.create(delivery_shop_dto)
                    return delivery_shop_dto
        else:
            address = self.view.get_address()
            if address is not None:
                delivery_courier_dto = DeliveryCourierDTO(address=address)
                self.delivery_courier_service.create(delivery_courier_dto)
                return delivery_courier_dto

    def get_shops(self):
        return self.shops_service.get_all()

    def get_pay_type(self):
        text = self.view.get_pay_type()

        for pay_type in self.pay_types:
            if pay_type.name == text:
                return pay_type
            else:
                continue
        return None

    def buy(self):
        if len(self.basket_dto.products) > 0 and (self.get_delivery() is not None):
            client = self.view.get_client()
            pay_type = self.get_pay_type()

            if pay_type.name == "По карте":
                payed = True
            else:
                payed = False

            order_dto = OrderDTO(client=self.find_client(),
                                 pay_type=pay_type,
                                 basket=self.basket_dto,
                                 payed=payed,
                                 delivery=self.get_delivery()
                                 )

            for product in self.basket_dto.products:
                product.quantity_in_basket = 0
                self.product_service.update(product)

            self.basket_service.create(self.basket_dto)
            self.order_service.create(order_dto)
            self.basket_dto = BasketDTO()
            self.view.address_line_edit.clear()

            cheque_view = ChequeView(order=order_dto)
            cheque_view.show()
        else:
            self.view.get_message_box("Ошибка при покупке")

    def get_basket(self):
        look_basket_view = LookBasketView(basket=self.basket_dto)
        look_basket_view.show()

    def get_product(self):
        index = self.view.get_selected_row_index()
        if index is not None:
            current_product = self.return_products[index]
            if current_product.quantity_in_basket == 0:
                self.basket_dto.add_product(current_product)
            else:
                self.basket_dto.update_product(current_product)

    def get_types(self, text):
        product_type_dto = ProductTypeDTO(name=text)
        return_types = []

        for tp in self.product_types:
            self.product_type_service.load_product_type(tp)
            if tp.product_type.name == product_type_dto.name:
                return_types.append(tp)

        return return_types

    def get_products(self, text):
        self.return_products.clear()
        for product in self.products:
            self.product_service.load_product_type(product)
            if text == product.product_type.name:
                self.return_products.append(product)

    def fill_table(self, text):
        self.get_products(text)
        self.view.set_table_row(len(self.return_products))

        for r, o in enumerate(self.return_products):
            self.fill_row(r, o)

    def fill_row(self, row, obj):
        self.view.set_item(row, 0, obj.color)
        self.view.set_item(row, 1, obj.product_type.name)
        self.view.set_item(row, 2, str(obj.size))
        self.view.set_item(row, 3, str(obj.price))
        self.view.set_item(row, 4, str(obj.quantity))
        self.view.set_item(row, 5, str(obj.quantity_in_basket))
