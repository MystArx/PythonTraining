import mysql.connector as ms
from mysql.connector import Error 
from studentlogging import logger


def create_connection():
    try:
        connection=ms.connect(
            host="localhost",
            user="root",
            password="password",
            database="PythonTraining"
        )
        logger.info("Connection Successful")
        return connection

    except Error as e:
        logger.error(f"Error encountered : \n{e}\n")
        print(f"Error {e}")
        return None