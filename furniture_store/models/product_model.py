
class Product:
    def __init__(self, name, image, category, description="", price=0.0, in_stock=0):
        self.name = name
        self.image = image
        self.category = category
        self.description = description
        self.price = price 
        self.in_stock = in_stock

    def to_tuple(self):
        return (self.name, self.image, self.category, self.description, self.price, self.in_stock)