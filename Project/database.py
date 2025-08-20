from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DB_URL = "mysql+mysqlconnector//:root:Vinayak%40@1844@localhost:3360/collegeDB"

engine = create_engine(DB_URL)
LocalSession = sessionmaker(autoflush = False,autocommit=False,bind = engine)

Base = declarative_base()
