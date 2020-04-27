from model.Delivery import Delivery
from pony.orm import Required


class DelivShop(Delivery):
    shop = Required('Shop')

    def set_shop(self, shop):
        self.shop = shop

    def get_shop(self):
        return self.shop

    '''
    def __init__(self, shop: Shop):
        self.shop = shop

    '''
