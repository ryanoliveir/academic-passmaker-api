from models.user import User
from models.premiumAccount import  PremiumAccount
from models.communAccount import CommunAccount
from models.service import Service


class Database():
    def __init__(self, users=None, services=None, accounts=None):
        self._users = users or []
        self._services = services or []
        self._accounts = accounts or []

            
    def init(self):
        print("Initializing Database...")
        
        # Create some users
        user1 = User(name="john_doe",email="john_doe@gmail.com")
        user2 = User(name="jane_smith", email="jane_smith@gmail.com")

        # Create some services (assuming you have a Service class)
        # You may need to adapt this part based on your actual Service implementation
        service1 = Service(name="Service1", site="www.google.com", userEmailService="john@google.com", servicePassword="john123")
        service2 = Service(name="Service2", site="www.facebook.com", userEmailService="jane@facebook.com", servicePassword="jane123")

        # Create some accounts
        premium_account1 = PremiumAccount(user=user1, password="password123", servicesList=[service1, service2], unlimitedService=True)
        commun_account1 = CommunAccount(user=user2, password="pass456", servicesList=[service1])

        # Add the created objects to the database
        self._users.extend([user1, user2])
        self._services.extend([service1, service2])
        self._accounts.extend([premium_account1, commun_account1])

        print("Database initialization complete.")


    def get_users(self):
        return self._users