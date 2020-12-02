"""
This class represent a User
"""

class User:
    def __init__(self, id = -1, name = "nombre", lastname = "lastname", birthday = "2020-01-01", cellphone = "55555555", email = "example@example.com"):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday
        self.email = email
        self.cellphone = cellphone
        self.id = id

### Getters
    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_birthday(self):
        return self.birthday

    def get_email(self):
        return self.email
    
    def get_cellphone(self):
        return self.cellphone

    def get_id(self):
        return self.id

### Setters

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_email(self, email):
        self.email = email
    
    def set_cellphone(self, cellphone):
        self.cellphone = cellphone

    def set_id(self, id):
        self.id = id