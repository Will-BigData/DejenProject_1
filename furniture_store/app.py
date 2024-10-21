
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController


class App:
    @staticmethod
    def main_menu():
        while True:
            print("\n===== Welcome to The Furniture Hub =====")
            print('\n')
            print("1. Manage Products")
            print("2. Manage Users")
            print("3. Manage Orders")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                App.product_menu()
            elif choice == '2':
                App.user_menu()
            elif choice == '3':
                App.order_menu()
            elif choice == '4':
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def product_menu():
        while True:
            print("\n===== Product Management =====")
            ProductController.product_menu()
            cont = input(
                "\nWould you like to continue managing products? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

    @staticmethod
    def user_menu():
        while True:
            print("\n===== User Management =====")
            UserController.user_menu()
            cont = input(
                "\nWould you like to continue managing products? (yes/no): ").strip().lower()
            if cont != 'yes':
                break


    @staticmethod
    def order_menu():
        while True:
            print("\n===== Order Management =====")
            OrderController.order_menu()
            cont = input(
                "\nWould you like to continue managing orders? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

        print("\n===== Order Management =====")


if __name__ == "__main__":
    App.main_menu()
