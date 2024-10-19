

import bcrypt
from DAO.user_dao import UserDao
import os

class UserController:
    @staticmethod
    def register_user(name, email, password):
        existing_user = UserDao.get_user_by_email(email)
        if existing_user:
            return None, "User with that email already exists"
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user_id = UserDao.insert_user(name, email, hashed_password)

        if user_id:
            return {
                "user_id": user_id,
                "name": name,
                "email": email,
                "is_admin": False,
            }, None
        else:
            return None, "Error registering user"

