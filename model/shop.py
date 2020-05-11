from database import db, PrimaryKey, Required, Set


class Shop(db.Entity):
    address = Required(str)
    delivery_shop = Set('DeliveryShop')