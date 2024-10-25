

from mysql.connector import connect, Error
from db.connection import get_db_connection

# this userdao handles the direct interaction with the database.
class UserDAO:

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user_id = int(user_id)  # Ensure user_id is an integer
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print(f"Error fetching user by ID: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()          
    @staticmethod
    def get_user_by_email(email):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print(f"Error fetching user by email: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def insert_user(name, email, password, is_admin=False):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = "INSERT INTO users (name, email, password, is_admin) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, password, is_admin))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error inserting user: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def update_user(user_id, name, email, hashed_password=None, is_admin=None):
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            # Build the update query dynamically based on which fields are updated
            query = "UPDATE users SET name = %s, email = %s"
            values = [name, email]

            if hashed_password:
                query += ", password = %s"
                values.append(hashed_password)

            if is_admin is not None:  # Only update is_admin if the admin wants to change it
                query += ", is_admin = %s"
                values.append(is_admin)

            query += " WHERE user_id = %s"
            values.append(user_id)

            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0  # Return True if the update affected any rows
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            cursor.close()




    @staticmethod
    def delete_user(user_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def get_all_users():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM users"
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Error fetching all users: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
