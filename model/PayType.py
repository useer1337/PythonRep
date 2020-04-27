from model.DataBase import db
from pony.orm import Optional, Required


class PayType(db.Entity):
    name = Required(str)
    order = Optional('Order')

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    '''
    def __init__(self, name: str):
        self.name = name
    '''