class User():
    id_user_controller = 0
    def __init__(self,name:str, email: str):
        User.id_user_controller += 1
        self.id_user = User.id_user_controller
        self.name = name
        self.email = email

    