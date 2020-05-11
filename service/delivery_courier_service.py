from dto.delivery_courier_dto import DeliveryCourierDTO
from repository.delivery_courier_repository import DeliveryCourierRepository
from service.service import CRUDService


class DeliveryCourierService(CRUDService):
    def __init__(self):
        super().__init__(DeliveryCourierDTO, DeliveryCourierRepository())


