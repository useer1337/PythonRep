from pony.orm import db_session

from model.delivery_shop import DeliveryShop
from model.shop import Shop
from repository.repository_imp import CRUDRepositoryImp


class DeliveryShopRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(DeliveryShop)

    @staticmethod
    @db_session
    def from_dict(deliv_shop):
        args = deliv_shop
        args['shop'] = Shop.get(id=args['shop']['id'])
        return args

    @staticmethod
    def to_dict(basket):
        d = basket.to_dict()
        d['shop'] = {'id': d['shop']}
        del d['classtype']
        return d
