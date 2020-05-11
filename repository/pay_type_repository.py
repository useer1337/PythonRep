from model.pay_type import PayType
from repository.repository_imp import CRUDRepositoryImp


class PayTypeRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(PayType)

    @staticmethod
    def to_dict(pay_type):
        return pay_type.to_dict()
