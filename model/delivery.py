from datetime import timedelta, datetime

from database import db, PrimaryKey, Optional


class Delivery(db.Entity):
    id = PrimaryKey(int, auto=True)
    order = Optional('Order')
    date = Optional(datetime, default=datetime.now() + timedelta(days=10))