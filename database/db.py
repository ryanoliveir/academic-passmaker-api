from model.user import User
from model.premiumAccount import  PremiumAccount
from model.communAccount import CommunAccount
from model.service import Service


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
        user3 = User(name="ryan_oliveira", email="ryan@gmail.com")
        user4 = User(name="Tester", email="t")


        # Create some services (assuming you have a Service class)
        # You may need to adapt this part based on your actual Service implementation
        service1 = Service(name="Google Account", site="www.google.com", userEmailService="john@google.com", servicePassword="john123")
        service2 = Service(name="Facebook Account", site="www.facebook.com", userEmailService="jane@facebook.com", servicePassword="jane123")
        service3 = Service(name="Insagram Account", site="www.instagram.com", userEmailService="ryan@gmail.com", servicePassword="ryan102030")
        service4 = Service(name="Test Website", site="www.test.com", userEmailService="TheGreatTester@test.com", servicePassword="RyanWest35")
        service5 = Service(name="THE HAMMER TIME", site="www.hammertime.com", userEmailService="HAMMERTIME@HAMMER.hammer", servicePassword="TheHammer06")


        # Create some accounts
        premium_account1 = PremiumAccount(user=user1, password="password123", servicesList=[service1, service2], unlimitedService=True)
        commun_account2 = CommunAccount(user=user2, password="pass456", servicesList=[service2], unlimitedService=False, maxServicesAllowed=5)
        commun_account3 = CommunAccount(user=user3, password="cyma102030", servicesList=[service3], unlimitedService=False, maxServicesAllowed=5)
        commun_account4 = CommunAccount(user=user4, password="t", servicesList=[service4,service5], unlimitedService=False, maxServicesAllowed=5)

        # Add the created objects to the database
        self._users.extend([user1, user2 ,user3, user2])
        self._services.extend([service1, service2, service3, service4, service5])
        self._accounts.extend([premium_account1, commun_account2, commun_account3,commun_account4])


        print("Database initialization complete.")


    def get_users(self):
        return self._users
    
    def get_services(self):
        return self._services
    
    def get_accounts(self):
        return self._accounts
    
    def createService(self, service, id_account):
        for account in self._accounts:
            if(account.id_account == id_account):
                account.servicesList.append(service)
                return
        

    def get_AccountServices(self, id_account):
        for account in self._accounts:
             if(account.id_account == id_account):
                return account.servicesList
    

    def delete_AccountService(self, id_service, id_account):
        for account in self._accounts:
            if account.id_account == id_account:

                for service in account.servicesList:
                    if(service.id_service == id_service):

                        account.servicesList.remove(service)
                        print(f"Service with id {id_service} deleted successfully.")
                        return

