employees = [
    (101, "Gaurav Joshi", "AI Developer", ["Payroll System", "HR Portal"]),
    (102, "Ananya Roy", "Backend Developer", ["API Gateway", "Auth Service"])
]

SearchByID = lambda id, emp_list: next((emp for emp in emp_list if emp[0] == id), None)

def getEmployee():
    if len(employees) == 1:
        return employees[0]
    id = int(input("Enter Employee ID : "))
    emp = SearchByID(id, employees)
    if emp == None:
        print("Employee not found.")
    return emp

def viewEmployeeDetails():
    emp = getEmployee()
    if emp != None:
        print(f"Employee ID       : {emp[0]}")
        print(f"Employee Name     : {emp[1]}")
        print(f"Department        : {emp[2]}")
        print(f"Assigned Projects : {', '.join(emp[3]) if emp[3] else 'None'}")

def addNewProject():
    emp = getEmployee()
    if emp != None:
        project_name = input("Enter Project Name : ")
        if project_name in emp[3]:
            print("Project already assigned to this employee.")
        else:
            emp[3].append(project_name)
            print("Project added successfully.")

def removeProject():
    emp = getEmployee()
    if emp != None:
        project_name = input("Enter Project Name : ")
        if project_name in emp[3]:
            emp[3].remove(project_name)
            print("Project removed successfully.")
        else:
            print("Project not found.")

def searchProject():
    emp = getEmployee()
    if emp != None:
        project_name = input("Enter Project Name : ")
        if project_name in emp[3]:
            print("Project Assigned.")
        else:
            print("Project Not Assigned.")

def displayTotalProjects():
    emp = getEmployee()
    if emp != None:
        print(f"Total Projects : {len(emp[3])}")

def displayProjectsAlphabetically():
    emp = getEmployee()
    if emp != None:
        sorted_projects = sorted(emp[3])
        print("\nProjects (Alphabetical Order):")
        for proj in sorted_projects:
            print(proj)

def main():
    while True:
        print("\n========== Employee Project Management System ==========")
        print("1. View Employee Details")
        print("2. Add New Project")
        print("3. Remove a Project")
        print("4. Search a Project")
        print("5. Display Total Number of Projects")
        print("6. Display Projects Alphabetically")
        print("7. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            viewEmployeeDetails()
        elif ch == 2:
            addNewProject()
        elif ch == 3:
            removeProject()
        elif ch == 4:
            searchProject()
        elif ch == 5:
            displayTotalProjects()
        elif ch == 6:
            displayProjectsAlphabetically()
        elif ch == 7:
            print("Exiting")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
