from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DB_URL = "mysql+mysqlconnector://root:Vinayak%401844@localhost:3306/collegeDB"

engine = create_engine(DB_URL)
LocalSession = sessionmaker(autoflush = False,autocommit=False,bind = engine)

Base = declarative_base()
