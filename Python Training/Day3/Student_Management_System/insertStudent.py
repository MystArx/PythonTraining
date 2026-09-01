from database import create_connection as cc
from studentlogging import logger

def insertStudent(id, name, age, course, marks, city, status):

    connection = None
    cursor = None

    try:
        connection = cc()

        if connection is not None:
            cursor = connection.cursor()

            query = """
                INSERT INTO students
                (student_id, student_name, student_age, student_course,
                 student_marks, student_city, student_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            student_data = (id,name,age,course,marks,city,status)

            cursor.execute(query, student_data)
            connection.commit()

            print("Student record inserted successfully!")
            logger.info(f"Record entered : {student_data}")

        else:
            print("Connection Failed: Ensure your MySQL server is running.")

    except Exception as error:
        print(f"Failed to insert record: {error}")
        logger.error(f"Failed to insert record: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()