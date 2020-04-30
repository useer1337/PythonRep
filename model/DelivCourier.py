from pony.orm import Required

from model.Delivery import Delivery


class DelivCourier(Delivery):
    address = Required(str)

    def set_address(self, address: str):
        self.address = address

    def get_address(self):
        return self.address

    '''
    def __init__(self, address: str):
        self.address = address
    '''
