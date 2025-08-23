from pydantic import BaseModel,ConfigDict
from fastapi import UploadFile


class ResourceUser(BaseModel):
    course:str
    scheme:int
    semester:int
    subject:str

class Resourceout(ResourceUser):
    id:int
    file:UploadFile
        
    class Config:
        model_config = ConfigDict(from_attributes=True)