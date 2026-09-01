from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship


Base= declarative_base()


class University(Base):
    __tablename__="universityDB"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),nullable=False)
    students = relationship("Student", back_populates="university",cascade="all,delete-orphan")



class Student(Base):
    __tablename__="studentDB"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    email=Column(String(20)  )
    course =Column(String(10))
    contact=Column(String(10))
    university_id=Column(Integer,ForeignKey("universityDB.id"),nullable=False)
    university = relationship("University", back_populates="students")