

from mysql.connector import connect, Error
from db.connection import get_db_connection

# this userdao handles the direct interaction with the database.
class UserDAO:

    @staticmethod
    def get_user_by_id(user_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            return cursor.fetchone()
        except Error as e:
            print("Error fetching user by id:", e)
            return None
        finally:
            cursor.close()
            
    
    @staticmethod
    def get_user_by_email(email):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cursor.fetchone()
        except Error as e:
            print("Error fetching user by email:", e)
            return None
        finally:
            cursor.close()
            

    @staticmethod
    def insert_user(name, email, password, is_admin=False):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("""
                INSERT INTO users (name, email, password, is_admin) 
                VALUES (%s, %s, %s, %s)
            """, (name, email, password, is_admin))
            connection.commit()
            return cursor.lastrowid  # Return the ID of the inserted user
        except Error as e:
            print("Error inserting user:", e)
            return None
        finally:
            cursor.close()
    
    @staticmethod
    def update_user(user_id, name, email, password=None):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        try:
            if password:
                cursor.execute("""
                    UPDATE users SET name = %s, email = %s, password = %s 
                    WHERE user_id = %s
                """, (name, email, password, user_id))
            else:
                cursor.execute("""
                    UPDATE users SET name = %s, email = %s 
                    WHERE user_id = %s
                """, (name, email, user_id))
            connection.commit()
            return True
        except Error as e:
            print("Error updating user:", e)
            return False
        finally:
            cursor.close()

    @staticmethod
    def delete_user(user_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print("Error deleting user:", e)
            return False
        finally:
            cursor.close()

    @staticmethod
    def get_all_users():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
        except Error as e:
            print("Error fetching all users:", e)
            return None
        finally:
            cursor.close()