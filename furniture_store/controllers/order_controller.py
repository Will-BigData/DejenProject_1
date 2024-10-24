from DAO.order_dao import OrderDAO
from DAO.product_dao import ProductDAO  # Assuming you have a product DAO to handle product operations
from models.order_model import Order, OrderProduct
from display import OrderDisplay 

class OrderController:

    @staticmethod
    def order_menu(user):
        while True:
            print("\nOrder Menu")
            print("1. Create New Order")
            print("2. View All Orders")
            print("3. View Order by ID")
            print("4. Update Order")
            print("5. Delete Order")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                OrderController.create_order(user['user_id'])
            elif choice == "2":
                OrderController.get_all_orders(user)
            elif choice == "3":
                OrderController.get_order_by_id(user)
            elif choice == "4":
                OrderController.update_order(user)
            elif choice == "5":
                OrderController.delete_order(user)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again")

            cont = input("\nWould you like to continue managing orders? (y/n): ").strip().lower()
            if cont != 'y':
                break

    @staticmethod
    def create_order(user_id):
        #Handles the process of creating an order by filling the cart first and then entering shipping details.
        try:
            print("\nFill your cart:")
            order_items = OrderController.add_to_cart()

            if order_items:
                proceed_to_checkout = input("\nAre you ready to check out? (y/n): ").strip().lower()
                if proceed_to_checkout == 'y':
                    shipping_address = input("Enter Shipping Address: ").strip()
                    city = input("Enter City: ").strip()
                    postal_code = input("Enter Postal Code: ").strip()
                    country = input("Enter Country: ").strip()

                    # Place the order
                    OrderController.place_order(user_id, shipping_address, city, postal_code, country, order_items)
                else:
                    print("Order not placed. You can continue shopping later.")
            else:
                print("No items added to the cart.")
        except Exception as e:
            print(f"Error creating order: {e}")

    @staticmethod
    def add_to_cart():
        #Collects product IDs and quantities to add to the cart (order_items list).
        order_items = []
        total_price = 0  # To calculate the total price of the order

        while True:
            try:
                product_id = int(input("Enter product ID to add to order (0 to finish): ").strip())
                if product_id == 0:
                    break

                # Fetch the product details from the database
                product = ProductDAO.get_product_by_id(product_id)
                if not product:
                    print(f"Product with ID {product_id} does not exist.")
                    continue

                product_name = product['name']  # Use dictionary keys instead of indices
                product_price = product['price']
                product_in_stock = product['in_stock']
                print(f"Product: {product_name}, Price: {product_price}, In Stock: {product_in_stock}")
                quantity = int(input("Enter quantity: ").strip())

                # Check if the requested quantity is available in stock
                if quantity > product_in_stock:
                    print(f"Only {product_in_stock} units are available in stock. Please adjust your quantity.")
                    continue

                # Calculate total price for the current product
                total_price += product_price * quantity

                order_items.append({
                    "product_id": product_id,
                    "quantity": quantity,
                    "price": product_price,
                    "name": product_name 
                })
            except ValueError:
                print("Invalid entry. Please enter numeric values for product ID and quantity.")
            except Exception as e:
                print(f"Error: {e}")

        print(f"Total price for the order: {total_price}")
        return order_items


    @staticmethod
    def place_order(user_id, shipping_address, city, postal_code, country, order_items):
        #Places a new order and adds the selected products to the order.
        try:
            # Create an Order object
            order = Order(user_id, shipping_address, city, postal_code, country)
            for item in order_items:
                # Ensure that the price is being passed when creating the OrderProduct
                order_item = OrderProduct(
                    product_id=item['product_id'],
                    count=item['quantity'],
                    price=item['price'],  # Store price for each product in the order
                    name=item['name']  # Store name for each product in the order
                )
                order.add_order_item(order_item)

                # Decrease the stock of the product
                ProductDAO.decrease_stock(item['product_id'], item['quantity'])

            # Insert the order into the database
            order_id, message = OrderDAO.create_order(order)

            if order_id:
                print(f"Order placed successfully with ID {order_id}.")
            else:
                print(f"Error placing order: {message}")
        except Exception as e:
            print(f"Error placing order: {e}")

    @staticmethod
    def get_all_orders(user):
        """Fetches and displays all orders."""
        try:
            if user['is_admin']:
                orders, error = OrderDAO.get_all_orders()
            else:
                orders, error = OrderDAO.get_orders_by_user_id(user['user_id'])

            if orders:
                # Display the orders using the display method
                OrderDisplay.display_orders_table(orders)
            else:
                print(error)
        except Exception as e:
            print(f"Error fetching orders: {e}")


    @staticmethod
    def get_order_by_id(user):
        try:
            order_id = int(input("Enter Order ID: ").strip())
            order, error = OrderDAO.get_orders_id(order_id)

            if order:
                if user['is_admin'] or order['user_id'] == user['user_id']:
                    print(f"Order ID: {order['order_id']}, User ID: {order['user_id']}, Shipping Address: {order['shipping_address']}, City: {order['city']}, Postal Code: {order['postal_code']}, Country: {order['country']}")
                    
                    order_items = OrderDAO.get_order_items_by_order_id(order_id)
                    if order_items:
                        for item in order_items:
                            print(f"   Product ID: {item['product_id']}, Quantity: {item['count']}, Price: {item['price']}")
                    else:
                        print("   No items found for this order.")
                else:
                    print("You do not have permission to view this order.")
            else:
                print(error)
        except Exception as e:
            print(f"Error fetching order: {e}")

    @staticmethod
    def update_order(user):
        #Updates an existing order. Only admins or order owners can update.
        try:
            order_id = input("Enter Order ID to update: ").strip()
            order, _ = OrderDAO.get_orders_id(order_id)

            if not order:
                print("Order not found.")
                return

            if user['is_admin'] or order['user_id'] == user['user_id']:
                shipping_address = input(f"Enter new shipping address (current: {order['shipping_address']}): ").strip() or order['shipping_address']
                city = input(f"Enter new city (current: {order['city']}): ").strip() or order['city']
                postal_code = input(f"Enter new postal code (current: {order['postal_code']}): ").strip() or order['postal_code']
                country = input(f"Enter new country (current: {order['country']}): ").strip() or order['country']

                updated_order = Order(order['user_id'], shipping_address, city, postal_code, country)
                updated, message = OrderDAO.update_order(order_id, updated_order)

                if updated:
                    print(f"Order '{order_id}' updated successfully.")
                else:
                    print(f"Error updating order: {message}")
            else:
                print("You do not have permission to update this order.")
        except Exception as e:
            print(f"Error updating order: {e}")

    @staticmethod
    def delete_order(user):
        #Deletes an order by its ID. Only admins or order owners can delete.
        try:
            order_id = int(input("Enter Order ID to delete: ").strip())
            order, _ = OrderDAO.get_orders_id(order_id)

            if not order:
                print("Order not found.")
                return

            if user['is_admin'] or order['user_id'] == user['user_id']:
                deleted, message = OrderDAO.delete_order(order_id)
                if deleted:
                    print(f"Order {order_id} deleted successfully.")
                else:
                    print(f"Error deleting order: {message}")
            else:
                print("You do not have permission to delete this order.")
        except Exception as e:
            print(f"Error deleting order: {e}")
