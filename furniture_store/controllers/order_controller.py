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

    @staticmethod
    def create_order():
        try:
            # Collect the necessary inputs for creating an order
            user_id = input("Enter User ID: ")
            shipping_address = input("Enter Shipping Address: ")
            city = input("Enter City: ")
            postal_code = input("Enter Postal Code: ")
            country = input("Enter Country: ")

            # Create the Order instance
            order = Order(user_id, shipping_address, city, postal_code, country)

            # Collect order items
            order_items_data = []
            while True:
                product_name = input("Enter Product Name: ")
                product_count = int(input("Enter Quantity: "))
                product_price = float(input("Enter Price: "))
                product_id = input("Enter Product ID: ")

                # Create order item data dictionary and add it to order_items_data list
                order_items_data.append({
                    "name": product_name,
                    "count": product_count,
                    "price": product_price,
                    "product_id": product_id
                })

                another_item = input("Add another item? (y/n): ").strip().lower()
                if another_item != 'y':
                    break

            # Add items to the order
            for item_data in order_items_data:
                order_item = SingleOrderProduct(
                    name=item_data['name'],
                    count=item_data['count'],
                    price=item_data['price'],
                    product_id=item_data['product_id']
                )
                order.add_order_item(order_item)

            # Call DAO to handle the database insertion
            order_id, message = OrderDAO.create_order(order)

            if order_id:
                return {"order_id": order_id}, "Order created successfully."
            else:
                return None, message

        except Exception as e:
            return None, f"Error creating order: {e}"