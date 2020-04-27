from model.DataBase import db
from pony.orm import Required, Set, Optional


class ProductType(db.Entity):
    name = Required(str)
    product = Set('Product')
    parent_type = Optional('ProductType')
    parent_type_reverse = Set('ProductType', reverse=parent_type)

    '''
    def __init__(self, name: str, parent_type = None):
        self.name = name
        self.parent_type = parent_type
        
    '''

    def set_nameType(self, name: str):
        self.name = name

    def set_parentType(self, parent_type):
        self.parent_type = parent_type

    def get_nameType(self):
        return self.name

    def get_parentType(self):
        return self.parent_type
