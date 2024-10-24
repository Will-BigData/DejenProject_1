
# Models.py
class OrderProduct:
    def __init__(self, count, product_id, name, price):
        self.name = name
        self.count = count
        self.price = price
        self.product_id = product_id  # Foreign key to the Product

    def to_tuple(self):
        """Converts the OrderProduct to a tuple for SQL insertion."""
        return (self.count, self.product_id, self.name, self.price)

class Order:
    def __init__(self, user_id, shipping_address, city, postal_code, country):
        self.user_id = user_id  # Foreign key to the User
        self.shipping_address = shipping_address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.order_items = []
        self.order_id = None 
    def to_tuple(self):
        #Converts the Order object to a tuple for SQL insertion.
        return (self.user_id, self.shipping_address, self.city, self.postal_code, self.country)

    def add_order_item(self, order_item):
        self.order_items.append(order_item)

    def calculate_total(self):
        return sum(item.price * item.count for item in self.order_items)