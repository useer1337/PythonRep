from datetime import datetime, timedelta
from model.DataBase import db
from pony.orm import Required, Optional


class Delivery(db.Entity):
    order = Optional('Order')

    def get_date(self):
        return datetime.now() + timedelta(days=10)

    '''
    
    def __init__(self):
        self.date = datetime.now() + timedelta(days=10)

    '''
