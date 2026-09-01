from database import create_connection as cc


class Student:

    def __init__(self, id, name, age, course, marks, city, status):
        self.student_id = id
        self.student_name = name
        self.student_age = age
        self.student_course = course
        self.student_marks = marks
        self.student_city = city
        self.student_status = status


    def displayStudent(self):
        print(f"ID : {self.student_id}")
        print(f"Name : {self.student_name}")
        print(f"Age : {self.student_age}")
        print(f"Course : {self.student_course}")
        print(f"Marks : {self.student_marks}")
        print(f"City : {self.student_city}")
        print(f"Status : {self.student_status}")


    def deleteStudent(self):
        connection = None
        cursor = None

        try:
            connection = cc()

            if connection is not None:
                cursor = connection.cursor()

                query = """
                    DELETE FROM students
                    WHERE student_id=%s
                """

                cursor.execute(query, (self.student_id,))
                connection.commit()

            else:
                print("Connection Failed: Ensure your MySQL server is running.")

        except Exception as error:
            print(f"Failed to Delete Student: {error}")

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()


    def updateMarks(self, marks):
        connection = None
        cursor = None

        try:
            connection = cc()

            if connection is not None:
                cursor = connection.cursor()

                query = """
                    UPDATE students
                    SET student_marks=%s
                    WHERE student_id=%s
                """

                cursor.execute(query, (marks, self.student_id))
                connection.commit()

                self.student_marks = marks

            else:
                print("Connection Failed: Ensure your MySQL server is running.")

        except Exception as error:
            print(f"Failed to Update Marks: {error}")

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()


    def updateCourse(self, course):
        connection = None
        cursor = None

        try:
            connection = cc()

            if connection is not None:
                cursor = connection.cursor()

                query = """
                    UPDATE students
                    SET student_course=%s
                    WHERE student_id=%s
                """

                cursor.execute(query, (course, self.student_id))
                connection.commit()

                self.student_course = course

            else:
                print("Connection Failed: Ensure your MySQL server is running.")

        except Exception as error:
            print(f"Failed to Update Course: {error}")

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()


    def updateStatus(self, status):
        connection = None
        cursor = None

        try:
            connection = cc()

            if connection is not None:
                cursor = connection.cursor()

                query = """
                    UPDATE students
                    SET student_status=%s
                    WHERE student_id=%s
                """

                cursor.execute(query, (status, self.student_id))
                connection.commit()

                self.student_status = status

            else:
                print("Connection Failed: Ensure your MySQL server is running.")

        except Exception as error:
            print(f"Failed to Update Status: {error}")

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()










