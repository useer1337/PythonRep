from dto.basket_dto import BasketDTO
from dto.order_dto import OrderDTO
from dto.product_dto import ProductDTO
from repository.basket_repository import BasketRepository
from repository.order_repository import OrderRepository
from repository.product_repository import ProductRepository
from service.service import CRUDService


class BasketService(CRUDService):
    def __init__(self):
        super().__init__(BasketDTO, BasketRepository())
        self.order_repository = OrderRepository()
        self.product_repository = ProductRepository()

    def load_order(self, event):
        if event.order and event.id:
            event.order = OrderDTO.from_dict(self.order_repository.find(event.order.id))

    def load_products(self, event):
        if event.products:
            event.products = list(
                    map(lambda item: ProductDTO.from_dict(self.product_repository.find(item.id)), event.products))


