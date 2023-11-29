from models.user import User
from models.password import Password
from models.service import Service


class Account():
    id_account = 0

    def __init__(self, user: User, password: Password, servicesList=None, unlimitedService=None):
        Account.id_account += 1
        self.user = user
        self.password = password
        self.servicesList = servicesList or []
        self.unlimitedService = unlimitedService
