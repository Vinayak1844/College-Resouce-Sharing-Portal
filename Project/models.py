from sqlalchemy import String, Integer, Column
from database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    course = Column(String(50), nullable=False)
    scheme = Column(Integer, index=True, nullable=False)
    semester = Column(Integer, index=True, nullable=False)
    subject = Column(String(50), nullable=False)
    file = Column(String(255), nullable=False)  # stores saved file path
