
import re
import bcrypt
from DAO.user_dao import UserDAO
from display import UserDisplay

class UserController:

    @staticmethod
    def is_valid_email(email):
        """Validate email format using regex."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def register_user(name, email, password, is_admin):
        # Validate email format
        if not UserController.is_valid_email(email):
            return False, "Invalid email format."

        # Check if the email already exists
        existing_user = UserDAO.get_user_by_email(email)
        if existing_user:
            return False, "User with that email already exists."

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        user_id = UserDAO.insert_user(name, email, hashed_password.decode(), is_admin)
        if user_id:
            return True, f"User {name} registered successfully!"
        else:
            return False, "Error registering user."

    @staticmethod
    def login_user(email, password):
        # Method to login a user with email and password
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
    def update_user(user_id):
        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()
        password = input("Enter new password (leave blank to keep current): ").strip()
        
        # Prompt to update the admin status
        is_admin_input = input("Is this user an admin? (yes/no, leave blank to keep current): ").strip().lower()
        
        if is_admin_input == 'yes':
            is_admin = True
        elif is_admin_input == 'no':
            is_admin = False
        else:
            is_admin = None  # Indicates we will keep the current value

        # Hash the new password only if provided
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() if password else None
        
        # Call DAO to update the user (make sure UserDAO.update_user is updated to handle is_admin)
        updated = UserDAO.update_user(user_id, name, email, hashed_password, is_admin)
        
        if updated:
            print("User updated successfully.")
        else:
            print("Error updating user.")



    @staticmethod
    def delete_user(user_id):
        deleted = UserDAO.delete_user(user_id)
        if deleted:
            print("User deleted successfully.")
        else:
            print("User ID not found")

    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        if users:
            UserDisplay.display_users_table(users)
        else:
            print("No users found")
