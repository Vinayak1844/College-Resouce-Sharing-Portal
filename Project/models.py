from pydantic import BaseModel
from Project.database  import Base
from sqlalchemy import String,Integer,Column

class Resource(Base):
    __tablename__="resources"
    id = Column(Integer,primary_key=True,index=True)
    course = Column(String(50))
    scheme = Column(Integer,index= True)
    semester = Column(Integer,index = True)
    subject = Column(String(50))
    file = Column(String(255))
    