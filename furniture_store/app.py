
import sys
from logging_config import logger
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController

class App:

    @staticmethod
    def main_menu():
        logger.info("Displaying main menu")
        while True:
            print("\n===== Welcome to The Furniture Hub =====")
            App.print_menu(["Register", "Login", "Exit"])

            choice = input("Select an option: ").strip()
            if choice == '1':
                App.register_user()
            elif choice == '2':
                App.login_user()
            elif choice == '3':
                logger.info("Exiting application.")
                print("Thank you for using the system. Goodbye!")
                sys.exit()
            else:
                logger.warning("Invalid choice entered in main menu")
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_menu(options):
        #Helper method to print a menu given a list of options.
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

    @staticmethod
    def register_user():
        #Handle user registration
        logger.info("User registration process started")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        #is_admin = input("Are you an admin? (y/n): ").strip().lower() == "y"
        is_admin = False

        success, message = UserController.register_user(name, email, password, is_admin)
        if success:
            logger.info(f"User {name} registered successfully.")
            print(f"User {name} registered successfully!")
        else:
            logger.error(f"Error registering user: {message}")
            print(f"Error registering user: {message}")

    @staticmethod
    def login_user():
        #Handle user login and display appropriate menus based on role
        logger.info("User login process started")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        user = UserController.login_user(email, password)
        if user:
            logger.info(f"User {email} logged in successfully")
            if user['is_admin']:
                App.admin_menu(user)
            else:
                App.user_menu(user)
        else:
            logger.warning(f"Failed login attempt for email: {email}")
            print("Invalid login credentials!")

    @staticmethod
    def admin_menu(user):
        #Admin menu with options to manage products, users, and orders
        logger.info(f"Admin {user['email']} accessed admin menu")
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
                OrderController.order_menu(user)
            elif admin_choice == "4":
                logger.info(f"Admin {user['email']} logged out")
                break
            else:
                logger.warning("Invalid choice entered in admin menu")
                print("Invalid choice. Please try again.")

    @staticmethod
    def manage_users():
        logger.info("Admin accessed user management menu")
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
                logger.warning("Invalid choice entered in user management menu")
                print("Invalid choice. Please try again.")

    @staticmethod
    def user_menu(user):
        """Display the user menu and handle order-related actions."""
        logger.info(f"User {user['email']} accessed user menu")
        while True:
            print("\nUser Menu")
            App.print_menu([
                "View Available Products",
                "View All Order Items",
                "Place an Order",
                "View All Orders",
                "View Order by ID",
                "Update Order",
                "Delete Order",
                "Logout"
            ])

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                ProductController.get_all_products()
            elif choice == "2":
                OrderController.view_all_order_items()  # New method to view order items
            elif choice == "3":
                OrderController.create_order(user['user_id'])
            elif choice == "4":
                OrderController.get_all_orders(user)
            elif choice == "5":
                OrderController.get_order_by_id(user)
            elif choice == "6":
                OrderController.update_order(user)
            elif choice == "7":
                OrderController.delete_order(user)
            elif choice == "8":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    logger.info("Application started")
    App.main_menu()