from database import create_connection as cc
from Studentclass import Student

def createStudentObjectfromDB(id):

    connection = None
    cursor = None

    try:
        connection = cc()

        if connection is not None:
            cursor = connection.cursor()

            query = """
                SELECT * FROM students
                WHERE student_id=%s
            """

            cursor.execute(query, (id,))
            student_row = cursor.fetchone()

            if student_row is not None:

                student_obj = Student(student_row[0],student_row[1],student_row[2],student_row[3],student_row[4],student_row[5],student_row[6])

                return student_obj

            else:
                return None

        else:
            print("Connection Failed: Ensure your MySQL server is running.")
            return None

    except Exception as error:
        print(f"Failed to Create Object {error}")
        return None

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()