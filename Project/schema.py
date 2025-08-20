from Project.models import Resource
from pydantic import BaseModel


class ResourceUser(BaseModel):
    course:str
    schema:int
    semester:int
    subject:str
    
class UserFile(ResourceUser):
    id:int
    file:str
        
    class Config:
        from_attributes = True