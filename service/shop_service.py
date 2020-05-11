from dto.shop_dto import ShopDTO
from repository.shop_repository import ShopRepository
from service.service import CRUDService


class ShopService(CRUDService):
    def __init__(self):
        super().__init__(ShopDTO, ShopRepository())