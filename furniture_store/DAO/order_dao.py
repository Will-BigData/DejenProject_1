from mysql.connector import connect, Error
from db.connection import get_db_connection

class OrderDAO:
    @staticmethod
    def create_order(order):
        """Inserts an order and its associated items into the database."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            order_query = """ 
            INSERT INTO orders (user_id, shipping_address, city, postal_code, country)
            VALUES (%s, %s, %s, %s, %s) 
            """
            cursor.execute(order_query, order.to_tuple())
            # Fetch the last inserted order_id
            order_id = cursor.lastrowid

            # Insert each order item into the order_items table
            item_query = """ 
            INSERT INTO order_items (order_id, product_id, name, count, price)
            VALUES (%s, %s, %s, %s, %s) 
            """
            for item in order.order_items:
                cursor.execute(item_query, (order_id, item.product_id, item.name, item.count, item.price))
            conn.commit()
            return order_id, None  
        except Error as e:
            conn.rollback()
            return None, f"Error creating order: {e}"
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def get_orders_by_user_id(user_id):
      #Fetches all orders for a specific user by their user_id.
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            order_query = """ SELECT * FROM orders WHERE user_id = %s """
            cursor.execute(order_query, (user_id,))
            orders = cursor.fetchall()

            if orders:
                return orders, None 
                return None, "No orders found for user."

        except Error as e:
            return None, f"Error fetching orders for user_id {user_id}: {e}"

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_orders_id(order_id):
       #Fetches an order and its associated items by order_id.
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            order_query = """ SELECT * FROM orders WHERE order_id = %s """
            cursor.execute(order_query, (order_id,))
            order_data = cursor.fetchone()

            if not order_data:
                return None, f"Order not found with ID {order_id}"

            item_query = """ SELECT * FROM order_items WHERE order_id = %s """
            cursor.execute(item_query, (order_id,))
            order_items = cursor.fetchall()
            order_data['items'] = order_items
            return order_data, None  
        except Error as e:
            return None, f"Error fetching order by id: {e}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_order_items_by_order_id(order_id):
      #Fetches the order items (products) for a given order ID.
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM order_items WHERE order_id = %s"
            cursor.execute(query, (order_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching order items: {e}")
            return None
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def get_all_orders():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            order_query = """ SELECT * FROM orders """
            cursor.execute(order_query)
            orders = cursor.fetchall()

            if orders:
                return orders, None  
            else:
                return None, "No orders found."  
        except Error as e:
            return None, f"Error fetching orders: {e}" 
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def get_all_order_items():
        """Fetches all order items from the database."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            # Query to fetch all order items
            query = """
                SELECT oi.item_id, oi.order_id, oi.product_id, p.name, oi.count, oi.price
                FROM order_items oi
                JOIN products p ON oi.product_id = p.product_id
            """
            cursor.execute(query)
            order_items = cursor.fetchall()

            return order_items, None  # Return all order items with no error

        except Error as e:
            return None, f"Error fetching order items: {e}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_order(order_id, shipping_address=None, city=None, postal_code=None, country=None):
        """Updates an existing order."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Prepare the SQL query dynamically based on what fields need updating
            fields = []
            values = []
            if shipping_address:
                fields.append("shipping_address = %s")
                values.append(shipping_address)
            if city:
                fields.append("city = %s")
                values.append(city)
            if postal_code:
                fields.append("postal_code = %s")
                values.append(postal_code)
            if country:
                fields.append("country = %s")
                values.append(country)

            values.append(order_id)

            query = f"UPDATE orders SET {', '.join(fields)} WHERE order_id = %s"
            cursor.execute(query, values)
            conn.commit()

            return cursor.rowcount > 0, None 
        except Error as e:
            return False, f"Error updating order: {e}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_order(order_id):
        """Deletes an order and its items by order_id."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            item_query = "DELETE FROM order_items WHERE order_id = %s"
            cursor.execute(item_query, (order_id,))
            order_query = "DELETE FROM orders WHERE order_id = %s"
            cursor.execute(order_query, (order_id,))
            conn.commit()
            return cursor.rowcount > 0, None 
        except Error as e:
            return False, f"Error deleting order: {e}"
        finally:
            cursor.close()
            conn.close()
