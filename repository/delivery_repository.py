from pony.orm import db_session

from model.delivery import Delivery
from model.order import Order
from repository.repository_imp import RORepositoryImp


class DeliveryRepository(RORepositoryImp):
    def __init__(self):
        super().__init__(Delivery)

    @staticmethod
    @db_session
    def from_dict(deliv):
        args = deliv
        args['order'] = Order.get(id=args['order']['id'])
        return args

    @staticmethod
    def to_dict(delivery):
        d = delivery.to_dict()
        d['order'] = {'id': d['order']}
        del d['classtype']
        return d
