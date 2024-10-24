from tabulate import tabulate

class OrderDisplay:

    @staticmethod
    def display_orders_table(orders):
        table = []
        for idx, order in enumerate(orders):
            order_id = order['order_id']
            user_id = order['user_id']
            shipping_address = order['shipping_address']
            city = order['city']
            postal_code = order['postal_code']
            country = order['country']

            # Add order info to the table with separate columns for each address component
            table.append([idx + 1, order_id, user_id, shipping_address, city, postal_code, country])

        headers = ['No.', 'Order ID', 'User ID', 'Shipping Address', 'City', 'Postal Code', 'Country']
        print(tabulate(table, headers, tablefmt="fancy_grid"))


class ProductDisplay:
    @staticmethod
    def display_products_table(products):
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