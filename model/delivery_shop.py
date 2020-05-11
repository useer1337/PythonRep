from model.delivery import Delivery
from database import Required


class DeliveryShop(Delivery):
    shop = Required('Shop')
