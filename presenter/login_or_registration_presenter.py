from dto.client_dto import ClientDTO
from exception.client_not_found_exception import ClientNotFoundException
from service.client_service import ClientService
from view.main_view import MainView


class LoginOrRegistrationPresenter:
    def __init__(self, view):
        self.view = view
        self.service = ClientService()
        self.client_dto = ClientDTO()

    def login(self):
        self.client_dto = ClientDTO(name=self.view.get_name(), login=self.view.get_login(),
                                    password=self.view.get_password())

        try:
            self.service.verification_client(self.client_dto)
            # TODO MB WRONG
            self.view.close()
            main_view = MainView(client=self.client_dto)
            main_view.show()
        except ClientNotFoundException:
            self.view.get_message_box("Такова клиента нет в базе")

    def registration(self):
        self.client_dto = ClientDTO(name=self.view.get_name(), login=self.view.get_login(),
                                    password=self.view.get_password())

        try:
            self.service.verification_client(self.client_dto)
            self.view.get_message_box("Такой клиент есть")
        except ClientNotFoundException:
            self.service.create(self.client_dto)
            print(self.client_dto)
