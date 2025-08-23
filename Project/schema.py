from pydantic import BaseModel,ConfigDict


class ResourceUser(BaseModel):
    course:str
    scheme:int
    semester:int
    subject:str

class Resourceout(ResourceUser):
    id:int
    file:str
        
    class Config:
        model_config = ConfigDict(from_attributes=True)