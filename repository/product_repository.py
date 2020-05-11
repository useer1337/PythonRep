from pony.orm import db_session

from model.product import Product
from model.product_type import ProductType
from repository.repository_imp import CRUDRepositoryImp


class ProductRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Product)

    @staticmethod
    @db_session
    def from_dict(prod):
        args = prod
        args['product_type'] = ProductType.get(id=args['product_type']['id'])
        return args

    @staticmethod
    def to_dict(product):
        d = product.to_dict()
        d['product_type'] = {'id': d['product_type']}
        #del d['classtype']
        return d
