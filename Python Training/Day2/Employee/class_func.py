emp_list=[]

class Employee:
    _counter=100
    def __init__(self,name,gender,email,age,salary):
        Employee._counter+=1
        self.emp_id=self._counter
        self.emp_name=name
        self.emp_gender=gender
        self.emp_email=email
        self.emp_age=age
        self.emp_salary=salary



    def displayEmployee(self):
        print(f"ID : {self.emp_id}")
        print(f"Name : {self.emp_name}")
        print(f"Gender : {self.emp_gender}")
        print(f"Email : {self.emp_email}")     
        print(f"Age : {self.emp_age}")
        print(f"Salary : {self.emp_salary}")   


    def deleteEmployee(self):
        emp_list.remove(self)    

    def updateEmployee(self,name,gender,email,age,salary):
        self.emp_name=name
        self.emp_gender=gender
        self.emp_email=email
        self.emp_age=age
        self.emp_salary=salary




def addEmployee():
        name=input("Enter name : ")
        gender=input("Enter Gender (M/F/O) : ")
        email=input("Enter email : ")
        age=int(input("Enter Age : "))
        salary=int(input("Enter Salary : "))

        employee_obj=Employee(name,gender,email,age,salary)
        emp_list.append(employee_obj)


SearchByID = lambda id,emp_list:next((emp for emp in emp_list if emp.emp_id==id),None)

SearchByName = lambda name,emp_list:[emp for emp in emp_list if emp.emp_name==name]

SearchByEmail = lambda email,emp_list:[emp for emp in emp_list if emp.emp_email==email]
