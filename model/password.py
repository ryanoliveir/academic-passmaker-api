class Password():
    def __init__(self, password: str):
        self._password = password 

    @property
    def password(self):
        return self._password
