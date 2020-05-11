from pony.orm import db_session

from model.delivery_courier import DeliveryCourier
from repository.repository_imp import CRUDRepositoryImp


class DeliveryCourierRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(DeliveryCourier)

    @staticmethod
    def to_dict(deliv_cour):
        d = deliv_cour.to_dict()
        del d['classtype']
        return d


