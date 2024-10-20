from mysql.connector import connect, Error
from db.connection import get_db_connection

# this orderdao handles the direct interaction with the database.

class OrderDAO:

    @staticmethod
    def insert_new_order(order):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            order_query = """ INSERT INTO orders (user_id, shipping_address, city, postal_code, country)
                    VALUES (%s, %s, %s, %s, %s) """
            cursor.execute(order_query, order.to_tuple())
            
            order_id = cursor.lastrowid

            item_query = """ INSERT INTO order_items (order_id, product_id, name, count, price)
                    VALUES (%s, %s, %s, %s, %s) """
            for item in order.order_items:
                cursor.execute(item_query, (order_id,) + item.to_tuple())

            conn.commit()
            return order_id, "Order created successfully."
        except Error as e:
            conn.rollback()
            return None, f"Error creating order: {e}"
        finally:
            cursor.close()
            conn.close()
        
