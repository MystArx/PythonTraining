from database import create_connection as cc
from Studentclass import Student
from studentlogging import logger

def displayAllStudents():

    connection = None
    cursor = None

    try:
        connection = cc()

        if connection is not None:
            cursor = connection.cursor()

            query = """
                SELECT * FROM students
            """

            cursor.execute(query)
            student_rows = cursor.fetchall()

            if len(student_rows) == 0:
                print("No student records available.")

            else:
                for student_row in student_rows:
                    student_obj = Student(student_row[0],student_row[1],student_row[2],student_row[3],student_row[4],student_row[5],student_row[6])
                    student_obj.displayStudent()
                    print()
            logger.info("Data displayed")
        else:
            print("Connection Failed: Ensure your MySQL server is running.")
            logger.error("Connection Failed")

    except Exception as error:
        print(f"Failed to Display Students: {error}")
        logger.error(f"Failed to Display Students: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()