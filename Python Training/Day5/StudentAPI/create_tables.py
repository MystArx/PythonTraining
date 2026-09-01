from models import Base
from database import engine

def create_database_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables Created")
    except Exception as e:
        print("Exception Creating tables")