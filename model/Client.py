class Client:
    def __init__(self, name: str, login: str, password: str):
        self.name = name
        self.login = login
        self.password = password

    def set_name(self, name: str):
        self.name = name

    def set_login(self, login: str):
        self.login = login

    def set_password(self, password: str):
        self.password = password

    def get_name(self):
        return self.name

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password