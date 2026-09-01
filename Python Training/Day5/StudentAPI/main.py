from models import Student,University
from database import SessionLocal
from create_tables import create_database_tables
from sqlalchemy import select,delete,update
from modules.displaystudents import displaystudents


from fastapi import FastAPI

app=FastAPI()
create_database_tables()

@app.get("/status")
def status():
    return{
        "message":"API Up"
    }


@app.get("/DisplayStudents")
def display_students():
    return displaystudents()


@app.post("/insertstudent")
def insert_student(
    name: str,
    email: str,
    course: str,
    contact: str,
    university_id: int
):

    session = SessionLocal()

    try:
        university = session.get(University, university_id)

        if university is None:
            return {
                "message": "University not found"
            }

        student = Student(
            name=name,
            email=email,
            course=course,
            contact=contact,
            university_id=university_id
        )

        session.add(student)
        session.commit()
        session.refresh(student)

        return {
            "message": "Student added successfully",
            "student_id": student.id
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to add student",
            "error": str(e)
        }


@app.get("/searchstudent")
def search_student(id: int):

    session = SessionLocal()

    try:

        query = select(Student).where(Student.id == id)

        student = session.scalars(query).first()

        if student is None:
            return {
                "message": "Student not found"
            }

        return student

    except Exception as e:

        return {
            "message": "Failed to find student",
            "error": str(e)
        }


@app.put("/updatestudent")
def update_student(
    id: int,
    name: str,
    email: str,
    course: str,
    contact: str,
    university_id: int
):

    session = SessionLocal()

    try:
        student = session.get(Student, id)

        if student is None:
            return {
                "message": "Student not found"
            }
        university = session.get(University, university_id)

        if university is None:
            return {
                "message": "University not found"
            }

        query = (
            update(Student)
            .where(Student.id == id)
            .values(
                name=name,
                email=email,
                course=course,
                contact=contact,
                university_id=university_id
            )
        )

        session.execute(query)
        session.commit()

        return {
            "message": "Student updated successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to update student",
            "error": str(e)
        }


@app.delete("/deletestudent")
def delete_student(id: int):

    session = SessionLocal()

    try:

        student = session.get(Student, id)

        if student is None:
            return {
                "message": "Student not found"
            }

        session.delete(student)
        session.commit()

        return {
            "message": "Student deleted successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to delete student",
            "error": str(e)
        }


@app.post("/insertuniversity")
def insert_university(name: str):

    session = SessionLocal()

    try:

        university = University(
            name=name
        )

        session.add(university)
        session.commit()
        session.refresh(university)

        return {
            "message": "University added successfully",
            "university_id": university.id
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to add university",
            "error": str(e)
        }


@app.get("/DisplayUniversities")
def display_universities():

    session = SessionLocal()

    try:

        query = select(University).order_by(University.id)

        universities = session.scalars(query).all()

        if not universities:
            return {
                "message": "No Universities Found"
            }

        return universities

    except Exception as e:

        return {
            "message": "Could Not Retrieve",
            "error": str(e)
        }



@app.get("/searchuniversity")
def search_university(id: int):

    session = SessionLocal()

    try:

        university = session.get(University, id)

        if university is None:
            return {
                "message": "University not found"
            }

        return university

    except Exception as e:

        return {
            "message": "Failed to find university",
            "error": str(e)
        }



@app.delete("/deleteuniversity")
def delete_university(id: int):
    session = SessionLocal()
    try:
        university = session.get(University, id)
        if university is None:
            return {
                "message": "University not found"
            }
        session.delete(university)
        session.commit()

        return {
            "message": "University deleted successfully"
        }

    except Exception as e:
        session.rollback()
        return {
            "message": "Failed to delete university",
            "error": str(e)
        }



@app.get("/university/students")
def students_from_university(id:int):
    session = SessionLocal()    
    try:    
        university = session.get(University, id)    
        if university is None:
            return {
                "message": "University not found"
            }
    
        query=select(Student,University.name).join(University,Student.university_id==University.id).where(University.id==id)
        result=session.execute(query).all()
        return result
    
    except Exception as e:
    
        return {
            "message": "Failed to find university",
            "error": str(e)
        }

