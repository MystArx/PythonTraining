class Student:
    
    def __init__(self,roll,name, course):
        self.roll=roll
        self.name=name
        self.course=course

    def display(self):
        print(f" Roll No : {self.roll}\n Name : {self.name}\n Course : {self.course}")


student_list=[]

def getStudent():
    
    roll=int(input("Enter roll no : "))
    name=input("Enter Name : ")
    course=input("Enter course : ")

    student_object= Student(roll,name,course)
    student_list.append(student_object)



getStudent()

for student in student_list:
    student.display()