from model.DataBase import db
from pony.orm import Required, Optional, Set


class Shop(db.Entity):
    address = Required(str)
    deliv_shop = Set('DelivShop')

    def set_address(self, address: str):
        self.address = address

    def get_address(self):
        return self.address

    '''
    
    def __init__(self, address: str):
        self.address = address
    
    '''
