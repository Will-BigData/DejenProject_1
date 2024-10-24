from DAO.product_dao import ProductDAO
from models.product_model import Product


class ProductController:

    @staticmethod
    def product_menu():
        while True:
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
            
            cont = input("\nWould you like to continue managing products? (y/n): ").strip().lower()
            if cont != 'y':
                break

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
    
    @staticmethod
    def get_product_by_id():
        product_id = int(input("Enter product ID: ").strip())
        product = ProductDAO.get_product_by_id(product_id)
        if product:
            print(product)
        else:
            print("Product not found")
    
    @staticmethod
    def update_product():
        product_id = input("Enter product ID to update: ")
        product = ProductDAO.get_product_by_id(product_id)
        if not product:
            print("Product not found.")
            return
        
        name = input(f"Enter new name (current: {product['name']}): ") or product['name']
        category = input(f"Enter new category (current: {product['category']}): ") or product['category']
        description = input(f"Enter new description (current: {product['description']}): ") or product['description']
        price = float(input(f"Enter new price (current: {product['price']}): ") or product['price'])
        in_stock = int(input(f"Enter new stock quantity (current: {product['in_stock']}): ") or product['in_stock'])

        updated_product = Product(product_id, name, category, description, price, in_stock)
        updated = ProductDAO.update_product(product_id, updated_product)

        if updated:
            print(f"Product '{name}' updated successfully.")
        else:
            print("Error updating product.")

    @staticmethod
    def delete_product():
        product_id = int(input("Enter product ID to delete: ").strip())
        deleted = ProductDAO.delete_product(product_id)

        if deleted:
            print("Product deleted successfully.")
        else:
            print("Error deleting product.")
