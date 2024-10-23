import sys
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController

class App:
    
    @staticmethod
    def main_menu():
        while True:
            print("\n===== Welcome to The Furniture Hub =====")
            App.print_menu(["Register", "Login", "Exit"])

            choice = input("Select an option: ").strip()

            if choice == '1':
                App.register_user()
            elif choice == '2':
                App.login_user()
            elif choice == '3':
                print("Thank you for using the system. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_menu(options):
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

    @staticmethod
    def register_user():
        #Handle user registration
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        is_admin = input("Are you an admin? (y/n): ").strip().lower() == "y"
        UserController.register_user(name, email, password, is_admin)
        print(f"User {name} registered successfully!")

    @staticmethod
    def login_user():
        #Handle user login and display appropriate menus based on role
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        user = UserController.login_user(email, password)

        if user:
            #print(f"Welcome {user['name']}!")
            if user['is_admin']:
                App.admin_menu()
            else:
                App.user_menu(user)
        else:
            print("Invalid login credentials!")

    @staticmethod
    def admin_menu():
        #Admin menu with options to manage products, users, and orders
        while True:
            print("\nAdmin Menu")
            App.print_menu(["Manage Products", "Manage Users", "Manage Orders", "Logout"])

            admin_choice = input("Select an option: ").strip()
            print('\n')

            if admin_choice == "1":
                ProductController.product_menu()
            elif admin_choice == "2":
                App.manage_users()
            elif admin_choice == "3":
                OrderController.order_menu()
            elif admin_choice == "4":
                break  # Logout
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def manage_users():
        #Submenu for user management
        while True:
            print("\nUser Management Menu")
            App.print_menu(["View All Users", "View User by ID", "Update User", "Delete User", "Back to Admin Menu"])

            user_choice = input("Enter your choice: ").strip()

            if user_choice == "1":
                UserController.get_all_users()
            elif user_choice == "2":
                user_id = input("Enter User ID to view profile: ").strip()
                UserController.get_user_profile(user_id)
            elif user_choice == "3":
                user_id = input("Enter User ID to update: ").strip()
                UserController.update_user(user_id)
            elif user_choice == "4":
                user_id = input("Enter User ID to delete: ").strip()
                UserController.delete_user(user_id)
            elif user_choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def user_menu(user):
        #Display the user menu and handle order-related actions
        while True:
            print("\nUser Menu")
            App.print_menu(["Place an Order", "View All Orders", "View Order by ID", "Update Order", "Delete Order", "Logout"])

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                OrderController.create_order(user['user_id'])
            elif choice == "2":
                OrderController.get_all_orders()
            elif choice == "3":
                OrderController.get_order_by_id()
            elif choice == "4":
                OrderController.update_order()
            elif choice == "5":
                OrderController.delete_order()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    App.main_menu()
