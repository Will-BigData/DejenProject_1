from DAO.order_dao import OrderDAO
from models.order_model import Order, SingleOrderProduct


class OrderController:

    def order_menu():
        while True:
            print("Order Menu")
            print("1. Create New Order")
            print("2. Get All Orders")
            print("3. Get Order by ID")
            print("4. Update Order")
            print("5. Delete Order")
            print("6. Back to Main Menu")

            choice  = input("Enter your choice: ").strip()

            if choice == "1":
                OrderController.create_order()
            elif choice == "2":
                OrderController.get_all_orders()
            elif choice == "3":
                OrderController.get_order_by_id()
            elif choice == "4":
                OrderController.update_order()
            elif choice == "5":
                OrderController.delete_order()
            elif choice == "6":
                return
            else:
                print("Invalid choice. Please try again")
                OrderController.order_menu()
            
            cont = input("\nWould you like to continue managing orders? (y/n): ").strip().lower()
            if cont != 'y':
                break


    