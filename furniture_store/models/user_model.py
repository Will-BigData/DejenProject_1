
import bcrypt

class User:
    def __init__ (self, user_id, name, email, password, is_admin=False):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.set_password(password) = password
        self.is_admin = is_admin
    
    def to_tuple(self):
        return (self.name, self.email, self.is_admin)
    
    def set_password(self, password):
        self.hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.hash_password)