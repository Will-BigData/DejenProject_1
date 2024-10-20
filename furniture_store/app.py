
from controllers.user_controller import UserController
#from controllers.product_controller import ProductController
#from controllers.order_controller import OrderController

class App:

    def __init__(self):
        self.user_controller = UserController()
        self.product_controller = ProductController()
        #self.order_controller = OrderController()

    def register_user(self, name, email, password):
        return self.user_controller.register_user(name, email, password)

    def get_user_profile(self, user_id):
        return self.user_controller.get_user_profile(user_id)

    def update_user_profile(self, user_id, name=None, email=None, password=None):
        return self.user_controller.update_user_profile(user_id, name, email, password)

    def delete_user(self, user_id):
        return self.user_controller.delete_user(user_id)

    def get_all_users(self):
        return self.user_controller.get_all_users()

    def add_product(self, name, category, description, price, in_stock):
        return self.product_controller.add_product(name, category, description, price, in_stock)

    def get_product(self, product_id):
        return self.product_controller.get_product(product_id)

    def update_product(self, product_id, name=None, category=None, description=None, price=None, in_stock=None):
        return self.product_controller.update_product(product_id, name, category, description, price, in_stock)

    def delete_product(self, product_id):
        return self.product_controller.delete_product(product_id)

    def get_all_products(self):
        return self.product_controller.get_all_products()

    # def create_order(self, user_id, shipping_address, city, postal_code, country):
    #     return self.order_controller.create_order(user_id, shipping_address, city, postal_code, country)

    # def add_order_item(self, order_id, name, count, price, product_id):
    #     return self.order_controller.add_order_item(order_id, name, count, price, product_id)

    # def get_order(self, order_id):
    #     return self.order_controller.get_order(order_id)

    # def get_user_orders(self, user_id):
    #     return self.order_controller.get_user_orders(user_id)

    # def get_all_orders(self):
    #     return self.order_controller.get_all_orders()

    # def delete_order(self, order_id):
    #     return self.order_controller.delete_order(order_id)

    # def delete_order_item(self, order_id, product_id):
    #     return self.order_controller.delete_order_item(order_id, product_id)