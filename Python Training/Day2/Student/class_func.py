student_list=[]

class Student:
    def __init__(self,id,name,age,course,marks,city):
        self.student_id=id
        self.student_name=name
        self.student_age=age
        self.student_course=course
        self.student_marks=marks
        self.student_city=city
        self.student_status="Active"


    def displayStudent(self):
        print(f"ID : {self.student_id}")
        print(f"Name : {self.student_name}")
        print(f"Age : {self.student_age}")
        print(f"Course : {self.student_course}")
        print(f"Marks : {self.student_marks}")
        print(f"City : {self.student_city}")
        print(f"Status : {self.student_status}")


    def deleteStudent(self):
        student_list.remove(self)


    def updateMarks(self,marks):
        self.student_marks=marks


    def updateCourse(self,course):
        self.student_course=course


    def updateStatus(self,status):
        self.student_status=status



def addStudent():
        id=int(input("Enter Student ID : "))
        name=input("Enter Student Name : ")
        age=int(input("Enter Age : "))
        course=input("Enter Course : ")
        marks=int(input("Enter Marks : "))
        city=input("Enter City : ")

        student_obj=Student(id,name,age,course,marks,city)
        student_list.append(student_obj)


SearchByID = lambda id,student_list:next((student for student in student_list if student.student_id==id),None)