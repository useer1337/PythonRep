from database import db, PrimaryKey, Required, Optional, Set


class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    size = Required(int)
    color = Required(str)
    price = Required(int)
    quantity = Required(int)
    product_type = Required('ProductType')
    basket = Set('Basket')
