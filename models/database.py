from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./my-fast-api.db"
SQLALCHEMY_DATABASE_URL="mysql+mysqlconnector://ins_stock:qwerty@192.168.16.140:3306/InsMachineDB"
                                                #user:pass@ip:port/db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#get database
#getttttttttttt
def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()
