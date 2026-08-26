import class_func as f

while True:
    print("1 - Add Student")
    print("2 - Display All Students")
    print("3 - Search Student")
    print("4 - Update Marks")
    print("5 - Change Course")
    print("6 - Change Status")
    print("7 - Delete Student")
    print("8 - Exit")

    ch=int(input("Enter Choice : "))

    if ch==1:
        id=int(input("Enter Student ID : "))

        obj=f.SearchByID(id,f.student_list)

        if obj!=None:
            print("Student ID already exists.")
        else:
            name=input("Enter Student Name : ")
            age=int(input("Enter Age : "))
            course=input("Enter Course : ")
            marks=int(input("Enter Marks : "))
            city=input("Enter City : ")

            if marks>=0 and marks<=100:
                student_obj=f.Student(id,name,age,course,marks,city)
                f.student_list.append(student_obj)
            else:
                print("Marks should be between 0 and 100.")

    if ch==2:
        if len(f.student_list)==0:
            print("No student records available.")
        else:
            for student in f.student_list:
                student.displayStudent()

    if ch==3:
        id=int(input("Enter Student ID : "))

        obj=f.SearchByID(id,f.student_list)

        if obj!=None:
            obj.displayStudent()
        else:
            print("Student not found.")

    if ch==4:
        id=int(input("Enter Student ID : "))
        marks=int(input("Enter New Marks : "))

        obj=f.SearchByID(id,f.student_list)

        if obj!=None:
            if marks>=0 and marks<=100:
                obj.updateMarks(marks)
                print("Marks Updated Successfully.")
                obj.displayStudent()
            else:
                print("Marks should be between 0 and 100.")
        else:
            print("Student not found.")

    if ch==5:
        id=int(input("Enter Student ID : "))

        obj=f.SearchByID(id,f.student_list)

        if obj!=None:
            course=input("Enter New Course : ")
            obj.updateCourse(course)
            print("Course Updated Successfully.")
            obj.displayStudent()
        else:
            print("Student not found.")

    if ch==6:
        id=int(input("Enter Student ID : "))

        obj=f.SearchByID(id,f.student_list)

        if obj!=None:
            status=input("Enter Status (Active/Inactive) : ")

            if status=="Active" or status=="Inactive":
                obj.updateStatus(status)
                print("Status Updated Successfully.")
            else:
                print("Invalid Status.")

        else:
            print("Student not found.")

    if ch==7:
        id=int(input("Enter Student ID : "))

        obj=f.SearchByID(id,f.student_list)

        if obj!=None:
            obj.deleteStudent()
            print("Student Deleted Successfully.")
        else:
            print("Student not found.")

    if ch==8:
        print("Exiting")
        break