from model.Delivery import Delivery
from model.DataBase import db
from pony.orm import Required


class DelivCourier(Delivery):
    address = Required(str)

    def set_address(self, address:str):
        self.address = address

    def get_address(self):
        return self.address

    '''
    def __init__(self, address: str):
        self.address = address
    '''
