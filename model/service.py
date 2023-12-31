from model.password import Password

class Service():
    id_service_controller = 0
    def __init__(self, name:str, site: str, userEmailService: str, servicePassword: Password):
        Service.id_service_controller += 1
        self.id_service = Service.id_service_controller
        self.name = name
        self.site = site
        self.userEmailService = userEmailService
        self.servicePassword = servicePassword




    def to_dict(self):
        return {
            'name': self.name,
            'site': self.site,
            'user_email_service': self.userEmailService,
            'service_password': self.servicePassword
        }