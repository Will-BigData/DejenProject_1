
class User:
    def __init__ (self, name, email, password, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
    
    def to_tuple(self):
        return (self.name, self.email, self.password, self.is_admin)