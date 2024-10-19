
# Models.py

class SingleOrderProduct:
    def __init__(self, name, count, price, product_id):
        self.name = name
        self.count = count
        self.price = price
        self.product_id = product_id  # Foreign key to the Product

    def to_tuple(self):
        """Converts the SingleOrderItem to a tuple for SQL insertion."""
        return (self.name, self.count, self.price, self.product_id)


class Order:
    def __init__(self, user_id, shipping_address, city, postal_code, country):
        self.user_id = user_id  # Foreign key to the user
        self.shipping_address = shipping_address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.order_items = []  # List of SingleOrderItem objects

    def to_tuple(self):
        """Converts the Order object to a tuple for SQL insertion."""
        return (self.user_id, self.shipping_address, self.city, self.postal_code, self.country)

    def add_order_item(self, order_item):
        """Adds a SingleOrderItem to the order."""
        self.order_items.append(order_item)
