from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


database_url=URL.create(
    drivername="mysql+pymysql",
    host="localhost",
    username="root",
    password="password",
    database="employee_fastapi",
    port=3306    
)

engine=create_engine(database_url,echo=False)
SessionLocal=sessionmaker(bind=engine)


