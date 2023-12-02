from model.account import Account
from model.password import Password
from model.service import Service
from model.user import User


class PremiumAccount(Account):
    def __init__(self,user: User, password: Password,servicesList=None, unlimitedService=False):
        super().__init__(user, password,servicesList, unlimitedService)

        