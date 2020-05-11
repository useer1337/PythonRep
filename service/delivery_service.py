from datetime import datetime, timedelta

from dto.delivery_dto import DeliveryDTO
from dto.order_dto import OrderDTO
from repository.delivery_repository import DeliveryRepository
from repository.order_repository import OrderRepository
from service.service import ROService


class DeliveryService(ROService):
    def __init__(self):
        super().__init__(DeliveryDTO, DeliveryRepository())
        self.order = OrderRepository()

    def load_order(self, event):
        if event.order:
            event.order = OrderDTO.from_dict(self.order_repository.find(event.order.id))

