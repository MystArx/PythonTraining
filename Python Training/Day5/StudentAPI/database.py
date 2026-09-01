from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


database=URL.create(
    drivername="mysql+pymysql",
    host="localhost",
    username="root",
    password="password",
    database="student_fastapi",
    port=3306
)

engine=create_engine(database,echo=False)
SessionLocal=sessionmaker(bind=engine)