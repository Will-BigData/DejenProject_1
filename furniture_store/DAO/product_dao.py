
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