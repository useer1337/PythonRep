from model.client import Client
from repository.repository_imp import CRUDRepositoryImp


class ClientRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Client)

    @staticmethod
    def to_dict(client):
        return client.to_dict()
