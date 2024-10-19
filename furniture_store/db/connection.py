import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

def get_db_connection():
    try:
        # Load environment variables from .env file
        load_dotenv()

        # Fetch values from environment variables
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_NAME')

        # Connect to the MySQL database using environment variables
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Connected to MySQL database: {database}")
        return connection

    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
