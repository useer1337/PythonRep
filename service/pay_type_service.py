from dto.pay_type_dto import PayTypeDTO
from repository.pay_type_repository import PayTypeRepository
from service.service import CRUDService


class PayTypeService(CRUDService):
    def __init__(self):
        super().__init__(PayTypeDTO, PayTypeRepository())