from datetime import datetime, timedelta

from pony.orm import Optional

from model.DataBase import db


class Delivery(db.Entity):
    order = Optional('Order')

    def get_date(self):
        return datetime.now() + timedelta(days=10)

    '''
    
    def __init__(self):
        self.date = datetime.now() + timedelta(days=10)

    '''
