from DAO.product_dao import ProductDAO
from models.product_model import Product


class ProductController:

    @staticmethod
    def product_menu():
        print("Product Menu")
        print("1. Add New Product")
        print("2. Get All Products")
        print("3. Get Product by ID")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            ProductController.add_product()
        elif choice == "2":
            ProductController.get_all_products()
        elif choice == "3":
            ProductController.get_product_by_id()
        elif choice == "4":
            ProductController.update_product()
        elif choice == "5":
            ProductController.delete_product()
        elif choice == "6":
            return
        else:
            print("Invalid choice. Please try again")
            ProductController.product_menu()

    @staticmethod
    def add_product():
        name = input("Enter product name: ").strip()
        category = input("Enter product category: ").strip()
        description = input("Enter product description: ").strip()
        price = float(input("Enter product price: ").strip())
        in_stock = int(input("Enter product stock: ").strip())

        product = Product(None, name, category, description, price, in_stock)
        product_id = ProductDAO.insert_product(product)
        if product_id:
            print("Product added successfully")
        else:
            print("Error adding product")

    @staticmethod
    def get_all_products():
        products = ProductDAO.get_all_products()
        if products:
            for product in products:
                print(product)
        else:
            print("No products found")
    