from dto.basket_dto import BasketDTO
from dto.client_dto import ClientDTO
from dto.delivery_courier_dto import DeliveryCourierDTO
from dto.delivery_dto import DeliveryDTO
from dto.delivery_shop_dto import DeliveryShopDTO
from dto.order_dto import OrderDTO
from dto.pay_type_dto import PayTypeDTO
from repository.basket_repository import BasketRepository
from repository.client_repository import ClientRepository
from repository.delivery_courier_repository import DeliveryCourierRepository
from repository.delivery_repository import DeliveryRepository
from repository.delivery_shop_repository import DeliveryShopRepository
from repository.order_repository import OrderRepository
from repository.pay_type_repository import PayTypeRepository
from service.service import CRUDService


class OrderService(CRUDService):
    def __init__(self):
        super().__init__(OrderDTO, OrderRepository())
        self.client_repository = ClientRepository()
        self.pay_type_repository = PayTypeRepository()
        self.basket_repository = BasketRepository()

    def load_client(self, event):
        if event.client:
            event.client = ClientDTO.from_dict(self.client_repository.find(event.client.id))

    def load_pay_type(self, event):
        if event.pay_type:
            event.pay_type = PayTypeDTO.from_dict(self.pay_type_repository.find(event.pay_type.id))

    def load_delivery(self, event):
        if event.delivery:
            if isinstance(event.delivery, DeliveryShopDTO):
                event.delivery = DeliveryShopDTO.from_dict(DeliveryShopRepository().find(event.delivery.id))
            else:
                event.delivery = DeliveryCourierDTO.from_dict(DeliveryCourierRepository().find(event.delivery.id))

    def load_basket(self, event):
        if event.basket:
            event.basket = BasketDTO.from_dict(self.basket_repository.find(event.basket.id))
