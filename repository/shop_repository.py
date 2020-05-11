from model.shop import Shop
from repository.repository_imp import CRUDRepositoryImp


class ShopRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Shop)

    @staticmethod
    def to_dict(shop):
        return shop.to_dict()
