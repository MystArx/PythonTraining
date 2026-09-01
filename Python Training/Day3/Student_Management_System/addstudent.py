from insertStudent import insertStudent
from studentlogging import logger


def addStudent():

    id = int(input("Enter Student ID : "))
    name = input("Enter Student Name : ")
    age = int(input("Enter Age : "))
    course = input("Enter Course : ")
    marks = int(input("Enter Marks : "))
    city = input("Enter City : ")
    status = "Active"
    logger.info(f"Data Recieved : {id},{name},{age},{course},{marks},{city},{status}")
    insertStudent(id,name,age,course,marks,city,status)