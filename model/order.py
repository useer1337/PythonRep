from datetime import datetime

from database import db, PrimaryKey, Optional, Required


class Order(db.Entity):
    id = PrimaryKey(int, auto=True)
    client = Required('Client')
    payed = Required(bool)
    pay_type = Required('PayType')
    delivery = Required('Delivery')
    basket = Required('Basket')
    date = Required(datetime, default=datetime.today())
