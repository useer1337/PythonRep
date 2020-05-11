from pony.orm import db_session

from model.basket import Basket
from model.order import Order
from model.product import Product
from repository.repository_imp import CRUDRepositoryImp


class BasketRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Basket)

    @staticmethod
    @db_session
    def from_dict(bsk):
        args = bsk
        #Костылик!!!!!!!!!!!!!!!!
        try:
            order =  Order.get(id=args['order']['id'])
        except Exception:
            order = None
        args['order'] = order

        products_set = set()
        for product in args['products']:
            products_set.add(Product.get(id=product['id']))

        args['products'] = products_set
        return args

    @staticmethod
    def to_dict(basket):
        d = basket.to_dict()
        d['order'] = {'id': d['order']}
        #del d['classtype']
        return d
