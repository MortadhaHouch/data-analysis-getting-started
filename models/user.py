from uuid import uuid4
class User:
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.id=uuid4()
    def get_id(self):
        return self.id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    def set_password(self,password):
        self.password = password
        return self.password
    def set_email(self,email):
        self.email = email
        return self.email
    def set_id(self,id):
        self.id = id
        return self.id