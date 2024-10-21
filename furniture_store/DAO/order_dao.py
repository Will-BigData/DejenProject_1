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
    

    @staticmethod
    def get_order_by_id(order_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # fetc the order details
            order_query = """ SELECT * FROM orders WHERE order_id = %s """
            cursor.execute(order_query, (order_id,))
            order_data = cursor.fetchone()

            if not order_data:
                return None, f"Order not found with ID {order_id}"
            
            # fetch the associated order items
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
    def get_all_orders():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            order_query = """ SELECT * FROM orders """
            cursor.execute(order_query)
            orders = cursor.fetchall()

            return orders, None if orders else "No orders found."
        except Error as e:
            return None, f"Error fetching orders: {e}"
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def update_order(order_id, shipping_address=None, city=None, postal_code=None, country=None):

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

            if cursor.rowcount > 0:
                return True, "Order updated successfully."
            else:
                return False, "No changes made or order not found."
        except Error as e:
            return False, f"Error updating order: {e}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_order(order_id):
        """Deletes an order by its ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Delete the order items first
            item_query = "DELETE FROM order_items WHERE order_id = %s"
            cursor.execute(item_query, (order_id,))

            # Then delete the order
            order_query = "DELETE FROM orders WHERE order_id = %s"
            cursor.execute(order_query, (order_id,))
            conn.commit()

            if cursor.rowcount > 0:
                return True, "Order deleted successfully."
            else:
                return False, "Order not found."
        except Error as e:
            return False, f"Error deleting order: {e}"
        finally:
            cursor.close()
            conn.close()



