
class User:
    def __init__ (self, user_id, name, email, password, is_admin=False):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
    
    def to_tuple(self):
        return (self.name, self.email, self.password, self.is_admin)