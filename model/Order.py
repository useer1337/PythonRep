from datetime import datetime
from model.DataBase import db
from pony.orm import Optional, Required


class Order(db.Entity):
    client = Required('Client')
    payed = Optional(bool)
    pay_type = Optional('PayType')
    delivery = Optional('Delivery')
    basket = Required('Basket')

    '''
    def __init__(self, client: Client = None, payed: bool = None, pay_type: PayType = None, delivery = None, basket: Basket = None):
        self.client = client
        self.payed = payed
        self.pay_type = pay_type
        self.delivery = delivery
        self.date = datetime.today()
        self.basket = basket
    '''

    def set_basket(self, basket):
        self.basket = basket

    def set_client(self, client):
        self.client = client

    def set_payed(self, payed: bool):
        self.payed = payed

    def set_payType(self, pay_type):
        self.pay_type = pay_type

    def set_delivery(self, delivery):
        self.delivery = delivery

    def get_basket(self):
        return self.basket

    def get_client(self):
        return self.client

    def get_payed(self):
        return self.payed

    def get_PayType(self):
        return self.pay_type

    def get_delivery(self):
        return self.delivery

    def get_date(self):
        return datetime.now()

    def __str__(self):
        return str(self.get_delivery().get_date())

