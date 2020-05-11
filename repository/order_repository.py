from pony.orm import db_session

from model.basket import Basket
from model.client import Client
from model.delivery import Delivery
from model.order import Order
from model.pay_type import PayType
from repository.repository_imp import CRUDRepositoryImp


class OrderRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Order)

    @staticmethod
    @db_session
    def from_dict(ord):
        args = ord
        args['client'] = Client.get(id=args['client']['id'])
        args['pay_type'] = PayType.get(id=args['pay_type']['id'])
        args['delivery'] = Delivery.get(id=args['delivery']['id'])
        args['basket'] = Basket.get(id=args['basket']['id'])

        return args

    @staticmethod
    def to_dict(order):
        d = order.to_dict()
        d['client'] = {'id': d['client']}
        d['pay_type'] = {'id': d['pay_type']}
        d['delivery'] = {'id': d['delivery']}
        d['basket'] = {'id': d['basket']}
        #del d['classtype']
        return d