from dto.client_dto import ClientDTO
from repository.client_repository import ClientRepository
from service.service import CRUDService


class ClientService(CRUDService):
    def __init__(self):
        super().__init__(ClientDTO, ClientRepository())
