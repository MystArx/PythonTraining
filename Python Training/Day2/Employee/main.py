import class_func as f

while True:
    print("1 - Display Employees")
    print("2- Add Employee")
    print("3- Search by ID")
    print("4- Search by Name")
    print("5- Delete By Id")
    print("6- Update Employee")
    print("7- Search by Email")
    print("8 - Exit")
    ch=int(input("Enter Choice : "))

    if ch==1:
        for emp in f.emp_list:
            emp.displayEmployee()
    if ch==2:
        f.addEmployee()
    if ch==3:
        id=int(input("Enter ID : "))
        obj=f.SearchByID(id,f.emp_list)
        if obj!=None:
            obj.displayEmployee()
        else:
            print("Employee not found.")
    if ch==4:
        name=input("Name : ")
        obj_lis=f.SearchByName(name,f.emp_list)
        for obj in obj_lis:
            if obj!=None:
                obj.displayEmployee()
            else:
                print("Employee not found.")
        
    if ch==5:
        id=int(input("Enter ID : "))
        obj=f.SearchByID(id,f.emp_list)
        if obj!=None:
            obj.deleteEmployee()
        else:
            print("Employee not found.")
    if ch==6:
        id=int(input("Enter ID : "))
        name=input("Enter name : ")
        gender=input("Enter Gender (M/F/O) : ")
        email=input("Enter email : ")
        age=int(input("Enter Age : "))
        salary=int(input("Enter Salary : "))
       
        obj=f.SearchByID(id,f.emp_list)
        obj.updateEmployee(name,gender,email,age,salary)


        
    if ch==7:
        email=input("Enter email : ")
        f.SearchByEmail(email,f.emp_list)
    if ch==8:
        break
    