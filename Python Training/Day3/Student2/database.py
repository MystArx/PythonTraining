import mysql.connector as mc

from mysql.connector import Error

def connect():
    try:
        connection=mc.connect(
            host="localhost",
            user="root",
            password="password",
            database="PythonTraining"
        )
        return connection
    
    except Error as e :
        print(f"Connection failed : {e}")
        return None

    
            