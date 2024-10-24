
from tabulate import tabulate

class UserDisplay:

    @staticmethod
    def display_users_table(users):
        """Displays all users in a table format."""
        table = []
        for idx, user in enumerate(users):
            table.append([
                idx + 1,
                user['user_id'],
                user['name'],
                user['email'],
                "Yes" if user['is_admin'] else "No"  
            ])

        headers = ['No.', 'User ID', 'Name', 'Email', 'Admin']
        print(tabulate(table, headers, tablefmt="fancy_grid"))


class ProductDisplay:
    @staticmethod
    def display_products_table(products):
        """Displays products in a table format."""
        table = []
        for idx, product in enumerate(products):
            product_id = product['product_id']
            name = product['name']
            category = product['category']
            description = product['description']
            price = product['price']
            in_stock = product['in_stock']

            # Add product info to the table
            table.append([idx + 1, product_id, name, category, description, price, in_stock])

        headers = ['No.', 'Product ID', 'Name', 'Category', 'Description', 'Price', 'In Stock']
        print(tabulate(table, headers, tablefmt="fancy_grid"))


class OrderDisplay:
    @staticmethod
    def display_orders_table(orders):
        """Displays all orders in a table format."""
        table = []
        for idx, order in enumerate(orders):
            order_id = order['order_id']
            user_id = order['user_id']
            shipping_address = order['shipping_address']
            city = order['city']
            postal_code = order['postal_code']
            country = order['country']

            # Add order info to the table
            table.append([idx + 1, order_id, user_id, shipping_address, city, postal_code, country])

        headers = ['No.', 'Order ID', 'User ID', 'Shipping Address', 'City', 'Postal Code', 'Country']
        print(tabulate(table, headers, tablefmt="fancy_grid"))


class OrderItemsDisplay:
    @staticmethod
    def display_order_items_table(order_items):
        """Displays order items in a table format."""
        table = []
        for idx, item in enumerate(order_items):
            # Add order item details to the table
            table.append([
                idx + 1,
                item['item_id'],
                item['order_id'],
                item['product_id'],
                item['name'],
                item['count'],
                item['price']
            ])

        headers = ['No.', 'Item ID', 'Order ID', 'Product ID', 'Product Name', 'Quantity', 'Price']
        print(tabulate(table, headers, tablefmt="fancy_grid"))
