from database import db, PrimaryKey, Required, Set


class Client(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    login = Required(str)
    password = Required(str)
    order = Set('Order')