from models import Base
from database import engine



def create_database_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables done")
    except:
        print("Exception Creating tables")