from model.DataBase import db
from pony.orm import Set, Required


class Client(db.Entity):
    name = Required(str)
    login = Required(str, unique=True)
    password = Required(str)
    order = Set('Order')

    '''
    def __init__(self, name: str, login: str, password: str):
        self.name = name
        self.login = login
        self.password = password
    '''

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
