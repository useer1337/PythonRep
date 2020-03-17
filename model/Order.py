from model.Client import Client
from model.PayType import PayType
from datetime import datetime


class Order:
    def __init__(self, client: Client, payed: bool, pay_type: PayType, delivery):
        self.client = client
        self.payed = payed
        self.pay_type = pay_type
        self.delivery = delivery
        self.date = datetime.today()

    def set_client(self, client: Client):
        self.client = client

    def set_payed(self, payed: bool):
        self.payed = payed

    def set_payType(self, pay_type):
        self.pay_type = pay_type

    def set_delivery(self, delivery):
        self.delivery = delivery

    def get_client(self):
        return self.client

    def get_payed(self):
        return self.payed

    def get_PayType(self):
        return self.pay_type

    def get_delivery(self):
        return self.delivery

    def get_date(self):
        return self.date
