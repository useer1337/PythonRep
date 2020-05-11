from database import db, PrimaryKey, Set, Optional, Required


class ProductType(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    product = Set('Product')
    product_type = Optional('ProductType')
    product_type_reverse = Set('ProductType', reverse=product_type)
