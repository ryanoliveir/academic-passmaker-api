from model.account import Account
from model.password import Password
from model.service import Service
from model.user import User


class CommunAccount(Account):
    def __init__(self, user: User, password: Password, maxServicesAllowed: int, unlimitedService: bool, servicesList=None, ):
        super().__init__(user, password, servicesList, unlimitedService)
        self.maxServicesAllowed = maxServicesAllowed

        