from pony.orm import db_session, RowNotFound

from exception.client_not_found_exception import ClientNotFoundException
from model.client import Client
from repository.repository_imp import CRUDRepositoryImp


class ClientRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Client)

    @db_session
    def verification_client(self, login, password):
        try:
            return self.to_dict(self.klass.get(login=login, password=password))
        except Exception:
            print("ClientNotFoundException")
            raise ClientNotFoundException("Нет такого клиента в базе!!!")


    @staticmethod
    def to_dict(client):
        return client.to_dict()
