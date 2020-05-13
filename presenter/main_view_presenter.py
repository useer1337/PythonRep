from dto.basket_dto import BasketDTO
from dto.order_dto import OrderDTO
from dto.product_type_dto import ProductTypeDTO
from service.basket_service import BasketService
from service.delivery_courier_service import DeliveryCourierService
from service.delivery_shop_service import DeliveryShopService
from service.pay_type_service import PayTypeService
from service.product_service import ProductService
from service.product_type_service import ProductTypeService
from service.shop_service import ShopService


class MainViewPresenter:
    def __init__(self, view):
        self.view = view
        self.product_type_service = ProductTypeService()
        self.pay_type_service = PayTypeService()
        self.delivery_shop_service = DeliveryShopService()
        self.delivery_courier_service = DeliveryCourierService()
        self.product_service = ProductService()
        self.basket_service = BasketService()
        self.shops_service = ShopService()

        self.product_types = self.product_type_service.get_all()
        self.pay_types = self.pay_type_service.get_all()
        self.products = self.product_service.get_all()

        self.return_products = []

        self.basket_dto = BasketDTO()

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
        order_dto = OrderDTO(client=self.view.get_client(),
                             pay_type=self.get_pay_type())

    def get_basket(self):
        for product in self.basket_dto.products:
            print(product)

    def get_product(self):
        index = self.view.get_selected_row_index()
        if index is not None:
            current_product = self.return_products[index]
            self.basket_dto.add_product(current_product)

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
        self.view.set_item(row, 0, str(obj.id))
        self.view.set_item(row, 1, str(obj.size))
        self.view.set_item(row, 2, obj.color)
        self.view.set_item(row, 3, str(obj.price))
        self.view.set_item(row, 4, str(obj.quantity))
        self.view.set_item(row, 5, obj.product_type.name)
