

import bcrypt
from DAO.user_dao import UserDAO
import os

class UserController:

    @staticmethod
    def register_user(name, email, password):
        existing_user = UserDAO.get_user_by_email(email)
        if existing_user:
            return None, "User with that email already exists"
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user_id = UserDAO.insert_user(name, email, hashed_password)

        if user_id:
            return {
                "user_id": user_id,
                "name": name,
                "email": email,
                "is_admin": False,
            }, None
        else:
            return None, "Error registering user"

    @staticmethod
    def get_user_profile(user_id):
        user_data = UserDAO.get_user_by_id(user_id)
        if user_data:
            return {
                "user_id": user_data["user_id"],
                "name": user_data["name"],
                "email": user_data["email"],
                "is_admin": user_data["is_admin"],
            }, None
        else:
            return None, "User not found"

    @staticmethod
    def update_user_profile(user_id, name=None, email=None, password=None):

        if password:
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        updated = UserDAO.update_user(user_id, name, email, password)

        if updated:
            return True, "User profile updated"
        else:
            return False, "Error updating user profile"
    
    @staticmethod
    def delete_user(user_id):
        deleted =  UserDAO.delete_user(user_id)

        if deleted:
            return True, "User deleted"
        else:
            return False, "Error deleting user"

    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        if users:
            return users, None
        else:
            return None, "Error fetching users"
