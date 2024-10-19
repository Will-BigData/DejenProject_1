from mysql.connector import connect, Error
from db.connection import get_db_connection

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
            connection.close()
    

