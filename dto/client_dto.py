from dto.dto import DTO


class ClientDTO(DTO):
    def __init__(self, id=None, name=None, login=None, password=None):
        self.id = id
        self.name = name
        self.login = login
        self.password = password

    def __str__(self):
        return f"Client id:{self.id} name:{self.name} login:{self.login} password:{self.password}"