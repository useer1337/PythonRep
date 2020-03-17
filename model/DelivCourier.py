from model.Delivery import Delivery


class DelivCourier(Delivery):
    def __init__(self, address:str):
        self.address = address

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address