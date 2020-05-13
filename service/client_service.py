from dto.client_dto import ClientDTO
from repository.client_repository import ClientRepository
from service.service import CRUDService


class ClientService(CRUDService):
    def __init__(self):
        super().__init__(ClientDTO, ClientRepository())

    def verification_client(self, client):
        return self.repository.verification_client(client.login, client.password)

