from db_connection import engine
from models import Base

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Created! ")
    except Exception as e:
        print("Error while creating tables:", e)    