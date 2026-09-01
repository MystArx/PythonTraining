from Studentclass import Student
from addstudent import addStudent
from displayAllStudents import displayAllStudents
from StudentObjfromDB import createStudentObjectfromDB

while True:
    print("1 - Add Student")
    print("2 - Display All Students")
    print("3 - Search Student")
    print("4 - Update Marks")
    print("5 - Change Course")
    print("6 - Change Status")
    print("7 - Delete Student")
    print("8 - Exit")

    ch = int(input("Enter Choice : "))

    if ch == 1:
        addStudent()

    if ch == 2:
        displayAllStudents()

    if ch == 3:
        id = int(input("Enter Student ID : "))

        obj = createStudentObjectfromDB(id)

        if obj is not None:
            obj.displayStudent()
        else:
            print("Student not found.")

    if ch == 4:
        id = int(input("Enter Student ID : "))
        marks = int(input("Enter New Marks : "))

        obj = createStudentObjectfromDB(id)

        if obj is not None:
            if marks >= 0 and marks <= 100:
                obj.updateMarks(marks)
                print("Marks Updated Successfully.")
                obj.displayStudent()
            else:
                print("Marks should be between 0 and 100.")
        else:
            print("Student not found.")

    if ch == 5:
        id = int(input("Enter Student ID : "))

        obj = createStudentObjectfromDB(id)

        if obj is not None:
            course = input("Enter New Course : ")
            obj.updateCourse(course)
            print("Course Updated Successfully.")
            obj.displayStudent()
        else:
            print("Student not found.")

    if ch == 6:
        id = int(input("Enter Student ID : "))

        obj = createStudentObjectfromDB(id)

        if obj is not None:
            status = input("Enter Status (Active/Inactive) : ")

            if status == "Active" or status == "Inactive":
                obj.updateStatus(status)
                print("Status Updated Successfully.")
                obj.displayStudent()
            else:
                print("Invalid Status.")

        else:
            print("Student not found.")

    if ch == 7:
        id = int(input("Enter Student ID : "))

        obj = createStudentObjectfromDB(id)

        if obj is not None:
            obj.deleteStudent()
            print("Student Deleted Successfully.")
        else:
            print("Student not found.")

    if ch == 8:
        print("Exiting")
        break