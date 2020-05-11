from dto.delivery_shop_dto import DeliveryShopDTO
from dto.shop_dto import ShopDTO
from repository.delivery_shop_repository import DeliveryShopRepository
from repository.shop_repository import ShopRepository
from service.service import CRUDService


class DeliveryShopService(CRUDService):
    def __init__(self):
        super().__init__(DeliveryShopDTO, DeliveryShopRepository())
        self.shop_repository = ShopRepository()

    def load_shop(self, event):
        if event.shop:
            event.shop = ShopDTO.from_dict(self.shop_repository.find(event.shop.id))
