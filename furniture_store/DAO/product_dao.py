
from db.connection import get_db_connection
from models.product_model import Product
class ProductDAO:

    @staticmethod
    def insert_product(product):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO products (name, category, description, price, in_stock) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(query, product.to_tuple())
        conn.commit()
        product_id = cursor.lastrowid
        cursor.close() 
        return product_id
    
    @staticmethod
    def get_all_products():
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()
        return products
    
    @staticmethod
    def get_product_by_id(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM products WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        cursor.close()
        return product
    
    @staticmethod
    def update_product(product):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE products SET name = %s, category = %s, description = %s, price = %s, in_stock = %s WHERE product_id = %s"
        cursor.execute(query, product.to_tuple() + (product.product_id,))
        conn.commit()
        cursor.close()
        return True
    
    @staticmethod
    def delete_product(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM products WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        conn.commit()
        cursor.close()
        return True
from db.connection import get_db_connection

class ProductDAO:
    
    @staticmethod
    def insert_product(product):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO products (name, category, description, price, in_stock) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, product.to_tuple())
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error inserting product: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all_products():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            query = "SELECT * FROM products"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all products: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_product_by_id(product_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            query = "SELECT * FROM products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error fetching product by ID: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update_product(product_id, product):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            query = "UPDATE products SET name = %s, category = %s, description = %s, price = %s, in_stock = %s WHERE product_id = %s"
            cursor.execute(query, product.to_tuple() + (product_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating product: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_product(product_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            query = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

            

    @staticmethod
    def decrease_stock(product_id, quantity):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            # Fetch current stock
            cursor.execute("SELECT in_stock FROM products WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            if not product:
                return False, "Product not found"

            current_stock = product['in_stock']  # Use dictionary key for stock value
            if current_stock < quantity:
                return False, "Insufficient stock"

            # Decrease stock
            new_stock = current_stock - quantity
            cursor.execute("UPDATE products SET in_stock = %s WHERE product_id = %s", (new_stock, product_id))
            connection.commit()
            return True, None
        except Exception as e:
            connection.rollback()
            return False, f"Error decreasing stock: {e}"
        finally:
            cursor.close()
            connection.close()