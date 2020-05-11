from database import db, PrimaryKey, Set, Optional, Required


class Basket(db.Entity):
    id = PrimaryKey(int, auto=True)
    products = Set('Product')
    order = Optional('Order')
    price = Required(int, default=0)
