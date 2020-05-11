from pony.orm import db_session

from model.product_type import ProductType
from repository.repository_imp import CRUDRepositoryImp


class ProductTypeRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(ProductType)

    @staticmethod
    @db_session
    def from_dict(prod_typ):
        args = prod_typ
        args['product_type'] = ProductType.get(id=args['product_type']['id'])
        return args

    @staticmethod
    def to_dict(product_type):
        d = product_type.to_dict()
        d['product_type'] = {'id': d['product_type']}
        #del d['classtype']
        return d