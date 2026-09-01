from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import declarative_base

Base=declarative_base()


host = 'localhost'
port=3306
username="root"
password="password"


engine = create_engine(URL.create(
    drivername="mysql+pymysql",
    username=username,
    password=password,
    host=host,
    database="employee_project_pydantic",
    port=port
))

LocalSession = sessionmaker(bind=engine)