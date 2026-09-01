from database import SessionLocal
from sqlalchemy import select
from models import Student

def displaystudents():
    session=SessionLocal()
    try:
        query=select(Student).order_by(Student.id)
        students=session.scalars(query).all()

        if not students:
            print("No Students")
            return

    except:
        return{"message":"Could Not Retrieve"}

    return(students)
