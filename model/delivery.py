from datetime import timedelta, datetime

from database import db, PrimaryKey, Optional, Required


class Delivery(db.Entity):
    id = PrimaryKey(int, auto=True)
    order = Optional('Order')
    date = Required(datetime, default=datetime.now() + timedelta(days=10))