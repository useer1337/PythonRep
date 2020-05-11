from model.delivery import Delivery
from database import Required


class DeliveryCourier(Delivery):
    address = Required(str)