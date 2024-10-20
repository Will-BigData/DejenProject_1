

import bcrypt
from DAO.user_dao import UserDAO
import os

class UserController:
    @staticmethod
    def user_menu():
        while True:
            print("1. Register New User")
            print("2. Get User Profile")
            print("3. Update User Profile")
            print("4. Delete User")
            print("5. Get All Users")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                UserController.register_user()
            elif choice == '2':
                UserController.get_user_profile()
            elif choice == '3':
                UserController.update_user_profile()
            elif choice == '4':
                UserController.delete_user()
            elif choice == '5':
                UserController.get_all_users()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

            cont = input("\nWould you like to continue managing users? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

    @staticmethod
    def register_user():
        # register a new user
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        existing_user = UserDAO.get_user_by_email(email)
        if existing_user:
            print("User with that email already exists.")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user_id = UserDAO.insert_user(name, email, hashed_password)

        if user_id:
            print(f"User {name} registered successfully!")
        else:
            print("Error registering user.")

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
    def update_user_profile():
        #Method to update an existing user
        user_id = input("Enter user ID to update: ").strip()
        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()
        password = input("Enter new password: ").strip()

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) if password else None
        updated, message = UserDAO.update_user(user_id, name, email, hashed_password)

        print(message)
    
    @staticmethod
    def delete_user():
        #Method to delete a user 
        user_id = input("Enter user ID to delete: ").strip()
        deleted, message = UserDAO.delete_user(user_id)
        print(message)


    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        if users:
            return users, None
        else:
            return None, "Error fetching users"
