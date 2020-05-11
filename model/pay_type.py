from database import db, PrimaryKey, Required, Set


class PayType(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    order = Set('Order')