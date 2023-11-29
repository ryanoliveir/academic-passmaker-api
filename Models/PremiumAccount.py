from models.account import Account
from models.password import Password
from models.service import Service
from models.user import User


class PremiumAccount(Account):
    def __init__(self,user: User, password: Password,servicesList=None, unlimitedService=False):
        super().__init__(user, password,servicesList, unlimitedService)

        