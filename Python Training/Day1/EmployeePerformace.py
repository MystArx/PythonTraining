def bonus(rating,yearsofExperience, projectstatus):
    if rating == 5 and projectstatus == "On Time":
        return 0.3
    elif rating == 4 and yearsofExperience >7:
        return 0.2
    elif rating == 3 and projectstatus == "delayed":
        return 0.05
    else:
        return 0   


rating=int(input("Enter rating : "))
yearsofExperience=int(input("Enter years of experience : "))
projectstatus=input("Enter project status : ")
salary=int(input("Enter salary : "))
print(f"The bonus is : {bonus(rating,yearsofExperience, projectstatus)*100}%, and new salary is {bonus(rating,yearsofExperience, projectstatus)*salary+salary}")