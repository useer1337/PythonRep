from model.Delivery import Delivery
from model.Shop import Shop


class DelivShop(Delivery):
    def __init__(self, shop: Shop):
        self.shop = shop

    def set_shop(self, shop):
        self.shop = shop

    def get_shop(self):
        return self.shop
