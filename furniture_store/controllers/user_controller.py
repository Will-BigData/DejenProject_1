

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
            print("6. Login")
            print("7. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                UserController.register_user_interactively()
            elif choice == '2':
                user_id = input("Enter the User ID: ").strip()
                UserController.get_user_profile(user_id)
            elif choice == '3':
                UserController.update_user_profile()
            elif choice == '4':
                UserController.delete_user()
            elif choice == '5':
                UserController.get_all_users()
            elif choice == '6':
                email = input("Enter your email: ").strip()
                password = input("Enter your password: ").strip()
                UserController.login_user(email, password)
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

            cont = input("\nWould you like to continue managing users? (yes/no): ").strip().lower()
            if cont != 'yes':
                break


    @staticmethod
    def register_user(name=None, email=None, password=None, is_admin=None):

        if not name:
            name = input("Enter your name: ").strip()
        if not email:
            email = input("Enter your email: ").strip()
        if not password:
            password = input("Enter your password: ").strip()
        if is_admin is None:
            is_admin_input = input("Are you registering as an admin? (yes/no): ").strip().lower()
            is_admin = True if is_admin_input == 'yes' else False

        # Check if user with the same email already exists
        existing_user = UserDAO.get_user_by_email(email)
        if existing_user:
            print("User with that email already exists.")
            return
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user_id = UserDAO.insert_user(name, email, hashed_password.decode(), is_admin)

        if user_id:
            print(f"User {name} registered successfully!")
        else:
            print("Error registering user.")
    

    @staticmethod
    def login_user(email, password):
        #Method to login a user with email and password
        user_data = UserDAO.get_user_by_email(email)

        if user_data:

            if bcrypt.checkpw(password.encode(), user_data['password'].encode()):
                print(f"Login successful! Welcome {user_data['name']}.")
                return user_data
            else:
                print("Incorrect password. Please try again.")
        else:
            print("User not found. Please register first.")
        return None



    @staticmethod
    def get_user_profile(user_id):
        user_data = UserDAO.get_user_by_id(user_id)
        if user_data:
            print(f"User ID: {user_data['user_id']}")
            print(f"Name: {user_data['name']}")
            print(f"Email: {user_data['email']}")
            print(f"Admin: {'Yes' if user_data['is_admin'] else 'No'}")
        else:
            print("User not found")

    @staticmethod
    def update_user_profile():
        user_id = input("Enter user ID to update: ").strip()
        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()
        password = input("Enter new password (leave blank to keep current): ").strip()

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() if password else None
        updated = UserDAO.update_user(user_id, name, email, hashed_password)

        if updated:
            print("User updated successfully.")
        else:
            print("Error updating user.")

    @staticmethod
    def delete_user():
        user_id = input("Enter user ID to delete: ").strip()
        deleted = UserDAO.delete_user(user_id)

        if deleted:
            print("User deleted successfully.")
        else:
            print("User ID not found")

    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        if users:
            for user in users:
                print(f"ID: {user['user_id']}, Name: {user['name']}, Email: {user['email']}, Admin: {user['is_admin']}")
        else:
            print("No users found")
