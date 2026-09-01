from database import connect
from mysql.connector import Error

def addStudent():
    
    university_id=input("Enter University ID : ")

    

    connection=None
    cursor=None

    try:
        
        connection=connect()

        if connection!=None:

            check_query="select * from university where university_id=%s"
            cursor=connection.cursor()
            cursor.execute(check_query,(university_id,))
            uid = cursor.fetchone()
            if uid!=None:
                id = int(input("Enter Student ID : "))
                check_query1 = """
                                SELECT *
                                FROM students
                                JOIN university
                                ON students.university_id = university.university_id
                                WHERE university.university_id = %s
                                AND students.student_id = %s
                                """
                cursor=connection.cursor()
                values1=(university_id,id)
                cursor.execute(check_query1,values1)
                user= cursor.fetchone()
                if user==None:
                    
                    name = input("Enter Student Name : ")
                    age = int(input("Enter Age : "))
                    course = input("Enter Course : ")
                    marks = int(input("Enter Marks : "))
                    city = input("Enter City : ")
                    status = "Active"
                    query="Insert into students values (%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(id,name,age,course,marks,city,status,university_id)
                    cursor.execute(query,values)
                    connection.commit()

                else:
                    print("Student Exists!")
            else:
                print("UID not found")

    except Error as e:
        print("Hi")
        print(e)

def addUniversity():

    uid=input("Enter University ID : ")
    name=input("Enter Name : ")

    

    try:
        connection=connect()
        if connection!=None:
            cursor=connection.cursor()

            check_query="SELECT * from university where university_id=%s"
            cursor.execute(check_query,(uid,))
            university=cursor.fetchone()

            if university==None:
                query="INSERT INTO university values (%s,%s)"
                values=(uid,name)
                cursor.execute(query,values)
                connection.commit()

            else:
                print("University ID exists")    

    except Error as e:
        print(e)

def displayStudent():

    connection=None
    cursor=None

    try:

        connection=connect()

        if connection!=None:

            query = """
                    SELECT students.student_id,
                           students.student_name,
                           students.student_age,
                           students.student_course,
                           students.student_marks,
                           students.student_city,
                           students.student_status,
                           university.university_id,
                           university.university_name
                    FROM students
                    JOIN university
                    ON students.university_id = university.university_id
                    """

            cursor=connection.cursor()
            cursor.execute(query)

            students=cursor.fetchall()

            if students!=None:

                for student in students:
                    print("Student ID : ",student[0])
                    print("Student Name : ",student[1])
                    print("Age : ",student[2])
                    print("Course : ",student[3])
                    print("Marks : ",student[4])
                    print("City : ",student[5])
                    print("Status : ",student[6])
                    print("University ID : ",student[7])
                    print("University Name : ",student[8])
                    print("-----------------------------")

            else:
                print("No Students Found")

    except Error as e:
        print(e)



while True:
    ch=int(input("1 : Add Student \n2 : Add University\n 3 : View Student\n 4 : Exit \n Choice : "))
    if ch==1:
        addStudent()
    if ch==2:
        addUniversity()
    if ch==3:
        displayStudent()
    if ch==4:
        break