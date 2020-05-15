import hashlib

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
        h = hashlib.md5(self.view.get_password().encode('UTF-8'))
        password = h.hexdigest()
        self.client_dto = ClientDTO(name=self.view.get_name(), login=self.view.get_login(),
                                    password=password)

        try:
            if len(self.view.get_name()) < 4:
                self.view.get_message_box("Длинна имени должна превышать 4 символа")
            elif len(self.view.get_login()) < 4:
                self.view.get_message_box("Длинна логина должна превышать 4 символа")
            else:
                self.service.verification_client(self.client_dto)
                # TODO MB WRONG
                self.view.close()
                main_view = MainView(client=self.get_client())
                main_view.show()
        except ClientNotFoundException:
            self.view.get_message_box("Такова клиента нет в базе")

    def registration(self):
        h = hashlib.md5(self.view.get_password().encode('UTF-8'))
        password = h.hexdigest()
        self.client_dto = ClientDTO(name=self.view.get_name(), login=self.view.get_login(),
                                    password=password)

        print(self.client_dto)

        try:
            self.service.verification_client(self.client_dto)
            self.view.get_message_box("Ошибка при создании")
        except ClientNotFoundException:
            if len(self.view.get_name()) < 4:
                self.view.get_message_box("Длинна имени должна превышать 4 символа")
            elif len(self.view.get_login()) < 4:
                self.view.get_message_box("Длинна логина должна превышать 4 символа")
            elif len(self.view.get_password()) < 6:
                self.view.get_message_box("Длинна пароля должна превышать 6 символов")
            else:
                self.service.create(self.client_dto)
                self.view.line_edit_name.clear()
                self.view.line_edit_login.clear()
                self.view.line_edit_password.clear()
                self.view.label_ok.show()

    def get_client(self):
        for client in self.service.get_all():
            if client.login == self.client_dto.login:
                client.name = self.client_dto.name
                self.service.update(client)
                return client