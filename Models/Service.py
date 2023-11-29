from models.password import Password

class Service():
    id_service = 0
    def __init__(self, name:str, site: str, userEmailService: str, servicePassword: Password):
        Service.id_service += 1
        self._name = name
        self._site = site
        self._userEmailService = userEmailService
        self._servicePassword = servicePassword